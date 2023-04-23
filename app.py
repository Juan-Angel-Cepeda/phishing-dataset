import streamlit as st
import pandas as pd
import prediction
import transforms
import sockets
import expiration
import examination

st.set_page_config(
    page_title= "Phishing predicitons",
    initial_sidebar_state="expanded"
)

st.title("Phishing Predictions")
st.sidebar.title("Models")
model = st.sidebar.selectbox(
    'Select Model',
    [
        'Support Vector Machine',
        'Random Forest Classifier',
        'Extra Trees Classifier'
    ]
)

if model == 'Support Vector Machine':
    st.sidebar.info('Accuracy: 95.39%', icon='✅')
    st.sidebar.info('F1 Score: 95.91%', icon='🎯')
    st.sidebar.info('Precision: 94.62%', icon='👌')
    st.sidebar.info('Recall: 97.24%', icon='🤝')
    st.sidebar.info('AUC: 95.15%', icon='📈')
elif model == 'Random Forest Classifier':
    st.sidebar.info('Accuracy: 97.11%', icon='✅')
    st.sidebar.info('F1 Score: 97.41%', icon='🎯')
    st.sidebar.info('Precision: 96.94%', icon='👌')
    st.sidebar.info('Recall: 97.89%', icon='🤝')
    st.sidebar.info('AUC: 97.01%', icon='📈')
elif model == 'Extra Trees Classifier':
    st.sidebar.info('Accuracy: 91.09%', icon='✅')
    st.sidebar.info('F1 Score: 92.44%', icon='🎯')
    st.sidebar.info('Precision: 87.57%', icon='👌')
    st.sidebar.info('Recall: 97.89%', icon='🤝')
    st.sidebar.info('AUC: 90.22%', icon='📈')
    
domain = st.text_input('Paste your domain')


having_IP_address = st.selectbox(
    'The page to analyze is an ip address insted of a domain',
    ['yes','no']
)
if having_IP_address == 'yes':
    having_IP_address = 1
else:
    having_IP_address = 0


URL_Length = transforms.longURL(domain)
Shortening_Service = transforms.shortener(domain)
having_At_Symbol = transforms.havingAt(domain)
double_slash_redirecting = transforms.redirecting(domain)
prefis_suffix = transforms.adding_prefix(domain)
having_sub_domain = transforms.dots_in_domain(domain)
SSLfinal_state = sockets.sslauthor(domain)
Domain_registration_length = expiration.expiration_domain_time(domain)

favicon = st.selectbox(
    'The page to analyze has a favIcon',
    ['yes','no']   
)
if favicon == 'yes':
    favicon = 1
else:
    favicon = 0
    
using_non_standard_port = sockets.ports_results(domain)
Https_token = transforms.https(domain)
RequestURL = examination.examination(domain)
URL_Anchor = examination.examinationTags(domain)
Link_in_tags = examination.link_in_meta_scrip_tags(domain)
SFH = examination.server_form_handler(domain)
submitting_to_email = examination.mail_or_mailto(domain)
abnormal = expiration.abnormal(domain)
redirect = examination.redirections(domain)
on_mouseover = examination.mouseOver(domain)
right_click = examination.rigthClick(domain)
pop_up_window = examination.pop_up_window(domain)
I_frame = examination.iframe(domain)
age_od_domain = expiration.age_of_domain(domain)
