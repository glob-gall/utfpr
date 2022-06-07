
b=input('Enter a n To Calculate F(n)/F(n-1) : ');

function f = fib(n)
  if (n <= 1)
    f = n;
  else
    f = fib(n - 1) + fib(n - 2);
  endif
endfunction

for i = 2 : b
  value1 = fib(i)
  value2 = fib(i-1)
  result = value1 / value2
  fprintf("f(%d) / f(%d) = %f\n",value1,value2,result);
endfor



