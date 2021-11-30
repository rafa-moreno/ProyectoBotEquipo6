from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
import re
import random
def start(update, context):
    update.message.reply_text(f"Oído cocina. Tú dirás...")

def final (update, context):
    update.message.reply_text('Hasta la proxima')

def funcita(update, context):
    cita= ['Al no ser los únicos, decidimos ser los mejores. (Gorka Lomeña)',
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
    varcita = random.choice(cita)
    return varcita

def funods(update, context):
    lista = ['Fin de la pobreza', 'Hambre cero', 'Salud y bienestar', 'Educacion de calidad', 'Igualdad de genero',
             'agua limpia y saneamiento', 'energía asequible y no contaminante', 'Trabajo decente y crecimiento economico',
             'Industria, innovacion e infraestructura', 'reduccion de las desigualdades', 'Ciudades y comunidades sostenibles',
             'Produccion y consumo responsable', 'accion por el clima', 'vida submarina', 'Vida de ecosistemas Terrestres',
             'Paz, Justicia e instituciones solidas', 'Alianzas para lograr los objetivos']
    lenf = random.choice(lista)
    return lenf

def main():
    TOKEN = "2106107047:AAF3G3rnt1OGxdUnPCiPh69nOwvRb-bK6Rg"
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("inicio", start))
    dispatcher.add_handler(CommandHandler("final", final))
    dispatcher.add_handler(CommandHandler("cita", funcita))
    dispatcher.add_handler(CommandHandler("ods", funods))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
