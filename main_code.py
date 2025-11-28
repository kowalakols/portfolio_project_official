#start 
    #remeber Euclidean Algorithm states
        # A = (Q * B) + R
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

