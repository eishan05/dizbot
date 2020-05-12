# dizbot

[![Build Status](https://travis-ci.org/eishan05/dizbot.svg?branch=master)](https://travis-ci.org/eishan05/dizbot)

A command line tool to seemlessly build discord bots in python

## How to use

![Demo](demo/demo.gif)

1. Go into the directory you want to have the bot code in
2. Run command `dizbot run` and walk through the prompts to add commands and event handlers and create the bot
3. Add your bot's client token in the `client_token.txt` file if you didn't already add it through the CLI
4. Run `python3 bot.py` and test out your bot!

dizbot saves your bot's configurations into `dizbot_config.json` file and reads from if you run `dizbot run` again

dizbot also appends `dizbot_config.json` and `client_token.txt` to your `.gitignore` to make sure that you do not accidently push sensitive info onto github or other websites

## How to install (temporary)
1. Clone this repo
2. Create a virtual python environment (optional but recommended)
3. Run `pip install --editable .`
