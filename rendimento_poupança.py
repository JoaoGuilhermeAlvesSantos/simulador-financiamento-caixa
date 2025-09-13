def rendimento_poupanca(valor_inicial, meses=1, taxa_mensal=0.00675):
    montante = valor_inicial * (1 + taxa_mensal) ** meses
    return montante


valor = 6000.0
total = 0
for mes in range(1, 25):
    montante = rendimento_poupanca(valor, mes)
    total += montante

print(f"Total investido (setembro-2027): R$ {total:,.2f}")


valor = 6000.0
total = 0
for mes in range(1, 27):
    montante = rendimento_poupanca(valor, mes)
    total += montante

print(f"Total investido (Dezembro-2027): R$ {total:,.2f}")

valor = 6000.0
total = 0
for mes in range(1, 39):
    montante = rendimento_poupanca(valor, mes)
    total += montante

print(f"Total investido (Dezembro-2028): R$ {total:,.2f}")

