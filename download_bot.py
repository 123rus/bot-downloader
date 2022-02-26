from multiprocessing import cpu_count
import telebot
import pytube
import os

token = '5293683527:AAG0PrrMCOvWsOa4WZc6iMF_Phqk3VY-1KA'

bot = telebot.TeleBot(token=token)
url = 'https://www.youtube.com/watch?v=b9ZCLDsUs7U'
current_path = os.path.abspath(os.getcwd())+'/videos/'
# print(current_path)


@bot.message_handler(commands=['start'])
def send_message(message):
    bot.send_message(message.chat.id, 'Я телеграм бот')


@bot.message_handler(content_types='text')
def send(message):
    url = message.text
    bot.send_message(message.chat.id, 'Video downloading...')
    pytube.YouTube(url).streams.filter(res='720p').first().download( output_path=current_path)
    video_title = pytube.YouTube(url).title + '.mp4'
    video = open(current_path+video_title, 'rb')
    bot.send_video(message.chat.id, video)

print('Бот работает...')
bot.infinity_polling()
