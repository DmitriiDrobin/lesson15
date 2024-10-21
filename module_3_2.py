def send_email(message, recipient,*, sender = "university.help@gmail.com"):
    n1 = recipient.find('@')
    n2 = sender.find('@')
    k1 = recipient.find('.com') + recipient.find('.ru') + recipient.find('.net')
    k2 = sender.find('.com') + sender.find('.ru') + sender.find('.net')
    if n1 > 0 and n2 > 0 and k1 > 0 and k2 > 0:
        if recipient == sender:
            print(f"Нельзя отправить письмо самому себе!")
        elif sender != "university.help@gmail.com":
            print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
        else:
            print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
send_email('Пытаюсь разобраться работает ли код', 'urban.')
