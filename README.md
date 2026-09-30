# 🤖 Automatización de Envío de Correos en Gmail con Python

Proyecto en Python enfocado en la automatización de tareas repetitivas utilizando las librerías `pyautogui`, `pyperclip` y `webbrowser`. Este script abre automáticamente el navegador, accede a Gmail, redacta un correo formal con el análisis financiero de una acción (ticker) y completa los campos de destinatario, asunto y mensaje.

---

## 🚀 Características

- **Automatización de interfaz web:** Simula interacciones de teclado y mouse mediante `pyautogui`.
- **Manejo del portapapeles:** Utiliza `pyperclip` para copiar y pegar textos de forma rápida y sin errores de codificación.
- **Mensajes dinámicos:** Incorpora cadenas formateadas (`f-strings`) para estructurar reportes personalizados con datos financieros (cotizaciones máxima, mínima y valor medio).

---

## 🛠️ Tecnologías y Librerías Utilizadas

- **Python 3.x**
- **PyAutoGUI**: Para la automatización del mouse y teclado.
- **Pyperclip**: Para la manipulación segura del portapapeles (útil para caracteres especiales o acentos).
- **Webbrowser**: Módulo estándar de Python para abrir URLs en el navegador web predeterminado.

---

## 📋 Requisitos Previos

Asegúrate de tener Python instalado en tu equipo. Luego, instala las librerías necesarias ejecutando el siguiente comando en tu terminal:

```bash
pip install pyautogui pyperclip