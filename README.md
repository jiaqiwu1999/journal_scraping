# journal_scraping_program

Goal: to help researches achieve efficient journal research and automated downloads
Beautifulsoup, HTML, XML, FTP, Selenium
Prerequisite: Chrome 

## Procedures:
1. Search criteria and size entered by user
2. Pubmed Central search using query string
3. Beautifulsoup to scrape the journal IDs
4. Use ID for PMC API
5. ftp url received from API's XML page
6. ftp request made and write the content to pdf file
7. To change page and obtain more inputs, Selenium is used

## Downloading Chrome Webdrivder
1. Create new folder to put
<img width="857" alt="Pasted Graphic" src="https://user-images.githubusercontent.com/59846636/138357854-6a190d4a-e491-4cf0-830c-88f6b0d77b81.png">
2. Copy the path of this folder and add it to system
<img width="510" alt="Pasted Graphic 1" src="https://user-images.githubusercontent.com/59846636/138357905-1e11d21c-b85f-45a2-8fa5-7afc06d793c7.png">
<img width="636" alt="Pasted Graphic 2" src="https://user-images.githubusercontent.com/59846636/138357978-459bf121-f891-4151-a66c-90b0a16485ae.png">
<img width="500" alt="Pasted Graphic 3" src="https://user-images.githubusercontent.com/59846636/138357986-a4b3f6b3-9c04-47db-b142-af6a627ad68d.png">
<img width="330" alt="Pasted Graphic 4" src="https://user-images.githubusercontent.com/59846636/138357993-8d4f137e-6272-433b-885e-aee3efa69f4c.png">
<img width="427" alt="Pasted Graphic 5" src="https://user-images.githubusercontent.com/59846636/138357998-1ba62247-aedb-479d-91cd-6d79a97cc8c2.png">
Paste it here
<img width="384" alt="Pasted Graphic 6" src="https://user-images.githubusercontent.com/59846636/138358016-0da1eb14-1b7b-415b-9fc5-ba96ee806a02.png">
<img width="344" alt="Pasted Graphic 7" src="https://user-images.githubusercontent.com/59846636/138358044-47b1ce11-5c3f-4e70-b7af-69476ba0356c.png">
3. Download chromedriver from website
https://chromedriver.storage.googleapis.com/index.html?path=94.0.4606.61/ get "win32"
4. Move the download to your folder created in step 1

## Problems to be considered:
1. Ranking of journals by no. of citations, or by recency
2. More efficient way to avoid repetition of journal downloads
