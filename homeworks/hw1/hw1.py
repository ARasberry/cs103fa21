import math

def myName (): 
	return 'Austin Rasberry'
	
print("My name is : {}".format(myName()))

# Practice Problems

def f(x):
    return 5*x-3

print (f(5))
print (f(0))
print (f(2.5))

# HW1 Problems

# 1. Area of the Circle
def areaCircle (r):
    
    return math.pi*r**2

print (areaCircle(1))
print (areaCircle(0.1))
print (areaCircle(12.34))


# 2. Special Operation
def specialOperation(n1,n2):
    if n1*n2 < 100:
        return n1*n2
    else: 
        return n1+n2

n1=4
n2=5
print(specialOperation(n1,n2))

n1=12
n2=7
print(specialOperation(n1,n2))

n1=15
n2=10
print(specialOperation(n1,n2))

# 3. Phone Bill
def phoneBill (m,tx):
    if m >= 50 and tx >= 50:
        return (15.44+((m-50)*.25)+((tx-50)*.15))*1.05
    elif m < 50 and tx >= 50:
        return (15.44+((tx-50)*.15))*1.05
    elif m >= 50 and tx < 50:
        return (15.44+((m-50)*.25))*1.05
    else: 
        return 15.44*1.05

m=70
tx=120
print(phoneBill (m,tx))

m=50
tx=50
print(phoneBill (m,tx))

m=127
tx=30
print(phoneBill (m,tx))

# 4. Grading System
def grader (avg_exams, avg_hw, attendance):
    if  avg_exams < 70 or avg_hw < 70:
        return False
    elif attendance <= 17:
        return False
    elif avg_exams < 80 and avg_hw < 80:
        return False
    else:
        return True
        
avg_exams = 76
avg_hw = 100
attendance =24
print(grader(avg_exams, avg_hw, attendance))

avg_exams = 100
avg_hw = 90
attendance =16
print(grader(avg_exams, avg_hw, attendance))

avg_exams = 72
avg_hw = 78
attendance =22
print(grader(avg_exams, avg_hw, attendance))

# 5. Radian to Degree conversion
def radToDegree(rad):
    
    return round(rad*(180/math.pi),2)
    
rad=100
print(radToDegree(rad))

rad=27
print(radToDegree(rad))

rad=1
print(radToDegree(rad))
