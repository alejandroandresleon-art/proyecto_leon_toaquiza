# Sistema de facturación
# Tarea 1: Inventario en memoria

nombre_empresa = "Tecnologia Springfield"
iva = 0.15

productos = [
    {
        "id": 1,
        "nombre": "Teclado",
        "precio": 15.00,
        "stock": 10
    },
    {
        "id": 2,
        "nombre": "Mouse",
        "precio": 8.50,
        "stock": 20
    },
    {
        "id": 3,
        "nombre": "Monitor",
        "precio": 180.00,
        "stock": 5
    }
]

print("================================")
print(nombre_empresa)
print("Sistema de facturación")
print("================================")
print(f"IVA configurado: {iva * 100}%")

print(productos[0]["nombre"])
