import random

# stats stored in a dictionary
stats = {
    "Grades": 50,
    "Money": 50,
    "Reputation": 50,
    "Attendance": 50
}

# simple helper to show stats
def show_stats():
    print("\nStats:")
    for k, v in stats.items():
        print(" ", k, ":", v)


# RANDOM EVENTS (using a list of dictionaries)
random_events = [
    {
        "event": "You got rejected :((",
        "changes": {"Grades": -5, "Money": 0, "Reputation": -15, "Attendance": -15}
    },
    {
        "event": "You lost your wallet :((",
        "changes": {"Grades": 0, "Money": -50, "Reputation": 0, "Attendance": 0}
    },
    {
        "event": "Your pens got stolen :((",
        "changes": {"Grades": -5, "Money": -10, "Reputation": 0, "Attendance": 0}
    },
    {
        "event": "Campus dog follows you around 🐶",
        "changes": {"Grades": 0, "Money": 0, "Reputation": +30, "Attendance": 0}
    },
    {
        "event": "You get full on a surprise test! 🎉",
        "changes": {"Grades": +20, "Money": 0, "Reputation": +20, "Attendance": 0}
    },
    {
        "event": "Library book is magically available 📚",
        "changes": {"Grades": +20, "Money": 0, "Reputation": 0, "Attendance": 0}
    },
]

def apply_changes(change_dict):
    """Add values from dictionary to stats dictionary"""
    for key in change_dict:
        stats[key] += change_dict[key]

def random_event(round_name):
    """Simple 30% chance random event"""
    chance = random.random()
    if chance < 0.3:
        event = random.choice(random_events)
        print("\n*** RANDOM EVENT in", round_name, "*")
        print(event["event"])
        apply_changes(event["changes"])


# -------------------- ROUND 1 --------------------

def round1():
    print("\n========== ROUND 1 ==========")

    # Q1
    while True:
        print("\nQ1. Your teacher locked you out!")
        print("a) Keep knocking")
        print("b) Wait outside")
        print("c) Go to library")
        c = input("Choose: ")

        if c == "a":
            apply_changes({"Reputation": -20, "Attendance": +20})
            break
        elif c == "b":
            apply_changes({"Reputation": -10, "Attendance": +10})
            break
        elif c == "c":
            apply_changes({"Grades": +20, "Attendance": -20})
            break
        else:
            print("Uh-oh, you entered the wrong character. Please try again.")

    # Q2
    while True:
        print("\nQ2. You forgot your notebook :(")
        print("a) Borrow from topper")
        print("b) Click photos")
        print("c) Ignore notes")
        c = input("Choose: ")

        if c == "a":
            apply_changes({"Grades": +10, "Reputation": +5})
            break
        elif c == "b":
            apply_changes({"Grades": +5, "Reputation": -5})
            break
        elif c == "c":
            apply_changes({"Grades": -15, "Reputation": +10})
            break
        else:
            print("Uh-oh, you entered the wrong character. Please try again.")

    # Q3
    while True:
        print("\nQ3. Classmate asks for help")
        print("a) Help fully")
        print("b) Give hints")
        print("c) Say you're busy")
        c = input("Choose: ")

        if c == "a":
            apply_changes({"Reputation": +15, "Grades": +5, "Attendance": -5})
            break
        elif c == "b":
            apply_changes({"Reputation": +5})
            break
        elif c == "c":
            apply_changes({"Grades": +10, "Reputation": -10, "Attendance": +5})
            break
        else:
            print("Uh-oh, you entered the wrong character. Please try again.")

    # Q4
    while True:
        print("\nQ4. Teacher calls on you unexpectedly")
        print("a) Try your best")
        print("b) Make up something")
        print("c) Pretend you didn't hear")
        c = input("Choose: ")

        if c == "a":
            apply_changes({"Grades": +10})
            break
        elif c == "b":
            apply_changes({"Reputation": -5})
            break
        elif c == "c":
            apply_changes({"Attendance": -10, "Reputation": -20})
            break
        else:
            print("Uh-oh, you entered the wrong character. Please try again.")

    random_event("Round 1")
    show_stats()


# -------------------- ROUND 2 --------------------

