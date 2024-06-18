import pandas as pd
import matplotlib.pyplot as plt
import yagmail
import os

# DATAFRAME
data = {
    'Nombre': ['Juan', 'Lucas', 'Luis', 'Fernando', 'Lopez', 'Elena'],
    'Altura': [1.75, 1.68, 1.82, 1.60, 1.78, 1.70],
}

df = pd.DataFrame(data)

def crear_graficos(df, filename):
    # Grafico altura amigos
    plt.figure(figsize=(6, 6))
    plt.bar(df['Nombre'], df['Altura'], color='skyblue')
    plt.xlabel('Nombre')
    plt.ylabel('Altura')
    plt.title('Alturas de amigos')
    plt.savefig(filename)
    plt.close()

def enviar_email_con_grafico(df, destinatario, asunto, cuerpo):
    # Crear y guardar grafico
    filename = 'grafico_alturas.png'
    crear_graficos(df, filename)

    # Cuenta de yagmail
    yag = yagmail.SMTP('desafioya.m.a.il@gmail.com', 'pcbfphsclbkmggzv') #Contraseña creada en "contraseña de apps", sin espacios y aparte necesito verificacion en 2 pasos

    # Enviar correo y grafico
    yag.send(
        to=destinatario,
        subject=asunto,
        contents=cuerpo,
        attachments=[filename]
    )


# Información del correo
destinatario = 'juanbermudez1234567890@gmail.com'
asunto = 'ALTURA'
cuerpo = 'Altura de los amigos a continuacion:'

# Enviar el correo
enviar_email_con_grafico(df, destinatario, asunto, cuerpo)