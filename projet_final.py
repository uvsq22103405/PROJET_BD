import pandas as pd
import random
import string

# Liste de noms d'utilisateurs
liste_noms_utilisateurs = ['john_doe', 'aloww', 'booob', 'emma_jackson', 'mike_miller','sara_wilson', 'david_brown', 'olivia_carter', 'tom_anderson', 'COP1']

#liste_de_type

liste_de_type = ["association", "personne"]

# Biographies
biographies = [
    "Passionné de technologie et de musique 🎸. Explorer le monde un clic à la fois.",
    "Amoureux de la nature et des animaux 🌿🐾.",
    "Artiste et rêveur ✨. Créateur de beauté à travers la peinture et la photographie.",
    "Enthousiaste de la cuisine et de la nourriture du monde 🍜🌎.",
    "Défenseur des droits de l'homme et de l'égalité ✊. Ensemble pour un monde meilleur.",
    "Explorateur de la science et de l'espace 🚀🔭. Plongeons dans les étoiles ensemble!",
    "Fanatique du fitness et du bien-être 💪. Transformons nos vies par la santé.",
    "Écrivain passionné et amoureux des livres 📚✒️. Partageons nos histoires.",
    "Voyageur du monde et amateur d'aventure 🌍⛰️. Découvrons des horizons nouveaux.",
    "Militant environnemental 🌱🌊. Agissons pour un avenir durable."
]
##############################################################  NEW  ###########################################

#Album
titres_albums = [
    "Back in Black",
    "The Dark Side of the Moon",
    "Thriller",
    "Abbey Road",
    "Rumours",
    "Led Zeppelin IV"
]

#Auteur
speudonyme_auteur=[
    "Alber",
    "Pierre",
    "Jessica",
    "Pink",
    "Jasmine",
    "Sweet"
]

#morceau
noms_morceau = [
    "Bohemian Rhapsody",
    "Stairway to Heaven",
    "Hotel California",
    "Imagine",
    "Smells Like Teen Spirit",
    "Sweet Child o' Mine",
    "Like a Rolling Stone",
    "Hey Jude",
    "Yesterday",
    "Let It Be",
    "Hallelujah",
    "Wonderwall",
    "Billie Jean",
    "I Will Always Love You",
    "Every Breath You Take",
    "Thriller",
    "Under the Bridge",
    "Another Brick in the Wall",
    "November Rain",
    "I Want to Hold Your Hand",
    "Purple Haze",
    "Boys Don't Cry",
    "Kashmir",
    "Don't Stop Believin'",
    "Livin' on a Prayer",
    "Dancing Queen",
    "Roxanne",
    "Nothing Else Matters",
    "Paint It Black",
    "A Day in the Life"
]

# Générer une combinaison d'album de morceau aléatoire
def genere_albums():
    albums = []
    for _ in range(6):
        album = {
            "id_album":_,
            "titre_album": random.choice(titres_albums),
            "auteur": random.choice(speudonyme_auteur),
            "morceaux": random.sample(noms_morceau, 5)
        }
        albums.append(album)
    return albums

##############################################################  FIN NEW  ###########################################"""""
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
    'age': [random.randint(14, 100) for _ in range(10)],
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


'''table EVENT'''

# Vérifier si la taille de la population est suffisante pour l'échantillonnage
person_users = users[users['type'] == 'personne']

if len(person_users) > 0:
    event = pd.DataFrame({
        'id_event': [random.choice(range(1, len(person_users) + 1)) for _ in range(len(person_users))],
        'users_id': random.sample(person_users['user_id'].tolist(), len(person_users)),
        'annoucement': ['participer' if random.choice([True, False]) else 'interesser' for _ in range(len(person_users))],
        'id_concert': random.sample(concerts['id_concert'].tolist(), len(person_users)),
    })
    print('\nLa table EVENT est :\n', event)
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


##############################################################  NEW  ###########################################"""""
albums= genere_albums()

###### MORCEAUX ######
# Création d'une liste pour stocker les informations des morceaux
infos_morceaux = []

# Parcours des albums pour récupérer les informations des morceaux
for album in albums:
    album_id = album["id_album"]
    titre_album = album["titre_album"]
    morceaux = album["morceaux"]

    # Parcours des morceaux de chaque album
    for index, morceau in enumerate(morceaux, start=1):
        # Génération aléatoire de la note pour chaque morceau
        note = random.randint(0, 20)

        # Création d'un dictionnaire avec les informations du morceau
        morceau_info = {
            'id_morceau': f"{album_id}-{index}",
            'id_album': album_id,
            'name': titre_album,
            'name_morceau': morceau,
            'note': note
        }

        # Ajout du dictionnaire à la liste des informations des morceaux
        infos_morceaux.append(morceau_info)