def round2():
    print("\n========== ROUND 2 ==========")

    # Q1
    while True:
        print("\nQ1. The canteen line is huge.")
        print("a) Wait patiently")
        print("b) Skip lunch")
        print("c) Jump line")
        c = input("Choose: ")

        if c == "a":
            apply_changes({"Attendance": -10, "Reputation": +5})
            break
        elif c == "b":
            apply_changes({"Money": +20, "Grades": -5})
            break
        elif c == "c":
            apply_changes({"Reputation": -20, "Money": -10})
            break
        else:
            print("Uh-oh, you entered the wrong character. Please try again.")

    # Q2
    while True:
        print("\nQ2. Surprise quiz!")
        print("a) Write seriously")
        print("b) Peek at friend's sheet")
        print("c) Submit blank")
        c = input("Choose: ")

        if c == "a":
            apply_changes({"Grades": +20})
            break
        elif c == "b":
            apply_changes({"Grades": +10, "Reputation": -10})
            break
        elif c == "c":
            apply_changes({"Grades": -20, "Reputation": -20})
            break
        else:
            print("Uh-oh, you entered the wrong character. Please try again.")

    # Q3
    while True:
        print("\nQ3. Friend wants to copy your assignment.")
        print("a) Let them copy")
        print("b) Refuse politely")
        print("c) Give half answers")
        c = input("Choose: ")

        if c == "a":
            apply_changes({"Reputation": +15, "Grades": -20})
            break
        elif c == "b":
            apply_changes({"Reputation": -5, "Grades": +5})
            break
        elif c == "c":
            apply_changes({"Reputation": +10})
            break
        else:
            print("Uh-oh, you entered the wrong character. Please try again.")

    # Q4
    while True:
        print("\nQ4. You see a professor walking to class.")
        print("a) Rush to class")
        print("b) Pretend to tie shoelace")
        print("c) Hide behind pillar")
        c = input("Choose: ")

        if c == "a":
            apply_changes({"Attendance": +10, "Reputation": -5})
            break
        elif c == "b":
            apply_changes({"Reputation": +5})
            break
        elif c == "c":
            apply_changes({"Reputation": -10, "Attendance": -10})
            break
        else:
            print("Uh-oh, you entered the wrong character. Please try again.")

    random_event("Round 2")
    show_stats()


# -------------------- ROUND 3 --------------------

def round3():
    print("\n========== ROUND 3 ==========")

    # Q1
    while True:
        print("\nQ1. You’re sleepy in class")
        print("a) Take notes anyway")
        print("b) Sleep at desk")
        print("c) Leave class for coffee")
        ch = input("Choose: ")

        if ch == "a":
            apply_changes({"Grades": +10})
            break
        elif ch == "b":
            apply_changes({"Attendance": -10, "Grades": -10, "Reputation": -5})
            break
        elif ch == "c":
            apply_changes({"Money": -20, "Attendance": +5, "Grades": -10, "Reputation": +5})
            break
        else:
            print("Uh-oh! You entered the wrong character!\n")

    # Q2
    while True:
        print("\nQ2. A group invites you to bunk and chill.")
        print("a) Join them")
        print("b) Refuse and attend")
        print("c) Convince them to come to class")
        ch = input("Choose: ")

        if ch == "a":
            apply_changes({"Reputation": +15, "Attendance": -20, "Grades": -5})
            break
        elif ch == "b":
            apply_changes({"Attendance": +20, "Grades": +5, "Reputation": -5})
            break
        elif ch == "c":
            apply_changes({"Reputation": +10, "Grades": +10})
            break
        else:
            print("Uh-oh! You entered the wrong character!\n")

    # Q3
    while True:
        print("\nQ3. You lose your pen.")
        print("a) Buy a new one")
        print("b) Borrow from someone")
        print("c) Don’t write anything today")
        ch = input("Choose: ")

        if ch == "a":
            apply_changes({"Money": -10})
            break
        elif ch == "b":
            apply_changes({"Reputation": +5})
            break
        elif ch == "c":
            apply_changes({"Grades": -15})
            break
        else:
            print("Uh-oh! You entered the wrong character!\n")

    # Q4
    while True:
        print("\nQ4. Lab session starts in 5 minutes.")
        print("a) Go early to prepare")
        print("b) Arrive just on time")
        print("c) Skip lab")
        ch = input("Choose: ")

        if ch == "a":
            apply_changes({"Grades": +10})
            break
        elif ch == "b":
            apply_changes({"Attendance": +5})
            break
        elif ch == "c":
            apply_changes({"Attendance": -15, "Grades": -10})
            break
        else:
            print("Uh-oh! You entered the wrong character!\n")

    random_event("Round 3")
    show_stats()


