cnp=0
cnc=0
cnt=0
while True:
    from random import choice
    l=["stone","paper","scissor"]
    m=['','stone','paper','scissor']
    a=choice(l)

    x=int(input('''1.stone
2.paper
3.scissor
4.stop  
Enter your choice: '''))
    
    if x==1 and a=="stone" or x==2 and a=="paper" or x==3 and a=="scissor":
        cnt+=1
        print("Your choice : ",m[x])
        print("Bot's choice is : ",a)
        print("tie")
        print(f"Score is you: {cnp} Bot: {cnc} ")

    elif x==1 and a=="paper" or x==2 and a=="scissor" or x==3 and a=="stone":  
        print("Your choice : ",m[x])
        print("Bot's choice is : ",a)
        print("You loose")
        cnc+=1
        print(f"Score is you: {cnp} Bot: {cnc} ")
    elif x==1 and a=="scissor" or x==2 and a=="stone" or  x==3 and a=="paper" :  
        print("Your choice : ",m[x])
        print("Bot's choice is : ",a)
        print("You win")
        cnp+=1
        print(f"Score is you: {cnp} Bot: {cnc} ")
    elif x==4:
        print(f'''Final Score is 
you: {cnp} 
Bot: {cnc} 
Tie: {cnt}''' )
        if cnp>cnc:
            print("Nice game ")
        else:
            print("Scared??? ")
        break
    else:
        print("Enter valid choice ")

    











