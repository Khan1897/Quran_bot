import pandas as pd
import keys
import telebot

print('Bot started...')
API_KEY = keys.token

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Ассаламу Алейкум! Опишите одним словом интересующюю вас тему и, через пробел, количество аятов, которые Вы хотели бы видеть (к примеру, Милость 5)')

@bot.message_handler(func=lambda msg: True)
def get_ayts(message):
    see = message.text
    word = (see.split())[0].lower()
    how_many = int((see.split())[-1])
    final_version = pd.read_csv(r"https://raw.githubusercontent.com/Khan1897/Just_graphs/main/Quran1.csv", encoding = 'utf-8', delimiter = ';')
    ayts_you_get = final_version[final_version['letters'].str.contains(word)][['Sura','Ayt','Rus_Trans']]
    a = ''
    try:
        needed_ayts = ayts_you_get.sample(frac = 1).head(how_many)
        for i,j,k in zip(list(needed_ayts['Sura']), list(needed_ayts['Ayt']), list(needed_ayts['Rus_Trans'])):
            a += (f"\n{i}:{j}\n{k}\n")
        bot.reply_to(message, a)
    except Exception:
        bot.reply_to(message,'Не подобрано подходящего значения')



if __name__ == '__main__':
    bot.skip_pending = True
    bot.polling(none_stop=True)