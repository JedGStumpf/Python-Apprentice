def get_bread():
    bread = input("What type of bread would you like? ")
    print(f"Getting {bread} bread...")
    return bread

def get_filling():
    filling = input("What filling do you want? ")
    print(f"Adding {filling}...")
    return filling

def add_condiments():
    condiments = input("Any condiments? (type 'none' for no condiments) ")
    if condiments.lower() != 'none':
        print(f"Spreading {condiments}...")
    else:
        print("No condiments added.")
    return condiments

def make_sandwich():
    print("\nWelcome to the Robot Sandwich Maker!")
    bread = get_bread()
    filling = get_filling()
    condiments = add_condiments()
    
    print("\nHere is your sandwich order:")
    print(f"Bread: {bread}")
    print(f"Filling: {filling}")
    if condiments.lower() != 'none':
        print(f"Condiments: {condiments}")
    print("Enjoy your sandwich!")




