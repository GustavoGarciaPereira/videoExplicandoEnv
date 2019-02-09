import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="programador",db="testePython")
# Cria um cursor
cursor = db.cursor()
cursor1 = db.cursor()
# Executa o SQL
cursor.execute("SELECT * FROM animals")
cursor1.execute("DESCRIBE animals")
# Pega o resultset como uma tupla
result = cursor.fetchall()
result1 = cursor1.fetchall()
# Itera (navega) pelo resultset
for record in result:
    print (record[0] , "-->", record[1])


for i in range(len(result1)):
    print("<Tabela> ",result1[i][0],"\n")
