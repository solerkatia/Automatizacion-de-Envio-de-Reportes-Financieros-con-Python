# 🤖 Automatizador de Reportes Financieros en Gmail con Python

Este proyecto es una herramienta de automatización (RPA) construida en Python que combina la obtención de datos financieros en tiempo real con la automatización del navegador web. 

El script descarga el historial de cotizaciones de cualquier acción bursátil (usando `yfinance`), calcula métricas clave (máxima, mínima y valor medio), y redacta y envía automáticamente un correo formal en **Gmail** con los resultados.

---

## 🚀 Características Principales

- **Datos Financieros en Tiempo Real:** Obtiene información actualizada del mercado de valores usando `yfinance`.
- **Automatización de Interfaz (RPA):** Simula acciones de mouse y teclado mediante `pyautogui` para interactuar con Gmail.
- **Manejo Seguro del Portapapeles:** Utiliza `pyperclip` para pegar textos largos o con caracteres especiales sin errores de codificación.
- **Flujo Completo:** Desde la entrada de datos por consola hasta el envío y cierre de la pestaña de forma automatizada.

---

## 🛠️ Tecnologías y Librerías Utilizadas

- **Python 3.x**
- [yfinance](https://pypi.org/project/yfinance/)
- [PyAutoGUI](https://pypi.org/project/PyAutoGUI/)
- [Pyperclip](https://pypi.org/project/pyperclip/)
- `webbrowser` y `time` (Módulos nativos de Python)

---

## 📦 Instalación y Configuración


### 1. Clonar el repositorio
Abre tu terminal y ejecuta el siguiente comando:
```bash
git clone [https://github.com/solerkatia/Automatizacion-de-Envio-de-Reportes-Financieros-con-Python.git](https://github.com/solerkatia/Automatizacion-de-Envio-de-Reportes-Financieros-con-Python.git)
```

### 2. Instalar las librerías necesarias (pip install)
```
pip install yfinance pyautogui pyperclip
```

### 3. Cómo obtener las coordenadas de tu pantalla
- Ejecuta en tu terminal el archivo obtener_coordenadas.py
```bash
python obtener_coordenadas.py
```
- Se abrirá Gmail automáticamente. Coloca el cursor del mouse justo en el centro del botón "Redactar" y no lo muevas antes de que terminen los 5 segundos.

- La terminal te arrojará unos valores (por ejemplo: Point(x=136, y=195)).

- Copia esos números (x e y) y pégalos en tu archivo principal main.py en la línea del clic:
```bash
pyautogui.click(x=136, y=195)  # Reemplaza con tus coordenadas
```
### 4. Ejecuta la automatizacion
Una vez configuradas tus coordenadas en main.py, ejecuta el script desde tu terminal:
```bash
python main.py
```
La consola te pedirá ingresar los datos requeridos paso a paso:

- Símbolo de la acción (Ej: AAPL, TSLA, MSFT)

- Fecha de inicio (aaaa-mm-dd)

- Fecha de finalización (aaaa-mm-dd)

- Correo del destinatario

- Asunto del correo

---
## ⚠️ Advertencia de Uso
No muevas el mouse ni el teclado mientras el script abre el navegador, procesa los datos y redacta el correo automáticamente.

Mantén tu ventana de Gmail maximizada o en la misma posición donde realizaste la calibración de coordenadas.

Puedes comentar o descomentar la línea de envío automático en el código (pyautogui.hotkey('ctrl', 'enter')) según prefieras revisar el correo antes de que se envíe
---

## 👤 Autor
Desarrollado por [Katia Soler / Usuario de Github: solerkatia]. ¡Las contribuciones y sugerencias son bienvenidas!