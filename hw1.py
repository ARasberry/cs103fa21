{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "3157265d",
   "metadata": {},
   "source": [
    "\n",
    "# HW1, CS103 Fall 2021\n",
    "# name: Austin Rasberry\n",
    "# blazerid: arasberr\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "ff256b1e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import math      # you will need the math module to answer some of the questions"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "622a8ab3",
   "metadata": {},
   "source": [
    "Let's define a sample function"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "879158d5",
   "metadata": {},
   "outputs": [],
   "source": [
    "def myName (): \n",
    "    # PLEASE REPLACE 'James Bond' BY YOUR NAME; do not change anything else;\n",
    "    # for example, leave the single quotes alone as you insert your name\n",
    "    return 'Austin Rasberry'\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0fb7d8d7",
   "metadata": {},
   "source": [
    "You need to run the function above before you \"call\" the function."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bcba3377",
   "metadata": {},
   "source": [
    "Now, we can call the function"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "fd3a59b5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "My name is : Austin Rasberry\n"
     ]
    }
   ],
   "source": [
    "print(\"My name is : {}\".format(myName()))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "554eb754",
   "metadata": {},
   "source": [
    "Now, change the \"James Bond\" part with your real name. Please note that if you change anything else, you may ruin the function "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4653cb89",
   "metadata": {},
   "source": [
    "# PRACTICE PROBLEM"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "aa815329",
   "metadata": {},
   "source": [
    "Please check hw1.pdf file and follow the instructions to solve this problem"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "d85fa814",
   "metadata": {},
   "outputs": [],
   "source": [
    "def f(x):\n",
    "    return 5*x-3"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e832e7f1",
   "metadata": {},
   "source": [
    "After you edit your function, we will be calling the function with different inputs(test cases) to compare the output"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6f5c2a78",
   "metadata": {},
   "source": [
    "First I will be calling the function using first test case (x=5)and the expected result is 22"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "13c5eb41",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "22\n"
     ]
    }
   ],
   "source": [
    "print (f(5))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "19f26822",
   "metadata": {},
   "source": [
    "Now, I will check the second test case (x=0) and the expected result is -3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "3cdbda4f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-3\n"
     ]
    }
   ],
   "source": [
    "print (f(0))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e3e9bd37",
   "metadata": {},
   "source": [
    "Let's check the final test case (x=2.5) and the expected result is 9.5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "f4b793c2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "9.5\n"
     ]
    }
   ],
   "source": [
    "print (f(2.5))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b53c47da",
   "metadata": {},
   "source": [
    "# HW1 Problems"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6515cd0a",
   "metadata": {},
   "source": [
    "Now it is your turn to solve the next 5 questions. Remember, you will first modify the function with the correct equation and then you will check the result of each test cases"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b8b2e469",
   "metadata": {},
   "source": [
    "# 1) Area of the Circle "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "0c1a53e9",
   "metadata": {},
   "outputs": [],
   "source": [
    "def areaCircle (r):\n",
    "    \n",
    "    return math.pi*r**2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "e44e6556",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3.141592653589793\n"
     ]
    }
   ],
   "source": [
    "print (areaCircle(1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "807e8127",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.031415926535897934\n"
     ]
    }
   ],
   "source": [
    "print (areaCircle(0.1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "be4379d8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "478.3879062809779\n"
     ]
    }
   ],
   "source": [
    "print (areaCircle(12.34))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "514d47ea",
   "metadata": {},
   "source": [
    "# 2) Special Operation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "5887b03e",
   "metadata": {},
   "outputs": [],
   "source": [
    "def specialOperation(n1,n2):\n",
    "    if n1*n2 < 100:\n",
    "        return n1*n2\n",
    "    else: \n",
    "        return n1+n2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "7d8d8af6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "20\n"
     ]
    }
   ],
   "source": [
    "n1=4\n",
    "n2=5\n",
    "print(specialOperation(n1,n2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "6b1be170",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "84\n"
     ]
    }
   ],
   "source": [
    "n1=12\n",
    "n2=7\n",
    "print(specialOperation(n1,n2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "c755ff77",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "25\n"
     ]
    }
   ],
   "source": [
    "n1=15\n",
    "n2=10\n",
    "print(specialOperation(n1,n2))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0c2da003",
   "metadata": {},
   "source": [
    "# 3) Phone Bill"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "79d84e3b",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "def phoneBill (m,tx):\n",
    "    if m >= 50 and tx >= 50:\n",
    "        return (15.44+((m-50)*.25)+((tx-50)*.15))*1.05\n",
    "    elif m < 50 and tx >= 50:\n",
    "        return (15.44+((tx-50)*.15))*1.05\n",
    "    elif m >= 50 and tx < 50:\n",
    "        return (15.44+((m-50)*.25))*1.05\n",
    "    else: \n",
    "        return 15.44*1.05\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "96f8099b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "32.487\n"
     ]
    }
   ],
   "source": [
    "m=70\n",
    "tx=120\n",
    "print(phoneBill (m,tx))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "ac6fa68a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "16.212\n"
     ]
    }
   ],
   "source": [
    "m=50\n",
    "tx=50\n",
    "print(phoneBill (m,tx))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "bfed922f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "36.4245\n"
     ]
    }
   ],
   "source": [
    "m=127\n",
    "tx=30\n",
    "print(phoneBill (m,tx))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "beb85d0a",
   "metadata": {},
   "source": [
    "# 4) Grading System"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "044795db",
   "metadata": {},
   "outputs": [],
   "source": [
    "def grader (avg_exams, avg_hw, attendance):\n",
    "    if  avg_exams < 70 or avg_hw < 70:\n",
    "        return False\n",
    "    elif attendance <= 17:\n",
    "        return False\n",
    "    elif avg_exams < 80 and avg_hw < 80:\n",
    "        return False\n",
    "    else:\n",
    "        return True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "1e2b1ae3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "avg_exams = 76\n",
    "avg_hw = 100\n",
    "attendance =24\n",
    "print(grader(avg_exams, avg_hw, attendance))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "03b40583",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "avg_exams = 100\n",
    "avg_hw = 90\n",
    "attendance =16\n",
    "print(grader(avg_exams, avg_hw, attendance))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "c3abdf85",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "avg_exams = 72\n",
    "avg_hw = 78\n",
    "attendance =22\n",
    "print(grader(avg_exams, avg_hw, attendance))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "65811d00",
   "metadata": {},
   "source": [
    "# 5) Radian to Degree convertion"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "c9255242",
   "metadata": {},
   "outputs": [],
   "source": [
    "def radToDegree(rad):\n",
    "    \n",
    "    return round(rad*(180/math.pi),2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "90af46e1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5729.58\n"
     ]
    }
   ],
   "source": [
    "rad=100\n",
    "print(radToDegree(rad))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "6c660d97",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1546.99\n"
     ]
    }
   ],
   "source": [
    "rad=27\n",
    "print(radToDegree(rad))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "69e6a5b7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "57.3\n"
     ]
    }
   ],
   "source": [
    "rad=1\n",
    "print(radToDegree(rad))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "109f63c3",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
