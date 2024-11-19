import random

def build_pc(budget, gaming=False, video_editing=False, storage_space=0):
    components = {
        "CPU": {
            "Intel Core i3-10100": 130,
            "Intel Core i5-10400": 200,
            "Intel Core i5-10600K": 250,
            "Intel Core i7-10700K": 350,
        },
        "GPU": {
            "Integrated Graphics": 0,
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
    
    recommendations = {
        "CPU": ["Intel Core i5-10400"],
        "GPU": ["Integrated Graphics"],
        "RAM": ["16GB DDR4"],
        "Storage": ["1TB SSD"],
        "Motherboard": ["B460M-DS3H"],
        "PSU": ["EVGA 600W"],
        "Case": ["Phanteks Eclipse P400A"],
    }
    
    if gaming:
        recommendations["GPU"] = ["NVIDIA GeForce GTX 1660"]
    
    if video_editing:
        recommendations["CPU"] = ["Intel Core i7-10700K"]
        recommendations["GPU"] = ["NVIDIA GeForce RTX 3060"]
        recommendations["RAM"] = ["32GB DDR4"]
    
    if storage_space:
        recommended_storage = []
        for item, price in components["Storage"].items():
            if price <= budget and storage_space <= int(item.split()[0]):
                recommended_storage.append(item)
        if recommended_storage:
            recommendations["Storage"] = recommended_storage
    
    pc = {
        "CPU": None,
        "GPU": None,
        "RAM": None,
        "Storage": None,
        "Motherboard": None
    }