from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from selenium.common.exceptions import TimeoutException
import urllib.request, os

def download_manga(url:str=None, download_path:str=None):
    if "nhentai.net" in url:
        browser = uc.Chrome(use_subprocess=True)
        browser.get(url)

        try:
            WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID, "messages")))

            title = browser.find_element(by=By.CLASS_NAME, value="pretty").text
            pages = browser.find_elements(by=By.CLASS_NAME, value="thumb-container")
            print(f"Manga Title: {title}\nPages: {len(pages)}")

            panel_links = []
            gallerythumb = browser.find_elements(by=By.CLASS_NAME, value="gallerythumb")

            for i in gallerythumb:
                panel_links.append(i.get_attribute("href"))

            for i in range(len(panel_links)):
                browser.get(panel_links[i])
                img = browser.find_elements(by=By.TAG_NAME, value="img")[1]
                img_src = img.get_attribute("src")
                split_link = img_src.split("/")

                if download_path == None:
                    try:
                        urllib.request.urlretrieve(img_src, f"./{split_link[4]}-{split_link[5]}")
                    except:
                        return "Something went wrong download the pages, Please try again..."
                else:
                    try:
                        urllib.request.urlretrieve(img_src, f"{os.path.abspath(download_path)}/{split_link[4]}-{split_link[5]}")
                    except:
                        return "Something went wrong download the pages, Please try again..."

                print(f"{split_link[4]}-{split_link[5]} Download Complete!")

            browser.quit()
            return "Done Downloading!"
        except TimeoutException:
            return "TimeoutException: Loading took so much time!"
    else:
        return "Are you sure this is the website?"

def popular_mangas():
    browser = uc.Chrome(use_subprocess=True)
    browser.get("https://nhentai.net")

    try:
        WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "gallery")))

        popular_list = []
        popular = browser.find_elements(by=By.CLASS_NAME, value="gallery")
        for i in popular[0:5]:
            caption = i.find_element(by=By.CLASS_NAME, value="caption")
            popular_list.append(caption.text)
            
        browser.quit()
        return popular_list
        
    except TimeoutException:
        return "TimeoutException: Loading took so much time!"

def new_uploads():
    browser = uc.Chrome(use_subprocess=True)
    browser.get("https://nhentai.net")

    try:
        WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "gallery")))

        uploads = []
        new_uploads = browser.find_elements(by=By.CLASS_NAME, value="gallery")
        for i in new_uploads[5:30]:
            caption = i.find_element(by=By.CLASS_NAME, value="caption")
            uploads.append(caption.text)

        browser.quit()
        return uploads
        
    except TimeoutException:
        return "TimeoutException: Loading took so much time!"

def tag(tag:str=None, popular:bool=None):
    if tag == None:
        return
    else:
        if popular == None:
            browser = uc.Chrome(use_subprocess=True)
            browser.get(f"https://nhentai.net/tag/{tag}/popular")

            try:
                WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "gallery")))

                mangas = []
                container = browser.find_elements(by=By.CLASS_NAME, value="gallery")
                for i in container:
                    caption = i.find_element(by=By.CLASS_NAME, value="caption")
                    mangas.append(caption.text)

                browser.quit()
                return mangas

            except TimeoutException:
                return "TimeoutException: Loading took so much time!"
        else:
            browser = uc.Chrome(use_subprocess=True)
            browser.get(f"https://nhentai.net/tag/{tag}")

            try:
                WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "gallery")))

                mangas = []
                container = browser.find_elements(by=By.CLASS_NAME, value="gallery")
                for i in container:
                    caption = i.find_element(by=By.CLASS_NAME, value="caption")
                    mangas.append(caption.text)

                browser.quit()
                return mangas

            except TimeoutException:
                return "TimeoutException: Loading took so much time!"

def random_manga():
    browser = uc.Chrome(use_subprocess=True)
    browser.get("https://nhentai.net/random")

    try:
        WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "gallery")))

        title = browser.find_element(by=By.CLASS_NAME, value="pretty").text
        id = browser.find_element(by=By.ID, value="gallery_id").text
        tags = []
        for i in browser.find_elements(by=By.CLASS_NAME, value="name"):tags.append(i.text)
        pages = browser.find_elements(by=By.CLASS_NAME, value="gallerythumb")

        browser.quit()
        return (f"Title: {title}"), (f"ID: {id}"), (f"Tags: {tags}"), (f"Number of Pages: {len(pages)}")

    except TimeoutException:
        return "Loading took so much time!"

def scrape_manga(url:str=None):
    if "nhentai.net" in url:
        browser = uc.Chrome(use_subprocess=True)
        browser.get(url)

        try:
            WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID, "messages")))

            try:
                title = browser.find_element(by=By.CLASS_NAME, value="pretty").text
                id = browser.find_element(by=By.ID, value="gallery_id").text
                tags = []
                for i in browser.find_elements(by=By.CLASS_NAME, value="name"):tags.append(i.text)
                pages = browser.find_elements(by=By.CLASS_NAME, value="gallerythumb")

                browser.quit()
                return (f"Title: {title}"), (f"ID: {id}"), (f"Tags: {tags}"), (f"Number of Pages: {len(pages)}")
            except:
                return "Something went wrong, Please try again..."

        except TimeoutException:
            return "TimeoutException: Loading took so much time!"
    elif url == None:
        return
    else:
        return "Are you sure this is the website?"