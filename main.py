print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name_1_lowercase = name1.lower()
name_2_lowercase = name2.lower()

names_together = name_1_lowercase + name_2_lowercase

t_times = int(names_together.count("t"))
r_times = int(names_together.count("r"))
u_times = int(names_together.count("u"))
e_times = int(names_together.count("e"))
l_times = int(names_together.count("l"))
o_times = int(names_together.count("o"))
v_times = int(names_together.count("v"))

first_number = str(t_times + r_times + u_times + e_times)
second_number = str(l_times + o_times + v_times + e_times)

final_love_score = int(first_number + second_number)

if (final_love_score < 10) or (final_love_score > 90):
    print(f"Your score is {final_love_score}, you go together like coke and mentos.")
elif (final_love_score > 40) and (final_love_score < 50):
    print(f"Your score is {final_love_score}, you are alright together.")
else:
    print(f"Your score is {final_love_score}.")

