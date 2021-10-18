import requests
import re
import os
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

def get_all_pmid(url):
    pass



def main():
    # api_url = "https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi?id=PMC7092636"
    # req = requests.get(api_url)
    # print(req.content)
    # soup = BeautifulSoup(req.content, 'lxml')
    # y = soup.find('records')
    # for i in y.contents:
    #     id = i['id']
    #     for j in i.contents:
    #         if j['format'] == 'tgz':
    #             print("tgz format")
    #     print(i)
    # filter_string = "filter=simsearch2.ffrft"
    # url = "ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_pdf/67/6d/main.PMC8454557.pdf"
    # resp = urlopen(url)
    # with open('trial.pdf', 'wb') as f:
    #     shutil.copyfileobj(resp, f)

    # search_input = input("Please enter search keywords, separated by space: ")
    # search_word = search_input.split()
    # size = input("Please enter the number of articles: ")
    # if size == '':
    #     size = 10
    search_word = ['NIR-II', 'imaging', 'liver', 'cancer']
    query_string = '+'.join(search_word)
    # print(query_string)
    base_url = "https://www.ncbi.nlm.nih.gov/pmc/"
    final_url = f"{base_url}?term={query_string}"
    p = '/usr/local/bin/chromedriver'
    driver = webdriver.Chrome(executable_path=p)
    driver.get(final_url)
    # x = driver.find_elements_by_tag_name('a')
    # driver.execute_script("document.getElementById('pageno').value = 2")
    for i in range(1, 10):
        y = driver.find_element_by_id('pageno')
        y.clear()
        y.send_keys(i)
        y.send_keys(Keys.ENTER)
    req = requests.get(final_url)
    soup = BeautifulSoup(req.content, 'html.parser')
    x = soup.find('a', class_='active page_link next')
    next = x.get('href', None)
    print(next)
    req2 = requests.get(next)



    url = "https://www.jle.com/download/epd-305192-29983-the_natural_history_and_prognosis_of_epilepsy-a.pdf"
    
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")




if __name__ == "__main__":
    main()
