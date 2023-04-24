import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from selenium import webdriver

def examination(domain):
    try:
        response = requests.get(domain)
        soup = BeautifulSoup(response.content,'html.parser')
        images = soup.find_all('img')
        results = []
    
        for img in images:
            image_url = img['src']
            image_domain = urlparse(image_url).netloc
            page_domain = urlparse(domain).netloc

            if image_domain != page_domain:
                results.append(1)

        bad_req = len(results)
        tot_req = len(images)
        if  tot_req == bad_req:
            return 1
        else:
            return -1
    finally:
        return -1
        
def examinationTags(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content,'html.parser')
        domain = urlparse(url).netloc
        results = []
        iteration = []
    
        for a in soup.find_all('a'):
            iteration.append(1)
            href = a.get('href')
            if href is None:
                continue
            href_domain = urlparse(href).netloc

            if href_domain != domain:
                results.append(1)
            elif href.startswith('#') or href.startswith('javascript'):
                print('does not link')
        req = len(results)
        tot_req = len(iteration)
        if  tot_req == req:
            return 1
        else:
            return -1
    finally:
        return -1

def link_in_meta_scrip_tags(url):
    try:
        differences = []
        response = requests.get(url)
        html_content = response.text
        soup = BeautifulSoup(html_content,"html.parser")
        meta_tags = soup.find_all("meta")
        script_tags = soup.find_all("script")
        domain = urlparse(url).netloc
    
        for tag in meta_tags + script_tags:
            if "src" in tag.attrs:
                src_domain = urlparse(tag["src"]).netloc
                if src_domain != domain:
                    differences.append(1)
            if "href" in tag.attrs:
                href_domain = urlparse(tag["href"]).netloc
                if href_domain != domain:
                    differences.append(1)
        tot_differences = len(differences)
        tot = len(meta_tags+script_tags)
        if tot_differences < (tot*.31):
            return 1
        if tot_differences < (tot*67):
            return -1
        else:
            return 0
    finally:
        return 0

def server_form_handler(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        form = soup.find("form")
    
        if form and "action" in form.attrs:
            action_url = urlparse(form["action"])
            if action_url.netloc != urlparse(url).netloc:
                return 0
            if action_url.netloc == " ":
                return -1
            else:
                return 1
    finally:
        return 1

def mail_or_mailto(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
    
        mail_links = soup.find_all(string=lambda text:text and("mail()"in text or "mailto" in text))
        if len(mail_links) != 0 :
            return -1
        else:
            return 1
    finally:
        return 1

def redirections(url):
    try:
        num_redirections = 0
        response = requests.get(url,allow_redirects=True)
    
        while response.history:
            num_redirections += 1
            response = requests.get(response.url,allow_redirects=True)
        if num_redirections <= 1:
            return 0
        else:
            return 1
    finally:
        return 1


def mouseOver(url):
    try:
        response = requests.get(url)
        html = response.content
        soup = BeautifulSoup(html,'html.parser')
        mouseover_links = soup.find_all('a',attrs={'onmouseover':True})
    
        for link in mouseover_links:
            if "window.status" in link['onmouseover']:
                return 0
    finally:    
        return 1

def rigthClick(url):
    try:
        response = requests.get(url)
        html = response.content
        soup = BeautifulSoup(html,'html.parser')
        bodies = soup.find_all('body')
    
        for body in bodies:
            if 'oncontextmenu' in body.attrs:
                return 0
    finally:        
        return 1

def pop_up_window(url):
    try:
        driver = webdriver.Chrome()
        driver.get(url)
    
        if len(driver.window_handles) > 1:
            driver.quit()
            return 0
        else:
            driver.quit()
            return 1
    finally:
        return 1

def iframe(url):
    try:
        response = requests.get(url)
        html = response.content
        soup = BeautifulSoup(html,'html.parser')
        iframes = soup.find_all('iframe')
        print(len(iframes))
    
        if len(iframes) > 0:
            return 0
        else:
            return 1
    finally:
        return 1


    
    