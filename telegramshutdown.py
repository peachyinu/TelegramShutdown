import telegram
import os


def main():

    bot = telegram.Bot(token='yourtokengoeshere') # Get the token from the Bot Father upon new bot creation 

    global LAST_UPDATE_ID

    LAST_UPDATE_ID = bot.getUpdates()[-1].update_id

    while True:
        for update in bot.getUpdates(offset = LAST_UPDATE_ID):
            text = update.message.text
            username = update.message.from_user.username
            chat_id = update.message.chat.id
            update_id = update.update_id
            if LAST_UPDATE_ID < update_id:
                if text == "shutdown" and username == "ownerusername":

                    try:
                        os.system('shutdown -s -t 5')
                        LAST_UPDATE_ID = update_id
                        bot.sendMessage(chat_id = update.message.chat_id, text = "I shut down your computer successfully! ~ <3")
                    except:
                        pass
                    if text == "reboot" and username == "ownerusername":
                        os.system('shutdown -r -t 5')
                        LAST_UPDATE_ID = update_id
                        bot.sendMessage(chat_id = update.message.chat_id, text = "I rebooted your computer successfully! ~ <3")
                    if username != "ownerusername": # Message to tell intruders kindly to go away :D
                        bot.sendMessage(chat_id = update.message.chat_id, text = "Sorry but only my owner can talk to me! :(")
                        LAST_UPDATE_ID = update_id


if __name__ == '__main__':
    main()
print(encoded)
