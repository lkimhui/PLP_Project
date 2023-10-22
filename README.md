# User Guide for ChatGRes
1. This user guide provides a simple and intuitive set of instructions to interact with the GenRes CUI.
2. By reading this document, user would understand the expected behaviour of the virtual assistant as well as ways to start the interaction.

### Technical Design of GenRes CUI
1. Understand the Framework:
    * This CUI adopts Open Source RASA framework which consists of RASA core and RASA nlu
    * This CUI utilises RASA core to navigate through various expected scenarios during user interaction and execute pre-defined events for exception handling
        * List of expected exception handling:
            - fallback for low confidence level (<0.3) during intent classification
            - out-of-scope whenever the request received is unknown to the Virtual Assistant
    * This CUI utilises RASA nlu to perform two main tasks namely:
        * Intent Classification
        * Entity Recognition

2. Technical Workflow:
    2.1 Pipeline
    2.2 


### Functional Design of GenRes CUI
1. Dialog Policy