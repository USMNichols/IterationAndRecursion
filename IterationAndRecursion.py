#Brandon Nichols
#Jay Gaines Cis261
#IterationAndRecursion


def factorial_iterative(num):
    fact = 1
    for number in range(2, num+1):
        fact = number * fact
    return fact

def Factorial_Recursive(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * Factorial_Recursive(num -1)

def main():
    print("results using iterative functions")
    print("0!", factorial_iterative(0))
    print("5!", factorial_iterative(5))
    print("10!", factorial_iterative(10))
    print("25!", factorial_iterative(25))
    print("50!", factorial_iterative(50))
    print("100!", factorial_iterative(100))

    print("results for recursive functions")
    print("0!", Factorial_Recursive(0))
    print("5!", Factorial_Recursive(5))
    print("10!", Factorial_Recursive(10))
    print("25!", Factorial_Recursive(25))
    print("50!", Factorial_Recursive(50))
    print("100!", Factorial_Recursive(100))
if __name__ == "__main__":
       main()
        