# -------------------- ROUND 4 --------------------

def round4():
    print("\n========== ROUND 4 ==========")

    # Q1
    while True:
        print("\nQ1. Evening tutorial gives extra credit.")
        print("a) Attend")
        print("b) Skip and go home")
        print("c) Join online & sleep")
        ch = input("Choose: ")

        if ch == "a":
            apply_changes({"Grades": +20, "Attendance": +10})
            break
        elif ch == "b":
            apply_changes({"Attendance": -10})
            break
        elif ch == "c":
            apply_changes({"Attendance": +5, "Grades": +5, "Reputation": -5})
            break
        else:
            print("Uh-oh! You entered the wrong character!\n")

    # Q2
    while True:
        print("\nQ2. A movie plan with friends.")
        print("a) Go with them")
        print("b) Refuse")
        print("c) Suggest group study")
        ch = input("Choose: ")

        if ch == "a":
            apply_changes({"Reputation": +20, "Money": -50, "Grades": -10})
            break
        elif ch == "b":
            apply_changes({"Grades": +10, "Reputation": -5})
            break
        elif ch == "c":
            apply_changes({"Grades": +15, "Reputation": +10})
            break
        else:
            print("Uh-oh! You entered the wrong character!\n")

    # Q3
    while True:
        print("\nQ3. You forgot your lunch.")
        print("a) Buy food")
        print("b) Borrow some from friend")
        print("c) Stay hungry")
        ch = input("Choose: ")

        if ch == "a":
            apply_changes({"Money": -40, "Attendance": -5})
            break
        elif ch == "b":
            apply_changes({"Reputation": +10})
            break
        elif ch == "c":
            apply_changes({"Grades": -10})
            break
        else:
            print("Uh-oh! You entered the wrong character!\n")

    # Q4
    while True:
        print("\nQ4. Class rep asks you to help distribute sheets.")
        print("a) Help")
        print("b) Make excuses")
        print("c) Run away")
        ch = input("Choose: ")

        if ch == "a":
            apply_changes({"Reputation": +10})
            break
        elif ch == "b":
            apply_changes({"Reputation": -5})
            break
        elif ch == "c":
            apply_changes({"Reputation": -15})
            break
        else:
            print("Uh-oh! You entered the wrong character!\n")

    random_event("Round 4")
    show_stats()


# -------------------- ROUND 5 --------------------

def round5():
    print("\n========== ROUND 5 ==========")

    # Q1
    while True:
        print("\nQ1. Fest rehearsal begins.")
        print("a) Join enthusiastically")
        print("b) Watch others rehearse")
        print("c) Leave campus")
        ch = input("Choose: ")

        if ch == "a":
            apply_changes({"Reputation": +20, "Attendance": -10})
            break
        elif ch == "b":
            apply_changes({"Reputation": +5})
            break
        elif ch == "c":
            apply_changes({"Attendance": -15})
            break
        else:
            print("Uh-oh! You entered the wrong character!\n")

    # Q2
    while True:
        print("\nQ2. You get an unexpected holiday.")
        print("a) Use it to study")
        print("b) Sleep whole day")
        print("c) Go out with friends")
        ch = input("Choose: ")

        if ch == "a":
            apply_changes({"Grades": +20})
            break
        elif ch == "b":
            apply_changes({"Attendance": -10})
            break
        elif ch == "c":
            apply_changes({"Reputation": +15, "Money": -60})
            break
        else:
            print("Uh-oh! You entered the wrong character!\n")

    # Q3
    while True:
        print("\nQ3. Group project deadline tomorrow.")
        print("a) Do all the work")
        print("b) Share work equally")
        print("c) Let others handle it")
        ch = input("Choose: ")

        if ch == "a":
            apply_changes({"Grades": +20, "Reputation": +10})
            break
        elif ch == "b":
            apply_changes({"Grades": +10})
            break
        elif ch == "c":
            apply_changes({"Reputation": -15, "Grades": -10})
            break
        else:
            print("Uh-oh! You entered the wrong character!\n")

    # Q4
    while True:
        print("\nQ4. Someone challenges you to a gaming match.")
        print("a) Accept and win")
        print("b) Accept and lose")
        print("c) Say you're busy")
        ch = input("Choose: ")

        if ch == "a":
            apply_changes({"Reputation": +10, "Money": +10})
            break
        elif ch == "b":
            apply_changes({"Reputation": -5, "Money": -10})
            break
        elif ch == "c":
            apply_changes({"Grades": +10})
            break
        else:
            print("Uh-oh! You entered the wrong character!\n")

    random_event("Round 5")
    show_stats()


