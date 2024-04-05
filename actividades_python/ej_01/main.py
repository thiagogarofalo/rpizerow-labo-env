from gpiozero import LED, Button
from signal import pause

# Configurar el LED (pin GPIO correspondiente)
led = LED(13)

# Configurar el pulsador (pin GPIO correspondiente)
button = Button(18)

# Asignar función para encender o apagar el LED cuando se presione o suelte el pulsador
button.when_pressed = led.on
button.when_released = led.off

# Mantener el programa en ejecución
pause()
