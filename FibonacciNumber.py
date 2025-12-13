class Solution:
    # This method calculates the Fibonacci number for a given n
    def fib(self, n: int) -> int:
        
        # Base case 1:
        # If n is 0, the Fibonacci value is 0
        if n == 0:
            return 0
        
        # Base case 2:
        # If n is 1, the Fibonacci value is 1
        if n == 1:
            return 1
        
        # Recursive case:
        # fib(n) = fib(n-1) + fib(n-2)
        # We call the same function for (n-1) and (n-2)
        return self.fib(n-1) + self.fib(n-2)


# Create an object of the Solution class
s = Solution()

# Take input from the user and convert it to an integer
n = int(input("Enter the value of n: "))

# Call the fib() method and print the result
print(s.fib(n))
