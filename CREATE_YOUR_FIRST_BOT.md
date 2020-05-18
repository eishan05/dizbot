# Create your first discord bot using dizbot

## Table
1. [Machine setup (install Python 3 and pip)](#machine-setup)
2. [Discord setup (create a bot account and add it to servers)](#discord-setup)
3. [dizbot usage (generate bot code using dizbot)](#dizbot-usage)

## Machine setup

You can skip this section if you already have Python 3 and pip installed on your machine

### Python 3 and Pip


#### Python installation
1. [Open command prompt](https://www.isunshare.com/windows-10/4-ways-to-open-command-prompt-in-windows-10.html) if on windows or [open Terminal](https://support.apple.com/en-ca/guide/terminal/apd5265185d-f365-44cb-8b09-71a064a42125/mac) if on Mac or Linux, and run `python3 -v` to check if you already have Python. If it prints out the version, you are done
2. Otherwise [download and install](https://www.python.org/downloads/) the latest Python 3 version for your OS

#### Pip installation
1. Pip is usually installed with Python 3 >= 3.4. To verify, run command `pip -v`. If it prints out the version, you are done
2. Otherwise, you can download [get-pip.py](https://bootstrap.pypa.io/get-pip.py)
2. Open command prompt or terminal and navigate to the folder containing the `get-pip.py` file. Learn how to do it on [Windows](https://www.youtube.com/watch?v=sjaCgavMO18) and/or [Mac/Linux](https://www.youtube.com/watch?v=j6vKLJxAKfw)
3. Run the command: `python get-pip.py`
4. Confirm installation by running `pip -v`

## Discord setup

If you already have a bot and its client token created on discord's developer portal, you can skip this section

1. [Make a discord account](https://discord.onl/2019/01/24/how-to-create-a-discord-account/) if you haven't already
2. Go to [developer portal](https://discord.com/developers/applications) and click on the `New Application` button on the top right
![Developer portal](demo/developer_portal.png)
3. Create the application and go to the `Bot` section and build a bot
![Bot page](demo/bot_section.png)
4. Copy and securely save your bot's client token
![Client token](demo/client_token.png)
5. Go to OAuth2 section, select the bot scope and add required permissions. Copy the generated URL and paste it into your browser (or send it to your server's admin)
![OAuth2](demo/oauth_bot.png)
6. Add the bot to a server you admin by following the instructions in this page
![Add bot page](demo/add_bot_page.png)
7. Congrats you have setup your new bot!


## dizbot usage

1. Install dizbot by running `pip install dizbot` in command prompt or terminal
2. Navigate to the directory you want your bot files to be in
2. Command `dizbot run` will walk you through adding functionality to your bot and generate bot code
3. You can add the client token you saved in step 4 of [Discord setup](#discord-setup) through the command line, or add it in the `client_token.txt` file that dizbot creates
4. Run command `python3 bot.py` to start the bot
5. Test out your bot by running a command in the discord server your bot is in!

![demo gif](demo/demo.gif)