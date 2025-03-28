import random
# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
    "// Esto es un comentario",
    "/* Esto es un comentario */",
    "-- Esto es un comentario",
    "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]
# Se inicializa el puntaje en 0
puntaje = 0
#Se combina las tres listas en una lista de tuplas y se elige 3 elementos aleatorios de la lista combinada, teniendo un trio ordenado por pregunta,respuestas y respuesta correcta
questions_to_ask = random.sample(list(zip(questions, answers, correct_answers_index)), k=3)
# El usuario deberá contestar 3 preguntas
for question, answers_options, correct_answer in questions_to_ask:

    # Se muestra la pregunta y las respuestas posibles
    print(question)
    for i, answer in enumerate(answers_options):
        print(f"{i + 1}. {answer}")

# El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = input("Respuesta: ")
        #Se verifica que el elemento sea un digito y este en el rango de respuesta
        if not user_answer.isdigit() or int(user_answer) > 4: 
            print("Respuesta no válida")
            exit(1)
        else:
            user_answer = int(user_answer) - 1
        # Se verifica si la respuesta es correcta
        if user_answer == correct_answer:
            print("¡Correcto!")
            puntaje += 1
            break
    else:
        # Si el usuario no responde correctamente después de 2 intentos,
        # se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        print(answers_options[correct_answer])
        puntaje -= 0.5

    # Se imprime un blanco al final de la pregunta
    print()
print("El puntaje final del jugador es " + str(puntaje))