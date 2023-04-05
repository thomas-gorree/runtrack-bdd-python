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
cur.execute("CREATE TABLE etage  (id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255), Numero INT, superficie INT);")
cur.execute("CREATE TABLE salles  (id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255), id_etage INT, capacite INT);")

conn.commit()