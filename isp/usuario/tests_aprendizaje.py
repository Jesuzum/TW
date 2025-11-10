TEST_PREGUNTAS = [
    {
        "pregunta": "Cuando aprendes algo nuevo, ¿qué prefieres hacer?",
        "opciones": {
            "visual": "Ver imágenes, diagramas o videos explicativos",
            "auditivo": "Escuchar explicaciones o grabaciones",
            "kinestesico": "Experimentar y hacerlo tú mismo"
        }
    },
    {
        "pregunta": "¿Cómo recuerdas mejor la información?",
        "opciones": {
            "visual": "Viendo apuntes o colores",
            "auditivo": "Escuchando mi propia voz o la de otros",
            "kinestesico": "Repitiendo la acción o practicando"
        }
    },
    {
        "pregunta": "¿Qué haces cuando intentas recordar algo?",
        "opciones": {
            "visual": "Visualizo la escena o el texto",
            "auditivo": "Escucho las palabras en mi cabeza",
            "kinestesico": "Recuerdo cómo me sentí o qué hice"
        }
    },
    {
        "pregunta": "En una conferencia, prefieres...",
        "opciones": {
            "visual": "Ver diapositivas e imágenes",
            "auditivo": "Escuchar al ponente",
            "kinestesico": "Tomar notas o participar activamente"
        }
    },
    {
        "pregunta": "Cuando lees un libro...",
        "opciones": {
            "visual": "Te imaginas las escenas",
            "auditivo": "Escuchas las voces de los personajes",
            "kinestesico": "Te identificas con las acciones físicas"
        }
    },
    {
        "pregunta": "¿Qué tipo de películas disfrutas más?",
        "opciones": {
            "visual": "Con buena fotografía o efectos visuales",
            "auditivo": "Con buena música y diálogos",
            "kinestesico": "Con acción o experiencias intensas"
        }
    },
    {
        "pregunta": "Cuando alguien te da direcciones, prefieres que te lo diga...",
        "opciones": {
            "visual": "Con un mapa o croquis",
            "auditivo": "Verbalmente paso a paso",
            "kinestesico": "Acompañándome o mostrándome en persona"
        }
    },
    {
        "pregunta": "Si estás aprendiendo algo nuevo, ¿qué te ayuda más?",
        "opciones": {
            "visual": "Esquemas o gráficos",
            "auditivo": "Explicaciones habladas",
            "kinestesico": "Probarlo y practicar"
        }
    },
    {
        "pregunta": "¿Cómo prefieres estudiar?",
        "opciones": {
            "visual": "Subrayando y usando colores",
            "auditivo": "Leyendo en voz alta",
            "kinestesico": "Moviéndome o escribiendo mucho"
        }
    },
    {
        "pregunta": "En tu tiempo libre prefieres...",
        "opciones": {
            "visual": "Ver series o dibujar",
            "auditivo": "Escuchar música o podcasts",
            "kinestesico": "Hacer ejercicio o salir"
        }
    }
]

def calcular_metodo(respuestas):
    conteo = {"visual": 0, "auditivo": 0, "kinestesico": 0}
    for r in respuestas:
        conteo[r] += 1
    return max(conteo, key=conteo.get)
