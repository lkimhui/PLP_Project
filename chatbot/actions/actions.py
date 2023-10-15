# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import random


class ActionGetName(Action):

    def name(self) -> Text:
        return "action_get_username"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        name = next(tracker.get_latest_entity_values("name"), None)
        print(f">>>>> name: {name}")
        
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
        
        required_slots = ["name", "education", "profession", "skillset"]
        
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
        
        response = domain["responses"]["utter_collect_info"][0]
        name = tracker.get_slot("name")
        education = tracker.get_slot("education")
        profession = tracker.get_slot("profession")
        skillset = tracker.get_slot("skillset")
        
        response_text = response["text"].format(name=name, education=education, profession=profession, skillset=skillset)
        
        dispatcher.utter_message(text=response_text)
        
        return []

