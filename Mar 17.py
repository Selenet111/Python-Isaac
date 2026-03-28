# import time

#________________________________________FIBONACCI SEQUENCE___________________________________
# def fibonacci(term):
#     value1 = 0
#     value2 = 1
#     iterations = term
#     if term == 0:
#         return 0
#     if term == 1:
#         return 1
#     if term > 1:
#         while iterations > 1:
#             if value1 <= value2:
#                 value1 += value2
#                 iterations -= 1
#             elif value2 < value1:
#                 value2 += value1
#                 iterations -= 1
    
#         if value1 >= value2:
#             return value1
#         if value2 > value1:
#             return value2

# startTime = time.time()
# print([fibonacci(i) for i in range(10)])
# timeTaken = time.time() - startTime
# print(timeTaken)



# def fib_rec(term):
#      if term == 0:
#         return 0
#      if term == 1:
#         return 1
     
#      return(fib_rec(term-1)) + (fib_rec(term-2))

# startTime = time.time()
# print([fib_rec(i) for i in range(10)])
# timeTaken = time.time() - startTime
# print(timeTaken)


# def fib_new(term):
#      if term == 0:
#         return 0
#      if term == 1:
#         return 1

#      numbersSoFar = [0, 1]
#      for i in range(term-1):
#          newNumber = numbersSoFar[-1] + numbersSoFar[-2]
#          numbersSoFar.append(newNumber)
    
#      return numbersSoFar[-1]

# startTime = time.time()
# print([fib_new(i) for i in range(10)])
# timeTaken = time.time() - startTime
# print(timeTaken)

#__________________________________BUBBLE SORT_______________________________
# import random

# random.seed(10)

# list1 = [random.randint(0, 25) for i in range(10)]
# list2 = [random.randint(0, 25) for i in range(10)]

# def bubbleSort(myList):
    
   

#     for _ in range (len(myList)):
#          for n in range (len(myList) - 1):
#              if myList[n] >= myList[n+1]:
#                  myList[n], myList[n+1] = myList[n+1], myList[n]                     
#     return myList
        
# print(list2)
# print(bubbleSort(list2))