from llm.prediction import generate_cover_letter

if __name__ == '__main__':
    model_name="t5-base-fine-tune-1024"
    input = {}

    input['job_title'] = "Senior Java Developer"
    input['preferred_qualification'] = "5+ years of Java, Spring Boot"
    input['hiring_company_name'] = "Netflix"
    input['user_name'] = "Emily Evans"
    input['past_working_experience'] = "Java Developer at XYZ for 4 years"
    input['current_working_experience'] = "Senior Java Developer at ABC for 1 year"
    input['skillset'] = "Java, Spring Boot, Microservices, SQL, AWS"
    input['qualification'] = "Master's in Computer Science"

    cover_letter = generate_cover_letter(input, model_name=model_name)

    print("Cover Letter Generated  : ", cover_letter)
