# Book-recommender

A simple Python-based content-based book recommendation system using basic filtering by **author** and **genre**, powered by `pandas`.

## 📂 Dataset

Located in **data/books.csv**

| Column | Description           | Example                |
|--------|-----------------------|------------------------|
| title  | Book title            | 1984                   |
| author | Author of the book    | George Orwell          |
| genre  | Main genre/category   | Dystopian              |

> You can extend the dataset by adding more columns such as `year`, `rating`, or `description`.
## 💡 How it works

The `BookRecommender`:

1. Loads the dataset using `pandas`.
2. Filters books by:
   - Exact **author** match (case-insensitive)
   - Exact **genre** match (case-insensitive)
3. Returns a list of matching titles.


## 🏁 Quickstart

### 🔧 Install requirements

```bash
pip install pandas
