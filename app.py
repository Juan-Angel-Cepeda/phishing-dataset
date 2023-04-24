import streamlit as st
import prediction
import web_scrapp

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

st.divider()

having_IP_address = st.selectbox(
    'The page to analyze is an ip address insted of a domain',
    ['yes','no']
)
if having_IP_address == 'yes':
    having_IP_address = 1
else:
    having_IP_address = 0

st.divider()

st.text('Go to: https://www.similarweb.com/ and paste the domain to analyze.')
web_traffic = st.selectbox("Does the domain analized is listed in ranking 100,000?",
                        ['Yes','No','domain was not found'])
if web_traffic == 'Yes':
    web_traffic = -1
elif web_traffic == 'No':
    web_traffic = 0
elif web_traffic == 'domain was not found':
    web_traffic == 1
else:
    web_traffic = 0
    
st.divider()

favicon = st.selectbox(
    'The page to analyze has a favIcon',
    ['yes','no']   
)
if favicon == 'yes':
    favicon = 1
else:
    favicon = 0

st.divider()

st.text('Go to google and write "site:"example.com" replacing example by the domain to analyze.')
google_index = st.selectbox('Does the searched domain shows in the results?',
                            ['yes','no'])
if google_index == 'yes':
    google_index = 1
else:
    google_index = -1

st.divider()

st.text('How did you reach the website to analyze?')
pointing_page = st.selectbox('Through a link in a known web, others (social, text message,not known website) or you trust the website',
             ['Known website','Trust','other'])
if pointing_page == 'Known website':
    pointing_page = -1
elif pointing_page == 'Trust':
    pointing_page = 0
else:
    pointing_page = 1

st.divider()

st.text('Go to https://phishtank.org/ and check if the website is listed there')
statisitcal_report = st.selectbox('Is it listed?',
                            ['yes','no'])
if statisitcal_report == 'yes':
    statisitcal_report = -1
else:
    statisitcal_report = 1
    
page_rank = -1 * web_traffic
if page_rank == 0:
    page_rank = -1

if st.button('Predict'):
    st.spinner('Checking ports, domains, DNS, etc...')
    data = web_scrapp.do_domain_scrappng(
        domain,
        having_IP_address,
        web_traffic,
        favicon,
        google_index,
        pointing_page,
        statisitcal_report,
        page_rank
        )
    preditcion_result = prediction.preditct(data,model)
    try:
        if preditcion_result == -1:
            st.error('The website is phishing')    
        else:
            st.success('The website is secure')
    finally:
        st.error('Website does not have enough information')
    
#boton con predicción lanza la función de scrapp

    