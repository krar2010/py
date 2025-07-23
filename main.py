from flask import Flask
from threading import Thread
import telebot

# ✅ تشغيل خادم Flask للحفاظ على النشاط من خلال UptimeRobot
app = Flask('')

@app.route('/')
def home():
    return "I'm alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# ✅ تفعيل السيرفر
keep_alive()

# 🔑 توكن البوت الخاص بك
BOT_TOKEN = "8097520541:AAEe_HlOl0sS6aFTMM9shiCRTA0CMCVSVMM"
bot = telebot.TeleBot(BOT_TOKEN)

# 📩 رد ترحيبي عند بدء المحادثة
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "👋 أهلاً بك في بوت كروري! سعيد بانضمامك.")

# ▶️ بدء تشغيل البوت
print("Bot is running...")
bot.polling()