# -------------------- FINAL RESULTS --------------------

def final_results():
    print("\n========================================")
    print("      WEEK OVER! FINAL RESULTS")
    print("========================================\n")
    show_stats()

    # Grading the final results
    print("\n--- GRADES ---")
    if stats["Grades"] >= 80:
        print("You're a topper!")
    elif stats["Grades"] >= 50:
        print("You're average. You can do better!")
    elif stats["Grades"] >= 30:
        print("You really need to lock in and grind!")
    else:
        print("You failed. Better luck next time.")
    
    print("\n--- MONEY ---")
    if stats["Money"] >= 80:
        print("You're rich!")
    elif stats["Money"] >= 50:
        print("You're average. You can do better!")
    elif stats["Money"] >= 30:
        print("You really need to lock in and grind!")
    else:
        print("You're broke!")
    
    print("\n--- REPUTATION ---")
    if stats["Reputation"] >= 80:
        print("You're super popular!")
    elif stats["Reputation"] >= 50:
        print("You're average. You can do better!")
    elif stats["Reputation"] >= 30:
        print("You really need to lock in and grind!")
    else:
        print("Nobody knows you...")
    
    print("\n--- ATTENDANCE ---")
    if stats["Attendance"] >= 80:
        print("Perfect attendance!")
    elif stats["Attendance"] >= 50:
        print("You're average. You can do better!")
    elif stats["Attendance"] >= 30:
        print("You really need to lock in and grind!")
    else:
        print("You barely came to college!")

    print("\n========================================")
    print("         YOUR FINAL ENDING")
    print("========================================\n")

    # Different endings based on stat combinations
    if stats["Grades"] >= 80 and stats["Reputation"] >= 80 and stats["Attendance"] >= 80:
        print("THE LEGEND")
        print("You are the perfect student! Good grades, popular, and always present.")
        print("Everyone wants to be like you!")

    elif stats["Grades"] >= 80 and stats["Money"] < 30:
        print("THE BROKE GENIUS")
        print("You're super smart but have no money!")
        print("Your grades are amazing but you can't even afford canteen food.")
    
    elif stats["Reputation"] >= 80 and stats["Grades"] < 40:
        print("THE POPULAR ONE")
        print("Everyone knows you and wants to hang out with you!")
        print("But your grades... let's not talk about that.")
    
    elif stats["Attendance"] >= 80 and stats["Grades"] < 40:
        print("THE ATTENDANCE GHOST")
        print("You come to college every day but don't pay attention in class!")
        print("Teachers wonder if you're actually learning anything.")
    
    elif stats["Money"] >= 150 and stats["Grades"] < 40:
        print("THE RICH KID")
        print("You have lots of money but terrible grades.")
        print("Money can't buy intelligence!")

    elif stats["Grades"] >= 70 and stats["Reputation"] < 30:
        print("THE LONELY NERD")
        print("You're doing great in studies but have no friends.")
        print("The library is your only friend!")
    
    elif (stats["Grades"] + stats["Reputation"] + stats["Attendance"]) / 3 >= 70:
        print("THE GOOD STUDENT")
        print("You're doing well in everything!")
        print("Not perfect but definitely above average.")
    
    elif (stats["Grades"] + stats["Reputation"] + stats["Attendance"]) / 3 >= 50:
        print("THE AVERAGE STUDENT")
        print("You're just getting by. Nothing special.")
        print("But hey, at least you're not failing!")
    
    elif (stats["Grades"] + stats["Reputation"] + stats["Attendance"]) / 3 >= 30:
        print("THE STRUGGLER")
        print("College is hard for you...")
        print("You need to work much harder next semester!")
    
    else:
        print("THE DISASTER")
        print("Everything is going wrong!")
        print("Your grades, attendance, reputation - all are terrible.")
        print("You need a complete change next semester!")
    
    print("\n========================================")

# Main game
print("========================================")
print("   COLLEGE CAMPUS ADVENTURE")
print("     One Week of College Life")
print("========================================\n")

input("Press Enter to start Round 1...")
round1()
input("\nPress Enter to start Round 2...")
round2()
input("\nPress Enter to start Round 3...")
round3()
input("\nPress Enter to start Round 4...")
round4()
input("\nPress Enter to start Round 5...")
round5()

final_results()

print("\nThanks for playing!")
