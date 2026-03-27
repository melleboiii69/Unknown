import time
pet_stats = {
    "hunger": 10,
    "happiness": 10,
    "energy": 10
}



while pet_stats["hunger"] > 0:
    
    pet_stats["hunger"] -= 1

    if pet_stats["hunger"] <= 3:
        print("( x . x )  I am starving...")
    elif pet_stats["happiness"] <= 3:
        print("( - . - )  I am bored...")
    elif pet_stats["energy"] <= 3:
        print("(¤ . ¤)  I am tired...")
    else:
        print("( ^ . ^ )  I am happy!")
        
        action = input("What do you want to do?").lower()
        
        if action == "feed":
            pet_stats["hunger"] += 2
            pet_stats["energy"] -= 1
            print("You fed you pet +1 hunger, I am getting tired")
        elif action == "play":
            pet_stats["happiness"] += 2
            pet_stats["energy"] -= 1
        elif action == "rest":
            pet_stats["energy"] += 3
    
    if pet_stats["hunger"] > 10:
        pet_stats["hunger"] = 10