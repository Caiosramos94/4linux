#import o módulo pymysql
import pymysql.cursors

try:
    conexao = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = '4linux',
        db = '4linux',
        charset = 'utf8mb4',
        cursorclass = pymysql.cursors.DictCursor)

Exception as err:
    print("Erro ao tentar conectar o mysql")
    print(err)
else:
    with conexao.cursor() as cursor:
        SQL = "SELECT * FROM pessoa"
        cursor.execute(SQL)
        for linha in cursor:
            print(linha)
finally:
    conexao.close()
