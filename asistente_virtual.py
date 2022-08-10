import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import webbrowser
import datetime
import wikipedia


# escuchar microfono y devolver texto
def transformar_audio_a_texto():
    # almacena recognicer en variable
    r = sr.Recognizer()

    # configuracion de microfono
    with sr.Microphone() as origen:
        # tiempo de espera
        r.pause_threshold = 0.8
        # informar que comenzp la grabacion
        print('Ya puedes hablar')
        # guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            # buscar en google lo que escucho
            pedido = r.recognize_google(audio, language="es_ar")
            # pruena de que pudo ingresar
            print("Dijiste: " + pedido)

            # devolver pedido
            return pedido
        # en caso de no poder comprender audio
        except sr.UnknownValueError:
            # prueba de que no comprendio el audio
            print("Ups, no hay servicio")
            # devolver error
            return "Sigo esperando"
        except sr.RequestError:
            # prueba de que no comprendio el audio
            print("Ups, no comprendi")
            # devolver error
            return "Sigo esperando"
        except:

            # prueba de que no comprendio el audio
            print("Ups, algo ha salido mal")
            # devolver error
            return "Sigo esperando"


transformar_audio_a_texto()
