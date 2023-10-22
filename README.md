<div align="center">
    <img align="center" src="./resources/templates/AppFrontPage.gif" alt="demonstration" width="100%">
</div>
<br />
# User Guide for ChatGRes
1. This user guide provides a simple and intuitive set of instructions to interact with the GenRes CUI.
2. By reading this document, user would understand the expected behaviour of the virtual assistant as well as ways to start the interaction.

# Technical Design of GenRes CUI

## Understand Framework:
    * This CUI adopts Open Source RASA framework due to its strong supporting community group and extensibility across closed-group and open-group implementation
    * This CUI utilises RASA core to navigate through various expected scenarios during user interaction and execute pre-defined events for exception handling
    * This CUI utilises RASA nlu to perform two main tasks namely: Intent Classification, Entity Recognition
    * Apart from Rasa core server, an additional built-in Action Server is utilised to enhance contextual awareness and personalization during human interaction

## Understand Components:
1. NLU
2. Data
3. Endpoint
4. Pipeline
5. Dialog Flow
6. Model
7. Action

## Enable Integration
### Open-group / Public
1. inside config.yml, add action_endpoints: with webhook url socket address
	```yml
	action_endpoint:
  	  url: "http://localhost:5055/webhook"
	```

2. inside endpoints.yml, uncomment action_endpoint to enable custom action response
	```yml
	action_endpoint:
	  url: "http://localhost:5055/webhook"
	```

3. inside credential.yml, uncomment socketio and filled up as per below:
	```yml
	socketio:
	  user_message_evt: user_uttered
	  bot_message_evt: bot_uttered
	  session_persistence: true
	```

4. Web HTML with Chat Widget
    - create a .html page within the same folder
    - paste below script within html body
    - on cmd line, run:
	```bash
	rasa run -m models --enable-api --cors "*"
	```
    - launch a new terminal, on cmd line, run:
	```bash
	rasa run actions
	```

	In your `<body/>`:
	```html
	<script>!(function () {
	  let e = document.createElement("script"),
	    t = document.head || document.getElementsByTagName("head")[0];
	  (e.src =
	    "https://cdn.jsdelivr.net/npm/rasa-webchat@1.x.x/lib/index.js"),
	    // Replace 1.x.x with the version that you want
	    (e.async = !0),
	    (e.onload = () => {
	      window.WebChat.default(
	        {
	          customData: { language: "en" },
	          socketUrl: "https://bf-botfront.development.agents.botfront.cloud",
	          // add other props here
	        },
	        null
	      );
	    }),
	    t.insertBefore(e, t.firstChild);
	})();
	</script>
	```

### Closed-group / Private
1. Slack
    - register ngrok account and get the auth token
    - install ngrok on local machine based on your OS system
    - on cmd line, run: 
        ngrok config add-authtoken <your_ngrok_token>
    - on cmd line, run: 
        rasa run --port <port> --models --enable-api --cors "*"
    - on another cmd line, run: 
        ngrok http <port>
    
    <div align="center">
    <img align="center" src="./resources/templates/SlackImplementation.png" alt="demonstration" width="100%">
    </div>
    <br />


### Functional Design of GenRes CUI
1. Dialog Policy