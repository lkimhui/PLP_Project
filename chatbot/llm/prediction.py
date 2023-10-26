from model_helper import call_t5_base_fine_tune_512


def generate_cover_letter(model_name, input):
    cover_letter = ""

    if model_name == "t5-base-fine-tune-1024":

        cover_letter = call_t5_base_fine_tune_512(model_name,input)

    return cover_letter
