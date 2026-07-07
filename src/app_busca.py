def buscar_restaurante(restaurantes, termo):
    return [r for r in restaurantes if termo.lower() in r.lower()]
