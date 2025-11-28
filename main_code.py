#start 
    #remeber Euclidean Algorithm states
        # A = (Q * B) + R
#accept input from the user
x = int(input("input 1st number "))
y = int(input("input 2nd number"))
#assign postion to input (basically make the bigger number(x/y) the first input(A) while the lower number (x/y) the second input(B))
if x > y :
    a = x
    b = y
elif x < y :
    a = y
    b = x
else:
    a = x
    b = y
#background / foundation function
def remainder(A,B):
    #finds the remainder
    R = A % B
    return R

def Quitent(A,B):
    # was producing an error cause
    Q = B
    return Q

def echideans(A, B):
    R = remainder(A,B)
    Q = Quitent(A,B)
    while R != 0:
        A = Q
        B = R
        R = remainder(A, B)
        Q = Quitent(A, B)
    return Q
#callback 
#print(remainder(a,b))
#print(Quitent(a,b))
answer = echideans(a,b)
print (answer)

#Testing
    #case1
        # test input 1 === 414
        # test input 2 === 662
        # output === 2
    #case 2
        # test input 1 === 270
        # test input 2 === 192
        # output === 6
    #case 3
        # test input 1 === 777
        # test input 2 === 777
        # output === 777
