import pandas as pd
import matplotlib.pyplot as plt
import os

#Dados da tabela 8 - Padrão de consumo de vários alimentos e a presença de ausência da_
#_doença em famílias dos sete vilarejos. 
#Padrão de consumo de vários alimentos e a presença de ausência da doença em famílias dos sete vilarejos.

#Parametro de controle: usar CSV ou dados internos
usar_csv = True
caminho_csv = "data/tabela8_pelagra.csv"

# Verifica se deve usar o CSV e se o arquivo existe
if usar_csv and os.path.exists(caminho_csv):
    alimentos_df = pd.read_csv(caminho_csv)
    print("Dados carregados do CSV com sucesso.")
else:
    print("CSV não encontrado ou uso de CSV desativado. Usando dados embutidos.")
    data = {
        "Alimento": ["Carne Fresca", "Carne Fresca", "Leite Fresco", "Leite Fresco", 
        "Carne de Porco Salgada", "Carne de Porco Salgada", "Melado", "Melado"],
        "Consumo": ["Alto", "Baixo", "Alto", "Baixo", "Alto", "Baixo", "Alto", "Baixo"],
        "Afetada": [9, 52, 6, 50, 29, 29, 18, 40],
        "Nao Afetada": [208, 472, 275, 396, 289, 391, 231, 451],
        "Total": [217, 524, 281, 446, 318, 420, 249, 491],
    }
# Criar DataFrame.
    alimentos_df = pd.DataFrame(data)

# Função para plotar gráficos e configurar estilo dos gráficos.
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
alimentos = alimentos_df["Alimento"].unique()
graph_positions = [(0, 0), (0, 1), (1, 0), (1, 1)]

for i, alimento in enumerate(alimentos):
    ax = axes[graph_positions[i]]
    subset = alimentos_df[alimentos_df["Alimento"] == alimento]

    ax.bar(subset["Consumo"], subset["Afetada"], color="red", alpha=0.7, label="Afetada")
    ax.bar(
        subset["Consumo"], 
        subset["Nao Afetada"], 
        bottom=subset["Afetada"], 
        color="blue", 
        alpha=0.7, 
        label="Não Afetada"
    )

    ax.set_title(f"{alimento}")
    ax.set_xlabel("Consumo")
    ax.set_ylabel("Número de Famílias")
    ax.legend()

# Ajustar espaçamento e exibir gráficos na tela.
plt.tight_layout()
plt.suptitle("Padrão de Consumo e Presença da Pelagra", fontsize=16, y=1.03)
plt.show()
plt.savefig("pelagra_graficos.png", dpi=300, bbox_inches="tight")

