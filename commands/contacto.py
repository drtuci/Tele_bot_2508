from telegram import Update
from telegram.ext import CallbackContext


async def contacto(update: Update, context: CallbackContext):
    try:
        await update.message.reply_text(
            "Para hablar con un representante y obtener más detalles, por favor proporciona tu nombre y correo electrónico. Así podremos ofrecerte una atención personalizada y responder a todas tus preguntas.\n\n"
            "Escribe tu nombre:")
        context.user_data['esperando_nombre'] = True
    except Exception as e:
        print(f"Error en el comando /contacto: {e}")
