
def suma_positiva(a, b):
    """Las afirmaciones
    permiten que las funciones levanten errores
    al ser utilizadas de forma erronea"""
    assert a >= 0, f'{a} no es un numero positivo'
    assert b >= 0, f'{b} no es un numero positivo'
    return a + b


if __name__ == "__main__":
    print(suma_positiva(-2, 4))
