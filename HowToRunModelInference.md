# T5 model Usage

Plese find below example how to generate cover letter for input directly from huggingface.

### Running the model on a GPU


```python
from transformers import T5Tokenizer, T5ForConditionalGeneration
tokenizer = T5Tokenizer.from_pretrained("ShashiVish/t5-base-fine-tune-1024-cover-letter")
model = T5ForConditionalGeneration.from_pretrained("ShashiVish/t5-base-fine-tune-1024-cover-letter" , max_length = 512 , device_map="auto")
job_title = "Senior Java Developer"
preferred_qualification = "3+ years of Java, Spring Boot"
hiring_company_name = "Google"
user_name = "Emily Evans"
past_working_experience= "Java Developer at XYZ for 4 years"
current_working_experience = "Senior Java Developer at ABC for 1 year"
skilleset= "Java, Spring Boot, Microservices, SQL, AWS"
qualification = "Master's in Electronics Science"
input_text = f" Generate Cover Letter for Role: {job_title}, \
 Preferred Qualifications: {preferred_qualification}, \
 Hiring Company: {hiring_company_name}, User Name: {user_name}, \
 Past Working Experience: {past_working_experience}, Current Working Experience: {current_working_experience}, \
 Skillsets: {skilleset}, Qualifications: {qualification} "
# Tokenize and generate predictions
input_ids = tokenizer.encode(input_text, return_tensors='pt', max_length=2048, truncation=False, padding=True)
input_ids = input_ids.to('cuda')
output_ids = model.generate(input_ids)
# Decode the output
output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
print("Generated Cover Letter:")
print(output_text)
```


### Running the model on a CPU


```python
from transformers import T5Tokenizer, T5ForConditionalGeneration
tokenizer = T5Tokenizer.from_pretrained("ShashiVish/t5-base-fine-tune-1024-cover-letter")
model = T5ForConditionalGeneration.from_pretrained("ShashiVish/t5-base-fine-tune-1024-cover-letter" , max_length = 512 )
job_title = "Senior Java Developer"
preferred_qualification = "3+ years of Java, Spring Boot"
hiring_company_name = "Google"
user_name = "Emily Evans"
past_working_experience= "Java Developer at XYZ for 4 years"
current_working_experience = "Senior Java Developer at ABC for 1 year"
skilleset= "Java, Spring Boot, Microservices, SQL, AWS"
qualification = "Master's in Electronics Science"
input_text = f" Generate Cover Letter for Role: {job_title}, \
 Preferred Qualifications: {preferred_qualification}, \
 Hiring Company: {hiring_company_name}, User Name: {user_name}, \
 Past Working Experience: {past_working_experience}, Current Working Experience: {current_working_experience}, \
 Skillsets: {skilleset}, Qualifications: {qualification} "
# Tokenize and generate predictions
input_ids = tokenizer.encode(input_text, return_tensors='pt', max_length=2048, truncation=False, padding=True)
output_ids = model.generate(input_ids)
# Decode the output
output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
print("Generated Cover Letter:")
print(output_text)
```