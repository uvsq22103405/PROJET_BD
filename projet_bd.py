
import pandas as pd
import random
import string

# Liste de noms d'utilisateurs
liste_noms_utilisateurs = ['john_doe', 'aloww', 'booob', 'emma_jackson', 'mike_miller','sara_wilson', 'david_brown', 'olivia_carter', 'tom_anderson', 'COP1']

#liste_de_type

liste_de_type = ["association", "personne"]

# Biographies
biographies = [
    "Passionné de technologie et de musique . Explorer le monde un clic à la fois.",
    "Amoureux de la nature et des animaux .",
    "Artiste et rêveur ✨. Créateur de beauté à travers la peinture et la photographie.",
    "Enthousiaste de la cuisine et de la nourriture du monde .",
    "Défenseur des droits de l'homme et de l'égalité . Ensemble pour un monde meilleur.",
    "Explorateur de la science et de l'espace . Plongeons dans les étoiles ensemble!",
    "Fanatique du fitness et du bien-être . Transformons nos vies par la santé.",
    "Écrivain passionné et amoureux des livres . Partageons nos histoires.",
    "Voyageur du monde et amateur d'aventure . Découvrons des horizons nouveaux.",
    "Militant environnemental . Agissons pour un avenir durable."
]

# Générer un mail
def generate_email_from_username(username):
    """Générer une adresse e-mail à partir d'un nom d'utilisateur."""
    domain = ''.join(random.choice(string.ascii_lowercase) for _ in range(6))
    extension = random.choice(['com', 'net', 'org', 'gov', 'edu'])
    return f"{username}@example.{extension}"

# Associer les noms d'utilisateurs et les e-mails dans le même ordre
noms_et_emails = [(username, generate_email_from_username(username)) for username in liste_noms_utilisateurs]

# Création de la table USERS
users = pd.DataFrame({
    'user_id': range(1, 11),
    'name_user': [nom for nom, email in noms_et_emails],
    'agee': [random.randint(14, 100) for _ in range(10)],
    'email': [email for nom, email in noms_et_emails],
    'type': [random.choice(liste_de_type) for _ in range(10)],
    'biographie': random.sample(biographies, k=10)
})

# Affichage de la table USERS
print('La table USERS est :\n', users.to_string(index=False))










'''la table concerts '''
# Liste de noms de concerts
liste_noms_concerts = ["Harmonie en Fusion","Éclats de Mélodie","Symphonie Nocturne",
"Vibrations Celtiques",
"Rythmes Urbains",
"Sérénade Sous les Étoiles",
"Mélodies Enchantées",
"Jazz Fusion Express",
"Rhapsodie du Monde",
"Concerto Magique"]

# Liste de noms d'organisateurs (associations)
liste_organisateurs = users.loc[users['type'] == 'association', 'name_user'].tolist()

#liste lieux 
liste_lieux_fr=["Paris","New York","Tokyo","Londres","Lille","Nice","Orleans","Marseille","Bordeaux","Paris"]

#liste cause que peut soutenir les concerts
liste_causes = ["Trisomie 21", "SIDA", "Environnement", "Éducation", "Santé mentale", "Droits de l'homme","Autisme",
    "Maladies rares", "Cancer"]
# Création de la table CONCERT
concerts = pd.DataFrame({
    'id_concert': range(1, 11),
    'name': [nom for nom in liste_noms_concerts],
    'lieu': [random.choice(liste_lieux_fr) for _ in range(10)],
    'organised_by': [random.choice(liste_organisateurs) for _ in range(10)],
    'nb_place': [random.randint(50, 900) for _ in range(10)],
    'enfant': [random.choice([True, False]) for _ in range(10)],
    'need_volunteers': [random.choice([True, False]) for _ in range(10)],
    'soutien':random.choices(liste_causes, k=10)
})

# Affichage de la table CONCERT
print('La table CONCERT est :\n', concerts.to_string(index=False))




