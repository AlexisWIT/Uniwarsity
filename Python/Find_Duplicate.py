
# Floyd's Tortoise and Hare
# A simple cycle detection algorithm where one pointer travels twice as faster as another
# once they meet you can trace back to the point where the cycle began
# https://www.youtube.com/watch?v=pKO9UjSeLew
def findDuplicate(numlist):
    num_A = numlist[0]
    num_B = numlist[0]

    while True:
        num_A = numlist[num_A]
        num_B = numlist[ numlist[num_B] ]
        if num_A == num_B:
            break
    
    ptr1 = numlist[0]
    ptr2 = num_A

    while ptr1 != ptr2:
        ptr1 = numlist[ptr1]
        ptr2 = numlist[ptr2]

    return ptr1