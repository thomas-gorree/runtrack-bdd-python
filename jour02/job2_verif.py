import mysql.connector
#connexion au base de données
db = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "Mdp62230@",
  database = "laplateforme"
)
#créer un curseur de base de données pour effectuer des opérations SQL
cur = db.cursor()
#exécuter le curseur avec la méthode execute() et transmis la requête SQL
cur.execute("SHOW TABLES")
#parcourir le curseur
for table in cur:
  print(table)