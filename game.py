import time
import random

import random

pet_dialogue = {
    "Can you give me belly rubs? (yes/no)": "yes",
    "Is it time for a treat? (yes/no)": "yes",
    "Am i a good pet? (yes/no)": "yes",
    "Want to watch a movie? (yes/no)": "yes",
    "Can we go for a walk? (yes/no)": "yes",
    "Do you want to see my tricks? (yes/no)": "yes",
    "Is your programming getting better? (yes/no)": "yes"
}

pet_stats = {
    "hunger": 10,
    "happiness": 10,
    "energy": 10
}



while pet_stats["hunger"] > 0:
    
    pet_stats["hunger"] -= 1
    
    print(f"\n--- STATS: Hunger: {pet_stats['hunger']} | Happiness: {pet_stats['happiness']} | Energy: {pet_stats['energy']} ---")


    # --- NEW: Question Logic ---
    # 20% chance to ask a question each turn
    if random.randint(1, 5) == 1:
        # Pick a random question (key) from our dialogue dictionary
            current_question = random.choice(list(pet_dialogue.keys()))
            correct_answer = pet_dialogue[current_question]
        
    print(f"\nYour pet asks: '{current_question}'")
    user_response = input("Your answer: ").lower()
        
        # Check if you answered correctly
    if user_response == correct_answer:
            pet_stats["happiness"] += 3
            print("Yay! You know me so well! (+3 Happiness)")
    else:
            pet_stats["happiness"] -= 2
            print("Hmph. That's not what I wanted to hear... (-2 Happiness)")
            break

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
            print("You fed you pet (+1 hunger)")
    elif action == "play":
            pet_stats["happiness"] += 2
            pet_stats["energy"] -= 1
    elif action in ["sleep", "rest"]:
            pet_stats["energy"] += 3
            pet_stats ["hapiness"] -= 2
    
    pet_stats["hunger"] = min(pet_stats["hunger"], 10)
    pet_stats["energy"] = min(pet_stats["energy"], 10)
    pet_stats["happiness"] = min(pet_stats["happiness"], 10)