from telegram import Update
from telegram.ext import CallbackContext


async def precios(update: Update, context: CallbackContext):
    try:
        precios_message = (
            "Aquí tienes nuestra estructura de precios diseñada para ofrecerte el mejor valor y flexibilidad. 💰\n\n"
            "<b>Precio Inicial:</b> $500 MXN para la configuración y personalización del bot.\n\n"
            "<b>Mantenimiento Mensual:</b> $200 MXN para mantenimiento, actualizaciones y soporte técnico.\n\n"
            "<b>Promoción de Lanzamiento:</b> 10% de descuento en la configuración inicial para los primeros 50 clientes.\n\n"
            "<b>Prueba Gratuita:</b> Disfruta de una prueba gratuita de una semana con funcionalidades limitadas.\n\n"
            "<b>Marketing de Referencias:</b> Obtén descuentos adicionales al referir nuevos clientes.\n\n"
            "¿Interesado en una oferta personalizada? Haz clic en el botón a continuación para solicitar una consulta gratuita."
        )

        keyboard = [[
            InlineKeyboardButton("Solicitar Consulta",
                                 callback_data='solicitar_consulta')
        ]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text(precios_message,
                                        parse_mode='HTML',
                                        reply_markup=reply_markup)
    except Exception as e:
        print(f"Error en el comando /precios: {e}")
