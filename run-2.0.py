import random
from colorama import Fore, Style, init

# Inicializar o colorama
init(autoreset=True)

def montar_pc(orçamento, gaming=False, edicao_video=False, espaco_armazenamento=0):
    componentes = {
        "CPU": {
            "Intel Core i3-10100": 130,
            "Intel Core i5-10400": 200,
            "Intel Core i5-10600K": 250,
            "Intel Core i7-10700K": 350,
        },
        "GPU": {
            "Gráficos Integrados": 0,
            "NVIDIA GeForce GTX 1650": 150,
            "NVIDIA GeForce GTX 1660": 200,
            "NVIDIA GeForce RTX 3060": 400,
        },
        "RAM": {
            "8GB DDR4": 50,
            "16GB DDR4": 100,
            "32GB DDR4": 200,
        },
        "Armazenamento": {
            "120GB SSD": 40,
            "240GB SSD": 60,
            "500GB SSD": 100,
            "1TB SSD": 200,
            "2TB SSD": 400,
        },
        "Placa-Mãe": {
            "B460M-DS3H": 80,
            "Z490 AORUS MASTER": 300,
        },
        "Fonte": {
            "EVGA 500W": 40,
            "EVGA 600W": 50,
            "EVGA 850W": 100,
        },
        "Gabinete": {
            "Corsair Carbide Series 100R": 50,
            "Phanteks Eclipse P400A": 80,
            "Lian Li PC-O11 Dynamic": 150,
        },
    }
    
    recomendacoes = {
        "CPU": ["Intel Core i5-10400"],
        "GPU": ["Gráficos Integrados"],
        "RAM": ["16GB DDR4"],
        "Armazenamento": ["1TB SSD"],
        "Placa-Mãe": ["B460M-DS3H"],
        "Fonte": ["EVGA 600W"],
        "Gabinete": ["Phanteks Eclipse P400A"],
    }
    
    if gaming:
        recomendacoes["GPU"] = ["NVIDIA GeForce GTX 1660"]
    
    if edicao_video:
        recomendacoes["CPU"] = ["Intel Core i7-10700K"]
        recomendacoes["GPU"] = ["NVIDIA GeForce RTX 3060"]
        recomendacoes["RAM"] = ["32GB DDR4"]
    
    if espaco_armazenamento:
        armazenamento_recomendado = []
        for item, preco in componentes["Armazenamento"].items():
            if preco <= orçamento and espaco_armazenamento <= int(item.split()[0].replace("GB", "").replace("TB", "000")):
                armazenamento_recomendado.append(item)
        if armazenamento_recomendado:
            recomendacoes["Armazenamento"] = armazenamento_recomendado
    
    pc = {}
    total = 0

    for categoria, opcoes in recomendacoes.items():
        escolhido = None
        for opcao in opcoes:
            if componentes[categoria][opcao] <= (orçamento - total):
                escolhido = opcao
                break
        if escolhido is None:
            alternativas = [comp for comp, preco in componentes[categoria].items() if preco <= (orçamento - total)]
            if alternativas:
                escolhido = random.choice(alternativas)
        
        if escolhido:
            pc[categoria] = escolhido
            total += componentes[categoria][escolhido]
        else:
            pc[categoria] = "Não foi possível incluir"
    
    pc["Custo Total"] = total
    
    # Impressão colorida
    print(Fore.CYAN + "\nConfiguração Final do PC:")
    for componente, escolha in pc.items():
        if componente == "Custo Total":
            print(Fore.GREEN + f"{componente}: ${escolha}")
        else:
            print(Fore.YELLOW + f"{componente}: " + Fore.WHITE + f"{escolha}")
    return pc

# Exemplo de uso
resultado = montar_pc(1000, gaming=True, edicao_video=False, espaco_armazenamento=500)