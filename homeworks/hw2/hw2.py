import math

def p(x):
    if x<0 or x>1:
        return 0
    else:
        return 1
p(-1)
p(0)
p(1)

def isOdd(n1):
    # Function takes a value and returns true if value is an int and odd, otherwise it returns false
    if n1%2 != 0 and type(n1) == int:
        return True
    else:
        return False

print(isOdd(1))
print(isOdd(4))
print(isOdd(11)

def paintTheRoom (length,width,height):
    '''
    Function takes 3 values, the first is wall length, the second is wall width, the third is wall height
    and calculates the area of each wall and ceiling, adds them together, divides by the amount of paint
    in one can and returns how many cans is needed to paint that much area.
    '''
    wall1 = 0
    wall2 = 0
    ceiling = 0
    wall1 = length * height
    wall2 = width * height
    ceiling = length * width
    area = (wall1*2)+(wall2*2)+ceiling
    return math.ceil(area/400)

print(paintTheRoom(10,12,8))
print(paintTheRoom(110,122,70))

def sumToMagic(listOfInt, magicSum):
    '''
    The function takes a list, adds each number in the list to each other number in the list, if the result is
    equal to the magic sum it returns where in the list each of the numbers is located.
    '''
    positionOfN = 0
    for n in range(0,len(listOfInt)):
        for m in range(0,len(listOfInt)):
            if listOfInt[n]+listOfInt[m] == magicSum:
                return('(' + str(n) + ',' + str(m) + ')')

print(sumToMagic((8,16,22,35),30))

def tupleCounter(t):
    # Checks if each number in a tuple is odd, and returns how many odd numbers are in the tuple.
    dm = 0
    for n in range(0,len(t)+1):
        if n%2 != 0:
            dm += 1
    return(dm)

print(tupleCounter((3,3,3,4,5,6,7,82,23,46)))

def smallerThanIndex(listOfNumbers):
    #Checks each value in a string against its index value and returns how many are below their index value
    length = len(listOfNumbers)
    dm = 0
    for n in range(0,len(listOfNumbers)):
        if listOfNumbers[n] < n:
            dm += 1
    return(dm)

print(smallerThanIndex((10,20,1,2,30)))
print(smallerThanIndex((1,2,0,44,29,309)))
print(smallerThanIndex((-4,-3,2,1,0)))
