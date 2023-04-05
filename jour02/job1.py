import mysql.connector


conn = mysql.connector.connect(
    host = "localhost",
    user =  'root',
    password = 'Mdp62230@',
    database = "Laplateforme"
)
cursor = conn.cursor()

cursor.execute('SELECT * FROM etudiants;')
resulta= cursor.fetchone()

print(resulta)
cursor.close()
conn.close()