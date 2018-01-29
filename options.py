from time import sleep
import random

list1=[]
objects=["gun", "table", "chair", "slav", "phone", "ice cream", "TV", "book", "couch", "sofa", "spoon", "computer", "bomb", "bread", "sandal", "",]
def add():
  while True:
    user=input("Name one thing in your fridge: ")
    user=user.lower()
    list1.append(user)
    print(list1)
     
    if user in objects:
      print("This does not belong in a fridge. ")
      list1.remove(user)
     
    user2=input("Is there anything else in your fridge? ")
      
    if user2 == "yes":
      add()
        
    elif user2 == "no":
      print("Goodbye. ")
      break


add()
