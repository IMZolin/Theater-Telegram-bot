import telebot
from telebot import types
from config import TOKEN


def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.send_message(message.chat.id,
                         "Hello, dear theater🥰! I'm Telegram bot Tia, and my job is to help you quickly and easily choose an event to have a good time! 🎭\n\n 💜Enter /help command to learn about bot functions💜")

    @bot.message_handler(commands=['help'])
    def send_message_after_help(message):
        bot.send_message(message.chat.id,
                         '🎭/searchbuttons - includes a menu to search for plays by specific data\n🎭/selections - sends theater selections compiled by experts\n🎭/test - theater world quiz')

    @bot.message_handler(commands=['searchbuttons'])
    def button_main_menu(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Search by title")
        item2 = types.KeyboardButton("Search by rating")
        item3 = types.KeyboardButton("Search by genre")
        item4 = types.KeyboardButton("Date")
        item5 = types.KeyboardButton("Search by price")
        item7 = types.KeyboardButton("Search by age")
        item8 = types.KeyboardButton("Back to the main commands")
        item = types.KeyboardButton("Info")
        markup.add(item1, item2, item3, item4, item5)
        markup.add(item7)
        markup.add(item8)
        markup.add(item)
        bot.send_message(message.chat.id,
                         'You are in the main menu! Here you can choose which selections to show me.',
                         reply_markup=markup)
        bot.send_message(message.chat.id,
                         'If you want to know which button is responsible for what, just click or send "INFO" to the chat room')

    @bot.message_handler(commands=['test'])
    def test(message):
        bot.send_message(message.chat.id,
                         'This function is in developing')

    @bot.message_handler(commands=['selections'])
    def send_message_after_selections(message):
        bot.send_message(message.chat.id,
                         'This team will help you see author picks from theater experts🤓')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("The 5 best plays for a date💏")
        item2 = types.KeyboardButton("5 performances to invite parents👫")
        item3 = types.KeyboardButton("5 performances for fans of modern theater🎆")
        item4 = types.KeyboardButton("5 performances that will suit everyone🌟")
        item5 = types.KeyboardButton("Back to other functions")
        markup.add(item1, item2)
        markup.add(item3)
        markup.add(item4)
        markup.add(item5)
        bot.send_message(message.chat.id, 'Choose the right selection', reply_markup=markup)

    # Answer to message "Genre"
    def message_answer_genre(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttongenre1 = types.KeyboardButton("Drama")
        buttongenre2 = types.KeyboardButton("Comedy")
        buttongenre3 = types.KeyboardButton("Musical")
        buttongenre4 = types.KeyboardButton("Ballet")
        buttongenre5 = types.KeyboardButton("Opera")
        buttongenre6 = types.KeyboardButton("Puppet show")
        buttongenre7 = types.KeyboardButton("Kids")
        buttongenre8 = types.KeyboardButton("Back to the main menu")
        markup.add(buttongenre1, buttongenre2, buttongenre3, buttongenre4)
        markup.add(buttongenre5, buttongenre6, buttongenre7, buttongenre8)
        bot.send_message(message.chat.id,
                         'You are in the "Genre" tab. Maybe you want to shed a tear while watching something as dramatic as Romeo and Juliet, or, conversely, laugh heartily while watching the comedy The Marriage of Figaro.',
                         reply_markup=markup)

    # Answer to message "Title"
    def message_answer_title(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttongenre3 = types.KeyboardButton("Back to the main menu")
        markup.add(buttongenre3)
        bot.send_message(message.chat.id,
                         'You are on the "Title" tab. This is where I can pick up performances on specific title! \nWant to know more about the performance? No problem! Just type in its name:',
                         reply_markup=markup)
    # Answer to message "Date"
    def message_answer_date(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttongenre3 = types.KeyboardButton("Back to the main menu")
        markup.add(buttongenre3)
        bot.send_message(message.chat.id,
                         'You are on the "Date" tab. This is where I can pick up performances on upcoming dates, or any specific date!',
                         reply_markup=markup)

    # Answer to message "Price"
    def message_answer_prise(message):
        markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttonprice1 = types.KeyboardButton("Choosing by price")
        buttonprice2 = types.KeyboardButton("Check price")
        buttonprice3 = types.KeyboardButton("Back to the main menu")
        markup3.add(buttonprice1, buttonprice2)
        markup3.add(buttonprice3)
        bot.send_message(message.chat.id,
                         'I will do my best to help you find an interesting theater performance at the perfect price!',
                         reply_markup=markup3)

    # Answer to message "Rating"
    def message_answer_rating(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttongenre1 = types.KeyboardButton("Rating from")
        buttongenre2 = types.KeyboardButton("5 top-rated plays")
        buttongenre3 = types.KeyboardButton("Back to the main menu")
        markup.add(buttongenre1, buttongenre2)
        markup.add(buttongenre3)
        bot.send_message(message.chat.id,
                         'You are on the "Rating" tab. Here you can choose what to show me - 5 plays with a rating matching the one you entered, or 5 plays with the highest rating.',
                         reply_markup=markup)
        bot.send_message(message.chat.id,
                         'Oh, yes, I tried to pick the shows with the lowest price! I hope you find something you like!')

    def message_answer_age(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("0+")
        item2 = types.KeyboardButton("6+")
        item3 = types.KeyboardButton("12+")
        item4 = types.KeyboardButton("16+")
        item5 = types.KeyboardButton("18+")
        item6 = types.KeyboardButton("Back to the main menu")
        markup.add(item1, item2, item3, item4, item5)
        markup.add(item6)
        bot.send_message(message.chat.id,
                         'You are in the "Age" tab! Here you can choose which selections to show me.',
                         reply_markup=markup)

    @bot.message_handler(content_types=['text'])
    def message_reply(message):
        # Main commands
        if message.text == 'start' or message.text == 'Start':
            send_welcome(message)
        elif message.text == 'buttons' or message.text == 'Buttons':
            button_main_menu(message)
        elif message.text == "help" or message.text == "help me":
            send_message_after_help(message)
        if message.text == "Back to the main commands":
            send_message_after_help(message)
        # Main buttons
        elif message.text == "Date":
            message_answer_date(message)
        elif message.text == "Search by title":
            message_answer_title(message)
            #bot.register_next_step_handler(message, search_performance_for_name, rsheet)
        elif message.text == "Search by rating":
            message_answer_rating(message)
        elif message.text == "Search by genre":
            message_answer_genre(message)
        elif message.text == "Search by price":
            message_answer_prise(message)
        elif message.text == "Search by age":
            bot.send_message(message.chat.id, 'Want to go to an age-appropriate play?')
            message_answer_age(message)
            #bot.register_next_step_handler(message, button_age_search2, rsheet)
        elif message.text == "info" or message.text == "INFO" or message.text == "Info":
            bot.send_message(message.chat.id,
                             'To see the buttons, click on the icon on the right side of the bar\n "Search by title" allows you to find information about five plays with the same name (date, time, price, etc.\n "Search by rating" creates a selection with the best rating\n "Search by date" shows what plays are on that date\n "Search by price" finds the cheapest plays at the entered price\n "Search by age" suggests plays with a certain age limit')

        elif message.text == "Back to the main menu":
            button_main_menu(message)

        elif (message.text == "The 5 best plays for a date💏"):
            bot.send_message(message.chat.id,
                             text='Written by Telegram channel Theatrical Hanger:\n🎭"Warsaw Melody" at the Theatre of Europe\n🎭"Juliet" at the Bolshoi Theatre\n🎭"Love Letters" at the Workshop\n🎭"Romeo and Juliet" at the Theatre of the Young Spectator\n🎭"Square" at the Bad Theatre')
        elif (message.text == "5 performances to invite parents👫"):
            bot.send_message(message.chat.id,
                             text='Author - Telegram channel "Theatrical Hanger":\n🎭"Glory" at the Bolshoi Theatre "Elder Son" at the Workshop\n🎭"Brothers and Sisters" at the Theatre of Europe\n🎭"Masquerade" at the Alexandrinsky Theatre\n🎭"My Grandfather Was a Cherry" at the BTK')
        elif (message.text == "5 performances for fans of modern theater🎆"):
            bot.send_message(message.chat.id,
                             text='Author - Telegram channel "Theatrical Hanger":\n🎭"Lear" at the Comedian AsylumMacbeth.Kino at the Lensoviet Theatre\n🎭"Reportage with a noose around the neck" at the Teatro Di Capua\n🎭"The phase of the mirror" at the Pop-up Theatre\n🎭"Pound of meat" at the Kamennostrovsky Theatre')
        elif (message.text == "5 performances that will suit everyone🌟"):
            bot.send_message(message.chat.id,
                             text='Author - Telegram channel "Theatre Hanger":\n🎭"The Cherry Orchard" at MDT Theater of Europe\n🎭"The Governor" at BDT\n🎭"Crime and Punishment" at NTT\n🎭"Vanya" at Karlsson Haus\n🎭"An Optimistic Tragedy" at Alexandrinsky Theater')
        elif message.text == "Other selections":
            send_message_after_selections(message)
        elif message.text == "Back to other functions":
            send_message_after_help(message)

    bot.polling(none_stop=True)

if __name__ == '__main__':
    telegram_bot(TOKEN)

