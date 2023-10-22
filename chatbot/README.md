# RASA installation
1. Currently RASA only supported by python3.4-3.9 due to bug found in abseil-py (sub-module in RASA)
2. Downgrade python version whenever necessary

# RASA initialization
1. command: rasa init --no-prompt (skip prompt, setup project automatically)

# RASA setup introduction
1. __init__.py: helps python to find actions
2. actions.py: custom actions
3. config.yml: configuration for NLU and core models
4. credentials.yml: details for connecting to other services
5. data/nlu.md: NLU training data
6. data/stories.md: stories
7. domain.yml: assistant's domain (define how the bot should act & respond)
8. endpoints.yml: details for connecting to channels like html webchat, slack or fb messenger
9. models/<timestamp>.tar.gz: initial model

# RASA will throw Exception "BlockingIOError" when running rasa interactive learning
1. use pip uninstall uvloop

# Entity Recognition
1. name: capital case, single word name
2. skillset: capital case
3. title: capital case

# Enable integration
1. inside config.yml, add action_endpoints: with webhook url socket address
	example: 	action_endpoint:
  			  url: "http://localhost:5055/webhook"

2. inside endpoints.yml, uncomment action_endpoint to enable custom action response
	example: 	action_endpoint:
			  url: "http://localhost:5055/webhook"

3. inside credential.yml, uncomment socketio
4. then fill up user_message_evt with user_uttered
5. and fill up bot_message_evt with bot_uttered
6. finally change session_persistence to true
	example: 	socketio:
			  user_message_evt: user_uttered
			  bot_message_evt: bot_uttered
			  session_persistence: true

# Integration
1. Web HTML with Chat Widget
    - create a .html page within the same folder
    - paste below script within html body
    - on cmd line, run:
	```bash
	rasa run --port <port> --models --enable-api --cors "*"
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


2. Slack
    - register ngrok account and get the auth token
    - install ngrok on local machine based on your OS system
    - on cmd line, run: 
        ngrok config add-authtoken <your_ngrok_token>
    - on cmd line, run: 
        rasa run --port <port> --models --enable-api --cors "*"
    - on another cmd line, run: 
        ngrok http <port>
    - 