# The inputs are the stories the output should be the record of the stories aseembled together 
#based on their categories and the translations. The process is creating a class for story and creating
#different methods to handle the trnslation and category of the stories
class Story:
    def __init__(self,story,language):
        self.story = story
        self.language = language
    def add_book(self, new_story):
        self.story+= new_story
        return f"{new_story} has been added to {self.story}."    
    def translate(self,new_language):
        new_language += self.language
        return f"{self.story} is now available in {new_language}"
    

#The following class has ingredients, preparation time, cooking method and nutritional info as inputs, 
#It has three methods one that explains the ingredients needed, other that explains the nutrition value
#and other that explains the steps followed.


class Recipe:
    def __init__(self,ingredients,prep_time,cooking_method,nutritional_info):
        self.ingredients= ingredients
        self.prep_time = prep_time
        self.cooking_method = cooking_method
        self.nutritional_info = nutritional_info
    def explain_recipe(self,name_of_food):
        return f"You need {self.ingredients}to prepare {name_of_food}"   
    def explain_value(self,name_of_food):
        return f"{name_of_food} has a nutritioal value of {self.nutritional_info}"
    def prep_step(self,name_of_food):
        return f"{name_of_food} takes {self.prep_time} to prepare. You must follow {self.prep_step} to prepare it"      

# class Wildlife:
#     def __init__(self,diet,lifespan, migration_pattern)





#The following class has inputs of prodct name price and quantity it will have an outcome of the 
#total value of the product

class product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_total_value(self,total_value):
        total_value = self.price*self.quantity    
        return f"{total_value} is the total value to pay for the purchase of {self.name}" 

#The following class will have student name age and grade as an input it will have methods to 
#display student information and to calculate the average grades

class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
            
    def display_info(self):
        return f"Hello{self.name} is {self.age} years old"
    # def calculate_avg(self):

    #The following class will have input of customer informaton and flight information
    #it will have methods to notify available flights, reserve seats and confirm notificatons and
    # display customer information.

class Booking:
    def __init__(self,name,available_flights,destination_with_date):
        self.name = name
        self.available_flights = available_flights
        self.destinaton_with_date = destination_with_date  
    def reserve_seats(self,status_of_seat):
        return f"{self.name} has reserved {status_of_seat}"
    def available_flight(self):
        if self.available_flights>=1 and self.destinaton_with_date >=1:
            return f"There is an available flight"
        else:
            return f"Sorry, there is no available flight at the moment"   
    def passenger_info(self):
        return f"{self.name} has {self.available_flights} to {self.destinaton_with_date}" 
#The following class will handle books it has methods to add new books, search for books by
#title or author, keep track of available copies, and display book details.

class Books:
    def __init__(self,books,title,author):
        self.books = books
        self.title = title
        self.author = author

    def add_new_books(self,new_book):
        self.books.append(new_book)  
        return f"{self.books} have been updated"


         