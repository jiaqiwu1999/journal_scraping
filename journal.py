import requests
import re
import os
import tarfile
import glob
import shutil
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pathlib import Path
from bs4 import BeautifulSoup

def save_existing_url(doi):
    with open('doi.txt', 'w') as f:
        f.writelines(doi)

def downloard(response, url, size):
    filename = re.search(r'/([\w_-]+[.](pdf))$', url)
    if filename is None:
        name = f"{size}.pdf"
    else:
        name = filename.group()
    with open(name, 'wb') as f:
        f.write(response.content)

def get_all_documents():
    dir = Path('.')
    print(str(dir))
    all_files = [x for x in dir.iterdir() if x.is_dir()]
    ll = []
    for each in all_files:
        ll.append((list)(each.glob('*.txt')))
    return len(ll)

def get_all_pmid(soup):
    pmids = soup.findAll('dl', class_='rprtid')
    ids = []
    for pmid in pmids:
        x = pmid.find('dd')
        if x is not None:
            ids.append(x.contents[0][3:])
    return ids

def save_pdfs(ftpUrl, file_name, dest):
    resp = urlopen(ftpUrl)
    with open(dest/file_name, 'wb') as f:
        shutil.copyfileobj(resp, f)

def save_tgz(ftpUrl, dest):
    resp = urlopen(ftpUrl)
    tar = tarfile.open(fileobj=resp, mode='r|gz')
    tar.extractall(path=dest)

def fetch_apis(id_list, dest_path):
    base_api = "https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi"
    for id in id_list:
        url = f"{base_api}?id=PMC{id}"
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'html.parser')
        y = soup.find('records')
        links = y.findAll('link')
        for link in links:
            if link.get('format', None) == 'pdf':
                save_pdfs(link.get('href', None), f"PMC{id}.pdf", dest_path)
                return
            else:
                tgz_link = link.get('href', None)
        save_tgz(tgz_link, dest_path)


def main():
    # search_input = input("Please enter search keywords, separated by space: ")
    # search_word = search_input.split()
    # size = input("Please enter the number of pages of articles (20 article per page): ")

    search_word = ['NIR-II', 'imaging']
    query_string = '+'.join(search_word)
    # print(query_string)
    base_url = "https://www.ncbi.nlm.nih.gov/pmc/"
    final_url = f"{base_url}?term={query_string}"
    req = requests.get(final_url)
    soup = BeautifulSoup(req.content, 'html.parser')
    id_curr_page = get_all_pmid(soup)
    path = Path('.')
    dest = path / query_string
    if not dest.exists():
        dest.mkdir()
    fetch_apis(id_curr_page, dest)

    # Starting from 2nd page, need to use selenium instead of soup
    p = '/usr/local/bin/chromedriver'
    driver = webdriver.Chrome(executable_path=p)
    driver.get(final_url)
    for i in range(2, 5):
        y = driver.find_element_by_id('pageno')
        y.clear()
        y.send_keys(i)
        y.send_keys(Keys.ENTER)
        ids = driver.find_elements_by_xpath("//dl[@class='rprtid']")
        id_list = []
        for id in ids:
            reg = r"[0-9]+"
            res = re.findall(reg, id.text)
            id_list.append(res[0])
        fetch_apis(id_list, dest)


if __name__ == "__main__":
    main()
