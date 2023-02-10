import random

def build_pc(budget):
    components = {
        "CPU": {
            "Intel Core i3-10100": 130,
            "Intel Core i5-10400": 200,
            "Intel Core i5-10600K": 250,
            "Intel Core i7-10700K": 350,
        },
        "GPU": {
            "NVIDIA GeForce GTX 1650": 150,
            "NVIDIA GeForce GTX 1660": 200,
            "NVIDIA GeForce RTX 3060": 400,
        },
        "RAM": {
            "8GB DDR4": 50,
            "16GB DDR4": 100,
            "32GB DDR4": 200,
        },
        "Storage": {
            "120GB SSD": 40,
            "240GB SSD": 60,
            "500GB SSD": 100,
            "1TB SSD": 200,
            "2TB SSD": 400,
        },
        "Motherboard": {
            "B460M-DS3H": 80,
            "Z490 AORUS MASTER": 300,
        },
        "PSU": {
            "EVGA 500W": 40,
            "EVGA 600W": 50,
            "EVGA 850W": 100,
        },
        "Case": {
            "Corsair Carbide Series 100R": 50,
            "Phanteks Eclipse P400A": 80,
            "Lian Li PC-O11 Dynamic": 150,
        },
    }
    
    pc = {
        "CPU": None,
        "GPU": None,
        "RAM": None,
        "Storage": None,
        "Motherboard": None,
        "PSU": None,
        "Case": None,
    }
    
    for component, prices in components.items():
        options = [(item, price) for item, price in prices.items() if budget >= price]
        if options:
            item, price = random.choice(options)
            pc[component] = item
            budget -= price
    
    if None in pc.values():
        return "Orçamento insuficiente para montar o PC."
    else:
        return pc
