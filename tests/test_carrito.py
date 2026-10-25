from src.carrito import calcular_total

def test_calcular_total_sin_descuento():
    assert calcular_total(100.0) == 100.0

def test_calcular_total_con_descuento_10():
    assert calcular_total(100.0, "DESC10") == 90.0

def test_calcular_total_con_descuento_20():
    assert calcular_total(100.0, "DESC20") == 80.0

def test_subtotal_negativo_lanza_error():
    try:
        calcular_total(-50.0)
    except ValueError:
        assert True
    else:
        assert False, "Debería haber lanzado un ValueError"