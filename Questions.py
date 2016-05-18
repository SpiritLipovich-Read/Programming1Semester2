import random
a = "Why is cannibalism taboo?"
b = "Who was the first person to have a name?"
c = "What does the inside of a sphere made out of a mirror look like?"
d = "Is anyhing original?"
e = "What does green mean?"
f = "When did time start?"
g = "Where did your ideas come from?"
h = "How can you ever be sure you're awake?"
i = "Can we ever truly know someone, even ourselves?"
j = "If noone believes it is it still true?"
stuffs =[a, b, c, d, e, f, g, h, i, j]
print(random.choice(stuffs))
my_file = open("output.txt", "w")

str = input("Penny for your thoughts?")
print("Thanks, here's a penny.")

my_file.close()
