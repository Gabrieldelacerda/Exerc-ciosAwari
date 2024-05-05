def calcular_juros_compostos(vp, taxa_juros, periodos):
    taxa_decimal = taxa_juros * 100
    vf = vp * (1 + taxa_decimal) ** periodos
    return vf

valor_principal = float(input("Digite o valor principal"))
taxa_juros_anual = float(input("Digite a taxa de juros anual"))
periodos = float(input("Numero de periodos"))

valor_final = calcular_juros_compostos(valor_principal, taxa_juros_anual, periodos)

print(valor_final)