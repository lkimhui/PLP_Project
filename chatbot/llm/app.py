import streamlit as st
from prediction import generate_cover_letter
import  time

models = ["t5-base-fine-tune-1024"]


# Streamlit UI
st.title("Cover Letter Generator")

model_name = st.selectbox("Select Model for Cover Letter Generation", models, index=0)  # The index parameter sets the default selection

job_title = st.text_input("Job Title", "Senior Java Developer")
preferred_qualification = st.text_input("Preferred Qualifications", "5+ years of Java, Spring Boot")
hiring_company_name = st.text_input("Hiring Company Name", "Netflix")
user_name = st.text_input("User Name", "Emily Evans")
past_working_experience = st.text_input("Past Working Experience", "Java Developer at XYZ for 4 years")
current_working_experience = st.text_input("Current Working Experience", "Senior Java Developer at ABC for 1 year")
skilleset = st.text_input("Skillset", "Java, Spring Boot, Microservices, SQL, AWS")
qualification = st.text_input("Qualifications", "Master's in Computer Science")

if st.button("Generate Cover Letter"):
    input_data = {
        'job_title': job_title,
        'preferred_qualification': preferred_qualification,
        'hiring_company_name': hiring_company_name,
        'user_name': user_name,
        'past_working_experience': past_working_experience,
        'current_working_experience': current_working_experience,
        'skilleset': skilleset,
        'qualification': qualification
    }
    cover_letter = generate_cover_letter(model_name ,input_data)

    #cover_letter = " I am writing to express my interest in the Data Scientist position at XYZ Corporation. With a strong background in data science and machine learning, I believe I have the skills and qualifications necessary to contribute to your team. In my previous role as a Data Analyst at ABC Company, I gained experience in developing and shipping production grade machine learning systems. I have a solid understanding of data science and machine learning, with a focus on developing and shipping production grade systems. Additionally, I have years of experience in building and shipping data science based personalization services and recommendation systems. I hold a BSc in Computer Science and have 5+ years of experience in data science and machine learning. I am proficient in Python, R, scikit-learn, Keras, and Tensorflow. I am confident that my strong analytical and data science skills, combined with my passion for leveraging data to drive business decisions, make me an ideal candidate for this position. Thank you for considering my application. I look forward to the opportunity to contribute to the success of XYZ Corporation. Sincerely, John Smith"

    st.subheader("Generated Cover Letter:")
    full_response = ""
    message_placeholder = st.empty()

    for chunk in cover_letter.split():
        full_response += chunk + " "
        time.sleep(0.05)
        # Add a blinking cursor to simulate typing
        message_placeholder.markdown(full_response + "▌")
    message_placeholder.markdown(full_response)
