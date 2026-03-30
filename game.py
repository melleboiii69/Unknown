import time
import random


thoughts= [
    "I want to play!",
    "Can we go for a walk?",
    "I feel like napping...",
    "Is it dinner time yet?",
    "I'm so happy to see you!"
]
pet_stats = {
    "hunger": 10,
    "happiness": 10,
    "energy": 10
}



while pet_stats["hunger"] > 0:
    
    pet_stats["hunger"] -= 1
    
    print(f"\n--- STATS: Hunger: {pet_stats['hunger']} | Happiness: {pet_stats['happiness']} | Energy: {pet_stats['energy']} ---")

    current_thought = random.choice(thoughts)
    print(current_thought)
    action = input("What do you want to do?").lower()
    
    if pet_stats["hunger"] <= 3:
        print("( x . x )  I am starving...")
    elif pet_stats["happiness"] <= 3:
        print("( - . - )  I am bored...")
    elif pet_stats["energy"] <= 3:
        print("(¤ . ¤)  I am tired...")
    else:
        print("( ^ . ^ )  I am happy!")
        
        if action in ["eat", "feed"]:
            pet_stats["hunger"] += 2
            pet_stats["energy"] -= 1
            print("You fed you pet +1 hunger, I am getting tired")
        elif action == "play":
            pet_stats["happiness"] += 2
            pet_stats["energy"] -= 1
        elif action in ["sleep", "rest"]:
            pet_stats["energy"] += 3
    
    pet_stats["hunger"] = min(pet_stats["hunger"], 10)
    pet_stats["energy"] = min(pet_stats["energy"], 10)
    pet_stats["happiness"] = min(pet_stats["happiness"], 10)