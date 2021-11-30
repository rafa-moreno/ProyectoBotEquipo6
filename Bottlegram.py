from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
import re
import random


def start(update, context):
    global salir
    salir = True
    if salir:
        update.message.reply_text("Oído cocina. Tú dirás...")
        salir = False


def help(update, context):
    if not salir:
        update.message.reply_text('help command received')


def error(update, context):
    if not salir:
        update.message.reply_text('an error occured')


def final(update, context):
    global salir

    if not salir:
        update.message.reply_text('Hasta la próxima')
        salir = True


def funcita(update, context):
    if not salir:
        cita = ['Al no ser los únicos, decidimos ser los mejores. (Gorka Lomeña)',
                'Si la depuración es el proceso de eliminar errores, entonces la programación debe ser el proceso de introducirlos. (Edsger Dijkstra)',
                'Pensar es el trabajo más difícil que existe. Quizá esa sea la razón por la que haya tan pocas personas que lo practiquen. (Henry Ford)',
                'No es que sea muy inteligente. Es simplemente que estoy más tiempo con los problemas. (Albert Einstein)',
                'Programar no es un talento; es una habilidad. En tu mano está desarrollarla. (Codecademy)',
                'No digas: “Es imposible”. Di: “No lo he hecho todavía”. (Proverbio japonés)',
                'La experiencia demuestra que el éxito de un curso de programación depende críticamente de la elección de los ejemplos que se utilice. (Niklaus Wirth)',
                'Al ordenador le importa tres leches tu problema, así que el esfuerzo por que éste realice un proceso por el cual se resuelve dicho problema lo tienes que hacer TÚ. Y el esfuerzo consiste en dárselo mascado para que lo lleve a cabo una y otra vez. (Alex Tolón)',
                'Las raíces del estudio son amargas. Los frutos, dulces. (Cicerón)',
                'Los malos programadores se preocupan del código. Los buenos se preocupan de las estructuras de datos y de sus relaciones. (Linus Torvalds)',
                'La práctica te perfecciona. Descubre cuánta práctica necesitas tú. (Alex Tolón)',
                'Un problema se transforma en desafío cuando le pones fecha de solución. (Anónimo)',
                'Si lo intentas, fallas. No importa. Inténtalo de nuevo. Falla de nuevo. Falla mejor. (Samuel Beckett)',
                'El futuro no es lo que va a pasar sino lo que   vamos a hacer. (Anónimo)']
        update.message.reply_text(random.choice(cita))


def funods(update, context):
    if not salir:
        ods = [
            'A nivel mundial, el número de personas que viven en situación de extrema pobreza disminuyó desde un 36 % en 1990 hasta un 10 % en 2015.'
            'No obstante, el ritmo al que se produce este cambio está disminuyendo, y la crisis de la COVID-19 pone en riesgo décadas de progreso en '
            'la lucha contra la pobreza. Más de 700 millones de personas, o el 10 % de la población mundial, aún vive en situación de extrema pobreza '
            'a día de hoy, con dificultades para satisfacer las necesidades más básicas, como la salud, la educación y el acceso a agua y saneamiento, '
            'por nombrar algunas. De hecho, el 8 % de los trabajadores de todo el mundo, y sus familias, vivían en situación de extrema pobreza en 2018',
            'Si la depuración es el proceso de eliminar errores, entonces la programación debe ser el proceso de introducirlos. (Edsger Dijkstra)',
            'Pensar es el trabajo más difícil que existe. Quizá esa sea la razón por la que haya tan pocas personas que lo practiquen. (Henry Ford)',
            'No es que sea muy inteligente. Es simplemente que estoy más tiempo con los problemas. (Albert Einstein)',
            'Programar no es un talento; es una habilidad. En tu mano está desarrollarla. (Codecademy)',
            'No digas: “Es imposible”. Di: “No lo he hecho todavía”. (Proverbio japonés)',
            'La experiencia demuestra que el éxito de un curso de programación depende críticamente de la elección de los ejemplos que se utilice. (Niklaus Wirth)',
            'Al ordenador le importa tres leches tu problema, así que el esfuerzo por que éste realice un proceso por el cual se resuelve dicho problema lo tienes que hacer TÚ. Y el esfuerzo consiste en dárselo mascado para que lo lleve a cabo una y otra vez. (Alex Tolón)',
            'Las raíces del estudio son amargas. Los frutos, dulces. (Cicerón)',
            'Los malos programadores se preocupan del código. Los buenos se preocupan de las estructuras de datos y de sus relaciones. (Linus Torvalds)',
            'La práctica te perfecciona. Descubre cuánta práctica necesitas tú. (Alex Tolón)',
            'Un problema se transforma en desafío cuando le pones fecha de solución. (Anónimo)',
            'Si lo intentas, fallas. No importa. Inténtalo de nuevo. Falla de nuevo. Falla mejor. (Samuel Beckett)',
            'El futuro no es lo que va a pasar sino lo que   vamos a hacer. (Anónimo)']

        update.message.reply_text(random.choice(ods))


def main():
    token = "2106107047:AAF3G3rnt1OGxdUnPCiPh69nOwvRb-bK6Rg"
    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher

    global salir
    salir = True
    dispatcher.add_handler(CommandHandler("inicio", start))

    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(CommandHandler("cita", funcita))
    dispatcher.add_handler(CommandHandler("ods", funods))
    dispatcher.add_handler(CommandHandler("final", final))

    dispatcher.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
