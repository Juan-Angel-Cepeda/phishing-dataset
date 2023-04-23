

def longURL(domain):
    long = len(domain)
    if long >= 54 and long <= 75:
        return 0
    elif long < 52:
        return 1
    else:
        return -1

def shortener(domain):
    if 'bit.ly' in domain:
        return 0
    else:
        return 1
    
def havingAt(domain):
    if '@' in domain:
        return 0
    else:
        return 1

def redirecting(domain):
    nohttps = domain[7:]
    if '//' in nohttps:
        return 1
    else:
        return 0

def adding_prefix(domain):
    if '-' in domain:
        return 0
    else:
        return 1

def dots_in_domain(domain):
    counter = 0
    dot = '.'
    
    for symbol in domain:
        if symbol == dot:
            counter = counter + 1
    
    if counter == 2:
        return -1
    elif counter == 3:
        return 0
    else:
        return 1

def https(domain):
    httpsverified = domain[:7]
    if('https' in httpsverified):
        return -1
    else:
        return 0


