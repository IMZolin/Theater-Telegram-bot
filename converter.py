import datetime
# Перевод введенного пользователем месяца в число.
def converting_a_month_to_numbers(strmonth):
    monthnumber = -1
    if ((strmonth == 'января') or (strmonth == 'янв') or (strmonth == '01') or (strmonth == '1')):
        monthnumber = 1
    elif ((strmonth == 'февраля') or (strmonth == 'фев') or (strmonth == '02') or (strmonth == '2')):
        monthnumber = 2
    elif ((strmonth == 'марта') or (strmonth == 'мар') or (strmonth == '03') or (strmonth == '3')):
        monthnumber = 3
    elif ((strmonth == 'апреля') or (strmonth == 'апр') or (strmonth == '04') or (strmonth == '4')):
        monthnumber = 4
    elif ((strmonth == 'мая') or (strmonth == 'май') or (strmonth == '05') or (strmonth == '5')):
        monthnumber = 5
    elif ((strmonth == 'июня') or (strmonth == 'июн') or (strmonth == '06') or (strmonth == '6')):
        monthnumber = 6
    elif ((strmonth == 'июля') or (strmonth == 'июл') or (strmonth == '07') or (strmonth == '7')):
        monthnumber = 7
    elif ((strmonth == 'августа') or (strmonth == 'авг') or (strmonth == '08') or (strmonth == '8')):
        monthnumber = 8
    elif ((strmonth == 'сентября') or (strmonth == 'сен') or (strmonth == '09') or (strmonth == '9')):
        monthnumber = 9
    elif ((strmonth == 'октября') or (strmonth == 'окт') or (strmonth == '10') or (strmonth == '10')):
        monthnumber = 10
    elif ((strmonth == 'ноября') or (strmonth == 'ноя') or (strmonth == '11') or (strmonth == '11')):
        monthnumber = 11
    elif ((strmonth == 'декабря') or (strmonth == 'дек') or (strmonth == '12') or (strmonth == '12')):
        monthnumber = 12
    return monthnumber
# Считывание данных, введенных пользователем.
    # Перевод текстовой даты, введенной пользователем в числа - день, месяц, год
def converting_a_message_string_to_numbers2(message):
    daymonthyearstr = message.text.split()
    daymonthyear = [-1, -1, -1]
    print(len(daymonthyearstr))
    if (len(daymonthyearstr) != 3):
        if (len(daymonthyearstr) == 1):
            daymonthyearstr = message.text.split('.')
        if (len(daymonthyearstr) != 3):
            return daymonthyear
    try:
        daymonthyear[0] = int(daymonthyearstr[0])
        daymonthyear[2] = int(daymonthyearstr[2])
        daymonthyear[1] = converting_a_month_to_numbers(daymonthyearstr[1])
    except ValueError:
        daymonthyear = [-1, -1, -1]
    if (daymonthyear[0] == -1 or daymonthyear[1] == -1 or daymonthyear[2] == -1):
        daymonthyear = [-1, -1, -1]
    return daymonthyear

def main_converting_a_message_string_to_numbers(date, message):
    daymonthyearstr = date.split()
    daymonthyear = [-1, -1, -1]
    print(len(daymonthyearstr))
    if (len(daymonthyearstr) != 3):
        if (len(daymonthyearstr) == 1):
            daymonthyearstr = date.split('.')
        if (len(daymonthyearstr) != 3):
            return daymonthyear
    try:
        daymonthyear[0] = int(daymonthyearstr[0])
        daymonthyear[2] = int(daymonthyearstr[2])
        daymonthyear[1] = converting_a_month_to_numbers(daymonthyearstr[1])
    except ValueError:
        daymonthyear = [-1, -1, -1]
    if (daymonthyear[0] == -1 or daymonthyear[1] == -1 or daymonthyear[2] == -1):
        daymonthyear = [-1, -1, -1]
    return daymonthyear

if __name__ == '__main__':
    converting_a_month_to_numbers(str)