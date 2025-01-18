# class 1
class Gambia():
    def capital(self):
        print("Banjul is the capital of Gambia")

    def language(self):
        print("wolof is the most widely spoken language of Gambia.")
        
    def type(self):
        print("Gamping is a developing country.")

# class 2
class USA():
    def capital(self):
        print("Washington, D.c. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developing country.")

# object creation 
obj_gam = Gambia()
obj_Usa = USA()
    
# common Interface
for country in (obj_gam, obj_Usa):
    country.capital()
    country.language()
    country.type()
    