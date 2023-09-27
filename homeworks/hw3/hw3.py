import math

def reverseNum(n):
    newString = ''
    s = str(n)
    for i in range(0,len(s)):
        newString += s[len(s)-i-1]
    return newString

print(reverseNum(12348098796))

def squareOfDigits(s):
    newInt = 0
    newNewInt = 0
    for n in range(0,len(s)):
        if s[n] == type(int) :
            newInt += s[n]
        else:
            continue
    newNewInt = newInt**2
    return newNewInt

print(squareOfDigits('num=10'))

def divideCircleEqual(r, numberOfPoints):
    degreeOfDivisions = (2*math.pi)/numberOfPoints
    listOfPoints = [0]
    x = 0
    y =0
    point = [0]
    for n in range (1,numberOfPoints+1):
        x = r*math.sin((r*(2*math.pi)/n))
        y = r*math.cos((r*(2*math.pi)/n))
        point = [x,y]
        listOfPoints.append(point)
    return listOfPoints

print(divideCircleEqual(10,10))

def cubeOfOdd(n2):
    cube = 0
    for n in range(0,n2):
        if n%2 != 0:
            cube = n**3
            print(cube)

cubeOfOdd(8)

def gcDivisor(k,m):
    gcf = 0
    for n in range(1,k+m*2):
        if m%n == 0 and k%n == 0 and n != 0:
            gcf = n
    return(gcf)

print(gcDivisor(54, 81))
