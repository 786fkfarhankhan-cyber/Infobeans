# 17. Write a Python program to create a class called "Movie" with attributes for title, director, actors, and reviews, and methods for adding and retrieving reviews.

class Movie:
    def __init__(self, title, director, actors, reviews):
        self.__title = title
        self.__director = director
        self.__actors = actors
        self.__reviews = reviews

    def add_review(self, review):
        self.__reviews.append(review)

    def get_reviews(self):
        return self.__reviews
    def detail(self):
        print(f"Title: {self.__title}")
        print(f"Director: {self.__director}")
        print(f"Actors: {self.__actors}")
        print(f"Reviews: {self.__reviews}")


movie1 = Movie(
    "3 Idiots",
    "Rajkumar Hirani",
    ["Aamir Khan", "R. Madhavan", "Sharman Joshi"],
    ["Excellent movie!"]
)
movie1.add_review("Very inspiring story.")
print(movie1.get_reviews())
movie1.detail()

print()

movie2 = Movie(
    "Hungama",
    "Priyadarshan",
    ["Akshaye Khanna", "Aftab Shivdasani", "Rimi Sen", "Paresh Rawal"],
    ["Very funny movie!", "Excellent comedy."]
)
movie2.add_review("Very Funny Story.")
print(movie2.get_reviews())
movie2.detail()




