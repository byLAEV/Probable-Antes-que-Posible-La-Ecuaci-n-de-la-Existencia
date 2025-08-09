"""
ecuacion_existencia.py
----------------------
Implementación de la Ecuación de la Existencia propuesta por
Lerry Alexander Elizondo Villalobos & Emilia Jiménez Artavia.

Ecuación:
    E(p) = 1 si P(p) * Pi(p) >= theta
           0 si no

Donde:
    - P(p): probabilidad en [0,1]
    - Pi(p): posibilidad en [0,1] (puede ser binaria o continua)
    - theta: umbral de colapso ontológico en (0,1]

Uso:
    from ecuacion_existencia import existe

    print(existe(0.9, 1, theta=0.1))  # True

Autor: LAEV & Emilia Jiménez Artavia
Licencia: Propiedad Intelectual Registrada
"""

from typing import Union

FloatLike = Union[float, int]


def existe(p_prob: FloatLike, p_poss: FloatLike, theta: float = 0.1) -> bool:
    """
    Determina si un fenómeno existe según la ecuación de la existencia.

    Args:
        p_prob (float): Probabilidad P(p) en [0,1].
        p_poss (float): Posibilidad Pi(p) en [0,1] (0 imposible, 1 posible).
        theta (float): Umbral de colapso ontológico, en (0,1].

    Returns:
        bool: True si existe (1), False si no (0).

    Raises:
        ValueError: Si los parámetros están fuera de rango.
    """
    if not (0.0 <= p_prob <= 1.0):
        raise ValueError("p_prob debe estar en [0,1]")
    if not (0.0 <= p_poss <= 1.0):
        raise ValueError("p_poss debe estar en [0,1]")
    if not (0.0 < theta <= 1.0):
        raise ValueError("theta debe estar en (0,1]")

    return (p_prob * p_poss) >= theta


if __name__ == "__main__":
    # Ejemplos de uso
    ejemplos = [
        (0.92, 1.0, 0.1),
        (0.05, 1.0, 0.1),
        (0.5, 0.5, 0.3),
        (1.0, 1.0, 0.99),
    ]

    for P, Pi, th in ejemplos:
        print(f"P={P}, Pi={Pi}, theta={th} -> Existe: {existe(P, Pi, th)}")
