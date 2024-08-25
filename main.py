import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from telegram.ext import CallbackContext
from commands import servicios, precios, ejemplos, contacto, cancelar
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


# Autenticación de Google Sheets
def authenticate_google_sheets():
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = {
        "type": os.getenv("KEY_TYPE"),
        "project_id": os.getenv("KEY_PROJECT_ID"),
        "private_key_id": os.getenv("KEY_PRIVATE_KEY_ID"),
        "private_key": os.getenv("KEY_PRIVATE_KEY").replace("\\n", "\n"),
        "client_email": os.getenv("KEY_CLIENT_EMAIL"),
        "client_id": os.getenv("KEY_CLIENT_ID"),
        "auth_uri": os.getenv("KEY_AUTH_URI"),
        "token_uri": os.getenv("KEY_TOKEN_URI"),
        "auth_provider_x509_cert_url": os.getenv("KEY_AUTH_PROVIDER_CERT_URL"),
        "client_x509_cert_url": os.getenv("KEY_CLIENT_CERT_URL")
    }

    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds, scope)
    client = gspread.authorize(creds)
    return client


async def start(update: Update, context: CallbackContext):
    try:
        keyboard = [
            [
                InlineKeyboardButton("Nuestros Servicios",
                                     callback_data='servicios')
            ], [InlineKeyboardButton("Precios", callback_data='precios')],
            [InlineKeyboardButton("Ejemplos", callback_data='ejemplos')],
            [InlineKeyboardButton("Contacto", callback_data='contacto')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        welcome_message = (
            "¡Hola! Soy tu asistente de automatización para Telegram. 🚀 "
            "Aquí puedes encontrar información sobre cómo optimizar tus grupos y mejorar tu estrategia de marketing.\n\n"
            "Utiliza los botones a continuación para explorar nuestros servicios y ofertas:"
        )

        await update.message.reply_text(welcome_message,
                                        reply_markup=reply_markup,
                                        parse_mode='HTML')
    except Exception as e:
        print(f"Error en el comando /start: {e}")


async def handle_message(update: Update, context: CallbackContext):
    try:
        text = update.message.text

        if context.user_data.get('esperando_nombre'):
            context.user_data['nombre'] = text
            context.user_data['esperando_nombre'] = False
            context.user_data['esperando_correo'] = True
            await update.message.reply_text(
                "Gracias, ahora proporciona tu correo electrónico.")
        elif context.user_data.get('esperando_correo'):
            context.user_data['correo'] = text
            nombre = context.user_data.get('nombre')
            guardar_lead(nombre, text)
            context.user_data['esperando_correo'] = False
            await update.message.reply_text(
                f"Gracias {nombre}, te contactaremos pronto.")
        else:
            if "automatización" in text or "grupos" in text or "chatbots" in text:
                await update.message.reply_text(
                    "Ofrecemos servicios de automatización para Telegram y chatbots..."
                )
            elif "precio" in text or "costo" in text or "tarifa" in text:
                await update.message.reply_text("Nuestros precios son...")
            elif "ejemplos" in text or "cómo funciona" in text or "demostraciones" in text:
                await update.message.reply_text(
                    "Aquí hay algunos ejemplos de cómo funciona...")
            elif "descuento" in text or "promoción" in text or "oferta" in text:
                await update.message.reply_text(
                    "Actualmente ofrecemos las siguientes promociones...")
            elif "hablar con alguien" in text or "contacto" in text or "ayuda" in text:
                await update.message.reply_text(
                    "Te conectaremos con un representante pronto...")
            else:
                await update.message.reply_text(
                    "No entendí tu mensaje. ¿Puedes intentar con otra pregunta?"
                )
    except Exception as e:
        print(f"Error en el procesamiento del mensaje: {e}")


def guardar_lead(nombre, correo):
    try:
        client = authenticate_google_sheets()
        sheet = client.open("Clientes").sheet1
        sheet.append_row([nombre, correo])
    except Exception as e:
        print(f"Error al guardar el lead en Google Sheets: {e}")


async def solicitar_contacto(update: Update, context: CallbackContext):
    try:
        await update.message.reply_text("Por favor, proporciona tu nombre.")
        context.user_data['esperando_nombre'] = True
    except Exception as e:
        print(f"Error en el comando /contacto: {e}")


def main():
    application = Application.builder().token(
        os.getenv("TELEGRAM_TOKEN")).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("servicios", servicios.servicios))
    application.add_handler(CommandHandler("precios", precios.precios))
    application.add_handler(CommandHandler("ejemplos", ejemplos.ejemplos))
    application.add_handler(CommandHandler("contacto", solicitar_contacto))
    application.add_handler(CommandHandler("cancelar", cancelar.cancelar))
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()


if __name__ == "__main__":
    main()
