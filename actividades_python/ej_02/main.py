from gpiozero import LED
from time import sleep

# Configurar los LEDs (pines GPIO correspondientes)
led_rojo = LED(13)
led_verde = LED(19)
led_azul = LED(26)

# Función para hacer parpadear el LED rojo cada segundo
def parpadear_rojo():
    while True:
        led_rojo.toggle()
        sleep(1)

# Función para hacer parpadear el LED azul cada medio segundo
def parpadear_azul():
    while True:
        led_azul.toggle()
        sleep(0.5)

# Función para hacer parpadear el LED verde cada un cuarto de segundo
def parpadear_verde():
    while True:
        led_verde.toggle()
        sleep(0.25)

# Iniciar los tres parpadeos en hilos separados
from threading import Thread

Thread(target=parpadear_rojo).start()
Thread(target=parpadear_azul).start()
Thread(target=parpadear_verde).start()

