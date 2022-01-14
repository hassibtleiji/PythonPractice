print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

both_names = name1 + name2
both_names_lwr = both_names.lower()

t_count = both_names_lwr.count("t")
r_count = both_names_lwr.count("r")
u_count = both_names_lwr.count("u")
e_count = both_names_lwr.count("e")

true = t_count + r_count + u_count + e_count
 
l_count = both_names_lwr.count("l")
o_count = both_names_lwr.count("o")
v_count = both_names_lwr.count("v")
e_count = both_names_lwr.count("e")

love = l_count + o_count + v_count + e_count

loveScore = int(str(true) + str(love))  

if ((loveScore < 10) or (loveScore > 90)):
    print(f"Your score is {loveScore}, you go together like coke and mentos.") 
elif ((loveScore >= 40) and (loveScore <= 50)):
    print(f"Your score is {loveScore}, you are alright together.")
else:
    print(f"Your score is {loveScore}.")
