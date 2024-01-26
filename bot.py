import os
import telebot

BOT_TOKEN = '6723198328:AAHIjZQ8TcEyadQqdA1DG8gOHpZaOfHO5nA'

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    welcome_message = "Hola, soy Sofi. ¡Bienvenido! ¿En qué puedo ayudarte?\n\n"
    welcome_message += "Puedes usar los siguientes comandos:\n"
    welcome_message += "/parciales - Ver parciales\n"
    welcome_message += "/temas - Ver temas\n"
    welcome_message += "/etc - Realizar alguna otra acción\n"
    bot.reply_to(message, welcome_message)

@bot.message_handler(commands=['parciales'])
def show_parciales(message):
    bot.reply_to(message, "Aquí están los parciales disponibles: [Lista de parciales]")

@bot.message_handler(commands=['temas'])
def show_temas(message):
    bot.reply_to(message, "Aquí están los temas disponibles: [Lista de temas]")

@bot.message_handler(commands=['etc'])
def do_something_else(message):
    bot.reply_to(message, "Aquí puedes realizar alguna otra acción: [Descripción de la acción]")

bot.infinity_polling()
