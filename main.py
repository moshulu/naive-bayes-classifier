# main.py
# A program that models P(Bad, A, High) given a dataset (see github documentation)
# Matt Drew (c) 2019

import math
import random

# student, assignement (0 = Bad, 1 = Good), Project (0 = C, 1 = B, 2 = A), Exam (0 = Low, 1 = High), Label (0 = Fail, 1 = Pass)
data = [[1,1,2,1,1],[2,1,1,1,1],[3,0,1,0,0],[4,0,0,1,0],[5,1,0,0,0],[6,1,0,1,1],[7,0,1,1,1],[8,1,2,0,1],[9,0,2,0,0],[10,1,1,0,1]]
trainSet = []
testSet = []

# seperates the dataset into training and testing datasets
def separate(dataset, trainSet, testSet):
    # set this number to something different if you want to have a testing/training dataset. int(len(dataset)) means that it will look at the entire dataset
    x = int(len(dataset))
    for i in range(x):
        trainSet.append(dataset[i])
    for j in range(x, int(len(dataset))):
        testSet.append(dataset[j])

    return (trainSet, testSet)

# seperates the dataset into passing (1) or failing (0)
def separatePassFail(dataset):
    separated = [[],[]]
    for i in range(len(dataset)):
        vector = dataset[i]
        # if at the end of the vector, it is 1, put in pass list...
        if(vector[len(vector) - 1] == 1):
            separated[1].append(vector)
        # ...otherwise put in fail list
        else:
            separated[0].append(vector)
    return separated

# calculates the mean
def mean(numbers):
	return sum(numbers)/float(len(numbers))

#  calculates the standard deviation
def stdev(numbers):
	avg = mean(numbers)
	variance = sum([pow(x-avg,2) for x in numbers])/float(len(numbers)-1)
	return math.sqrt(variance)

# =========================================== #

# seperate the data into both training and testing datasets
(trainSet, testSet) = separate(data, trainSet, testSet)

# get the list of passing and failing from training set (separated[1] = passing tuples, separated[0] = failing tuples)
separated = separatePassFail(trainSet)

passingProb = float(len(separated[1]))/(float(len(separated[0])) + float(len(separated[1])))
failingProb = float(len(separated[0]))/(float(len(separated[0])) + float(len(separated[1])))

# now we need to do p(pass | cj) = p(assignment = 0, project = 2, exam = 1)
assignmentProb = []
projectProb = []
examProb = []
for i in separated[1]:
    count = 0
    for j in i:
        if((count == 1) & (j == 0)):
            assignmentProb.append(1)
        if((count == 2) & (j == 2)):
            projectProb.append(2)
        if((count == 3) & (j == 1)):
            examProb.append(1)
        count = count + 1

# print("P(assignment = 0 | pass): " + str(len(assignmentProb)) + "/" + str(len(separated[1])))
# print("P(project = 2 | pass): " + str(len(projectProb)) + "/" + str(len(separated[1])))
# print("P(exam = 1 | pass): " + str(len(examProb)) + "/" + str(len(separated[1])))

assignmentProb = float(len(assignmentProb))/float(len(separated[1]))
projectProb = float(len(projectProb))/float(len(separated[1]))
examProb = float(len(examProb))/float(len(separated[1]))

# print("p(assignment = 0, project = 2, exam = 1 | pass): " + str(assignmentProb * projectProb * examProb))
print("P(pass | assignment = 0, project = 2, exam = 1): " + str((assignmentProb * projectProb * examProb) * passingProb))

# now we need to do p(fail | cj) = p(assignment = 0, project = 2, exam = 1)
assignmentProb = []
projectProb = []
examProb = []
for i in separated[0]:
    count = 0
    for j in i:
        if((count == 1) & (j == 0)):
            assignmentProb.append(1)
        if((count == 2) & (j == 2)):
            projectProb.append(2)
        if((count == 3) & (j == 1)):
            examProb.append(1)
        count = count + 1

# print("P(assignment = 0 | fail): " + str(len(assignmentProb)) + "/" + str(len(separated[0])))
# print("P(project = 2 | fail): " + str(len(projectProb)) + "/" + str(len(separated[0])))
# print("P(exam = 1 | fail): " + str(len(examProb)) + "/" + str(len(separated[0])))

assignmentProb = float(len(assignmentProb))/float(len(separated[0]))
projectProb = float(len(projectProb))/float(len(separated[0]))
examProb = float(len(examProb))/float(len(separated[0]))

# print("p(assignment = 0, project = 2, exam = 1 | fail): " + str(assignmentProb * projectProb * examProb))
print("P(fail | assignment = 0, project = 2, exam = 1): " + str((assignmentProb * projectProb * examProb) * failingProb))
