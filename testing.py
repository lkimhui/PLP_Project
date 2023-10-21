from scripts import *
from scripts import main as llm

def prepare_input(user_name, qualification, skillset, current_working_experience, past_working_experience, hiring_company_name="ABC Company & Co", job_title=None, preferred_qualification=None):
    return {
        "user_name": user_name,
        "job_title": job_title, #requirement - job role applied to
        "qualification": qualification,
        "skillset": skillset,
        "preferred_qualification": preferred_qualification,
        "hiring_company_name": hiring_company_name,
        "past_working_experience": past_working_experience,
        "current_working_experience": current_working_experience
    }
    
input = prepare_input("Eve", "Master in Computer Science", "SQL, Python, Tableau, Data Analysis, Algorithm", "Senior Data Scientist", "Data Analyst at Meta")

output = llm.generate_cover_letter(input=input, model_name="t5-base-fine-tune-1024")
print(output)