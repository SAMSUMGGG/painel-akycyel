from os import system


class panel:

    def __init__(self, senha): self.senha = senha

    def verify(self):
        senha = 'akycyel'
        while self.senha != senha:
            print('Senhha incorreta. Tente novamente.')
            self.senha = input('Digite a senha novamente: ')
            if self.senha == 'sair':
                return
        show.opc()
        condicao.opc_user()
    
        

        
    
class show:
    @staticmethod
    def opc():
        print('\033[1;31m[01] RECURSOS NMAP\033[m \n\033[1;32m[02] RECURSOS REQUEST\033[m')

class condicao:
    def opc_user():
        user = int(input('Digite a opção: '))
        if user == 1:
            print('nmap funções')


system('cls')
senha = input('\033[1;33mDigite a senha para acessar ao painel:\033[m ')
senha = panel(senha).verify()

