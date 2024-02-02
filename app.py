import telebot
from bot_config import TOKEN, values
from extensions import APIException, CurrencyConverter


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def get_help(message: telebot.types.Message):
    text_help = ("Чтобы начать работу отправьте сообщение боту в следующем формате: \n <имя валюты, цену которой "
                 "хотите узнать> \n<имя валюты, в которой надо узнать цену первой валюты> \n<количество первой валюты>"
                 "\n\nК примеру: \t<евро рубли 112>"
                 "\n\nУвидеть доступные валюты для конвертирования - введите команду \n\t/values ")
    bot.reply_to(message, text_help)


@bot.message_handler(commands=['values'])
def get_values(message: telebot.types.Message):
    text = "Доступные для перевода валюты:"
    for cur in values.keys():
        text = "\n".join((text, cur,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        mes_text = message.text.lower()
        user_input = mes_text.split(' ')

        if len(user_input) != 3:
            raise APIException('Не верно введены параметры.')

        quote, base, amount = user_input
        text = CurrencyConverter.get_price(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя. \n{e}')
    except Exception as e:
        bot.reply_to(message, f"Не удалось обработать команду \n{e}")
    else:
        bot.send_message(message.chat.id, text)



bot.polling()
