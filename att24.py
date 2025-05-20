def bhaskara(a, b, c):
    delta = b**2 - 4*a*c

    if delta < 0:
        return "Não existem raízes reais"
    elif delta == 0:
        x = -b / (2*a)
        return f"Raiz única: x = {x}"
    else:
        # Cálculo da raiz quadrada na mão (delta ** 0.5)
        raiz_delta = delta ** 0.5
        x1 = (-b + raiz_delta) / (2*a)
        x2 = (-b - raiz_delta) / (2*a)
        return f"Duas raízes reais: x1 = {x1}, x2 = {x2}"

# Exemplo de uso
a = 1
b = -3
c = 2
print(bhaskara(a, b, c))
