import lyricsgenius
import telegram_send
import colorama
from colorama import Fore, Back
from flask import Flask
app = Flask(__name__)


substring = '['
substring2 = '('
genius = lyricsgenius.Genius('BjqDZhDb9WUL9AfzhDjwxSKJSxG1GrLTDIXCSZEhgi1FFZSg8H7N_mXnedjLlTG_')

#artist_name = input("Entrez l'artiste recherché : ")
artist_name = "playboi carti"
artist = genius.search_artist(artist_name, max_songs=0)
#genius.verbose = False


#song_name = input('Entrez la chanson recherchée : ')
song_name = "beno"
print("\n")

song = artist.song(song_name)

lyrics = song.lyrics
'''
for line in lyrics.splitlines():
    if line.find(substring) != -1:
        print(Fore.LIGHTBLUE_EX + line)
    #elif line.find(substring2) != -1:
     #   print(Fore.GREEN + line)
    else:
        print(Fore.WHITE + line)
'''

#print(lyrics)
print(dir(song.year))
print(lyrics.upper())
if song.album == song.artist:
    output = "\n\nReleased le " + song.year + " sur l'album éponyme de " + song.artist
else:
    output = "\n\nReleased le " + song.year + " sur l'album " + song.album
print(output)

telegram_send.send(messages=[lyrics, output])
#song.save_lyrics()
'''
@app.route('/')
def hello():
    return song.lyrics #ne print pas de maniere clean sur le site, ca reste a corriger


if __name__ == '__main__':
    app.run()

import telegram_send

while 1 == 1:
    telegram_send.markup('oui', 'red')
    telegram_send.send(messages=[input()])
'''





'''import logging


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

my_token = '1461825208:AAHI_bkm8aQ-RJ9qrRqUevLIRIb6BvTflS8'

msg = 'ceci est un message du gouvernement du canada toumtimtiloum'

def send(msg, chat_id, token=my_token):
    bot = telegram.Bot(token=my_token)
    bot.send_message(chat_id=1471971882, text='oui')'''