import random

enter_goals_here = [
    "goal 1",
    "goal 2",
    "goal 3",
    "goal 4",
    "goal 5",
    "goal 6",
    "goal 7",
    "goal 8",
    "goal 9",
    "goal 10",
    "goal 11",
    "goal 12",
    "goal 13",
    "goal 14",
    "goal 15",
    "goal 16",
    "goal 17",
    "goal 18",
    "goal 19",
    "goal 20",
    "goal 21",
    "goal 22",
    "goal 23",
    "goal 24",
    "goal 25"
]

new_list = random.sample(enter_goals_here, 25)
for i in range(25):
    while len(new_list[i]) < 4*12:
        new_list[i] += " "

line = ""
for i in range(80):
    line += "-"

print(line)
iterator_goals = iter(new_list)

for row in range(5):
    box1 = next(iterator_goals).split()
    box2 = next(iterator_goals).split()
    box3 = next(iterator_goals).split()
    box4 = next(iterator_goals).split()
    box5 = next(iterator_goals).split()
    goals = [box1, box2, box3, box4, box5]
    
    for height in range(5):
        p_str = "| "

        for i in range(5):
            words = ""
            while len(goals[i]) > 0 and len(words + goals[i][0]) < 13:
                words += goals[i][0] + " "
                del goals[i][0]
            while len(words) < 13:
                words += " " 
            p_str += words + " | "
        print(p_str)

    print(line)

    
    
