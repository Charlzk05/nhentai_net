## nhentai_net
nHentai.net Scraper and Downloader
Uses selenium and undetected_webdriver to scrape and download from nHentai.net

### Installation
- ``git clone https://github.com/Charlzk05/nhentai_net.git``
- ``pip -r install requirements.txt``

### Examples
- Download Manga(URL, Download_Path=None)
```python
import nhentai_net

# Download all panels from manga
nhentai_net.download_manga("https://nhentai.net/g/177013/", "Downloads")
```
- Popular Mangas() - List
```python
import nhentai_net

# Return all current popular mangas
for i in nhentai_net.popular_mangas():
    print(i)
```
- New Uploads() - List
```python
import nhentai_net

# Return all new uploaded mangas
for i in nhentai_net.new_uploads():
    print(i)
```
- Tags(TAG, Popular=False) - List
```python
import nhentai_net

# Return all newly uploaded and all time popular mangas with tags
for i in nhentai_net.tags("yaoi", popular=True):
    print(i)
```
- Random Manga() - List
```python
import nhentai_net

# Return Random Manga
for i in nhentai_net.random_manga():
    print(i)
```
- Scrape Manga(URL) - List
```python
import nhentai_net

for i in nhentai_net.scrape_manga("https://nhentai.net/g/177849/"):
    print(i)
```
