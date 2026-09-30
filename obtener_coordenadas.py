import time
import pyautogui
import webbrowser

webbrowser.open("https://www.gmail.com")
print(
    "👉 Tienes 5 segundos para mover el mouse exactamente encima del botón 'Redactar' de Gmail..."
)
time.sleep(5)
r = pyautogui.position()
print(r)
# Muestra la posición actual del cursor
print("¡Listo! Las coordenadas de tu pantalla son:", pyautogui.position())