#Importanto as bliotecas a serem utilizadas
import os, sqlite3
import pandas as pd

#Inserir o caminho local
os.chdir(r'D:\') 

#Criar conexão
con = sqlite3.connect('')  #Substituir pelo nome do db

#Realizar query e armazenar em um objeto pandas
cursor = con.execute("SELECT * FROM ") #Usar query desejada
resultado = cursor.fetchall()

consulta_sql = pd.DataFrame(resultado, columns=[campo[0]for campo in cursor.description])

#Encerrar conexão
con.close()
