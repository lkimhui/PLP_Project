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

# Falcon model Usage (Additional Notes)




# Llama2 model Usage 

Plese find below example how using llama2 model loaded from Hugging Face.
Note on Prompt format for llama2 chat model (Different from above T5 and Falcon)

### Running the model on GPU (A100 GPU on Google Collab)

```python
from datasets import load_dataset
from transformers import AutoTokenizer
from transformers import pipeline

model2="kwanyick/llama-2-7b-chat-cover-letter"
tokenizer2 = AutoTokenizer.from_pretrained(model2, use_auth_token=True)

# using text-generation pipeline for Llama-2-7b-chat-hf
llama_pipeline2 = pipeline(
    task="text-generation",
    model=model2,
    tokenizer=tokenizer2,
    max_length=400
)

def get_llama_response2(prompt: str) -> None:
    """
    Generate a structured cover letter for given user input.

    Parameters:
        prompt (str): The user's input/question for the model.

    Returns:
        None: Prints the model's response.
    """
    # Format the input to match llama's prompt template
    sequences = llama_pipeline2(f"<s>[INST] {prompt} [/INST]")
    print("Cover letter:", sequences[0]['generated_text'])

# Define the function to generate cover letters using training datasets
# Format the input to match llama's prompt template
def generate_cover_letter2(row):
    prompt = f"""<<SYS>>Generate a structured cover letter for given user input<</SYS>>
      Job Title: {row['Job Title']},
      Preferred Qualifications: {row['Preferred Qualifications']},
      Hiring Company: {row['Hiring Company']},
      Applicant Name: {row['Applicant Name']},
      Past Working Experience: {row['Past Working Experience']},
      Current Working Experience: {row['Current Working Experience']},
      Skillsets: {row['Skillsets']},
      Qualifications: {row['Qualifications']}"""
    generated_text = get_llama_response2(prompt)
    return generated_text

# Define User Inputs
# Run text generation pipeline with our next model
# format the input to match llama e's prompt template
prompt = """<<SYS>>Generate a structured cover letter for given user input<</SYS>>
  Job Title: Data Analyst,
  Preferred Qualifications: Bachelor in Data Science or Economics,
  Hiring Company: Accenture,
  Applicant Name: Oliver Jane,
  Past Work Experience: AI Engineer at Tesla for 2 years,
  Current Working Experience: Generative AI Engineer at Apple for 3 years,
  Skillsets: Python, C++, AI, Machine Learning, Generative Models,
  Qualifications: Masters in Data Science
"""

# Generate cover letters and save them in a new column in an output excel file
df['Generated Cover Letter by 7b-chat-fine-tuned'] = df.apply(generate_cover_letter2, axis=1)
output_file_path = '/content/gdrive/MyDrive/Colab Data/cover_letter_data_test_first10_add2.xlsx'
try:
    df.to_excel(output_file_path, index=False)
    print("Excel file saved successfully.")
except Exception as e:
    print(f"An error occurred while saving the Excel file: {str(e)}")
