n = int(input("Enter the number of terms: "))

if n <= 0:
    print("Fibonacci series up to", n, "is not defined.")
elif n == 1:
    print("The first 1 number in the fibonacci series = 0")
else:
    first = 0
    second = 1
    print("The first", n, "numbers in the fibonacci series =")
    print(first, second, sep=", ", end="")
    
    for i in range(2, n):
        fib = first + second
        print(",", fib, end="")
        first = second
        second = fib
    print()  
