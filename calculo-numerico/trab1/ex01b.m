syms('OK', 'P0', 'P1', 'TOL', 'NO', 'FLAG', 'NAME', 'OUP', 'F0');
 syms('I', 'F1', 'P', 'FP','s','x');
 TRUE = 1;
 FALSE = 0;


a = input("a: ")
b = input("b: ")
x = linspace(a, b); % define intervalo de x para plotar no gr ́afico.
% Escolha valores de a e b no dom ́ınio da fun ̧c ̃ao f(x) abaixo e coloque no comando linspace(a,b).
f = input('digite a função 1: ');
y1 = inline(f,'x');
#y1 = f(x); % define a fun ̧c ̃ao y1=f(x) do item (a);
#plot(x, y1) % plota o gr ́afico da fun ̧c ̃ao y1=f(x) com valores dados em x no in ́ıcio;

 if a > b
 X = a;
 a = b;
 b = X;
 end
x1=a:.1:b;

plot(x1,y1(x1),'LineWidth', 1.5);
hold on % mant ́em o gr ́afico anterior na pr ́oxima plotagem

g = input('digite a função 2: ');
y2 = inline(g,'x');

plot(x1,y2(x1),'LineWidth', 1.5);
hold on
title('Gráfico de f(x)');
 grid on
