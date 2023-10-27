# from llm import *
import main as llm

def prepare_input(user_name, job_title, qualification, skillset, past_working_experience, preferred_qualification=None, hiring_company_name="ABC Company & Co", current_working_experience=None):
    return {
        "user_name": user_name,
        "job_title": job_title,
        "qualification": qualification,
        "skillset": skillset,
        "preferred_qualification": preferred_qualification,
        "hiring_company_name": hiring_company_name,
        "past_working_experience": past_working_experience,
        "current_working_experience": current_working_experience
    }
    
input = prepare_input("Eve", "Senior Software Engineer", "Master in ", "SQL, Python, Tableau, Data Analysis, Algorithm", "Software Engineer at Meta", "3+ years in multi-thread networking development", "ABC Company & Co", "Senior Software Engineer at Meta")

letter = llm.generate_cover_letter(input=input, model_name="t5-base-fine-tune-1024")

print(letter)