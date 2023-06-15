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

class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
            
    def display_info(self):
        return f"Hello{self.name} is {self.age} years old"
    # def calculate_avg(self):
         