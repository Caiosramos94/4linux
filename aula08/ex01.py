#importar o módulo pymysql
import pymysql.cursors

try:
    conexao = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = '4linux',
        db = '4linux',
        charset = 'utf8mb4',
        cursorclass = pymysql.cursors.DictCursor)

except Exception as err:
    print("Não foi possivel conectar com o Banco de dados")
    print(err)
else:
    with conexao.cursor() as cursor:
        SQL = "SELECT * FROM pessoa"
        cursor.execute(SQL)
        for linha in cursor:
            print(linha)
finally:
    conexao.close()
    
    
