import socket
import ssl

def ports_results(domain):
    try:
        create_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        count = 0
        ports = [21,22,23,80,443,445,1433,1521,3306,3389]
        results = []
    
        for port in ports:
            destination = (domain,port)
            result = create_socket.connect_ex(destination)
            results.append(result)
    except:
        for i in range(10):
          results.append(1)
    
    finally:    
        if results[3] == 0 or results[4] == 0:
            for res in results[:2]:
                if res == 0:
                    count = count + 1
            for res in results[5:]:
                if res == 0:
                    count = count + 1
        if count > 0:
            return 0
        else:
            return 1

def sslauthor(domain):
    try:
        port = 443
        context = ssl.create_default_context()
        with socket.create_connection((domain,port)) as sock:
            with context.wrap_socket(sock,server_hostname=domain) as ssock:
                certificate = ssock.getpeercert()
        valid = ssl.match_hostname(certificate,domain)
    except:
        valid = 0
    finally:
        if valid == None:
            return 1
        else:
            return 0


