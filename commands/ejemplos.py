from telegram import Update
from telegram.ext import CallbackContext


async def ejemplos(update: Update, context: CallbackContext):
    try:
        ejemplos_message = (
            "Aquí te mostramos cómo hemos ayudado a otros negocios a automatizar y optimizar sus grupos de Telegram. 📈\n\n"
            "<b>Ejemplo 1:</b> <i>E-commerce XYZ:</i> Implementamos un bot que gestionó más del 50% de las consultas automáticamente, reduciendo el tiempo de respuesta a minutos.\n\n"
            "<b>Ejemplo 2:</b> <i>Redes Sociales ABC:</i> Automatizamos las publicaciones y analizamos el rendimiento, incrementando el engagement en un 30%.\n\n"
            "<b>Ejemplo 3:</b> <i>Consultoría DEF:</i> Creamos un sistema de informes personalizados que permitió tomar decisiones basadas en datos reales.\n\n"
            "<a href='https://tu-testimonio.com'>Lee más testimonios de nuestros clientes</a>."
        )
        await update.message.reply_text(ejemplos_message,
                                        parse_mode='HTML',
                                        disable_web_page_preview=False)
    except Exception as e:
        print(f"Error en el comando /ejemplos: {e}")
