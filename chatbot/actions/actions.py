# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

import random
import time
from typing import Any, Dict, List, Text

from llm import *
from llm import prediction as llm_model
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher


class ActionGetName(Action):

    def name(self) -> Text:
        return "action_ask_form_permission"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        name = next(tracker.get_latest_entity_values("name"), None)
        
        # send message to greet user based on name
        # meanwhile request for user's acknowledgement
        messages = [
            f"Nice to meet you {name}. ",
            f"Hey {name}. Nice to meet you. ",
            f"Cool {name}. Nice to serve you today. ",
            f"Hi {name}. It's my pleasure to serve you today. "
                   ]
        ask_more_details = domain["responses"]["utter_request_details"]
        message = messages[random.randint(0, len(messages)-1)] + "\n" + ask_more_details[random.randint(0, len(ask_more_details)-1)]["text"]
        
        # send a default message whenever NLU confidence is low
        rephrase_messages = domain["responses"]["utter_default"]
        rephrase = rephrase_messages[random.randint(0, len(rephrase_messages)-1)]["text"]
        
        if name:
            dispatcher.utter_message(text=message)
        else:
            dispatcher.utter_message(text=rephrase)

        return []
    
    
class ActionProcessUserForm(Action):

    def name(self) -> Text:
        return "action_process_user_form"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        thankyou_messages = [
            "Thank you. Let's start.",
            "So great to hear that. Let's jump into the topics.",
            "Great to hear that. Let's begin with the first topic.",
            "My pleasure to hear that. Let's start.",
            "Great! Let's start. "
        ]
        
        message = thankyou_messages[random.randint(0, len(thankyou_messages)-1)]

        dispatcher.utter_message(text=message)

        return []
    
    
class ValidateUserForm(Action):

    def name(self) -> Text:
        return "user_details_form"

    async def run(self, 
                  dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        required_slots = ["name", "qualification", "title", "skillset"]
        
        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                return [SlotSet('requested_slot', slot_name)]
        
        return [SlotSet('requested_slot', None)]


class ActionSubmit(Action):
    
    def name(self) -> Text: 
        return "action_submit_user_form"
    
    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        collect_into_messages = domain["responses"]["utter_collect_info"]
        acknowledgement_messages = domain["responses"]["utter_request_acknowledgement"]
        response = collect_into_messages[random.randint(0, len(collect_into_messages) - 1)]["text"]
        acknowledgement = acknowledgement_messages[random.randint(0, len(acknowledgement_messages)-1)]["text"]
        
        # get required slots
        name = tracker.get_slot("name")
        qualification = tracker.get_slot("qualification")
        title = tracker.get_slot("title")
        skillset = list(dict.fromkeys(tracker.get_slot("skillset")))
        
        # get optional slot
        principle = tracker.get_slot("principle")
        seniority = tracker.get_slot("seniority")
        
        response_text = response.format(name=name, qualification=qualification, title=title, skillset=skillset, principle=principle, seniority=seniority) + acknowledgement
        
        dispatcher.utter_message(text=response_text)
        
        return []
    
class ActionGenerateCoverLetter(Action):
    
    def name(self) -> Text:
        return "action_generate_cover_letter"
    
    async def run(self, dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # get required slots
        name = tracker.get_slot("name")
        qualification = tracker.get_slot("qualification")
        title = tracker.get_slot("title")
        skillset = list(dict.fromkeys(tracker.get_slot("skillset")))
        
        # get optional slot
        principle = tracker.get_slot("principle") if tracker.get_slot("principle") is not None else ""
        seniority = tracker.get_slot("seniority") if tracker.get_slot("seniority") is not None else ""
        
        # generate cover letter
        MODEL_NAME = "t5-base-fine-tune-1024"
        input = prepare_input(user_name=name, current_working_experience=seniority+" "+title, qualification=qualification+" "+principle, skillset=skillset)
        letter = llm_model.generate_cover_letter(model_name=MODEL_NAME, input=input)
        
        gratitude_messages = domain["responses"]["utter_express_gratitude"]
        express_gratitude = gratitude_messages[random.randint(0, len(gratitude_messages)-1)]["text"]
        present_cv = "Here is the cover letter:\n"
        technical_error = "Sorry, seems like we encountered a technical error. Please try again later."
        
        if (len(letter) > 0):
            dispatcher.utter_message(present_cv+"\n"+letter+"\n")
            time.sleep(1)
            dispatcher.utter_message(express_gratitude)
        else:
            dispatcher.utter_message(technical_error)

        return []
        

def prepare_input(user_name, current_working_experience, qualification, skillset, preferred_qualification=None, hiring_company_name="ABC Company & Co", job_title=None, past_working_experience=None):
    return {
        "user_name": user_name,
        "job_title": current_working_experience, # job title is make up, match with current title
        "qualification": qualification,
        "skillset": skillset,
        "preferred_qualification": preferred_qualification,
        "hiring_company_name": hiring_company_name,
        "past_working_experience": past_working_experience,
        "current_working_experience": current_working_experience
    }

