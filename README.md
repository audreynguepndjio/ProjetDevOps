Projet 3DVP - API REST avec FastAPI
Description
Ce projet est une implémentation d'une API REST en Python utilisant FastAPI, réalisée dans le cadre du TP 3DVP de l'école IT. L'API gère une liste d'items avec des opérations CRUD (Create, Read, Update, Delete) et inclut une pipeline CI/CD avec GitHub Actions pour l'automatisation des tests et du linting. Le déploiement a été configuré manuellement sur Render.
Fonctionnalités

Endpoints :
GET / : Retourne un message de statut ("API en ligne").
GET /items : Liste tous les items.
GET /items/{item_id} : Affiche un item spécifique.
POST /items : Crée un nouvel item.
PUT /items/{item_id} : Met à jour un item.
DELETE /items/{item_id} : Supprime un item.


Modèle Item : id (int), name (str), price (float), in_stock (bool).

Prérequis

Python 3.12
Pip (gestionnaire de paquets Python)
Git (pour le versioning)

Installation

Clonez le dépôt :git clone https://github.com/audreynguepndjio/ProjetDevOps
cd ProjetDevOps


Créez un environnement virtuel :python -m venv env


Activez l'environnement virtuel :
Windows : env\Scripts\activate

Installez les dépendances :pip install -r requirements.txt


Lancez l'API localement :uvicorn main:app --reload

L'API sera accessible à http://127.0.0.1:8000.

Tests

Exécutez les tests unitaires :pytest tests/ -v


Vérifiez la qualité du code :flake8 . --max-line-length=88 --extend-ignore=E402,W291



Pipeline CI/CD

Configurée avec GitHub Actions dans .github/workflows/ci.yml.
Étapes :
Linting avec flake8.
Exécution des tests avec pytest.
Analyse de sécurité avec bandit.


Statut visible dans les badges GitHub (images/pipeline_CI.png).

Déploiement

API déployée manuellement sur Render

 URL de l’API : https://projetdevops-1.onrender.com

Étapes de déploiement :
Connecter votre compte GitHub à Render

Créer un Nouveau Web Service

Sélectionner le dépôt GitHub → branche main

Définir :

Runtime : Python

Build command : pip install -r requirements.txt

Start command : uvicorn main:app --host 0.0.0.0 --port 10000

Lancer le déploiement

Bonus

Documentation Swagger : FastAPI fournit automatiquement une documentation interactive via Swagger UI, accessible à /docs ( https://projetdevops-1.onrender.com/docs ). Cette interface permet de visualiser et tester tous les endpoints de l'API.

Vérification de sécurité avec Bandit : Intégration de Bandit pour analyser le code et détecter des failles de sécurité potentielles. Bandit est exécuté automatiquement dans la pipeline CI/CD via GitHub Actions (voir ".github/workflows/ci.yml").

Captures d'écran

API en ligne : [images/api.png].
GitHub Actions : [images/pipeline_CI.png].
Render : [images/Deploiement1.png,images/Deploiement2.png].

Structure du projet
DVP/
├── main.py               # Code de l'API principale
├── models.py             # Modèles de données (Pydantic)
├── schemas.py            # Schémas pour validation d'entrée
├── crud.py               # Fonctions CRUD
├── tests/
│   └── test_items.py     # Tests unitaires
├── .github/workflows/
│   └── ci.yml            # CI avec GitHub Actions
├── requirements.txt      # Dépendances Python
├── .gitignore
└── README.md             # Documentation du projet


Réalisé par : Audrey Nguepndjio



