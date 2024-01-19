from itertools import product

# Definindo os dados para cadeiras e mesas
cadeira = {"tabuas": 5, "horas": 10, "lucro": 180}
mesa = {"tabuas": 20, "horas": 15, "lucro": 320}

# Recursos disponíveis
tabuas_disponiveis = 400
horas_disponiveis = 450

# Calculando o número máximo de cadeiras e mesas que podem ser produzidas
max_cadeiras = tabuas_disponiveis // cadeira["tabuas"]
max_mesas = tabuas_disponiveis // mesa["tabuas"]

max_cadeiras_horas = horas_disponiveis // cadeira["horas"]
max_mesas_horas = horas_disponiveis // mesa["horas"]

max_produtos = min(max_cadeiras_horas, max_mesas_horas)

max_profit = 0
best_num_cadeiras = 0
best_num_mesas = 0

# Testando todas as combinações possíveis de cadeiras e mesas dentro das restrições de recursos
for num_cadeiras, num_mesas in product(range(max_produtos + 1), repeat=2):
    total_tabuas = num_cadeiras * cadeira["tabuas"] + num_mesas * mesa["tabuas"]
    total_horas = num_cadeiras * cadeira["horas"] + num_mesas * mesa["horas"]

    if total_tabuas <= tabuas_disponiveis and total_horas <= horas_disponiveis:
        total_profit = num_cadeiras * cadeira["lucro"] + num_mesas * mesa["lucro"]

        if total_profit > max_profit:
            max_profit = total_profit
            best_num_cadeiras = num_cadeiras
            best_num_mesas = num_mesas

# Exibindo os resultados
print(f"Quantidade máxima de cadeiras produzidas: {best_num_cadeiras}")
print(f"Quantidade máxima de mesas produzidas: {best_num_mesas}")
print(f"Lucro máximo obtido: R$ {max_profit}")
