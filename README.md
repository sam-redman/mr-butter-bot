# Mr. Butter Bot
Discord bot made using Pycord. It doesn't serve any singular purpose, it was made for fun.

## Table of Contents
* [Getting Started](#getting-started)
* [Prerequisites](#prerequisites)
* [Modules](#modules)
* [Running the Application Locally](#running-the-application-locally)
* [Deployment](#deployment)

## Getting Started
Every Discord bot requires a token in order for it to run. You can generate one by following this guide: https://www.writebots.com/discord-bot-token/ .

Once you have a token, you need to create a .env file in your bot file directory simply called '.env' - this file should contain one line: 
````
BOT_TOKEN=TOKENHERE
````

### Prerequisites
* [Python](https://www.python.org/downloads/)
* [Discord](https://discord.com/)

### Modules
````
# Pycord
pip install py-cord

# python-dotenv
pip install python-dotenv

# Requests
pip install requests
````

### Running the Application Locally
````
# Run the program.
python main.py
````

## Deployment
If you are hosting externally then specify an environment variable with BOT_TOKEN as the key and the value as the generated token value. You should enver upload a private token directly to Github or a third-party host.

````
# Start command when hosted by a third-party.
python main.py
````
