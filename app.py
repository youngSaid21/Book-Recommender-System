import pickle
import streamlit as st
import numpy as np

# Affiche un en-tête pour l'application Streamlit
st.header("Book Recommender System using Machine Learnig")

# Chargement des fichiers modèles et données via pickle
# 'model.pkl' : le modèle de recommandation basé sur la méthode des k plus proches voisins (KNN)
# 'books_name.pkl' : liste des noms des livres disponibles
# 'final_rating.pkl' : dataframe avec les informations sur les livres (titres, URLs des images, etc.)
# 'book_pivot.pkl' : tableau croisé des livres utilisé pour calculer les recommandations
model = pickle.load(open('artifacts/model.pkl', 'rb'))
books_name = pickle.load(open('artifacts/books_name.pkl', 'rb'))
final_rating = pickle.load(open('artifacts/final_rating.pkl', 'rb'))
book_pivot = pickle.load(open('artifacts/book_pivot.pkl', 'rb'))

# Cette fonction sert à récupérer les URLs des posters des livres recommandés
def fetch_poster(suggestion):
	books_name = []  # Liste pour stocker les noms des livres
	ids_index = []   # Liste pour stocker les indices des livres
	poster_url = []  # Liste pour stocker les URLs des images des posters

	# Boucle pour extraire les noms des livres à partir des suggestions fournies par le modèle
	for book_id in suggestion:
		books_name.append(book_pivot.index[book_id])

	# Trouver l'index de chaque livre dans le dataframe final_rating basé sur le titre
	for name in books_name[0]:
		ids = np.where(final_rating['title'] == name)[0][0]
		ids_index.append(ids)

	# Extraire les URLs des images correspondantes aux livres à partir de final_rating
	for idx in ids_index:
		url = final_rating.iloc[idx]['img_url']
		poster_url.append(url)

	return poster_url  # Retourner les URLs des images des posters


# Fonction principale pour recommander des livres basés sur un nom de livre donné
def recommend_books(book_name):
	book_list = []  # Liste pour stocker les livres recommandés

	# Trouver l'index du livre sélectionné dans book_pivot
	book_id = np.where(book_pivot.index == book_name)[0][0]

	# Utiliser le modèle KNN pour trouver les 6 livres les plus proches du livre sélectionné
	distance, suggestion = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1), n_neighbors=6)

	# Récupérer les URLs des posters pour les livres recommandés
	poster_url = fetch_poster(suggestion)

	# Boucle pour extraire les titres des livres recommandés
	for i in range(len(suggestion)):
   		books = book_pivot.index[suggestion[i]]
   		for x in books:
   			book_list.append(x)  # Ajouter chaque livre à la liste des recommandations

	return book_list, poster_url  # Retourner la liste des livres recommandés et les URLs des posters


# Création d'une boîte de sélection pour choisir un livre parmi la liste books_name
selected_books = st.selectbox(
	"Type or select a book",
	books_name
)

# Affiche les recommandations lorsque l'utilisateur clique sur le bouton "Show Recommendation"
if st.button('Show Recommendation'):
	recommendation_book, poster_url = recommend_books(selected_books)  # Appel de la fonction pour générer les recommandations

	# Création de 5 colonnes pour afficher les livres recommandés et leurs posters
	col1, col2, col3, col4, col5 = st.columns(5)

	# Chaque colonne contient un livre recommandé et son poster associé
	with col1:
		st.text(recommendation_book[1])
		st.image(poster_url[1])

	with col2:
		st.text(recommendation_book[2])
		st.image(poster_url[2])

	with col3:
		st.text(recommendation_book[3])
		st.image(poster_url[3])

	with col4:
		st.text(recommendation_book[4])
		st.image(poster_url[4])

	with col5:
		st.text(recommendation_book[5])
		st.image(poster_url[5])
