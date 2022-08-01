## nhentai_net
nHentai.net Scraper and Downloader
- Uses selenium and undetected_webdriver to scrape nHentai.net

### Examples
- Download Manga
```python
import nhentai_net

# Download all panels from manga
nhentai_net.download_manga("https://nhentai.net/g/177013/")
```
- Popular Mangas (list)
```python
import nhentai_net

# Return all current popular mangas
for i in nhentai_net.popular_mangas():
    print(i)
```
- New Uploads (list)
```python
import nhentai_net

# Return all new uploaded mangas
for i in nhentai_net.new_uploads():
    print(i)
```
- Tags (list)
```python
import nhentai_net

# Return all newly uploaded and all time popular mangas with tags
for i in nhentai_net.tags("yaoi", popular=True):
    print(i)
```
- Random Manga (list)
```python
import nhentai_net

# Return all newly uploaded and all time popular mangas with tags
for i in nhentai_net.tags("yaoi", popular=True):
    print(i)
```
- 
