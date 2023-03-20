import re

def find_email(text):
    """ Функция для поиска всех e-mail адресов в тексте"""

    email = text
    pattern = r'[\w\.-]+@[\w-]+\.[\w]+[\.\w]*'
    email_list = re.findall(pattern, email)
    return email_list