# Création du DataFrame pandas à partir des informations des morceaux
morceau = pd.DataFrame(infos_morceaux)

# Affichage de la table morceaux
print('La table morceau est :\n', morceau.to_string(index=False))

###### ALBUMS   #######
album = pd.DataFrame({
    'id_album': [album["id_album"] for album in albums],
    'artist': [album["auteur"] for album in albums],  # Si l'auteur est défini dans vos données
    'title': [album["titre_album"] for album in albums]
})

# Affichage de la table album
print('La table album est :\n', album.to_string(index=False))

#####PLAYLIST #######

# Création de la table PLAYLISTS
playlist_data = []
playlist_counter = 1  # Compteur pour les identifiants de playlist

# Génération de playlists aléatoires pour chaque utilisateur
for user_id in users['user_id']:
    num_playlists = random.randint(1, 10)  # Nombre aléatoire de playlists par utilisateur

    for _ in range(num_playlists):
        num_morceaux = random.randint(5, 20)  # Nombre aléatoire de morceaux par playlist (maximum de 20)
        selected_morceaux = random.sample(list(morceau['id_morceau']), k=min(num_morceaux, len(morceau)))

        playlist_data.extend([{
            'id_playlist': playlist_counter,
            'id-user': user_id,
            'name': users.loc[users['user_id'] == user_id, 'name_user'].iloc[0],
            'id_morceau': morceau_id,
            'id_album': morceau[morceau['id_morceau'] == morceau_id]['id_album'].values[0]
        } for morceau_id in selected_morceaux])

        playlist_counter += 1  # Incrémentation du compteur pour l'identifiant de playlist

# Création de la DataFrame PLAYLISTS à partir de la liste de dictionnaires
playlist = pd.DataFrame(playlist_data)

# Affichage de la table PLAYLISTS
print(playlist)


########  PAGE ######

# Création de la table PAGE
page_data = []

# Obtenir les ID uniques des utilisateurs
unique_users = playlist['id-user'].unique()

# Génération des pages pour chaque utilisateur
for user_id in unique_users:
    user_playlists = playlist[playlist['id-user'] == user_id]['id_playlist'].unique()

    page_data.append({
        'id_page': user_id,  # Vous pouvez changer cela selon vos besoins
        'id_user': user_id,
        'id_playlist': ','.join(map(str, user_playlists))  # Regroupement des ID de playlists en une seule chaîne
    })

# Création de la DataFrame PAGE à partir de la liste de dictionnaires
page = pd.DataFrame(page_data)

# Affichage de la table PAGE
print(page)

###  SUGGESTION ####

# Génération de la table SUGGESTION
suggestion_data = []

# Générer des suggestions aléatoires pour chaque utilisateur
for user_id in range(1, 11):

    # Sélectionner un autre utilisateur aléatoire (différent de l'utilisateur actuel) pour suggérer une affinité
    affinite_user_id = random.choice([i for i in range(1, 11) if i != user_id])

    # Sélectionner un lieu aléatoire pour la suggestion
    lieu_id = random.randint(1, 10)  # ID de lieu aléatoire

    suggestion_data.append({
        'id_suggestion': f"{user_id}_{affinite_user_id}",  # Identifiant unique pour chaque suggestion
        'id_user': user_id,
        'id_user_affinite_with': affinite_user_id,
        'lieux': lieu_id  # Lieu associé à la suggestion
    })

# Création de la DataFrame SUGGESTION à partir de la liste de dictionnaires
suggestion = pd.DataFrame(suggestion_data)

# Affichage de la table SUGGESTION
print('La table SUGGESTION est :\n', suggestion)

#### AVIS ####

# Génération aléatoire de commentaires, notes et IDs
comments = ["Excellent!", "Très bon!", "Pas mal.", "Peut être amélioré.", None]*4
notes = [random.randint(1, 20) if comment else None for comment in comments]
lieux_ids = random.choices(lieux['id_lieux'].tolist(), k=20)  # Utilisation des identifiants de lieux existants

