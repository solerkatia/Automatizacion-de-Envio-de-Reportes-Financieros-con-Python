import time
import webbrowser
import pyautogui
import pyperclip
import yfinance

#pip install yfinance pyautogui pyperclip
# --- 1. ENTRADA DE DATOS DINÁMICA ---
ticker = input("Ingrese el código de acción (ej. AAPL, TSLA): ").upper()
dt_inicial = input("Introduzca la fecha de inicio (aaaa-mm-dd): ")
dt_final = input("Introduzca la fecha de finalización (aaaa-mm-dd): ")
destinatario = input("Ingrese el correo del destinatario: ")
asunto = input("Ingrese el asunto del correo: ")

print("\nDescargando datos y procesando análisis...")

# --- 2. ANÁLISIS FINANCIERO CON YFINANCE ---
datos = yfinance.Ticker(ticker)
tabla = datos.history(start=dt_inicial, end=dt_final)

cierre = tabla["Close"]

maxima = round(cierre.max(), 2)
minima = round(cierre.min(), 2)
valor_medio = round(cierre.mean(), 2)

# --- 3. CONSTRUCCIÓN DEL MENSAJE ---
mensaje = f"""Buen día,
A continuación se presenta el análisis de la acción {ticker} del periodo solicitado: {dt_inicial} a {dt_final}:
Cotización máxima: USD {maxima}
Cotización mínima: USD {minima}
Valor medio: USD {valor_medio}"""

# --- 4. AUTOMATIZACIÓN CON PYAUTOGUI ---
# Establecer una pausa de seguridad entre las acciones de pyautogui
pyautogui.PAUSE = 2

# Abre el navegador en Gmail
webbrowser.open("https://www.gmail.com")
print(
    "Esperando a que cargue Gmail (5 segundos)... No muevas el mouse ni el teclado."
)
time.sleep(5)

# 1. Hacer clic en el botón "Redactar" / "Escribir" usando coordenadas
pyautogui.click(x=136, y=195)
time.sleep(5)

# 2. Rellenar el destinatario
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")

# 3. Rellenar el asunto
pyperclip.copy(asunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")

# 4. Rellenar el cuerpo del mensaje
pyperclip.copy(mensaje)
pyautogui.hotkey("ctrl", "v")

print("\n¡Correo redactado con éxito!")
# 5. Enviar el correo (Comentar la siguiente línea si deseas que se envíe automáticamente)
pyautogui.hotkey("ctrl", "enter")
# 6. Cerrar la pestaña
pyautogui.hotkey("ctrl", "f4")
print("¡E-mail enviado exitosamente!")