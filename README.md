# Probable-Antes-que-Posible-La-Ecuaci-n-de-la-Existencia
Una ecuación filosófica y matemática que redefine la existencia como el resultado de la intersección entre lo probable y lo posible. Solo aquello que es estructuralmente viable y estadísticamente probable, y que supera un umbral crítico, puede colapsar en realidad y ser considerado existente.


# 📐 Probable Antes que Posible – La Ecuación de la Existencia

> *“La existencia no es un capricho del pensamiento,  
sino una consecuencia inevitable de la estadística.”*  
> – LAEV

---

## 🧠 Descripción General

Este proyecto presenta una **teoría ontológica original** y su correspondiente **ecuación formal**, que redefinen la manera en que concebimos la existencia. A diferencia de modelos tradicionales donde la posibilidad precede a la existencia, esta propuesta invierte la lógica:

> **Primero es lo probable. Luego, lo posible. Finalmente, lo existente.**

A través de un marco que une lógica, probabilidad y fenomenología, la ecuación expresa que solo aquello que se sostiene tanto en lo estructural (posibilidad) como en lo estadístico (probabilidad) puede emerger como ente real.

---

## 🧮 La Ecuación de la Existencia

```math
E(p) =
\begin{cases}
1 & \text{si } P(p) \cdot \Pi(p) \geq \theta \\
0 & \text{si no}
\end{cases}




---

📐 Explicación de la Ecuación de la Existencia

Título formal: “Probable Antes que Posible”


---

🧮 La Ecuación

E(p) =
\begin{cases}
1 & \text{si } P(p) \cdot \Pi(p) \geq \theta \\
0 & \text{si no}
\end{cases}


---

📖 Explicación Conceptual

Esta ecuación representa una nueva forma de entender la existencia, donde lo que es, no proviene del deseo ni de la mera posibilidad, sino de una intersección crítica entre lo probable y lo estructuralmente viable.

Dicho de otra forma:

> Algo no existe porque puede existir. Existe porque fue probable y posible al mismo tiempo, y superó un umbral de realidad.




---

🧩 Definición de Variables


Resultado de existencia del fenómeno .

Valor 1: el fenómeno existe (colapsa en la realidad).

Valor 0: el fenómeno no existe (permanece en latencia o solo como idea).




---


Probabilidad cuantificable del fenómeno .

Se expresa en el intervalo real .

Representa qué tan probable es que ocurra, dentro de un entorno físico, estadístico, simbólico o narrativo.




---


Posibilidad lógica del fenómeno .

Valor binario:

1 si el fenómeno es estructuralmente posible (no viola las reglas del sistema donde intenta manifestarse).

0 si el fenómeno es imposible (incoherente, contradictorio o físicamente inviable).





---


Umbral mínimo de existencia.

Es el punto donde la combinación de posibilidad y probabilidad se vuelve suficiente para colapsar en existencia.

Este umbral puede variar según el sistema:

En universos físicos → puede implicar una constante cuántica.

En inteligencia artificial → puede representar una política de activación.

En arte o narrativa → puede ser definido estéticamente o por diseño.





---

🔁 Lógica de Funcionamiento

1. Si el fenómeno es imposible ()
→ entonces su existencia será 0, aunque sea altamente probable.


2. Si el fenómeno es posible pero poco probable ()
→ no alcanza el umbral para manifestarse.


3. Solo si el fenómeno es posible y lo suficientemente probable,
→ 
→ el fenómeno colapsa en existencia.




---

🧠 Ejemplos Ilustrativos

Ejemplo 1: Unicornio realista

Posibilidad lógica:  (biológicamente es posible diseñar un mamífero con cuerno).

Probabilidad:  (muy baja frecuencia histórica o evolutiva).

Umbral: 


Resultado:

E = 1 \cdot 0.001 = 0.001 < 0.05 \Rightarrow \text{No existe}


---

Ejemplo 2: Movimiento cuántico de una partícula








E = 0.92 \Rightarrow \text{Existe}


---

Ejemplo 3: Un cuadrado con cinco lados

 (es lógicamente imposible)




E = 0 \cdot 1 = 0 \Rightarrow \text{No existe}


---

🧬 Aplicación Ontológica

La ecuación permite construir sistemas donde la existencia no sea un absoluto fijo, sino un evento emergente y medible. Esto puede cambiar la forma en que:

Se desarrollan narrativas dinámicas.

Se diseñan sistemas de decisión en IA.

Se programan tokens digitales con condiciones ontológicas.

Se analiza la historia o evolución de eventos complejos.



---

🔮 Filosofía Final

> La existencia es el resultado de un equilibrio brutal:
lo que puede ser + lo que tiene chances reales de ser.



Esta ecuación no depende de voluntad, ni de fe, ni de diseño divino, sino de un cálculo frío, pero bello:

> La estadística decide el ser.


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

---



