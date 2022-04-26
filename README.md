# mr-butter-bot
Discord bot made using Pycord. It doesn't serve any singular purpose, it was made for fun.

## Table of Contents
* [Getting Started](#getting-started)
* [Prerequisites](#prerequisites)
* [Modules](#modules)
* [Deployment](#deployment)

## Getting Started

### Prerequisites
* Python 3.9

### Modules
````
# Pycord
python3 -m pip install -U py-cord --pre

# python-dotenv
pip install python-dotenv

# Requests
pip install requests
````

## Deployment
You can run this locally in an IDE that supports Python to start the bot. Alternatively, you can host the bot somewhere else so long as you have the packages in requirements.txt installed on the host.

Every Discord bot requires a token in order for it to run. You can generate one by following this guide: https://www.writebots.com/discord-bot-token/ .

Once you have a token, you need to create a .env file in your bot file directory simply called '.env' - this file should contain one line: 
````
BOT_TOKEN=TOKENHERE
````
