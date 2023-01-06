subjects = ["physics", "calculus", "poetry", "history"]
grade = [98, 97, 85, 88]

gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]
print(gradebook)

gradebook.append(["computer science", 100])
print(gradebook)
gradebook.append(["visual arts", 93])
print(gradebook)

vis_art = gradebook[-1][-1] = 98
print(gradebook)

gradebook[2].remove(85)
print(gradebook)
