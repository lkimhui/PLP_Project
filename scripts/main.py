from prediction import generate_cover_letter

if __name__ == '__main__':
    model_name = "t5-base-fine-tune-512"
    intput = {}

    intput['job_title'] = "Senior Java Developer"
    intput['preferred_qualification'] = "5+ years of Java, Spring Boot"
    intput['hiring_company_name'] = "Netflix"
    intput['user_name'] = "Emily Evans"
    intput['past_working_experience'] = "Java Developer at XYZ for 4 years"
    intput['current_working_experience'] = "Senior Java Developer at ABC for 1 year"
    intput['skilleset'] = "Java, Spring Boot, Microservices, SQL, AWS"
    intput['qualification'] = "Master's in Computer Science"

    cover_letter = generate_cover_letter(model_name, intput)

    print("Cover Letter Generated  : ", cover_letter)
