# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

c_s = name1 + name2

lower_s = c_s.lower()

t = lower_s.count("t")
r = lower_s.count("r")
u = lower_s.count("u")
e = lower_s.count("e")

true = t+ r+ u+ e

l = lower_s.count("l")
o = lower_s.count("o")
v = lower_s.count("v")
e = lower_s.count("e")

love = l+ o+ v+ e

love_score = str(true + love)

print(love_score)

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score>90):
    print(f"Your love score is {love_score}, you go together like coke and mentos.")
elif(love_score>=40)  and (love_score <=50):
    print(f"Your love score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")    
