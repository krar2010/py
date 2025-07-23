import telebot
from keep_alive import keep_alive

# شغّل السيرفر للحفاظ على التشغيل المستمر
keep_alive()

# ضع توكن البوت هنا
BOT_TOKEN = "YOUR_BOT_TOKEN"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 أهلاً بك في البوت يا بطل!")

# تشغيل البوت
print("Bot is running...")
bot.polling()
