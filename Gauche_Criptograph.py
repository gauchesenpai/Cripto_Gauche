#Gauche Criptograph
print ("Script de Criptografia de Arquivos (.enc) desenvolvido por: t.me/Gauchesenpai\n")

import os
import base64
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        data = f.read()
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data)
    return encrypted_data

def encrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypted_data = encrypt_file(file_path, key)
            with open(file_path + '.enc', 'wb') as f:
                f.write(encrypted_data)
            os.remove(file_path)

def convert_to_base64(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
    return base64.b64encode(data)

def main():
    print("Selecione o que deseja criptografar:")
    print("1. Arquivo")
    print("2. Pasta")
    choice = input("Digite o número da opção: ")

    key = generate_key()

    if choice == '1':
        file_path = input("Digite o caminho do arquivo: ")
        encrypted_data = encrypt_file(file_path, key)
        with open(file_path + '.enc', 'wb') as f:
            f.write(encrypted_data)
    elif choice == '2':
        folder_path = input("Digite o caminho da pasta: ")
        encrypt_folder(folder_path, key)
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()
