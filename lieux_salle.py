import pandas as pd
import random
import string

'''table LIEUX'''
#liste lieux 
liste_lieux_fr=["Paris","New York","Tokyo","Londres","Lille","Nice","Orleans","Marseille","Bordeaux","Paris"]


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




# Enregistrer les tables en fichiers CSV


lieux.to_csv('lieux1.csv', index=False)
salle.to_csv('salle1.csv', index=False)

