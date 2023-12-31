from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch


def call_t5_base_fine_tune_512(model_name, input):
    cover_letter = ""

    # Load the tokenizer
    print("Loading Model...")
    tokenizer = T5Tokenizer.from_pretrained('t5-base', model_max_length=1024)
    model = T5ForConditionalGeneration.from_pretrained("ShashiVish/t5-base-fine-tune-1024-cover-letter", max_length=2044)

    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model.to(device)

    # job_title = "Senior Java Developer"
    # preferred_qualification = "5+ years of Java, Spring Boot"
    # hiring_company_name = "Netflix"
    # user_name = "Emily Evans"
    # past_working_experience = "Java Developer at XYZ for 4 years"
    # current_working_experience = "Senior Java Developer at ABC for 1 year"
    # skilleset = "Java, Spring Boot, Microservices, SQL, AWS"
    # qualification = "Master's in Computer Science"

    job_title = input['job_title']
    preferred_qualification = input['preferred_qualification']
    hiring_company_name = input['hiring_company_name']
    user_name = input['user_name']
    past_working_experience = input['past_working_experience']
    current_working_experience = input['current_working_experience']
    skillset = input['skillset']
    qualification = input['qualification']

    input_text = f" Generate Cover Letter for Role: {job_title}, \
     Preferred Qualifications: {preferred_qualification}, \
     Hiring Company: {hiring_company_name}, User Name: {user_name}, \
     Past Working Experience: {past_working_experience}, Current Working Experience: {current_working_experience}, \
     Skillsets: {skillset}, Qualifications: {qualification} "

    print("Making Prediction...")
    # Tokenize and generate predictions
    input_ids = tokenizer.encode(input_text, return_tensors='pt', max_length=1024, truncation=False, padding=True)
    input_ids = input_ids.to(device)
    output_ids = model.generate(input_ids)

    # Decode the output
    output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)

    cover_letter = output_text
    return cover_letter
