# PIC — Site Joback

Projet pédagogique avec une interface baby pink, une démonstration de connexion, un calculateur Joback et une tentative de visualisation 3D via PubChem + 3Dmol.js.

## Structure
- `index.html` : interface web
- `api/index.py` : API Python qui utilise `ugropy`
- `requirements.txt` : dépendance Python
- `vercel.json` : configuration Vercel minimale

## Tester en local
1. Ouvrir le dossier dans VS Code.
2. Dans le terminal, activer l'environnement virtuel.
3. Installer les dépendances : `pip install -r requirements.txt`.
4. Pour lancer l'application complète localement, utiliser Vercel CLI :
   - `npm install -g vercel`
   - `vercel dev`
   - ouvrir l'URL locale affichée par Vercel.

Ouvrir `index.html` directement dans le navigateur permet de voir l'interface, mais le calcul `/api` ne fonctionnera pas sans le serveur de fonctions.

## Déploiement
Importer le dépôt GitHub dans Vercel, avec le framework preset `Other`, puis déployer. La fonction `api/index.py` est exposée à `/api` et `index.html` est la page d'accueil statique.

## Important — connexion
Le formulaire de connexion inclus est une **démonstration front-end** : il accepte tout nom d'utilisateur et tout mot de passe non vides. Il ne protège aucun compte ni aucune donnée. Pour un vrai système d'authentification, il faut ajouter un fournisseur d'authentification ou une base de données avec mots de passe hachés côté serveur.

## Important — visualisation 3D
La page tente de récupérer un fichier 3D SDF depuis PubChem et l'affiche avec 3Dmol.js. Cette fonctionnalité nécessite une connexion Internet et une structure 3D disponible pour la molécule. Toutes les molécules n'ont pas forcément de structure 3D dans PubChem.
