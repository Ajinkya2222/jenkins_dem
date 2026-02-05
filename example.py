def fib(n):
     a, b ,c= 0, 1,2
     while a < n:
         print(a, end=' ')
         a, b = b, a+b
     print(c)
fib(1000)
