# hello_psg.py

import PySimpleGUI as sg

import random

acierto = 0
fallo = 0
totales = 0

# pyinstaller --onefile prueba.py

def iniciarVocabulario():

    # Leer las palabras del fichero vocabulario.txt, y meterlas en una lista sabiendo que están separadas por comas

    vocabulario = open("vocabulario.txt", "r")

    vocabularioNP = vocabulario.read().split(",")

    vocabulario.close()

    return vocabularioNP

    



# Create a layout with 5 buttons

layout = [[sg.Text('Bienvenidos al vocabulario del Panda. Si es la primera vez que inicias el programa, haz click en "Iniciar Vocabulario"', key='Intro')],

    [sg.Text("", key='palabra')],
    
    [sg.Button('Iniciar Vocabulario'), sg.Button('Acierto'), sg.Button('Fallo')],
    
    [sg.Button('Cerrar'), sg.Button('Reiniciar'), sg.Text('Aciertos: '), sg.Text(acierto, key='Acierto_txt'), sg.Text('Fallos: '), sg.Text(fallo, key='Fallo_txt'), sg.Text('Total: '), sg.Text(totales, key='Total_txt')],

    ]

def nuevaPalabra(vocabNP):

    palabra = random.choice(vocabNP)
    vocabNP.remove(palabra)
    window['palabra'].update(palabra)

    return vocabNP


# Create the window
window = sg.Window("Vocabulario", layout)
window.set_icon('images/panda.ico')

# Create an event loop
while True:
    event, values = window.read()
    
    # Crea una variable para el vocabulario tipo lista

    if event == "Reiniciar":
        vocabulario = iniciarVocabulario()
        totales = len(vocabulario)
        window['Total_txt'].update(totales)
        window['palabra'].update(" === REINICIADO === ")
        acierto = 0
        fallo = 0
        window['Acierto_txt'].update(acierto)
        window['Fallo_txt'].update(fallo)
        
        
    if event == "Iniciar Vocabulario":
        vocabulario = iniciarVocabulario()
        totales = len(vocabulario)
        window['Total_txt'].update(totales)
        vocabulario = nuevaPalabra(vocabulario)

    if event == "Acierto":
        try:
            nuevaPalabra(vocabulario)
            acierto += 1
            window['Acierto_txt'].update(acierto)
            totales -= 1
            window['Total_txt'].update(totales)
        except:
            window['palabra'].update("Si es la primera vez, activa el vocabulario")
    
    if event == "Fallo":
        try:
            nuevaPalabra(vocabulario)
            fallo += 1
            window['Fallo_txt'].update(fallo)
            totales -= 1
            window['Total_txt'].update(totales)
        except:
            window['palabra'].update("Si es la primera vez, activa el vocabulario")

    # Si no existen mas palabras, preguntar si se quiere reiniciar

    if totales == 0:
        window['palabra'].update("No quedan mas palabras, reinicia el vocabulario")

    if event == "Cerrar" or event == sg.WIN_CLOSED:
        break

window.close()