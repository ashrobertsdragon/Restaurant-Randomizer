import random
import os
import time
import json 

def loadfile():
	if os.path.exists("favorites.json"):
		f = open("favorites.json", "r")
		favorites_dict = json.load(f)
		f.close()
	else:
		favorites_dict = {}

	return favorites_dict

def create_favorites(favorites_dict):
	
	
	print("Menu:")
	print()
	print("1. Create new location")
	print("2. Add new restaurant to location")

	menu_choice = int(input(" > "))
	if menu_choice == 1:
	
		print()
		print("Enter a location for this group of restaurants (i.e. work, home, etc.)")
		location = input(" > ")
		favorites_dict[location] = []

		another_location = input("Add another location? (y/n) ")
		if another_location.lower() == "n":
			time.sleep(1)
			os.system("clear")
			
			return
		
		else:
			time.sleep(1)
			os.system("clear")
			create_favorites(favorites_dict)

	elif menu_choice == 2:
		for i, location in location:
			print(f"{i + 1}:. {location}")
		add_to_location = input("Which location do you want to add a restaurant to?")
		for restaurant in location[add_to_location - 1]:
			print(f"{restaurant}, ")

		print()
		while True:
			restaurant = input("What restaurants do you want to add > ")
			favorites_dict[add_to_location].append(restaurant)
			another_restaurant = input("Add another restaurant? (y/n) ")
			if another_restaurant.lower() == "n":
				break
	else:
		print("Invalid choice")

	return

def restaurant_randomizer(favorites_dict):
	locations = list(favorites_dict.keys())
	locations.remove("favorites")
	location = random.choice(locations)
	restaurants = favorites_dict[location]
	restaurant = random.choice(restaurants)
	print(f"{restaurant}")
	end_program = input ("End program? (y/n) ")
	if end_program.lower() == "y":
		exit()

def view_favorites(favorites_dict):
	
	for i, location in favorites_dict:
		print(f"{i + 1}. {location}")

	which_location = input("Which location do you want to view? ")
	view_location = favorites_dict[which_location - 1]
	for restaurant in view_location:
		print(f"{restaurant}")

	

	go_back = input("Go back? (y/n) ")
	if go_back.lower() == "y":
		time.sleep(1)
		os.system("clear")

		return
	
	else:
		another = input("Another location? (y/n) ")
		if another.lower() == "y":
			time.sleep(1)
			os.system("clear")
			view_favorites(favorites_dict)
		else:
			exit()

def remove_favorites(favorites_dict):
	
	print("Menu:")
	print()
	print("1. Remove location")
	print("2. Remove restaurant")

	menu_choice = int(input(" > "))
	if menu_choice == 1:

		for i, location in favorites_dict:
			print(f"{i + 1}. {location}")
		remove_location = input("Which location do you want to remove? > ")
		favorites_dict.pop(remove_location - 1)
		another_location = input("Add another location? (y/n) > ")
		if another_location.lower() == "n":
			time.sleep(1)
			os.system("clear")
			
			return
		
		else:
			time.sleep(1)
			os.system("clear")
			remove_favorites(favorites_dict)
	
	if menu_choice == 2:
		for i, location in favorites_dict:
			print(f"{i + 1}. {location}")
		remove_restaurant_from_location = int(input("Which location do you want to remove a restaurant from? > "))
	
		for i, restaurant in favorites_dict[remove_restaurant_from_location - 1]:
			print(f"{i + 1}. {restaurant}")
		
		remove_restaurant = input("Which restaurant do you want to remove from {location}? (y/n) > ")
		favorites_dict[location].pop(remove_restaurant - 1)

		another_restaurant = input("Remove another restaurant? (y/n) > ")
		if another_restaurant.lower() == "n":
			time.sleep(1)
			os.system("clear")
			
			return
		
		else:
			time.sleep(1)
			os.system("clear")
			remove_favorites(favorites_dict)

def main():
	
	favorites_dict = loadfile()

	print("Menu:")
	print()
	print("1. Restaurant randomizer")
	print("2. View favorites")
	print("3. Add new restaurant or location")
	print("4. Remove restaurant or location")
	print("5. Exit")

	menu_choice = int(input(" > "))
	if menu_choice == 1:
		restaurant_randomizer(favorites_dict)
	elif menu_choice == 2:
		view_favorites(favorites_dict)
	elif menu_choice == 3:
		create_favorites(favorites_dict)
	elif menu_choice == 4:
		remove_favorites(favorites_dict)
	elif menu_choice == 5:
		exit()
		
if __name__ == "__main__":
    main()