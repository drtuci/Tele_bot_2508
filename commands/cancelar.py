from telegram import Update
from telegram.ext import CallbackContext


async def cancelar(update: Update, context: CallbackContext):
    try:
        await update.message.reply_text(
            "Operación cancelada. Si necesitas más ayuda, no dudes en usar cualquier otro comando."
        )
    except Exception as e:
        print(f"Error en el comando /cancelar: {e}")
