# Book Recommender System using Machine Learning

Ce projet est une application **Streamlit** qui recommande des livres similaires à celui sélectionné par l'utilisateur, en utilisant un modèle de **Machine Learning** basé sur l'algorithme **K-Nearest Neighbors (KNN)**.

## Fonctionnalités

- **Sélection de livre** : Permet à l'utilisateur de choisir un livre parmi une liste déroulante.
- **Recommandations personnalisées** : Propose 5 livres similaires basés sur la sélection de l'utilisateur.
- **Affichage des posters** : Montre les images des livres recommandés.

## Installation et Exécution
Clonez le dépôt Git :

```bash
git clone https://github.com/votre-utilisateur/book-recommender-system.git
```
## Installation des Dépendances

1. **Créez un environnement virtuel** (si ce n'est pas déjà fait) :

    ```bash
    python -m venv env
    ```

2. **Activez l'environnement virtuel** :

    - Sous Windows :

      ```bash
      env\Scripts\activate
      ```

    - Sous macOS et Linux :

      ```bash
      source env/bin/activate
      ```

3. **Installez les dépendances** à l'aide du fichier `requirements.txt` :

    ```bash
    pip install -r requirements.txt
    ```

4. Lancez l'application Streamlit :
```bash
streamlit run app.py
```

Accédez à l'interface web via votre navigateur pour utiliser l'application.

## Structure du Projet
app.py : Le code source de l'application Streamlit.
artifacts/ : Dossier contenant les fichiers nécessaires pour le modèle et les données :
model.pkl : Le modèle KNN.
books_name.pkl : Liste des noms des livres.
final_rating.pkl : DataFrame avec les informations sur les livres.
book_pivot.pkl : Tableau croisé des livres.

## Utilisation
Sélectionnez un livre dans le menu déroulant.
Cliquez sur Show Recommendation pour afficher les 5 livres recommandés et leurs posters.
