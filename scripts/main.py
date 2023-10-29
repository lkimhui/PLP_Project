from prediction import generate_cover_letter

if __name__ == '__main__':
    model_name = "t5-base-fine-tune-1024"
    intput = {'job_title': "Senior Java Developer", 'preferred_qualification': "5+ years of Java, Spring Boot",
              'hiring_company_name': "Netflix", 'user_name': "Emily Evans",
              'past_working_experience': "Java Developer at XYZ for 4 years",
              'current_working_experience': "Senior Java Developer at ABC for 1 year",
              'skilleset': "Java, Spring Boot, Microservices, SQL, AWS",
              'qualification': "Master's in Computer Science"}

    cover_letter = generate_cover_letter(model_name, intput)

    print("Cover Letter Generated  : ", cover_letter)
