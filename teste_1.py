import re 
from cryptographyFramework import *

def valida_username(username):
    if not username[0].isupper():
        return False
    if not re.match(r'^\w+$', username):
        return False
    if len(username) > 30:
        return False
    return True

def valida_password(password):
    if len(password) < 10:
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    return True

def valida_message(message):
    if len(message) > 70:
        return False
    return True

def login():
    while True:
        username = input("Digite o nome de usuário: ")
        password = input("Digite a senha: ")
        if valida_username(username) and valida_password(password):
            print("Login realizado com sucesso!")
            break
        else:
            print("Usuário ou senha inválidos. Tente novamente.")

def input_message():
    while True:
        message = input("Digite a mensagem criptografada (até 70 caracteres): ")
        if valida_message(message):
            print("Mensagem criptografada recebida com sucesso!")
            break
        else:
            print("Mensagem inválida. Tente novamente.")

login()
input_message()



initializeWrite()
user = "Fulano"
password = "1234"
encryptedText = encryptMessage(user, password, "")
saveNewLine(encryptedText)
encryptedText = encryptMessage(user, password, "teste novooooooooo!")
saveNewLine(encryptedText)