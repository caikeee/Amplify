import sqlite3
from getpass import getpass
from time import sleep
from colorama import init, Fore
import stdiomask
import amplify

class Usuario:
    
  def __init__(self, db_name="caixa.db"):
        
        self.conn = sqlite3.connect(db_name)
        self.create_table()
       
  def create_table(self):
    with self.conn:
      self.conn.execute('''
        CREATE TABLE IF NOT EXISTS usuario(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          nome  TEXT NOT NULL,
          senha  TEXT NOT NULL                         
          )
          ''')
  def criar_usuario(self,nome,senha):
    with self.conn:
      self.conn.execute( '''    
        INSERT INTO usuario (nome,senha)
        VALUES(?,?)''',( nome,senha))
      print(Fore.BLUE + "Usuario registrado com sucesso!!")
    

  def buscar_usuario(self,nome,senha):
    cursor  = self.conn.cursor()

    cursor.execute(
      '''
      SELECT * FROM usuario WHERE nome = ? AND senha = ?
      ''',(nome,senha))
    return cursor.fetchone()
  
  
def exibir_menu():
    print(Fore.GREEN + '''
        Bem-vindo ao sistema de login
          
        Navegue através do menu abaixo:
        [1] Cadastrar novo usuário
        [2] Efetuar login
        [3] Sair
      ''')
    opcao = int(input('Digite a opção que deseja: '))
    return opcao
    
def fazer_login():
    login = input("Digite o nome do usario:")
    senha = stdiomask.getpass(prompt="Senha:",mask = "*")
    return (login,senha)
  
def main():
    usuario = Usuario()
    
    while True:
        opcao = exibir_menu()
        
        if opcao == 1:
            nome, senha = fazer_login()
            if nome == senha:
                print(Fore.YELLOW + 'Sua senha deve ser diferente do login!')
                senha = getpass('Senha: ')
            if usuario.buscar_usuario(nome, senha):
                print(Fore.RED + 'Usuário já existe!')
                sleep(2)
            else:
                usuario.criar_usuario(nome, senha)
                sleep(1)

        elif opcao == 2:
            nome, senha = fazer_login()
            if usuario.buscar_usuario(nome, senha):
                print(Fore.CYAN + 'Login realizado com sucesso!')
                sleep(1)
                amplify.main()
                
            else:
                print(Fore.RED + 'Você deve ter digitado o nome de usuário ou a senha errados!')
                sleep(2)
        
        elif opcao == 3:
            print(Fore.LIGHTMAGENTA_EX + 'Goodbye!')
            break
        
        else:
            print(Fore.RED + 'Opção inválida! Tente novamente.')
            sleep(2)

if __name__ == "__main__":
    main()
    
       