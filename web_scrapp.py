import scrapping.examination as examination
import scrapping.expiration as expiration
import scrapping.sockets as sockets
import scrapping.transforms as transforms
import pandas as pd

def do_domain_scrappng(domain,having_IP_address,web_traffic,favicon,google_index,pointing_page,statistical_report,page_rank):
    URL_Length = transforms.longURL(domain)
    Shortening_Service = transforms.shortener(domain)
    having_At_Symbol = transforms.havingAt(domain)
    double_slash_redirecting = transforms.redirecting(domain)
    prefis_suffix = transforms.adding_prefix(domain)
    having_sub_domain = transforms.dots_in_domain(domain)
    SSLfinal_state = sockets.sslauthor(domain)
    Domain_registration_length = expiration.expiration_domain_time(domain)
    using_non_standard_port = sockets.ports_results(domain)
    Https_token = transforms.https(domain)
    RequestURL = examination.examination(domain)
    URL_Anchor = examination.examinationTags(domain)
    Link_in_tags = examination.link_in_meta_scrip_tags(domain)
    sfh = examination.server_form_handler(domain)
    submitting_to_email = examination.mail_or_mailto(domain)
    abnormal = expiration.abnormal(domain)
    redirect = examination.redirections(domain)
    on_mouseover = examination.mouseOver(domain)
    right_click = examination.rigthClick(domain)
    pop_up_window = examination.pop_up_window(domain)
    I_frame = examination.iframe(domain)
    age_of_domain = expiration.age_of_domain(domain)
    DNS_record = expiration.DNS_record(domain)
    
    data = pd.DataFrame({
    "having_IP_Address":[having_IP_address],
    "URL_Length":[URL_Length],
    "Shortining_Service":[Shortening_Service],
    "having_At_Symbol":[having_At_Symbol],
    "double_slash_redirecting":[double_slash_redirecting],
    "Prefix_Suffix":[prefis_suffix],
    "having_Sub_Domain":[having_sub_domain],
    "SSLfinal_State":[SSLfinal_state],
    "Domain_registeration_length":[Domain_registration_length],
    "Favicon":[favicon],
    "port":[using_non_standard_port],
    "HTTPS_token":[Https_token],
    "Request_URL":[RequestURL],
    "URL_of_Anchor":[URL_Anchor],
    "Links_in_tags":[Link_in_tags],
    "SFH":[sfh],
    "Submitting_to_email":[submitting_to_email],
    "Abnormal_URL":[abnormal],
    "Redirect":[redirect],
    "on_mouseover":[on_mouseover],
    "RightClick":[right_click],
    "popUpWidnow":[pop_up_window],
    "Iframe":[I_frame],
    "age_of_domain":[age_of_domain],
    "DNSRecord":[DNS_record],
    "web_traffic":[web_traffic],
    "Page_Rank":[page_rank],
    "Google_Index":[google_index],
    "Links_pointing_to_page":[pointing_page],
    "Statistical_report":[statistical_report]
    })
    return data

