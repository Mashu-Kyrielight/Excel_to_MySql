import pandas as pd
import mysql.connector

# file route
archivo_excel = pd.read_excel('extra.xlsx')

# column titles
columnas = ['name', 'last_name', 'age', 'number_phone']
info_selected = archivo_excel[columnas]


#column position
nom = info_selected[columnas[0]]
ape = info_selected[columnas[1]]
age = info_selected[columnas[2]]
cel = info_selected[columnas[3]]

i = 0
try:    # connection to MySql
        cn = mysql.connector.connect(host="localhost", user="user", passwd="123456", database="database_name")
        mycursor = cn.cursor()
        sql = f'''INSERT INTO person (idPer, nomPer, apePer, edad, phonePer) VALUES (null, '{nom[i]}', '{ape[i]}', {age[i]}, {cel[i]});'''
        mycursor.execute(sql)
        cn.commit()
        i = + 1
except Exception as ex:
    print(f'Error: {ex}')
finally:
    print("\n finalized :)")

