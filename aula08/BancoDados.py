
import pymysql.cursors

class BancoDados:
    def __init__(self):
        self.host = 'localhost'
        self.usuario = 'root'
        self.senha = '4linux'
        self.banco = '4linux'
        self.charset = 'utf8mb4'
        self.conexao = ''
        
    def inciaConexao(self):
        try:
            self.conexao = pymysql.connect(
            host = self.host,
            user = self.usuario,
            password = self.senha,
            db = self.banco,
            charset = self.charset,
            cursorclass = pymysql.cursors.DictCursor)
        except Exception as err:
            print(err)
        
    def insereRegistro(self):
        dic = { "nome_pessoa":"","nac_pessoa":"","idade_pessoa":""}
        
        dic["nome_pessoa"] = input("Digite o Nome: ")
        dic["nac_pessoa"] = input("Digite a Nacionalidade: ")
        dic["idade_pessoa"] = input("Digite a Idade: ")
        
        with self.conexao.cursor() as cursor:
            SQL = "INSERT INTO pessoa(nome_pessoa, nac_pessoa, idade_pessoa) VALUES ('{}', '{}', {})" \
                .format(dic["nome_pessoa"], dic["nac_pessoa"], dic["idade_pessoa"])
            cursor.execute(SQL)
            self.conexao.commit()
            
    def consultaRegistro (self):
        with self.conexao.cursor() as cursor:
            SQL = "SELECT * FROM pessoa"
            cursor.execute(SQL)
            for linha in cursor:
                print("-----------------------------------------------------")
                print("ID :", linha["id_pessoa"])
                print("nome:", linha["nome_pessoa"])
                print("Nacionalidade:", linha["nac_pessoa"])
                print("idade:", linha["idade_pessoa"])
            
    def atualizaRegistro (self):
        with self.conexao.cursor() as cursor:
            idade = input("Informe a idade:")
            id_pessoa = input("Informe o ID: ")
            
            SQL = "UPDATE pessoa SET idade_pessoa = {} WHERE id_pessoa = {}".format(idade, id_pessoa)
            
            cursor.execute(SQL)
            self.conexao.commit()
            
    def removeRegistro (self):
        with self.conexao.cursor() as cursor:
            id_pessoa = input("Informe o ID: ")
            
            SQL = "DELETE FROM pessoa WHERE id_pessoa = {}".format(id_pessoa)
            
            cursor.execute(SQL)
            self.conexao.commit()
            
    def consultaRegistro (self):
        with self.conexao.cursor() as cursor:
            SQL = "SELECT * FROM pessoa"
            cursor.execute(SQL)
            for linha in cursor:
                print("-----------------------------------------------------")
                print("ID :", linha["id_pessoa"])
                print("nome:", linha["nome_pessoa"])
                print("Nacionalidade:", linha["nac_pessoa"])
                print("idade:", linha["idade_pessoa"])
                
                
    
    
    
        
        

