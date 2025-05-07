import random

list = ["What do you call a singer with a laptop on her head? A-Dell.",
        "When is a door not a door? When it's ajar.",
        "What do toilets do when they're embarrassed? They get a bit flush.",
        "Why do pancakes always win at baseball? They have the best batter.",
        "Why did the robot arrive at the event so tired? He had a hard drive.",
        "What do runners eat before a race? Nothing. They fast.",
        "How do you stop an astronaut’s toddler from crying? You rocket.",
        "hat do you call an unpredictable camera? A loose Canon.",
        "What did the policeman say to his nipple? You're under a vest.",
        "What did the policeman say to his nipple? You're under a vest.",
        "What did the dentist win at the competition? A little plaque.",
        "Why do ghosts like to take the elevator? It lifts their spirits.",
        "Why doesn't Dracula have any friends? He's a bit of a pain in the neck."]
while True:
    h = input("joke?")
    if h == "yes":
       print(random.choice(list))
    elif h == "exit":
        break
