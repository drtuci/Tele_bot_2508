from telegram import Update
from telegram.ext import CallbackContext


async def servicios(update: Update, context: CallbackContext):
    try:
        servicios_message = (
            "Nuestros servicios de automatización están diseñados para facilitar la gestión de tus grupos y mejorar tu marketing en Telegram. 🌟\n\n"
            "<b>1. Automatización de Mensajes:</b> Envía mensajes automáticos para mantener a tu audiencia comprometida.\n\n"
            "<b>2. Gestión de Interacciones:</b> Responde a mensajes de manera automática según palabras clave.\n\n"
            "<b>3. Automatización de Campañas:</b> Diseña y ejecuta campañas de marketing sin esfuerzo. Personaliza los mensajes y alcanza a tus usuarios en el momento adecuado.\n\n"
            "<a href='https://tu-caso-de-estudio.com'>Lee más sobre nuestros casos de éxito</a>."
        )
        await update.message.reply_text(servicios_message,
                                        parse_mode='HTML',
                                        disable_web_page_preview=False)
    except Exception as e:
        print(f"Error en el comando /servicios: {e}")
