import streamlit as st
import numpy as np   
from sklearn.tree import DecisionTreeClassifier 
import pickle 

@st.cache_resource()
def load_classifier():
    pickle_in = open('decision_tree_model.pkl', 'rb')
    return pickle.load(pickle_in) 

classifier = load_classifier() 

yes_no = {"Yes":1, "No":0} 
p_m_e = {"poor":0, "medium":1, "excellent":2} 
cert_dict = {'app development':0, 'distro making':1, 'full stack':2, 'hadoop':3, 'information security':4, 'machine learning':5, 'python':6, 'r programming':7, 'shell programming':8} 
workshops_dict = {'cloud computing':0, 'data science':1, 'database security':2, 'game development':3, 'hacking':4, 'system designing':5, 'testing':6, 'web technologies':7} 
subjects_dict = {'Computer Architecture': 0, 'IOT': 1, 'Management': 2, 'Software Engineering': 3, 'cloud computing': 4, 'data engineering': 5, 'hacking': 6, 'networks': 7, 'parallel computing': 8, 'programming': 9} 
career_dict = {'Business process analyst': 0, 'cloud computing': 1, 'developer': 2, 'security': 3, 'system developer': 4, 'testing': 5}
company_dict = {'BPA': 0, 'Cloud Services': 1, 'Finance': 2, 'Product based': 3, 'SAaS services': 4, 'Sales and Marketing': 5, 'Service Based': 6, 'Testing and Maintenance Services': 7, 'Web Services': 8, 'product development': 9}
books_dict = {'Action and Adventure': 0, 'Anthology': 1, 'Art': 2, 'Autobiographies': 3, 'Biographies': 4, 'Childrens': 5, 'Comics': 6, 'Cookbooks': 7, 'Diaries': 8, 'Dictionaries': 9, 'Drama': 10, 'Encyclopedias': 11, 'Fantasy': 12, 'Guide': 13, 'Health': 14, 'History': 15, 'Horror': 16, 'Journals': 17, 'Math': 18, 'Mystery': 19, 'Poetry': 20, 'Prayer books': 21, 'Religion-Spirituality': 22, 'Romance': 23, 'Satire': 24, 'Science': 25, 'Science fiction': 26, 'Self help': 27, 'Series': 28, 'Travel': 29, 'Trilogy': 30}
job_dict = {"job": 0, "higherstudies": 1} 
behavior_dict = {"gentle": 0, "stubborn": 1} 
mt_dict = {"Management": 0, "Technical": 1} 
worker_dict = {"hard worker": 0, "smart worker": 1} 

def predict(com, hr, lq, hack, code, speak, long, self_learn, course, test, olympiads, read, memory, job_hs, inputs, games, behavior, mt, worker, teams, intro, cert, workshops, sub, career, company, books): 
    inp = np.array([[com, hr, lq, hack, code, speak, yes_no[long], yes_no[self_learn], yes_no[course], yes_no[test], yes_no[olympiads], p_m_e[read], p_m_e[memory], job_dict[job_hs], yes_no[inputs], yes_no[games], behavior_dict[behavior], mt_dict[mt], worker_dict[worker], yes_no[teams], yes_no[intro], cert_dict[cert], workshops_dict[workshops], subjects_dict[sub], career_dict[career], company_dict[company], books_dict[books]]]) 
    pred = classifier.predict(inp) 
    return pred

def main(): 
    st.title("Choose your Career") 
    com = st.number_input("Percentage in Communication Skills") 
    hr = st.number_input("Hours working per day")  
    lq = st.number_input("Logical Quotient rating (1-9)") 
    hack = st.number_input("Hackathons (0-6)") 
    code = st.number_input("Coding skills rating (1-9)") 
    speak = st.number_input("Public speaking points (1-9)") 
    long = st.selectbox("Can work long time before system?", ["Yes", "No"]) 
    self_learn = st.selectbox("Self-learning capability", ["Yes", "No"]) 
    course = st.selectbox("Extra-courses did?", ["Yes", "No"]) 
    test = st.selectbox("Talent tests taken?", ["Yes", "No"]) 
    olympiads = st.selectbox("Olympiads", ["Yes", "No"]) 
    read = st.selectbox("Reading and writing skills", ["poor", "medium", "excellent"])  
    memory = st.selectbox("Memory capability score", ["poor", "medium", "excellent"]) 
    job_hs = st.selectbox("Job/Higher studies", ["job", "higherstudies"]) 
    inputs = st.selectbox("Taken inputs from seniors or elders", ["Yes", "No"])
    games = st.selectbox("Interested in games", ["Yes", "No"]) 
    behavior = st.selectbox("Gentle or Tuff behavior", ["gentle", "stubborn"]) 
    mt = st.selectbox("Management or Technical", ["Management", "Technical"]) 
    worker = st.selectbox("Hard/smart worker", ["hard worker", "smart worker"]) 
    teams = st.selectbox("Worked in teams ever?", ["Yes", "No"]) 
    intro = st.selectbox("Introvert?", ["Yes", "No"]) 
    cert = st.selectbox("Certifications", ['app development', 'distro making', 'full stack', 'hadoop', 'information security', 'machine learning', 'python', 'r programming', 'shell programming'])
    workshops = st.selectbox("Workshops", ['cloud computing', 'data science', 'database security', 'game development', 'hacking', 'system designing', 'testing', 'web technologies']) 
    sub = st.selectbox("Interested subject", ['Computer Architecture', 'IOT', 'Management', 'Software Engineering', 'cloud computing', 'data engineering', 'hacking', 'networks', 'parallel computing', 'programming'])
    career = st.selectbox('Interested career area', ['Business process analyst', 'cloud computing', 'developer', 'security', 'system developer', 'testing']) 
    company = st.selectbox('Type of company want to settle in?', ['BPA', 'Cloud Services', 'Finance', 'Product based', 'SAaS services', 'Sales and Marketing', 'Service Based', 'Testing and Maintenance Services', 'Web Services', 'product development'])
    books = st.selectbox('Interested Type of books', ['Action and Adventure', 'Anthology', 'Art', 'Autobiographies', 'Biographies', 'Childrens', 'Comics', 'Cookbooks', 'Diaries', 'Dictionaries', 'Drama', 'Encyclopedias', 'Fantasy', 'Guide', 'Health', 'History', 'Horror', 'Journals', 'Math', 'Mystery', 'Poetry', 'Prayer books', 'Religion-Spirituality', 'Romance', 'Satire', 'Science', 'Science fiction', 'Self help', 'Series', 'Travel', 'Trilogy']) 
    if st.button('Predict'): 
        pred = predict(com, hr, lq, hack, code, speak, long, self_learn, course, test, olympiads, read, memory, job_hs, inputs, games, behavior, mt, worker, teams, intro, cert, workshops, sub, career, company, books) 
        st.success(pred[0])

if __name__ == '__main__':
    main()
    