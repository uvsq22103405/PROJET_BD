from sqlalchemy import create_engine

# Remplacez 'root' et 'votre_mot_de_passe' par le nom d'utilisateur et le mot de passe réels
# Remplacez 'localhost' par l'adresse IP ou le nom de domaine du serveur MySQL
# Remplacez 'nom_de_la_base_de_donnees' par le nom de votre base de données
engine = create_engine('mysql://root:03012003ines1438@localhost:3306/Local_instance_3306')

# Établir la connexion
connection = engine.connect()

# Exécuter vos requêtes SQL ici

# Fermer la connexion
connection.close()





''' 
LOAD DATA INFILE '/Bureau/L3BI/semestre1/BD/projet/PROJET_BD/cause.csv'
INTO TABLE nom_de_la_table
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS; -- Si la première ligne contient les en-têtes et doit être ignorée

SELECT * FROM cause WHERE colonne = 'Trisomie 21';
'''

