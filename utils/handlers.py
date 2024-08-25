from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from telegram.ext import CallbackContext
from .google_sheets import authenticate_google_sheets


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


async def button_handler(update: Update, context: CallbackContext):
    try:
        query: CallbackQuery = update.callback_query
        data = query.data

        if data == 'servicios':
            await query.message.edit_text(
                "Nuestros servicios de automatización están diseñados para facilitar la gestión de tus grupos y mejorar tu marketing en Telegram. 🌟..."
            )
        elif data == 'precios':
            await query.message.edit_text(
                "Aquí tienes nuestra estructura de precios diseñada para ofrecerte el mejor valor y flexibilidad. 💰..."
            )
        elif data == 'ejemplos':
            await query.message.edit_text(
                "Aquí te mostramos cómo hemos ayudado a otros negocios a automatizar y optimizar sus grupos de Telegram. 📈..."
            )
        elif data == 'contacto':
            await query.message.edit_text(
                "Para hablar con un representante y obtener más detalles, por favor proporciona tu nombre y correo electrónico. Así podremos ofrecerte una atención personalizada y responder a todas tus preguntas. Escribe tu nombre:"
            )
        elif data == 'solicitar_consulta':
            await query.message.edit_text(
                "¡Genial! Un representante se pondrá en contacto contigo pronto para discutir los detalles. Gracias por tu interés. 😊"
            )
        elif data == 'aprovechar_oferta':
            await query.message.edit_text(
                "¡Genial! Te hemos registrado para la oferta limitada. Un representante te contactará para confirmar los detalles y comenzar con el servicio. 🚀"
            )
    except Exception as e:
        print(f"Error en el procesamiento del botón: {e}")
