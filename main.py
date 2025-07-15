
from recommender.book_recommender import BookRecommender

def main():
    recommender = BookRecommender("data/books.csv")
    print("Recommendations for author='George Orwell', genre='Dystopian':")
    print(recommender.recommend(author='George Orwell', genre='Dystopian'))

if __name__ == "__main__":
    main()
