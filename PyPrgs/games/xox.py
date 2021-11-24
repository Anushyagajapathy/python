
count=0
list=['_','_','_','_','_','_','_','_','_']

def condi():
    global count
    if list[0]==list[4]==list[8]=='X' or list[2]==list[4]==list[6]=='X' or list[0]==list[1]==list[2]=='X' or list[3]==list[4]==list[5]=='X' or list[6]==list[7]==list[8]=='X' or list[0]==list[3]==list[6]=='X' or list[1]==list[4]==list[7]=='X' or list[2]==list[5]==list[8]=='X':
        print("Player2 is winner!!")
        count += 1
    elif list[0]==list[4]==list[8]=='O' or list[2]==list[4]==list[6]=='O' or list[0]==list[1]==list[2]=='O' or list[3]==list[4]==list[5]=='O' or list[6]==list[7]==list[8]=='O' or list[0]==list[3]==list[6]=='O' or list[1]==list[4]==list[7]=='O' or list[2]==list[5]==list[8]=='O':
        print("Player1 is winner!!")
        count += 1
print('\n',list[0], list[1], list[2],'\n',list[3], list[4], list[5],'\n',list[6], list[7], list[8])
while True:
    x = int(input("Enter Player1 move(O): "))
    list[x-1]='O'
    print('\n', list[0], list[1], list[2], '\n', list[3], list[4], list[5], '\n', list[6], list[7], list[8])
    condi()
    if count==1:
        break
    y = int(input("Enter Player2 move(X): "))
    list[y-1]='X'
    print('\n', list[0], list[1], list[2], '\n', list[3], list[4], list[5], '\n', list[6], list[7], list[8])
    condi()
    if count==1:
        break    
