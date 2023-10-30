# How to Use FineTuned Models from Huggingface

This document provides how you can download fine tuned model from huggingface and generate cover letter by prompting model.

## Pre-requisite 

Please install below python libraries for run model for generating cover letter.

```shell
pip install transformers 
pip install SentencePiece
```

## T5 model Usage

This code serves as an example of using the Hugging Face Transformers library to automate the generation of cover letters for job applications. 
It uses a pre-trained T5 model fine-tuned specifically for this task. 

You can easily customize the input data by changing the values of variables like job_title, preferred_qualifications, hiring_company_name, and others. 
This allows you to generate cover letters tailored to specific job applications.
### Running the model on a GPU


```python
from transformers import T5Tokenizer, T5ForConditionalGeneration

# Load the tokenizer and model
tokenizer = T5Tokenizer.from_pretrained("ShashiVish/t5-base-fine-tune-1024-cover-letter")
model = T5ForConditionalGeneration.from_pretrained("ShashiVish/t5-base-fine-tune-1024-cover-letter", max_length=512, device_map="auto")

# Input data
job_title = "Senior Java Developer"
preferred_qualifications = "3+ years of Java, Spring Boot"
hiring_company_name = "Google"
user_name = "Emily Evans"
past_working_experience = "Java Developer at XYZ for 4 years"
current_working_experience = "Senior Java Developer at ABC for 1 year"
skillset = "Java, Spring Boot, Microservices, SQL, AWS"
qualification = "Master's in Electronics Science"

# Create the input text
input_text = (
    f"Generate Cover Letter for Role: {job_title},\n"
    f"Preferred Qualifications: {preferred_qualifications},\n"
    f"Hiring Company: {hiring_company_name}, User Name: {user_name},\n"
    f"Past Working Experience: {past_working_experience},\n"
    f"Current Working Experience: {current_working_experience},\n"
    f"Skillsets: {skillset},\n"
    f"Qualifications: {qualification}"
)

# Tokenize and generate predictions
input_ids = tokenizer.encode(input_text, return_tensors='pt', max_length=2048, truncation=False, padding=True)
input_ids = input_ids.to('cuda')
output_ids = model.generate(input_ids)

# Decode the output
output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)

# Print the generated cover letter
print("Generated Cover Letter:")
print(output_text)

```


### Running the model on a CPU


```python
from transformers import T5Tokenizer, T5ForConditionalGeneration

# Load the tokenizer and model
tokenizer = T5Tokenizer.from_pretrained("ShashiVish/t5-base-fine-tune-1024-cover-letter")
model = T5ForConditionalGeneration.from_pretrained("ShashiVish/t5-base-fine-tune-1024-cover-letter", max_length=512)

# Input data
job_title = "Senior Java Developer"
preferred_qualifications = "3+ years of Java, Spring Boot"
hiring_company_name = "Google"
user_name = "Emily Evans"
past_working_experience = "Java Developer at XYZ for 4 years"
current_working_experience = "Senior Java Developer at ABC for 1 year"
skillset = "Java, Spring Boot, Microservices, SQL, AWS"
qualification = "Master's in Electronics Science"

# Create the input text
input_text = (
    f"Generate Cover Letter for Role: {job_title},\n"
    f"Preferred Qualifications: {preferred_qualifications},\n"
    f"Hiring Company: {hiring_company_name}, User Name: {user_name},\n"
    f"Past Working Experience: {past_working_experience},\n"
    f"Current Working Experience: {current_working_experience},\n"
    f"Skillsets: {skillset},\n"
    f"Qualifications: {qualification}"
)

# Tokenize and generate predictions
input_ids = tokenizer.encode(input_text, return_tensors='pt', max_length=2048, truncation=False, padding=True)
output_ids = model.generate(input_ids)

# Decode the output
output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)

# Print the generated cover letter
print("Generated Cover Letter:")
print(output_text)

```

## Falcon model Usage
### Running the model on GPU (A100 GPU on Google Colab)

```python
#load the falcon 7b model and tokenize
finetunedmodel = AutoModelForCausalLM.from_pretrained(
    "wanqi27/falcon-7b-finetuned",
    trust_remote_code=True,
)

tokenizer = AutoTokenizer.from_pretrained(
    "wanqi27/falcon-7b-finetuned",
)

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

#creating the prompt
prompt = f"""
    <human>: {input_text}
    <assistant>:
    """.strip()

#encode the prompt
encoding = tokenizer.encode(prompt, return_tensors= "pt", max_length=2048, truncation=False, padding=True)

#import torch
import torch

#set the generation configuration params
gen_config = finetunedmodel.generation_config
gen_config.max_new_tokens = 250
gen_config.temperature = 0.2
gen_config.top_p = 0.7
gen_config.num_return_sequences = 1
gen_config.pad_token_id = tokenizer.eos_token_id
gen_config.eos_token_id = tokenizer.eos_token_id
gen_config.do_sample = True  
gen_config.use_cache = False

#produce a prediction
with torch.inference_mode():
    outputs = finetunedmodel.generate(input_ids=encoding, generation_config=gen_config)

decoded_output = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(decoded_output)

```

## Llama2 model Usage 

Please find below example how using llama2 model loaded from Hugging Face.
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

# Generate cover letters and save them in a new column in an output excel file
df['Generated Cover Letter by 7b-chat-fine-tuned'] = df.apply(generate_cover_letter2, axis=1)
output_file_path = '/content/gdrive/MyDrive/Colab Data/cover_letter_data_test_first10_add2.xlsx'
try:
    df.to_excel(output_file_path, index=False)
    print("Excel file saved successfully.")
except Exception as e:
    print(f"An error occurred while saving the Excel file: {str(e)}")
```

Feel free to raise a pull request for any changes.