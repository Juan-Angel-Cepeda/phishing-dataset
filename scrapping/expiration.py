import whois
from datetime import datetime
import dns.resolver

def expiration_domain_time(domain):
    delta = 0
    rest_time = 0
    try:
        web = whois.whois(domain)
        exp_date = web.expiration_date
        now_time = datetime.now()
        rest_time = exp_date[0] - now_time
        
        web = whois.whois(domain)
        exp_date = web.expiration_date
        now_time = datetime.now()
        rest_time = exp_date - now_time
    except:
        print(type(rest_time))
        delta = int(rest_time.total_seconds())
        if delta > 31536000:
            return 0
        else:
            return 1
    
    finally:
        return 1

def abnormal(url):
    try:
        domain = whois.whois(url)
    
        for name in domain["domain_name"]:
            if name in url:
                return 0
    finally:
        return 1

def age_of_domain(url):
    try:
        domain = whois.whois(url)
        now_time= datetime.now()
        creation_date = domain["creation_date"]
        age_of_domain = now_time - creation_date
        age_of_domain_sec = age_of_domain.total_seconds()
        age_of_domain_sec = round(age_of_domain_sec)
        
        if age_of_domain_sec > 15778476:
            return -1
    
    finally:
        return 1
    
    
def DNS_record(url):
    try:
        domain = whois.whois(url)
        record = domain["domain_name"]
        if 'https' in domain:
            url_without_http = url[8:]
        else:
            url_without_http = url[7:]
        if '/' in url_without_http:
            url_without_http = url_without_http[:-1]
        answers = dns.resolver.resolve(url_without_http)
        name = answers.canonical_name

        if record in name:
            return -1
        else:
            return 1
    finally:
        return 1

