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
8. endpoints.yml: details for conncting to channels like fb messenger
9. models/<timestamp>.tar.gz: initial model