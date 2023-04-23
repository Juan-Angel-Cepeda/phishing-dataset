import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def examination(domain):
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
        
def examinationTags(url):
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
    
        
    
#examination('https://hostinger.mx/')
examinationTags('https://hostinger.mx/')
    