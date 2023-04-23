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

