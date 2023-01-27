"""The Python time module provides many ways of representing time in code"""
import time
final_list = []
def factorial(num):
    '''Function for factorial'''
    time.sleep(.1)
    factorial = 1
    for i in range (1,num+1):
        factorial = factorial * i
    return factorial
def sum_factorial():
    '''Function for sum of Factorial'''
    for i in range(50):
        final_list.append(factorial(i))
    result=sum(final_list)
    res=f'Final SUM = {result}'
    print(res)
    return res

if __name__ == "__main__":
    sum_factorial()
