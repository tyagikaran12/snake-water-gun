import random
list1 = [1,2,3]
choice = int(input("Enter your choice: \n1) Snake \n2)Water \n3)Gun\n"))
score =0
comp = random.choice(list1)
if comp == choice:
    score+=0.5
elif comp == 1 and choice == 2:
    quit
elif comp == 1 and choice == 3:
    score +=1
elif comp == 2 and choice == 1:
    score+=1
elif comp == 2 and choice == 3:
    quit
elif comp == 3 and choice==1:
    quit
elif comp == 3 and choice == 2:
    score +=1
else:
    print("Choose one of the given choices.")

print(f"computer choice = {comp}")
print("Score = {}".format(score))
