word="secure"
allowed_errors=5
guess=[]
for i in word:
    guess.append('_ ')
print(*guess)
def check():
    n=input("chances: ")
    for i in range(len(word)): 
        if n not in word:
            allowed_error=1
            if(allowed_error==0):
                print("you lose")
                break
        elif(word[i]==n):
            guess[i]=n
            print(*guess)
          
for letter in word:
    check()

