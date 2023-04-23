import whois
from datetime import datetime
def expiration_domain_time(domain):
    delta = 0
    rest_time = 0
    try:
        web = whois.whois(domain)
        exp_date = web.expiration_date
        now_time = datetime.now()
        rest_time = exp_date[0] - now_time
    except:
        web = whois.whois(domain)
        exp_date = web.expiration_date
        now_time = datetime.now()
        rest_time = exp_date - now_time
    finally:
        delta = int(rest_time.total_seconds())
        if delta > 31536000:
            return 0
        else:
            return 1

def abnormal(url):
    domain = whois.whois(url)
    print(domain["domain_name"])
    print(url)
    for name in domain["domain_name"]:
        if name in url:
            return 0
    else:
        return 1

def age_of_domain(url):
    domain = whois.whois(url)
    now_time= datetime.now()
    creation_date = domain["creation_date"]
    age_of_domain = now_time - creation_date
    print(age_of_domain)
    print(type(age_of_domain))
    #sprint(domain)
    

age_of_domain('http://fing.uach.mx/')