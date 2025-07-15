
import pandas as pd

class BookRecommender:
    def __init__(self, csv_path):
        self.data = pd.read_csv(csv_path)

    def recommend(self, author=None, genre=None):
        result = self.data
        if author:
            result = result[result['author'].str.lower() == author.lower()]
        if genre:
            result = result[result['genre'].str.lower() == genre.lower()]

        return result['title'].tolist()
