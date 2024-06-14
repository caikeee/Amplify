from colorama import Fore, Style, init
import sqlite3
init(autoreset=True)


   
class Caixa:
    def __init__(self, db_name="caixa.db"):
        
        self.conn = sqlite3.connect(db_name)
        self.create_table()
       

    def create_table(self):
         with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS transacoes(
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  nome  TEXT NOT NULL,
                  cod  TEXT NOT NULL,    
                  valor  REAL NOT NULL,    
                  parcelas  INTEGER NOT NULL,  
                  juros  REAL NOT NULL                 
                )
                ''')
         


    def registrar_caixa(self,nome, cod, valor, parcelas, juros):
        with self.conn:
            self.conn.execute( '''    
                INSERT INTO transacoes (nome,cod,valor,parcelas, juros)
                VALUES(?,?,?,?,?)''',(nome,cod,valor,parcelas,juros))
        print(Fore.BLUE + "Transação de caixa registrada com sucesso!!")
        
       
        # self.caixa.append(transacao)
        # print(Fore.BLUE + "Transação de caixa registrada com sucesso!")


    def mostrar_caixa(self):
         cursor = self.conn.cursor()
         cursor.execute('SELECT * FROM transacoes')
         transacoes = cursor.fetchall()
         if transacoes:
              print('registro de caixa:')
              for transacao in transacoes:
                   print( Fore.GREEN + f"""
                   Nome: {transacao[1]}      
                   Código: {transacao[2]}      
                   Valor: {transacao[3]}      
                   Parcelas: {transacao[4]}      
                   Jurus: {transacao[5]}""")
         else:
             print("Nenhuma transação de caixa registrada.") 




    def calcular_total_emprestado(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT COUNT(*), SUM(valor) FROM transacoes')
        qtd_emprestimo, total_emprestado = cursor.fetchone()
        print(f"Quantidade de empretimos realizados:{qtd_emprestimo}")
        print(f"Valor total emprestado: R$ {total_emprestado}")


    def calcular_retorno(self): 
     cursor = self.conn.cursor()
     cursor.execute('SELECT SUM( VALOR *(1 + juros)) FROM transacoes')
     total_com_juros = cursor.fetchone()[0]
     print(f"total a receber com juros: R$ {total_com_juros}")
      

class Pessoa:

    def __init__(self, nome, caixa):
            self.nome = nome
            self.caixa = caixa
            self.registro_emprestimos = []

    def pegar_emprestado(self):
        while True:
            try:
                valor_emprestado = float(input('Qual valor você precisa: '))
                parcelas = int(input('Em quantas parcelas: '))
                juros = float(input('Digite o juros a ser aplicado (ex: 0.10): '))
                                    
                    # Cria um dicionário com as informações do empréstimo
                emprestimo = {
                                    "nome": self.nome,
                                    "valor_emprestado": valor_emprestado,
                                    "parcelas": parcelas,
                                    "juros": juros
                                    }
                self.registro_emprestimos.append(emprestimo)
                print(Fore.BLUE + "Empréstimo realizado com sucesso!")

                # Registra a transação de caixa
                cod_transacao = f"TX-{len(self.registro_emprestimos)}"
                self.caixa.registrar_caixa(nome, cod_transacao, valor_emprestado, parcelas, juros)
                                    
            except ValueError:
                    print(Fore.RED + "Entrada inválida. Por favor, tente novamente.")
                    continue

            continuar = input("Deseja adicionar outro empréstimo? (s/n): ")
            if continuar.lower() != 's':
                break

# Exemplo de uso:
caixa = Caixa()
nome = input("Digite o nome da pessoa: ")
pessoa = Pessoa(nome, caixa)

pessoa.pegar_emprestado()
caixa.mostrar_caixa()
caixa.calcular_retorno()

