# Movie Rating System
# Create a class Movie with fields: name, genre, and rating.
# Use setters and create a method isHit() that returns true if rating ≥ 8.0.

class Rating_system:
    def __init__(self):
        self.__name =None
        self.__genre = None
        self.__rating = None

    def set_name(self,name):
        self.__name = name
    def set_genre(self,genre):
        self.__genre = genre
    def set_rating(self,rating):
        self.__rating = rating     
        
    def is_hit(self):
        return self.__rating >=8.0

    def display_movie_rating(self):
        print(f"Name of Movie     : {self.__name}")
        print(f"Category of Movie : {self.__genre}")
        print(f"Movie Rating      : {self.__rating}")
        if self.is_hit():
            print("Movie Hit")
        else:
            print("Flop")

m1 = Rating_system()
m1.set_name("Pal Pal Dil Ke Pass")
m1.set_genre("Romance")
m1.set_rating(7.0)
m1.is_hit()
m1.display_movie_rating()

m2 = Rating_system()
m2.set_name("End Game")
m2.set_genre("Reality Show")
m2.set_rating(9.0)
m2.is_hit()
m2.display_movie_rating()

# m3 = Rating_system()
# m3.set_name("Journey To The West")
# m3.set_genre("Action")
# m3.set_rating(8.0)
# m3.display_movie_rating()










