import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from app_busca import buscar_restaurante

def test_busca_categoria_valida():
    restaurantes = ["Sushi Bar (Japonesa)", "Pizzaria Roma (Italiana)"]
    resultado = buscar_restaurante(restaurantes, "Japonesa")
    assert len(resultado) == 1
    assert resultado[0] == "Sushi Bar (Japonesa)"

def test_busca_categoria_invalida():
    restaurantes = ["Sushi Bar", "Pizzaria Roma"]
    resultado = buscar_restaurante(restaurantes, "Marciana")
    assert len(resultado) == 0
