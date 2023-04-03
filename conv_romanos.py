def int_para_romano(num):
    valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    simbolos = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    resultado = ""
    i = 0
    while num > 0:
        for _ in range(num // valores[i]):
            resultado += simbolos[i]
            num -= valores[i]
        i += 1
    return resultado

num = int(input("Digite um número inteiro que converto pra números Romanos: "))
print(int_para_romano(num))