'''table LIEUX'''
# Liste des lieux avec leurs noms en français, anglais et arabe
liste_lieux_en=['Paris', 'New York', 'Tokyo', 'London', 'Lille', 'Nice', 'Orleans', 'Marseille', 'Bordeaux', 'Paris']
liste_lieux_arabic=['باريس', 'نيويورك', 'طوكيو', 'لندن', 'ليل', 'نيس', 'أورليانز', 'مرسيليا', 'بوردو', 'باريس']
lieux =pd.DataFrame({
    'id_lieux': range(1, 11),
    'name_fr': [random.choice(liste_lieux_fr) for _ in range(10)],
    'name_en': [random.choice(liste_lieux_en) for _ in range(10)],
    'name_arabic': [random.choice(liste_lieux_arabic) for _ in range(10)],
})



# Sélectionner un indice aléatoire pour chaque ligne
indices = random.sample(range(10), 10)

# Appliquer les indices pour garantir que les noms correspondent
lieux['name_fr'] = [liste_lieux_fr[i] for i in indices]
lieux['name_en'] = [liste_lieux_en[i] for i in indices]
lieux['name_arabic'] = [liste_lieux_arabic[i] for i in indices]


# Afficher la table "lieux"
print('La table LIEUX est :\n', lieux)




'''table salle '''

# Créer une table "salle"
salle = pd.DataFrame({
    'id_salle': range(1, 11),
})

# Afficher la table "salle"
print('La table SALLE est :\n', salle)


'''table CAUSE'''
# Créer une table "Cause"
cause = pd.DataFrame({
    'id_soutien': range(1, len(liste_causes) + 1),
    'nom_soutien': liste_causes,
})

# Afficher la table "Cause"
print('La table CAUSE est :\n', cause)





'''table FOLLOW'''
# Créer une table Follow avec des id_user_A et id_user_B provenant de la table USERS
follow = pd.DataFrame({
    'id_follow':range(1, 11),
    'id_user_A': random.sample(users['user_id'].tolist(), 10),
    'id_user_B': random.sample(users['user_id'].tolist(), 10),
    'A_follow_B': [random.choice([True, False]) for _ in range(10)],
    'B_follow_A': [random.choice([True, False]) for _ in range(10)],
})

# Afficher la table Follow
print('\nLa table FOLLOW est :\n', follow)


'''table EVENNEMENT'''

# Vérifier si la taille de la population est suffisante pour l'échantillonnage
person_users = users[users['type'] == 'personne']

if len(person_users) > 0:
    evennement = pd.DataFrame({
        'id_event': [random.choice(range(1, len(person_users) + 1)) for _ in range(len(person_users))],
        'users_id': random.sample(person_users['user_id'].tolist(), len(person_users)),
        'annoucement': ['participer' if random.choice([True, False]) else 'interesser' for _ in range(len(person_users))],
        'id_concert': random.sample(concerts['id_concert'].tolist(), len(person_users)),
    })
    print('\nLa table EVENT est :\n', evennement)
else:
    print("La taille de la population de personnes est insuffisante pour l'échantillonnage.")


# a finir historique faut rajouter id morceaux id playlist et avis
'''table historique'''

historique = pd.DataFrame({
    'id_hist': range(1,11),
    'id_user': random.sample(users['user_id'].tolist(), 10),
    'id_concert': random.sample(concerts['id_concert'].tolist(), 10),
})

# Affichage de la table HISTORIQUE
print('La table HISTORIQUE est :\n', historique)



#Enregistrer la table en fichier CSV
users.to_csv('users.csv', index=False, quoting=1)  # quoting=1 pour ajouter des guillemets doubles aux chaînes
concerts.to_csv("concerts.csv",index=False,quoting=1)
lieux.to_csv('lieux.csv', index=False)
salle.to_csv('salle.csv', index=False)
cause.to_csv('cause.csv', index=False)
follow.to_csv('follow.csv', index=False)
evennement.to_csv('event.csv', index=False)
historique.to_csv('historique.csv', index=False)



