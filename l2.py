
def display(l):
    for i in range(len(l)):
        if i%3==0:
            print()
        print(l[i],end=" ")

def reset(l):
    for i in range(9):
        l.append(0)

def check(l,p):
    if ((l[0]==p and l[1]==p and l[2]==p) or (l[3]==p and l[4]==p and l[5]==p) or (l[6]==p and l[7]==p and l[8]==p) or (l[0]==p and l[3]==p and l[6]==p) or (l[1]==p and l[4]==p and l[7]==p) or (l[2]==p and l[5]==p and l[8]==p) or (l[0]==p and l[4]==p and l[8]==p) or (l[2]==p and l[4]==p and l[6]==p)):
        return p
    else:
        return -1
#main
l=[]
reset(l)
display(l)
moves=1
while(moves<=9):
    if moves%2==1:
        print('Player1 make the move ')
        pos=int(input('Enter the position :'))
        while(pos>9 or pos<1 or l[pos-1]!=0):
            pos = int(input('ReEnter the position :'))
        l[pos-1]=1
        p=1
    else:
        print('Player2 make the move ')
        pos = int(input('Enter the position :'))
        while (pos > 9 or pos < 1 or l[pos - 1] != 0):
            pos = int(input('ReEnter the position :'))
        l[pos-1]=2
        p=2

    print(display(l))
    if (check(l,p)==p):
        print('Player:',p,'is the Winner')
        break
    moves+=1
if moves>9:
    print('Match Drawn ')