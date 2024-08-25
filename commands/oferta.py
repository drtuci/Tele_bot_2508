from telegram import Update
from telegram.ext import CallbackContext


async def oferta(update: Update, context: CallbackContext):
    try:
        oferta_message = (
            "¡Oferta Limitada! 🎉\n\n"
            "Solo por tiempo limitado, puedes obtener un <b>15% de descuento</b> en la configuración inicial del bot y un mes de mantenimiento gratuito. 🚀\n\n"
            "¿Te gustaría aprovechar esta oferta? Haz clic en el botón a continuación para obtener más detalles y comenzar ahora mismo."
        )

        keyboard = [[
            InlineKeyboardButton("Aprovechar Oferta",
                                 callback_data='aprovechar_oferta')
        ]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text(oferta_message,
                                        parse_mode='HTML',
                                        reply_markup=reply_markup)
    except Exception as e:
        print(f"Error en el comando /oferta: {e}")
