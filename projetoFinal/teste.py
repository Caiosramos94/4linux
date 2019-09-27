import pymysql.cursors

class CadastroUsuario:
    
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
    
    def exibirMenu(self):
        print("1 - Inserir novo cadastro")
        print("2 - Consultar cadastro por nome")
        print("3 - Resetar tentativas")
        print("4 - Atualizar usuário")
        print("4 - remover usuário")
        print("4 - Simular login")
        
        opcao = int(input("Ecolha uma opcao:"))
        return opcao
        
    def cpf(self):
        dic = {"cpf_pessoa":""}
        
        dic["cpf_pessoa"]= input("Digite o cpf do usuário: ")

    def inserircadastro(self):
        dic = { "cpf_pessoa":"","nome_pessoa":"","endereco_pessoa":"","idade_pessoa":"","telefone_pessoa":""}
        
        dic["cpf_pessoa"] = input("Digite o cpf do usuário: ")
        dic["nome_pessoa"] = input("Digite a Nome do usuário: ")
        dic["endereco_pessoa"] = input("Digite o endereço do usuário: ")
        dic["idade_pessoa"] = input("Digite a Idade do usuário: ")
        dic["telefone_pessoa"] = input("Digite o telefone do usuário: ")
        
        with self.conexao.cursor() as cursor:
            SQL = "INSERT INTO funcionario (cpf_pessoa, nome_pessoa, endereco_pessoa, idade_pessoa, telefone_pessoa) VALUES ('{}', '{}', '{}','{}',{})"\
                .format(dic["cpf_pessoa"], dic["nome_pessoa"], dic["endereco_pessoa"], dic["idade_pessoa"], dic["telefone_pessoa"])
            cursor.execute(SQL)
            self.conexao.commit()
            
    def Consultacadastro(self):
        dic = {"nome_pessoa":""}
       
        dic["nome_pessoa"] = input("Digite o nome do usuário: ")
        with self.conexao.cursor() as cursor:
            SQL = "SELECT * FROM funcionario WHERE  nome_pessoa LIKE '%{}%'".format("nome_pessoa")
            cursor.execute(SQL)
            for linha in cursor:
                print("nome:", linha["nome_pessoa"])
                
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
            

            
            
  
        
      

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


