from telegram import Update
from telegram.ext import CallbackContext


async def testimonios(update: Update, context: CallbackContext):
    try:
        testimonios_message = (
            "Nuestros clientes han experimentado mejoras significativas con nuestra automatización. Aquí algunos testimonios:\n\n"
            "<b>Testimonio 1:</b> <i>“El bot ha transformado la manera en que gestionamos nuestras interacciones en Telegram. La automatización ha sido clave para nuestro crecimiento.”</i> - Ana P., E-commerce\n\n"
            "<b>Testimonio 2:</b> <i>“No solo hemos ahorrado tiempo, sino que también hemos visto un aumento en el engagement de nuestros usuarios. Altamente recomendado.”</i> - Luis M., Agencia de Marketing\n\n"
            "<a href='https://tu-testimonios.com'>Lee más testimonios de nuestros clientes</a>."
        )
        await update.message.reply_text(testimonios_message,
                                        parse_mode='HTML',
                                        disable_web_page_preview=False)
    except Exception as e:
        print(f"Error en el comando /testimonios: {e}")
