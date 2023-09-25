import csv

def numOfDepts():
    '''
    takes a file and prints the number of departments
    parameters - none
    prints - number and names of departments
    '''
    with open ('students_dataset.csv', 'r') as studentsDataset:
        readStuData = csv.reader(studentsDataset, delimiter = ',')
        records = []
        for row in readStuData:
            records.append(row)
        numRows = len(records)
        numCols = len(records [0])
        numDept = 0
        departments = []
        for row in range(1,numRows):
            if records [row] [2] not in departments:
                numDept += 1
                departments.append(records [row][2])
        print(numDept)
        print(departments)

def highestGPA():
    """
    takes a file and prints the name of the student with the highest gpa
    parameters - none
    prints - highest GPA and the name of the student that made it
    """
    with open ('students_dataset.csv', 'r') as studentsDataset:
        readStuData = csv.reader(studentsDataset, delimiter = ',')
        records = []
        for row in readStuData:
            records.append(row)
        numRows = len(records)
        numCols = len(records [0])
        highGpa = 0
        highGpaStuFN = ''
        highGpaStuLN = ''
        for row in range(1, numRows):
            if float(records[row][4])> highGpa:
                highGpa = float(records[row][4])
                highGpaStuFN = (records[row] [0])
                highGpaStuLN = (records[row] [1])
        print(highGpa)
        print(highGpaStuFN , highGpaStuLN)



def avgCompSciCreditHours():
    """
    takes a file and prints the average number of credit hours in the Comp Sci department
    parameters - none
    prints - average number of credit hours in the Comp Sci department
    """
    with open ('students_dataset.csv', 'r') as studentsDataset:
        readStuData = csv.reader(studentsDataset, delimiter = ',')
        records = []
        for row in readStuData:
            records.append(row)
        numRows = len(records)
        numCols = len(records [0])
        credHours = 0
        numOfCompSci = 0
        for row in range(1, numRows):
            if records [row][2] == 'Computer Science':
                numOfCompSci += 1
                credHours += float(records[row][5])
        print(round((credHours/numOfCompSci),2))

def bioTAGPA():
    """
    takes a file and prints the average GPA of the biology TA's
    parameters - none
    prints - average GPA of the biology TA's
    """
    with open ('students_dataset.csv', 'r') as studentsDataset:
        readStuData = csv.reader(studentsDataset, delimiter = ',')
        records = []
        for row in readStuData:
            records.append(row)
        numRows = len(records)
        numCols = len(records [0])
        GPA = 0
        numOfBioTA = 0
        for row in range(1, numRows):
            if records [row][2] == 'Biology' and records [row][6] == 'Yes':
                GPA += float(records[row][4])
                numOfBioTA += 1
        print(round((GPA/numOfBioTA),2))

def taCount():
    """
    takes a file and returns the name of the TA's and the number of students they have
    parameters - none
    prints - dictionary of the names of the TA's and the numeber of students they have
    """
    with open ('students_dataset.csv', 'r') as studentsDataset:
        readStuData = csv.reader(studentsDataset, delimiter = ',')
        records = []
        for row in readStuData:
            records.append(row)
        numRows = len(records)
        numCols = len(records [0])
        advisorDict = {}
        advisorNameList = []
        advisorCountList = []
        advisorCount = 0
        zippedAdvisor = []
        for row in range(1,numRows):
            if records [row][7] not in advisorNameList:
                advisorCount = 0
                advisorNameList.append(str(records [row][7]))
                for rows in range(1,numRows):
                    if records [rows][7] == records [row][7]:
                        advisorCount += 1 
                advisorCountList.append(advisorCount)
        zippedAdvisor = zip(advisorNameList, advisorCountList)
        advisorDict = {key:value for key, value in zip(advisorNameList, advisorCountList)}
        print(advisorDict)

taCount()

