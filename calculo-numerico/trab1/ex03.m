syms('OK', 'P0', 'P1', 'TOL', 'NO', 'FLAG', 'NAME', 'OUP', 'F0');
 syms('I', 'F1', 'P', 'FP','s','x');
 TRUE = 1;
 FALSE = 0;

#entrada: f, a, b, epsilon
#sa ́ıda: Aproxima ̧c ̃ao
#1. syms x % cria a vari ́avel simb ́olica x
#2. f2 = f′′(x)
#3. Se f(a) · f′′(a) > 0 ent ̃ao
#4. x0 = a
#5. sen ̃ao
#6. x0 = b
#7. fim
#8. Se f(a) · f(b) > 0 ent ̃ao
#9. escolha outros valores de a e b, pois f(a) · f(b) > 0
#10. sen ̃ao
#11. f1 = f′(x)
#12. k = 1
#13. erro=∞
#14. enquanto erro > epsilon
#15. k = k + 1
#16. u = x0
#17. x0 = x0 − f(x0)/f1
#18. erro = abs(u − x0)
#19. Aproxima ̧c ̃ao=u
#20. fim
#21. fim
syms x
a = input('Informe romanticamente o nosso a: ')
b = input('Informe romanticamente o nosso b: ')
f0str = input('Informe a função f em string: ')
f0 = input('Informe a função f: ')

f1 = diff(f0,x) %derivada
whos f1
f2 = diff(f1,x) % segunda derivada

F0 = inline(f0str,'x')
F1 = inline(f1,'x')
F2 = inline(f2,'x')

OK = FALSE;
while OK == FALSE
   fprintf(1,'Insira as extremidades A < B em linhas separadas\n');
   A = input(' ');
   B = input(' ');
   if A > B
    X = A;
    A = B;
    B = X;
   end
   if A == B
    fprintf(1,'a não pode ser igual a b\n');
   else
    FA = F(A);
    FB = F(B);
   if FA*FB > 0
    fprintf(1,'f(a) e f(b) têm o mesmo sinal.\n');
   else
    OK = TRUE;
   end
    FPP0 = FPP(0);
    FPPA = FPP(A);
   if FPPA*FA>0
    P0 = A;
   else
    P0 = B;
   end
   end
 end
 OK = FALSE;

