# Hello, this is a snippet
from button import *
from gtts import gTTS
from io import BytesIO
import time

lasttext = ""
sound = None
def speechfly(text, language='en'):
    global lasttext, sound

    if lasttext != text:
        lasttext = text
        print("new text")
        mp3_fo = BytesIO()
        tts = gTTS(text, lang=language)
        tts.write_to_fp(mp3_fo)
        mp3_fo.seek(0)
        pygame.mixer.init()
        sound = pygame.mixer.Sound(mp3_fo)
    sound.play()


def speak1():
    speechfly("See ya in the next video",
        "en")


pygame.init()
pygame.display.set_caption('Speakpyg')
screen = pygame.display.set_mode((1200, 900))
clock = pygame.time.Clock()

b1 = Button(text="ONE", fontsize=36,
            command=speak1)

def update():
    buttons.update()         # button 2
    buttons.draw(screen)     # button 3
    pygame.display.update()


is_running = True
while is_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if user quits window with [x] 
            is_running = False
    update()
    clock.tick(60)

pygame.quit()