# WRITE YOUR FUNCTIONS HERE


# Petshop name function
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

#return total cash
def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

#change the value of total cash
def add_or_remove_cash(pet_shop, money):
    pet_shop["admin"]["total_cash"] = pet_shop["admin"]["total_cash"] + money
    # pet_shop["admin"]["total_cash"] += amount   this is shorthand for above line!
    return pet_shop["admin"]["total_cash"] #doesn't need to return

#return list of pets sold
def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

# Increase the number of pets sold in pet shop
def increase_pets_sold(pet_shop, num_of_pets):
    pet_shop["admin"]["pets_sold"] = pet_shop["admin"]["pets_sold"] + num_of_pets
    # pet_shop["admin"]["pets_sold"] += num_of_pets   this is shorthand for above line!
    return pet_shop["admin"]["pets_sold"] # return not needed here!

# check the stock count of pets
def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

# find how many pets of a certain breed they have at the pet shop
def get_pets_by_breed(pet_shop, breed):
    pets = []
    for i in range(len(pet_shop["pets"])):
        if pet_shop["pets"][i]["breed"] == breed:
            pets.append(pet_shop["pets"][i]) #forgot to add index i & 
                                        #using append return value which is actually None!
            #print(pets)
    return pets

def find_pet_by_name(pet_shop, name):
        for i in range(len(pet_shop["pets"])):
            if pet_shop["pets"][i]["name"] == name:
                return pet_shop["pets"][i]
        return None


def remove_pet_by_name(pet_shop, name):
    for i in range(len(pet_shop["pets"])):
        #print(pet_shop["pets"][i]["name"])
        if pet_shop["pets"][i]["name"] == name:
            pet_shop["pets"].remove(pet_shop["pets"][i])
            break
#Took me ages to work out why I was geting an index error.
#Once I had removed the pet, the length of my list changed.
#Simply needed to break out of the loop as soon as pet was removed.

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, amount):
    customer["cash"] = customer["cash"] - amount

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)
        

# --- OPTIONAL ---

def customer_can_afford_pet(customer, new_pet):
    if customer["cash"] >= new_pet["price"]:
        return True
    else:
        return False
    #short hand - this could be one line
    # return customer["cash"] >= new_pet["price"]

# These are 'integration' tests so we want multiple asserts.
# If one fails the entire test should fail

def sell_pet_to_customer(pet_shop, pet, customer): #feeds in Arthur, Alice & shop
    if pet == None: #checks that pet exists in list
        return
    if customer == None: #checks that customer exists
        return
    if not customer_can_afford_pet(customer, pet): #checks the customer has cash to pay for pet.
        return
    add_pet_to_customer(customer, pet) #this increases customers pet count
    increase_pets_sold(pet_shop, 1) # this increases pets sold count by 1
    remove_pet_by_name(pet_shop, pet) #this removes pet from list of pets to sell
    remove_customer_cash(customer, pet["price"])  # this takes the price of the pet bought, from the customer's cash
    add_or_remove_cash(pet_shop, pet["price"]) #this adds the price of the pet sold to the total cash of the shop



