"""
Aplicación Botarate.
Desarrollo de un bot que responde de manera automática según lo que
el usuario le diga. Tendrá diferentes niveles de funcionalidad,
desde respuestas simples, respuestas basadas en patrones regulares,
hasta respuestas almacenadas en fichero externo. También se podrá pedir
un PDF con las entradas y salidas de esta ultima opción

Autores:
-Rafael Ruiz Moreno
-Silvia Barea Gómez
-Pablo Lupión Márquez
-Manuel Castellano
"""
import datetime
import pickle
import random
import re

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# Lista de respuestas que el bot propocionará al usuario en caso de recibir un saludo simple
respuestasSaludo = [">Hola, encantado de conocerte", ">¡Buenas!", ">¿Me estás hablando a mi?",
                    ">¡Hey! ¿Cómo te llamas?"]


def obtenerdia():
    diaIngles = datetime.datetime.today().strftime('%A')
    if diaIngles == "Monday":
        return "Lunes"
    elif diaIngles == "Tuesday":
        return "Martes"
    elif diaIngles == "Wednesday":
        return "Miercoles"
    elif diaIngles == "Thursday":
        return "Jueves"
    elif diaIngles == "Friday":
        return "Viernes"
    elif diaIngles == "Saturday":
        return "Sábado"
    else:
        return "Domingo"


# Primera opción del programa, en la que el bot responderá de forma simple a preguntas pre-establecidas
def botsimple():
    # Diccionario que contendrá las diferentes preguntas y respuestas a las mismas.
    dicrespuestas = {"Hola": ">Muy buenas, usuario. Soy Botarate",
                     "¿Qué sabes de música?": ">Pues la verdad que de eso sé poco",
                     "¿Qué sabes de informática?": ">Se mucho sobre eso, ¡Soy un robot!",
                     "Hola, soy Manuel": ">Muy buenas, Manuel. Yo soy Botarate",
                     "Hola, soy Rafa": ">Hola, Rafa, encantado de conocerte. Yo soy Botarate",
                     "Hola, soy Silvia": ">Encantado Silvia, yo soy Botarate",
                     "Hola, soy Pablo": ">Buenas, Pablo, yo soy Botarate",
                     "Hola, soy Alex": ">Encantado Alex, yo soy Botarate",
                     "¿Cómo está el tiempo hoy?": ">Seguramente llueva, o no",
                     "¿Cuál es tu comida favorita?": ">Si pudiera comer, sólo comería pizzas pepperoni",
                     "¿Cuántos años tienes?": ">¡Qué maleducado!",
                     "¿Qué día es hoy?": ">¡Hoy es un gran día!",

                     "Alt": ">Lo siento, no te he entendido"}
    entrada = ""
    print("\t\tBot a la escucha...(pregunta cuando quieras)\n")
    # Mientras la entrada no sea "salir" o "Salir", el bot funcionará
    while entrada.casefold() != "salir".casefold():
        entrada = input("\t\t>")
        # Si la entrada se encuentra en el diccionario, se imprimirá la respuesta que tiene asignada
        if entrada in dicrespuestas:
            print("\t\t>", dicrespuestas.get(entrada))
        # Si la entrada es salir o Salir, imprimirá un mensaje de despedida
        elif entrada.casefold() == "salir":
            print("\t\t>¡Hasta la próxima!\n")
        # En caso de que la entrada no esté en el diccionario, el bot imprimirá un mensaje alternativo
        else:
            print("\t\t>", dicrespuestas.get("Alt"))


def obtenercadena(fpatron, fcadena):
    # Lista de palabras (agrupadas en una tupla) de la cadena que coinciden con el patrón
    listaPalabras = re.findall(fpatron, fcadena)
    # Se eliminan de la cadena todas las palabras de esta tupla, quedando sólo lo que no está en el patrón
    for palabra in listaPalabras[0]:
        fcadena = fcadena.replace(palabra, "")
    return fcadena


# Función auxiliar del bot REGEX, en la que se buscan patrones regulares en la entrada
def comprobarentrada(cadena):
    # Patrón que corresponde a un saludo con nombre
    if re.search(patronSaludoNombre, cadena):
        nombre = obtenercadena(patronSaludoNombre, cadena)
        print(f"\t\t>Muy buenas, {nombre}. Soy Botarate")

    # Patrón que corresponde a un saludo simple
    elif re.search(patronSaludoSimple, cadena):
        # Se imprime una respuesta aleatoria correspondiente a un saludo simple
        print(f"\t\t>{respuestasSaludo[random.randint(0, len(respuestasSaludo) - 1)]}")

    # Patrón que corresponde a una presentación simple
    elif re.search(patronNombre, cadena):
        nombre = obtenercadena(patronNombre, cadena)
        print(f"\t\t>Encantado de conocerte, {nombre}. ")

    # Patrón que coresponde a una pregunta sobre si sabe algo de alguna materia
    elif re.search(patronPregunta, cadena):
        materia = obtenercadena(patronPregunta, cadena).replace("?", "")
        print(f"\t\t>De {materia} se poco la verdad")

    elif re.search(patronQueDiaEsHoy, cadena):
        print(f"\t\t>Hoy es {obtenerdia()}")

    # Si la cadena introducida es "salir" o "Salir", finaliza el bot
    elif cadena.casefold() == "salir":
        return
    # Si la cadena no coincide con ningún patrón, el bot responderá un mensaje prederterminado
    else:
        print("\t\t>Lo siento, no te he entendido")


