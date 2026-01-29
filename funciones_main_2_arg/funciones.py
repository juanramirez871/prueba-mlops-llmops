def _to_float(v) -> float:
    if isinstance(v, (int, float)):
        return float(v)
    if isinstance(v, str):
        try:
            return float(v)
        except ValueError:
            pass
    raise TypeError("valor no convertible a float")


def sumar(x: float, y: float) -> float:
    return _to_float(x) + _to_float(y)


def multiplicar(x: float, y: float) -> float:
    return _to_float(x) * _to_float(y)


def dividir(x: float, y: float) -> float:
    b = _to_float(y)
    if b == 0.0:
        raise ZeroDivisionError("division por cero")
    return _to_float(x) / b


def potencia(x: float, y: float) -> float:
    return _to_float(x) ** _to_float(y)


def promedio(valores: list[float]) -> float:
    if not valores:
        raise ValueError("lista vacia")
    s = 0.0
    n = 0
    for v in valores:
        s += _to_float(v)
        n += 1
    return s / n


def suma_acumulada(valores: list[float]) -> list[float]:
    res: list[float] = []
    total = 0.0
    for v in valores:
        total += _to_float(v)
        res.append(total)
    return res


def estadisticas(valores: list[float]) -> dict[str, float]:
    if not valores:
        raise ValueError("lista vacia")
    first = _to_float(valores[0])
    min_v = first
    max_v = first
    suma_v = 0.0
    n = 0
    for v in valores:
        fv = _to_float(v)
        if fv < min_v:
            min_v = fv
        if fv > max_v:
            max_v = fv
        suma_v += fv
        n += 1
    prom = suma_v / n
    return {"min": min_v, "max": max_v, "suma": suma_v, "promedio": prom}


def normalizar(valores: list[float]) -> list[float]:
    if not valores:
        return []
    vals = [_to_float(v) for v in valores]
    min_v = vals[0]
    max_v = vals[0]
    for v in vals:
        if v < min_v:
            min_v = v
        if v > max_v:
            max_v = v
    rango = max_v - min_v
    if rango == 0.0:
        return [0.0 for _ in vals]
    return [(v - min_v) / rango for v in vals]


def aplicar_operacion(op: str, x: float, y: float) -> float:
    if op == "sumar":
        return sumar(x, y)
    if op == "multiplicar":
        return multiplicar(x, y)
    if op == "dividir":
        return dividir(x, y)
    if op == "potencia":
        return potencia(x, y)
    raise ValueError("operacion no soportada")
