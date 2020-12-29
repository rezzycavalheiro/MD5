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
    
def salt(pwd):
    pwd = pwd.lower()
    pwd = pwd.replace('a', '4')
    pwd = pwd.replace('e', '3')
    pwd = pwd.replace('i', '1')
    pwd = pwd.replace('o', '0')
    pwd = pwd.replace('u', '9')
    pwd = pwd.replace('b', '8')
    pwd = pwd.replace('z', '2')
    pwd = pwd.replace('s', '5')
    pwd = pwd.replace('g', '6')
    pwd = pwd.replace('t', '7')
    return pwd

def md5(pwd):
    pwd = salt(pwd)
    print(pwd)
    encryptedPwd = hashlib.md5(pwd.encode()).hexdigest()
    return encryptedPwd

def writeFile(name, encryptedPwd):
    cadastro = open("cadastro.txt", "a")
    cadastro.write(name + ";" + encryptedPwd + "\n")
    cadastro.close()
    return cadastro

def readFile():
    cadastro = open("cadastro.txt", "r")
    lines = []
    profile = {}
    with open ("cadastro.txt", "rt") as file:
        for line in file:
            line = line.split(";")
            for item in line:
                profile['name'] = line[0]
                profile['pwd'] = line[1]
            profile['pwd'] = profile['pwd'].replace("\n", "")
            lines.append(profile.copy())    
    return lines           

def checkLogin(nameLogin, pwdLogin):
    nameLogin, pwdLogin = nameLogin[0:4], pwdLogin[0:4]
    checkProfile = readFile()
    check = False
    for profile in checkProfile:
        if(profile['name'] == nameLogin and profile['pwd'] == md5(pwdLogin)):
            check = True
    return check
        
def menu():
    selected = int(input("\nSelecione a opção: \n1 - Fazer cadastro\n2 - Fazer login\n3 - Sair\n"))
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
        nameLogin, pwdLogin = cadastro()
        check = checkLogin(nameLogin, pwdLogin)
        if(check):
            print("\nLogin autenticado com sucesso!\n")
        else:
             print("\nNome e/ou senha inválidos.\n")
        main()
    elif (selected == 3):
        exit
    else:
        print("Opção inválida")
        exit

main()