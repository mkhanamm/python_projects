import random

favorite_movies = []  

movies = [
    {"title": "Inception", "genre": "Sci-Fi", "year": 2010, "rating": 8.8},
    {"title": "Interstellar", "genre": "Sci-Fi", "year": 2014, "rating": 9.6},
    {"title": "The Matrix", "genre": "Sci-Fi", "year": 1999, "rating": 8.7},
    {"title": "Mad Max: Fury Road", "genre": "Action", "year": 2015, "rating": 8.1},
    {"title": "John Wick", "genre": "Action", "year": 2014, "rating": 7.4},
    {"title": "The Dark Knight", "genre": "Action", "year": 2008, "rating": 9.0},
    {"title": "The Grand Budapest Hotel", "genre": "Comedy", "year": 2014, "rating": 8.1},
    {"title": "Superbad", "genre": "Comedy", "year": 2007, "rating": 7.6},
    {"title": "Step Brothers", "genre": "Comedy", "year": 2008, "rating": 8.9},
    {"title": "La La Land", "genre": "Romance", "year": 2016, "rating": 8.0},
    {"title": "The Notebook", "genre": "Romance", "year": 2004, "rating": 7.9},
    {"title": "Titanic", "genre": "Romance", "year": 1997, "rating": 8.8},
    {"title": "A Quiet Place", "genre": "Horror", "year": 2018, "rating": 9.5},
    {"title": "Get Out", "genre": "Horror", "year": 2017, "rating": 9.7},
    {"title": "The Conjuring", "genre": "Horror", "year": 2013, "rating": 7.5},
]

def recommend_movies():
    genre = input("Enter the genre you want to watch: ").strip()
    min_rating = input("Enter the minimum rating (0-10) [optional]: ").strip()
    min_year = input("Enter the minimum year [optional]: ").strip()

    
    combined_movies = movies + favorite_movies

    recommendations = combined_movies

    
    if genre:
        recommendations = [movie for movie in recommendations if movie['genre'].lower() == genre.lower()]

    
    if min_rating:
        try:
            min_rating = float(min_rating)
            recommendations = [movie for movie in recommendations if movie['rating'] >= min_rating]
        except ValueError:
            print("Invalid rating input. Ignoring rating filter.")

    
    if min_year:
        try:
            min_year = int(min_year)
            recommendations = [movie for movie in recommendations if movie['year'] >= min_year]
        except ValueError:
            print("Invalid year input. Ignoring year filter.")

    
    if recommendations:
        print("\nRecommended Movies:")
        for movie in recommendations:
            print(f"- {movie['title']} (Genre: {movie['genre']}, Rating: {movie['rating']}, Year: {movie['year']})")
    else:
        print("No movies found based on your preferences.")

def add_to_favorites():
    movie_title = input("Enter the movie title to add to your favorites: ").strip()
    genre = input("Enter the genre of the movie: ").strip()
    year = input("Enter the release year of the movie: ").strip()
    rating = input("Enter the rating of the movie (0-10): ").strip()

    try:
        year = int(year)
        rating = float(rating)
        favorite_movies.append({"title": movie_title, "genre": genre, "year": year, "rating": rating})
        print(f"'{movie_title}' has been added to your favorite movies!")
    except ValueError:
        print("Invalid year or rating. Movie not added.")

def view_favorites():
    print("\nYour Favorite Movies:")
    if favorite_movies:
        for movie in favorite_movies:
            print(f"- {movie['title']} (Genre: {movie['genre']}, Rating: {movie['rating']}, Year: {movie['year']})")
    else:
        print("You have no favorite movies yet.")

def random_movie():
    combined_movies = movies + favorite_movies
    movie = random.choice(combined_movies)
    print(f"\nRandom Movie Recommendation: {movie['title']} (Genre: {movie['genre']}, Rating: {movie['rating']}, Year: {movie['year']})")

def main_menu():
    while True:
        print("\n--- Movie Recommendation System ---")
        print("1. Recommend Movies")
        print("2. Add to Favorite Movies")
        print("3. View Favorite Movies")
        print("4. Random Movie Recommendation")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            recommend_movies()
        elif choice == '2':
            add_to_favorites()
        elif choice == '3':
            view_favorites()
        elif choice == '4':
            random_movie()
        elif choice == '5':
            print("Thank you for using the Movie Recommendation System!")
            break
        else:
            print("Invalid choice. Please try again.")

main_menu()