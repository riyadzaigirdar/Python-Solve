A = float(input())
B = float(input())
C = float(input())
pi = 3.14159

Tr = 0.5 * A * C
C = pi * C * C
Tp = ((A + B) / 2)*C
Q = B * B
R = A * B


print("TRIANGULO: %.3f" % Tr)
print("CIRCULO: %.3f" % C)
print("TRAPEZIO: %.3f" % Tp)
print("QUADRADO: %.3f" % Q)
print("RETANGULO: %.3f" % R)