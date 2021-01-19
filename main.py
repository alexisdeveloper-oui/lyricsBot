import logging
import time
import config

import lyricsgenius

from telegram import Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackContext,
    ConversationHandler
)
import telegram

switch = False

updater = Updater(config.telegram_api_key, use_context=True)  # Enter your telegram API key here

dispatcher = updater.dispatcher

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

genius = lyricsgenius.Genius(config.genius_api_key)  # Enter your genius API key here

logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    '''ENVOYER MESSAGE QUAND COMMANDE START EST RECUE'''
    update.message.reply_text('Yo big c moe denis')
    time.sleep(1)
    update.message.reply_text('Je suis une intelligence artificielle de ***très haute qualité***',
                              parse_mode='MarkdownV2')
    time.sleep(1)
    update.message.reply_text("[Appuyez ici](pistacherigolo.com) *afin d'avoir plus d'informations*",
                              parse_mode='MarkdownV2')
    time.sleep(1)
    update.message.reply_text("La commande /lyrics est utilisée afin de trouver les paroles d'une chanson.")


aide = 'ouin big c normal que tu me demande de laide parce que moi aussi je comprend fkal mais allez visiter pistacherigolo.com pour plus de détails'


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text(aide)

def intro(update: Update, context: CallbackContext) -> int:
    if switch:
        artist_name = ''
    update.message.reply_text('Enter artist')
    return artist


def artist(update: Update, context: CallbackContext) -> int:
    update.message.reply_text("oui")
    global artist_name
    artist_name = update.message.text
    # This variable needs to be stored globally to be retrieved in the next state
    # artist = genius.search_artist(artist_name, max_songs=0)
    update.message.reply_text('Enter song title')
    # Let the conversation proceed to the next state
    return title


def title(update: Update, context: CallbackContext) -> int:
    song_name = update.message.text
    update.message.reply_text(artist_name + ', ' + song_name)
    time.sleep(1)
    update.message.reply_text("I'm thinking...")
    artists = genius.search_artist(artist_name, max_songs=0)
    song = artists.song(song_name)
    update.message.reply_text(song.lyrics)
    # return ConversationHandler.END to end the conversation
    switch = True
    return ConversationHandler.END


def oui(artist_name):
    return artist_name


def quit(update: Update, context: CallbackContext):
    return ConversationHandler.END

def main():
    """Ceci start monsieur Denis"""
    dispatcher.add_handler(CommandHandler('start', start))
    # dispatcher.add_handler(CommandHandler('help', help_command))

    # dispatcher.add_handler(CommandHandler('lyrics', lyrics))

    dispatcher.add_handler(ConversationHandler(
        entry_points=[CommandHandler('lyrics', intro)],
        states={
            artist: [MessageHandler(Filters.text, callback=artist)],
            title: [MessageHandler(Filters.text, callback=title)]
        },
        fallbacks=[CommandHandler('quit', quit)]
    ))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
