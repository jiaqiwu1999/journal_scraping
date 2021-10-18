# journal_scraping_program

Goal: to help researches achieve efficient journal research and automated downloads
Beautifulsoup, HTML, XML, FTP, Selenium

## Procedures:
1. Search criteria and size entered by user
2. Pubmed Central search using query string
3. Beautifulsoup to scrape the journal IDs
4. Use ID for PMC API
5. ftp url received from API's XML page
6. ftp request made and write the content to pdf file
7. To change page and obtain more inputs, Selenium is used

## Problems to be considered:
1. Ranking of journals by no. of citations, or by recency
2. More efficient way to avoid repetition of journal downloads
