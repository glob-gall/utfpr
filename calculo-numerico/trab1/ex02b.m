
b=input('Enter a n To Calculate F(n)/F(n-1) : ');

function f = fib(n)
  if (n <= 1)
    f = n;
  else
    f = fib(n - 1) + fib(n - 2);
  endif
endfunction

value1 = fib(b)
value2 = fib(b-1)
result = value1 / value2
printf("f(%d) / f(%d) = %f",value1,value2,result);

