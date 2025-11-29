int_1 = 123
int_2 = 456

print(int_1, int_2)

if int_1 < int_2:
    int_1, int_2 = int_2, int_1

print(int_1, int_2)

"""
Instead of:

x = a

y = b

"""