# Utilisation des identifiants existants pour morceaux, concerts, albums et playlists
morceau_ids = random.choices(morceau['id_morceau'].tolist(), k=20)
concert_ids = random.choices(concerts['id_concert'].tolist(), k=20)
album_ids = random.choices(album['id_album'].tolist(), k=20)
playlist_ids = random.choices(playlist['id_playlist'].tolist(), k=20)

# Sélection aléatoire d'ID d'utilisateur existants pour la colonne user_id
user_ids = random.choices(users['user_id'].tolist(), k=20)

# vérifie si la longueur des listes son équivalente 
print("*******************************************************************************************************")
print("*******************************************************************************************************")
print("*******************************************************************************************************")
print(len(user_ids))
print(len(comments))
print(len(morceau_ids))
print(len(concert_ids))
print(len(lieux_ids))
print(len(notes))
print(len(album_ids))
print(len(playlist_ids))
print("*******************************************************************************************************")
print("*******************************************************************************************************")
print("*******************************************************************************************************")

# Création de la table Avis
avis = pd.DataFrame({
    'id_avis': range(1, 21),  # Générer des ID d'avis
    'user_id': user_ids,
    'commentaire': random.choices(comments, k=20),  # Choix aléatoire parmi les commentaires et des valeurs nulles
    'id_morceau': morceau_ids,
    'id_concert': concert_ids,
    'id_lieux': lieux_ids,
    'note': notes,
    'id_album': album_ids,
    'id_playlist': playlist_ids
})

# Affichage de la table Avis
print('La table Avis est :\n', avis)

########  After  ####################

# Génération aléatoire des IDs de concert, avis et autres valeurs pour la table after
id_concerts = random.choices(concerts['id_concert'].tolist(), k=20)
id_avis = random.choices(avis['id_avis'].tolist(), k=20)
nb_participants = [random.randint(1, 1000) for _ in range(20)]  # Génération aléatoire du nombre de participants
photos = [f"photo_{i}.jpg" for i in range(1, 21)]  # Noms de fichiers de photos aléatoires
videos = [f"video_{i}.mp4" for i in range(1, 21)]  # Noms de fichiers vidéo aléatoires

# Création de la table After
after = pd.DataFrame({
    'id_after': range(1, 21),  # Générer des ID pour les after
    'id_concert': id_concerts,
    'nb_participant': nb_participants,
    'id_avis': id_avis,
    'photos': photos,
    'video': videos
})

# Affichage de la table After
print('La table After est :\n', after)

#########  Pics ##############

# Génération aléatoire des IDs d'utilisateur, d'after, des noms de photos et de vidéos
user_ids = random.choices(users['user_id'].tolist(), k=50)
id_afters = random.choices(after['id_after'].tolist(), k=50)
photos = [f"photo_{i}.jpg" for i in range(1, 51)]  # Noms de fichiers de photos aléatoires
videos = [f"video_{i}.mp4" for i in range(1, 51)]  # Noms de fichiers vidéo aléatoires

# Création de la table Pics
pics = []
for i in range(50):
    choice = random.choice(['photos', 'video'])  # Choisir aléatoirement entre photo ou vidéo

    if choice == 'photos':
        pics.append({
            'id_pics': i + 1,
            'user_id': user_ids[i],
            'id_after': id_afters[i],
            'photos': photos[i],
            'video': None
        })
    else:
        pics.append({
            'id_pics': i + 1,
            'user_id': user_ids[i],
            'id_after': id_afters[i],
            'photos': None,
            'video': videos[i]
        })

# Création du DataFrame Pics
pics_df = pd.DataFrame(pics)

# Affichage de la table Pics
print('La table Pics est :\n', pics_df)



#Enregistrer la table en fichier CSV
users.to_csv('users.csv', index=False, quoting=1)  # quoting=1 pour ajouter des guillemets doubles aux chaînes
concerts.to_csv("concerts.csv",index=False,quoting=1)
lieux.to_csv('lieux.csv', index=False)
salle.to_csv('salle.csv', index=False)
cause.to_csv('cause.csv', index=False)
follow.to_csv('follow.csv', index=False)
event.to_csv('event.csv', index=False)
historique.to_csv('historique.csv', index=False)
album.to_csv('album.csv', index=False)
morceau.to_csv('morceau.csv', index=False)
playlist.to_csv('playlist.csv', index=False)
page.to_csv('page.csv', index=False, quoting=1)
suggestion.to_csv('suggestion.csv', index=False)
avis.to_csv('avis.csv', index=False)
after.to_csv('after.csv', index=False)

pics_df.to_csv('pics.csv', index=False)