# Segunda opción del programa, en la que el bot responderá analizando la pregunta buscando patrones regulares
def botsimpleregex():
    entrada = ""
    print("\t\tBot a la escucha...(pregunta cuando quieras)\n")
    # Mientras la entrada no sea "salir" o "Salir", el bot funcionará
    while entrada.casefold() != "salir".casefold():
        entrada = input("\t\t>")
        comprobarentrada(entrada)

    print("\t\t>¡Hasta la próxima!\n")


def comprobarentradafichero(cadenafichero):
    fichero = open("preguntasrespuestas", "rb")
    listaPatronRespuesta = pickle.load(fichero)
    patrones = listaPatronRespuesta[0]
    respuestas = listaPatronRespuesta[1]
    cont = 0
    respuesta = ""
    encontrada = False
    for patron in patrones:
        if re.search(patron, cadenafichero):
            if patron == patronSaludoSimple:
                respuesta = f"\t\t{respuestas[cont][random.randint(0, len(respuestasSaludo) - 1)]}"
                print(respuesta)

            elif patron == patronQueDiaEsHoy:
                respuesta = str(respuestas[cont]).replace("xx", obtenerdia())
                print(respuesta)

            else:
                respuesta = (str(respuestas[cont]).replace("xx", obtenercadena(patron, cadenafichero).replace("?", "")))
                print(respuesta)
            encontrada = True
            break
        cont += 1

    fichero.close()
    if not encontrada and cadenafichero != "salir".casefold():
        respuesta = "\t\t>Lo siento no te he entendido"
        print(respuesta)

    conversacionBot = open("conversacion.txt", "a")
    conversacionBot.writelines(f"\n\t\t>{cadenafichero}")
    conversacionBot.writelines(f"\n{respuesta}")
    conversacionBot.close()


def botfichero():
    fichero = open("preguntasrespuestas", 'wb')
    listaPatronesRespuestas = [[patronSaludoNombre, patronNombre, patronSaludoSimple, patronPregunta,
                                patronQueDiaEsHoy],
                               ["\t\t>Muy buenas, xx. Soy Botarate", "\t\t>Encantado de conocerte, xx.",
                                respuestasSaludo, "\t\t>De xx se poco la verdad", "\t\t>Hoy es xx"]]
    pickle.dump(listaPatronesRespuestas, fichero)
    fichero.close()

    entrada = ""
    print("\t\tBot a la escucha...(pregunta cuando quieras)\n")
    # Mientras la entrada no sea "salir" o "Salir", el bot funcionará
    while entrada.casefold() != "salir".casefold():
        entrada = input("\t\t>")
        comprobarentradafichero(entrada)

    print("\t\t>¡Hasta la próxima!\n")
    c = open("conversacion.txt", "a")
    c.write("\t\t>¡Hasta la próxima!\n")


def informeconversacion():
    doc = canvas.Canvas("informe.pdf", pagesize=A4)
    doc.drawImage("chatbot_python.jpg", 120, 600, width=350, height=175)
    doc.setFont("Helvetica-Bold", 21)
    doc.drawString(123, 560, "INFORME DE LA CONVERSACIÓN")
    doc.setFont("Helvetica", 12)
    texto = doc.beginText(60, 530)
    conversacionInf = open("conversacion.txt", "r")
    listaCadenas = conversacionInf.readlines()
    for cadena in listaCadenas:
        texto.textLine(cadena)

    conversacionInf.close()
    doc.save()


# Programa principal
patronSaludoNombre = re.compile(r"^(Hola|Buenas)(,?)( *soy )|( *me llamo )|( *mi nombre es )", re.IGNORECASE)
patronSaludoSimple = re.compile(r"^(Hola|Buenas)([A-Za-z ])*", re.IGNORECASE)
patronNombre = re.compile(r"^(Soy )|(Me llamo )|(Mi nombre es )", re.IGNORECASE)
patronPregunta = re.compile(r"([¿]?Qué sabes de )\w+|(^[¿]*sabes algo de )\w+", re.IGNORECASE)
patronQueDiaEsHoy = re.compile(r"[¿]?Qué día es hoy[?]?\w*", re.IGNORECASE)

conversacion = open("conversacion.txt", "w")
conversacion.close()

salir = False
while not salir:

    # Menú principal del programa con las 5 opciones posibles
    print("\t\t\tAPLICACIÓN BOT-ARATE")
    print("\t\t1) Bot simple (respuestas planas...)")
    print("\t\t2) Bot simple (respuestas REGEX)")
    print("\t\t3) Bot simple mejorado desde fichero")
    print("\t\t4) Informe de la conversación (PDF)")
    print("\t\t5) Salir")

    opcion = int(input("Opción: "))
    if opcion == 1:
        botsimple()
    elif opcion == 2:
        botsimpleregex()
    elif opcion == 3:
        botfichero()
    elif opcion == 4:
        informeconversacion()
    elif opcion == 5:
        salir = True
    else:
        print("Introduzca una opción válida")
