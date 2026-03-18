class Solution:
    def fib(self, n: int) -> int:
        def fib(x) -> int:
            if x < 2:
                return x
            else:
                return fib(x-1) + fib(x-2)
        return fib(n)