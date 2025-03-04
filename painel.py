import instaloader
from time import sleep
from os import system
import os
import pyfiglet



class painel:
    def __init__(self, senha) : self.senha = senha
    def play(self):
        if self.senha == '1':
            print('\033[1;32mSenha correta!...Entrando.\033[m')
            sleep(3)
            very_user.user()
            show.opc()
        else:
            system('cls')
            print('\033[1;31mSenha incorreta...encerrando.\033[m')

class show:
    def opc():
        from dados import user
        from dados import pws_
        usuario = input('\033[1;32mDigite o usuário que você quer stalkear:\033[m ')
        system('cls')
        bot = instaloader.Instaloader()
        bot.login(user, pws_)
        system('cls')
        perfil = instaloader.Profile.from_username(bot.context, usuario)
        text = pyfiglet.figlet_format(usuario)
        
        print(f'\033[1;34m{text}\033[m')
        print('-' * 50)
        print(f'\n\n\033[1;31mUSUÁRIO ENCONTRADO: @{perfil.username}\033[m')
        print(f'\033[1;32mID DO USUÁRIO:\033[m {perfil.userid}')
        print(f'\033[1;33mNOME COMPLETO NO INSTAGRAM:\033[m {perfil.full_name}')
        print(f'\033[1;34mBIO DA CONTA:\033[m {perfil.biography}')
        print(f'\033[1;35mURL EXISTENTES NO PERFIL:\033[m {perfil.external_url}')
        print(f'\033[1;31mQUANTIDADE DE SEGUIDORE:\033[m {perfil.followers}')
        print(f'\033[1;32mESTÁ SEGUINDO:\033[m {perfil.followees}')
        print('-' * 50)
        
        

class very_user:
    def user():
        arquivo = 'dados.py'
        if  not os.path.exists(arquivo):
            system('cls')
            print('\033[1;33mDetectamos que você não contém login do instagram.🙄')
            sleep(3)
            system('cls')
            print('Digite o usuário e senha para fazermos login na sessão pra você.😀🥰\033[m')
            sleep(2.5)
            user = input('\033[1;31muser:\033[m ')
            pws_ = input('\033[1;31mpassword:\033[m ')
            with open('dados.py', 'w') as create:
                create.write(f'user = "{user}"')
                create.write(f'\npws_ = "{pws_}"')
                print(f'\033[1;32mCriado com sucesso!! Iremos sempre logar como\033[m [{user}].')

class senha:
    def painel_():
        system('cls')
        user = input(('Digite a senha fornecida pelo \033[1;32m@akycyel: \033[m'))
        play = painel(user).play()

                    


            

class inicio:
    def opc():
        print('\033[1;32m[01] ENTRAR\033[m\n\033[1;33m[02] FAZER NOVO LOGIN\033[m\nfaça novo login caso digitou senha ou user errado.')
        user = input('Digite a opção: ')
        

        if user == '1' or user == '01':
            senha.painel_()

        elif user == '2' or '02':
            system('cls')
            os.remove('dados.py')
            user_ = input('Digite o usuário: ')
            senha_ = input('Digite a senha: ')
            with open('dados.py', 'w') as create:
                create.write(f'user = "{user_}"')
                create.write(f'\npws_ = "{senha_}"')
                print('Criado com sucesso novo login!!!')
        else:
            print(f'\033[1;31mEssa opção [{user}] não existe!😠\033[m')
            print('encerrando...')

inicio.opc()