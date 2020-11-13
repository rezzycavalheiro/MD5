# Item 01
# Desenvolva um programa que implemente uma aplicação que possui duas
# funcionalidades: cadastrar e autenticar usuário. Um usuário possui os seguintes atributos:
# nome (string de 4 caracteres) e senha (string de 4 caracteres). O cadastro dos usuários deve ser
# armazenado em um arquivo no formato txt. A aplicação deve utilizar o algoritmo MD5 para
# realizar a função hash para armazenamento da senha.

import hashlib 

def cadastro():
    name = input("Digite seu nome: ")
    pwd = input("Digite a senha: ")
    if (len(name) > 4):
        name = name[0:4]
    if(len(pwd) > 4):
        pwd = pwd[0:4]
    return name, pwd

def md5(pwd):
    encryptedPwd = hashlib.md5(pwd.encode()).hexdigest()
    return encryptedPwd

def writeFile(name, encryptedPwd):
    cadastro = open("cadastro.txt", "a")
    cadastro.write(name + ";" + encryptedPwd + "\n")
    cadastro.close()
    return cadastro

def readFile(file):
    print(file.read())

def checkLogin(nameLogin, pwdLogin):
    nameLogin, pwdLogin = nameLogin[0:4], pwdLogin[0:4]
    if((nameLogin == name) and (md5(pwdLogin) == encryptedPwd)):
        print("Login feito com sucesso!")
    else:
        print("Nome ou senha inválida.")
        exit
        
def menu():
    selected = int(input("Selecione a opção: \n1 - Fazer cadastro\n2 - Fazer login\n3 - Sair\n"))
    return selected

def main():
    selected = menu()
    if (selected == 1):
        name, pwd = cadastro()
        encryptedPwd = md5(pwd)
        file = writeFile(name, encryptedPwd)
        print("\nUsuário cadastrado com sucesso.\n\n")
        main()
    
    elif (selected == 2):
        name, pwd = cadastro()
        readFile(file)
        checkLogin(name, pwd)
        main()
    elif (selected == 3):
        exit
    else:
        print("Opção inválida")
        exit

main()