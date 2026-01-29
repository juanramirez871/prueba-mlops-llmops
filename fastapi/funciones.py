def calcular_promedio(numeros: list, decimales: int = 2) -> float:
    if not numeros:
        return 0.0
    promedio = sum(numeros) / len(numeros)
    return round(promedio, decimales)


def concatenar_texto(texto1: str, texto2: str, separador: str = " ") -> str:
    return f"{texto1}{separador}{texto2}"


def calcular_area_rectangulo(base: float, altura: float) -> dict:
    area = base * altura
    perimetro = 2 * (base + altura)
    return {
        "area": area,
        "perimetro": perimetro,
        "base": base,
        "altura": altura
    }


def filtrar_lista(lista: list, criterio: str, valor) -> list:
    if criterio == "mayor":
        return [item for item in lista if item > valor]
    elif criterio == "menor":
        return [item for item in lista if item < valor]
    elif criterio == "igual":
        return [item for item in lista if item == valor]
    else:
        return lista


def procesar_datos(datos: dict, operacion: str) -> dict:
    valores = list(datos.values())    
    if operacion == "suma":
        return {"resultado": sum(valores), "operacion": "suma"}
    elif operacion == "multiplicacion":
        resultado = 1
        for v in valores:
            resultado *= v
        return {"resultado": resultado, "operacion": "multiplicacion"}
    
    elif operacion == "estadisticas":
        return {
            "suma": sum(valores),
            "promedio": sum(valores) / len(valores) if valores else 0,
            "maximo": max(valores) if valores else None,
            "minimo": min(valores) if valores else None,
            "cantidad": len(valores)
        }
    else:
        return {"error": "Operación no válida"}