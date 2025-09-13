import pandas as pd

# Lê os dois arquivos
df_price = pd.read_csv("price.csv")
df_sac = pd.read_csv("sac.csv")

# Calcula o custo total (prestação * 12 somado em todas as linhas)
total_price = (df_price["Prestação"] * 12).sum()
total_sac = (df_sac["Prestação"] * 12).sum()

print(f"Custo total PRICE: R$ {total_price:,.2f}")
print(f"Custo total SAC:   R$ {total_sac:,.2f}")


print("Percentual Price:", (total_price / 232050.06))
print("Percentual SAC:", (total_sac / 183476.21))
