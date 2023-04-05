import mysql.connector
#connexion au base de données
conn = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "Mdp62230@",
  database = "laplateforme"
)
#créer un curseur de base de données pour effectuer des opérations SQL
cur = conn.cursor()
#exécuter le curseur avec la méthode execute() et transmis la requête SQL
sql = "INSERT INTO person (nom, nomero, superficie) VALUES (%s, %s, %s)"

value = [
    ("RDC", 0, 500)
    ("R+1", 1, 500)
]
cur.executemany(sql, value)

conn.commit()

