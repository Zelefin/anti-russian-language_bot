import telebot
from googletrans import Translator

translator = Translator() ## adding translator

bot = telebot.TeleBot("YOUR_BOT_TOKEN") ## adding bot

RussianLetters = ["ы", "Ы", "э", "Э", "ё", "Ё", "ъ", "Ъ"] ## unique russian letters


@bot.message_handler(commands=['help']) ## answer to a /help command
def send_welcome(message):
    bot.reply_to(message, "Hello! This bot automatically checks the message for containing russian letters.")


@bot.message_handler(func=lambda message: True) ## checking all messages
def check_all(message):
    for letter in message.text: ## For each letter in message
        for k in RussianLetters: ## for each unique letter in RussianLetters
            if letter == k: ## If they are the same
                bot.reply_to(message, "User " + message.from_user.first_name + " " + message.from_user.last_name
                             + " sent a message in russian.\nThe message probably meant to say: \n 🇺🇸"
                             + translator.translate(message.text).text + " \n 🇺🇦"
                             + translator.translate(message.text, dest="uk").text) ## Reply to the message and translate it

                bot.delete_message("@YOUR_CHAT", message.message_id) ## Deletes the message
                ## We must reply(!) and then delete in case of if message was sent as comment below the post in main channel
                ## so people could see the corrected message from bot in the comments.


bot.infinity_polling()
