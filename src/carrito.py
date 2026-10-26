def calcular_total(subtotal, codigo_descuento=None):
    if subtotal < 0:
        raise ValueError("El subtotal no puede ser negativo")
    
    total = subtotal
    if codigo_descuento == "DESC10":
        total = subtotal * 0.90  # 10% de descuento
   # <-- El error introducido
   # if codigo_descuento == "DESC10":
    #    total = subtotal * 0.95  
    elif codigo_descuento == "DESC20":
        total = subtotal * 0.80  # 20% de descuento
        
    return round(total, 2)