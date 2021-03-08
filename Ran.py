import random
size = int(input("Enter the number of time wanna play this game:"))
user_point = 0
cmp_point = 0
for i in range(size):
    rnd = random.choice(["stone","paper","scissor"])
    while(True):
        print("""Press 1 for stone\nPress 2 for paper\nPress 3 for scissor""")
        c = input("Enter choice for %d game:"%(i+1))
        if(c=="1"):
            c = "stone"
            break
        elif(c=="2"):
            c = "paper"
            break
        elif(c=="3"):
            c ="scissor"
            break
        else:
            print("pls,select the right choice")
    if((c=="stone" and rnd == "scissor") or \
        (c == "paper" and rnd == "stone") or\
        (c == "scissor" and rnd == "paper")):
        user_point +=1
    elif(c==rnd):
        pass
    else:
        cmp_point+=1
    print("User choice for %d match is %s"%(i+1,c))
    print("Computer choice for %d match %s"%(i+1,rnd))
    print("Total point of user=",user_point)
    print("Total point of computer=",cmp_point)
    if(cmp_point==user_point):
        print("Match tie")
    elif(cmp_point>user_point):
        print("Computer won the game")
    else:
        print("User won the game")
