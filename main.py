# MyProfile app

SEPARATOR = '------------------------------------------'


def print_general_info(name_parameter, age_parameter, phone_parameter, email_parameter, index_parameter,
                       postal_parameter, information_parameter):
    print(SEPARATOR)
    print('Имя:    ', name_parameter)
    if 11 <= age_parameter % 100 <= 19:
        years_parameter = 'лет'
    elif age_parameter % 10 == 1:
        years_parameter = 'год'
    elif 2 <= age_parameter % 10 <= 4:
        years_parameter = 'года'
    else:
        years_parameter = 'лет'

    print('Возраст:', age_parameter, years_parameter)
    print('Телефон:', phone_parameter)
    print('E-mail: ', email_parameter)
    print('Индекс: ', index_parameter)
    print('Почтовый адрес: ', postal_parameter)
    if information:
        print('')
        print('Дополнительная информация:')
        print(information_parameter)


def print_entrepreneur_info():
    print('Информация о предпринимателе')
    print('ОГРНИП: ', registration_number)
    print('ИНН:    ', payer_number)
    print('Банковские реквизиты')
    print('Р/с:    ', payment_account)
    print('Банк:   ', bank_name)
    print('БИК:    ', identification_code)
    print('К/с:    ', correspondent_account)


def numeral_count(number):
    count = 0
    while number > 0:
        number //= 10
        count += 1
    return count


def input_general_info():
    # input general info
    record_name = input('Введите имя: ')
    while 1:
        # validate user age
        record_age = int(input('Введите возраст: '))
        if record_age > 0:
            break
        print('Возраст должен быть положительным')

    record_number_phone = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
    record_phone = ''
    for ch in record_number_phone:
        if ch == '+' or ('0' <= ch <= '9'):
            record_phone += ch

    record_email = input('Введите адрес электронной почты: ')
    record_index = int(input('Введите почтовый индекс: '))
    record_postal_address = input('Введите почтовый адрес (без индекса): ')
    record_information = input('\nВведите дополнительную информацию:')

    return record_name, record_age, record_phone, record_email, record_index, record_postal_address, record_information


def input_businessman_info():
    # input information about the entrepreneur
    record_number_registration = int(input('Введите  ОГРНИП: '))
    while True:
        quantity = numeral_count(record_number_registration)
        if quantity != 15:
            print('Ошибка. ОГРНИП должен содержать 15 чисел.')
            record_number_registration = int(input('Введите  ОГРНИП: '))
        else:
            break

    record_number_payer = int(input('Введите ИНН: '))
    record_payment_account = int(input('Введите расчётный счёт: '))
    while True:
        quantity = numeral_count(record_payment_account)
        if quantity != 20:
            print('Ошибка. Расчётный счёт должен содержать 20 чисел')
            record_payment_account = int(input('Введите расчётный счёт: '))
        else:
            break

    record_bank_name = input('Введите название банка: ')
    record_identification_code = int(input('Введите  БИК: '))
    record_correspondent_account = input('Введите корреспондентский счёт: ')

    return record_number_registration, record_number_payer, record_payment_account, record_bank_name, record_identification_code, record_correspondent_account


# user profile
name = ''
age = 0
phone = ''
email = ''
index = 0
postal_address = ''
information = ''
# information about the entrepreneur
registration_number = 0
payer_number = 0
payment_account = 0
bank_name = ''
identification_code = 0
correspondent_account = ''

print('Приложение MyProfile')
print('Сохраняй информацию о себе и выводи ее в разных форматах')
while True:
    # main menu
    print(SEPARATOR)
    print('ГЛАВНОЕ МЕНЮ')
    print('1 - Ввести или обновить информацию')
    print('2 - Вывести информацию')
    print('0 - Завершить работу')

    option = int(input('Введите номер пункта меню: '))
    if option == 0:
        break

    if option == 1:
        # submenu 1: edit info
        while True:
            print(SEPARATOR)
            print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
            print('1 - Личная информация')
            print('2 - Информация о предпринимателе')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                name, age, phone, email, index, postal_address, information = input_general_info()

            elif option2 == 2:
                registration_number, payer_number, payment_account, bank_name, identification_code, correspondent_account = input_businessman_info()

            else:
                print('Введите корректный пункт меню')
    elif option == 2:
        # submenu 2: print info
        while True:
            print(SEPARATOR)
            print('ВЫВЕСТИ ИНФОРМАЦИЮ')
            print('1 - Общая информация')
            print('2 - Вся информация')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                print_general_info(name, age, phone, email, index, postal_address, information)

            elif option2 == 2:
                print_general_info(name, age, phone, email, index, postal_address, information)

                # print entrepreneur
                print_entrepreneur_info()
            else:
                print('Введите корректный пункт меню')
    else:
        print('Введите корректный пункт меню')
