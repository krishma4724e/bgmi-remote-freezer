from telegram.ext import Updater, CommandHandler
import requests
import os

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

def attack(update, context):
    try:
        target_ip = context.args[0]
        target_port = context.args[1]
        duration = context.args[2]

        update.message.reply_text(f"Sending freeze command to {target_ip}:{target_port} for {duration} seconds...")

        url = f"http://{target_ip}:5000/freeze"
        payload = {"port": target_port, "duration": duration}
        response = requests.post(url, json=payload)

        if response.status_code == 200:
            update.message.reply_text("Freeze command sent successfully.")
        else:
            update.message.reply_text(f"Failed to send command. Status code: {response.status_code}")
    except Exception as e:
        update.message.reply_text(f"Error: {e}\nUsage: /attack <ip> <port> <duration>")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("attack", attack))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
