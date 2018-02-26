from time import sleep
import random

list1=[]
objects=["gun", "table", "chair", "slav", "phone", "ice cream", "TV", "book", "couch", "sofa", "spoon", "computer", "bomb", "bread", "sandal", "",]

def ham():
  print("1 pack of ham is 150 calories. ")
   
def milk():
  print("If you have 3 litres, then calories = 3000. ")
  print("If you have 2 litres, then calories = 2300. ")
 
def egg():
  print("1 Egg is 155 calories. A dozen eggs is 936 calories. ")
 
def banana():
  print("A banana is 89 calories.")
  
def cheese():
  print("There is 402 calories in every 100 grams of cheddar cheese. ")
  
def butter():
  print("There is 717 calories in every 100 grams of butter. ")
  
def ketchup():
  print("There is 112 calories in every 100 grams of ketchup")
  
def coleslaw():
  print("There is 152 calories in every 100 grams of store-bought coleslaw. ")
  print("In every 100 grams of home-made coleslaw, there is only 78 calories. ")
  
def yoghurt():
  print("There is 59 calories in every 100 grams of greek yoghurt. ")
  print("In every 100 grams of frozen yoghurt, there is 160 calories. ")
  
def pepper():
  print("There is 43 in a large red pepper. ")
  print("In a large yellow pepper, there is 27 calories. ")
  print("There is 20 calories in a large green pepper. ")
  
def mushroom():
  print("There is 20 calories in every 100 grams of white mushrooms. ")
  
def salad_leaves():
  print("There is 2 calories in one spinach leaf. ")
  print("Rocket leaves have 0 calories. ")
  
def beetroot():
  print("There is 35 calories in a single beetroot. ")
  
def lettuce():
  print("There is 75 calories in a single head of iceberg lettuce. ")
  
def mayo():
  print("There is 680 calories in every 100 grams of mayonnaise. ")

def mustard():
  print("There is 66 calories in every 100 grams of Heinz mustard. ")
  print("In Dijon mustard, there is 160 calories in every 100 grams. ")
  


def add():
  while True:
    user=input("Name one thing in your fridge: ")
    user=user.lower()
    list1.append(user)
    print(list1)
     
    if user in objects:
      print("This does not belong in a fridge. ")
      list1.remove(user)
      
    user3=input("How much " + user + " is there in the fridge? ")
    user3=user3.lower()
    user4=input("How would you measure this product? (Packets/slices/grams/litres depending on the product.) ")
    user4=user4.lower()
    
    def quantity():
      print("You have " + user3 + " " + user4 + " of " + user)
  
      print("That is equal to " )
  
    
     
    user2=input("Is there anything else in your fridge? ")
      
    if user2 == "yes":
      add()
        
    elif user2 == "no":
      print("Here is information about the contents of your fridge: ")
      
      if "ham" in list1:
        ham()
        quantity()
        break
        
        if "butter" in list1:
          butter()
          quantity()
          break
      
          if "milk" in list1:
            milk()
            quantity()
            break
        
            if "egg" in list1:
              egg()
              quantity()
              break
        
              if "banana" in list1:
                banana()
                quantity()
                break
      
                if "cheese" in list1:
                  cheese()
                  quantity()
                  break
        
        
        


add()




