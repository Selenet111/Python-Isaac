import random

randomList = [random.randint(0, 10000) for i in range(10)]
listOfNumbers = [5, 6, 21, 30, 40, 67, 81, 11, 2]
listOfNumbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10000000]

def largest_product2(myList):
    
    largestNum, secondLargestNum = 0, 0
    for i in myList:
        if i > largestNum:
            largestNum, secondLargestNum = i, largestNum
        elif i > secondLargestNum:
            secondLargestNum = i
    
    largestProduct = largestNum * secondLargestNum
    print(f"The largest prodcut was: {largestProduct}")
    print(f"The two numbers are {largestNum} and {secondLargestNum}") 
    
            
largest_product2(listOfNumbers)
'''def largest_product1(myList):
    biggestProductSoFar = 0
    bestNumbers = []
    for num1 in myList:
        for num2 in myList:
            if num1 != num2 and num1 * num2 > biggestProductSoFar:
                biggestProductSoFar = num1 * num2
                bestNumbers = [num1, num2]

    print(f"The largest prodcut was: {biggestProductSoFar}")
    print(f"The two numbers are {bestNumbers[1]} and {bestNumbers[0]}")


largest_product1(listOfNumbers)
'''
'''

def largest_product(list):
    list.sort()
    list.reverse()
    largest = list[0] * list [1]
    print(largest)


print(randomList)
print(largest_product(randomList))
largest_product(listOfNumbers)
largest_product(listOfNumbers2)'''