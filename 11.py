def fibonacci_ate(numero):
    a, b = 0, 1
    while a <= numero:
        print(a, end= " ")
        a, b = b, a + b

limite = int(input("Digite até qual número quer: "))
print(fibonacci_ate(limite))