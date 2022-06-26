print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


name1 = name1.lower()
name2 = name2.lower()

T = name1.count("t") + name2.count("t")
R = name1.count("r") + name2.count("r")
U = name1.count("u") + name2.count("u")
E = name1.count("e") + name2.count("e")

truu = T + R + U + E

L = name1.count("l") + name2.count("l")
O = name1.count("o") + name2.count("o")
V = name1.count("v") + name2.count("v")
E = name1.count("e") + name2.count("e")

luve = L + O + V + E

truu_luve = int(str(truu) + str(luve))

if truu_luve < 10 or truu_luve > 90:
  print(f"Your score is {truu_luve}, you go together like coke and mentos.")
elif truu_luve >= 40 and truu_luve <= 50:
  print(f"Your score is {truu_luve}, you are alright together")
else:
  print(f"Your score is {truu_luve}")
  
