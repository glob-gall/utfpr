a = input("a: ")
b = input("b: ")
x = linspace(a, b); % define intervalo de x para plotar no gr ́afico.
% Escolha valores de a e b no dom ́ınio da fun ̧c ̃ao f(x) abaixo e coloque no comando linspace(a,b).
y1 = input("função 1: "); % define a fun ̧c ̃ao y1=f(x) do item (a);
plot(x, y1) % plota o gr ́afico da fun ̧c ̃ao y1=f(x) com valores dados em x no in ́ıcio;
hold on % mant ́em o gr ́afico anterior na pr ́oxima plotagem
y2 = input("função 2: "); %define a fun ̧c ̃ao y2=g(x) do item (b);
plot(x, y2) % plota o gr ́afico de x, y1 e y2;
xline(0); % desenha o eixo das abcissas
yline(0); % exibe o eixo das ordenadas
legend('y1 = f(x)','y2 = g(x)') % aqui escreva no lugar de f(x) e g (x) as fun ̧c ̃oes descritas nos itens (a) e (b),
% respectivamente;

hold off % finaliza a jun ̧c ̃ao de v ́arias fun ̧c ̃oes no mesmo gr ́afico; Isso  ́e interessante quando se quer fazer um
% novo gr ́afico, mas com nova fun ̧c ̃oes sem a necessidade de incluir as anteriores.
