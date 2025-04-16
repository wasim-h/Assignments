from random import choice
p_score=0
o_score=0
t_score=None
def bat():
    global p_score,o_score,t_score
    while True:
        p=[1,2,3,4,5,6]
        b=choice(p)
        k=int(input('''Batting
1.one
2.two
3.three
4.four
5.five
6.six
Enter your choice : '''))
        if k<=6:
            if k==b:
                print("Its out")
                print(f"Your score is {p_score}")
                break
            
            else:
                p_score+=k
                print(f"Your score is : {p_score}")

                if t_score is not None and p_score>t_score:
                        print("You Win!!")
                        return
        else:
            print("Range is from 1 to 6")
        




def ball():
    global p_score,o_score,t_score
    while True:
        p=[1,2,3,4,5,6]
        b=choice(p)
        k=int(input('''
Bowling
1.one
2.two
3.three
4.four
5.five
6.six
Enter your choice : '''))
        if k<=6:
            if k==b:
                print("Its out")
                print(f"Opponent's score is : {o_score}")
                break
                
            else:
                o_score+=b
                print(f"Opponent's score is : {o_score}")
                if t_score is not None and o_score>t_score:
                    print("Oponent wins")

                    return
        else:
            print("Range is from 1 to 6")           

              
x=int(input('''1.Head 
or
2.Tail
Enter your choice : '''))

t=[1,2]
a=choice(t)
if x==a:
    y=int(input('''1.Batting
2.Bowling
Enter your choice : '''))
    if y==1:
        bat()
        t_score=p_score
        ball()
    else:
        ball()
        t_score=o_score  
        bat()
else:
    ball()
    t_score=o_score  
    bat()



if p_score>o_score :
    dif=p_score-o_score
    print(f'You win by {dif} runs')
    print(f"Your score is : {p_score}")
    print(f"Opponent's score is : {o_score}")

            
else:
    dif=o_score-p_score
    print(f'You loose by {dif} runs')
    print(f"Your score is : {p_score}")
    print(f"Opponent's score is : {o_score}")






