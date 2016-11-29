import pygame
from time import sleep
from random import randint

must = (0, 0, 0)
helemust = (56, 56, 56)
valge = (255, 255, 255)
hall = (105, 105, 105)
helehall = (199, 199, 199)
lillakas = (117, 117, 255)
erkpunane = (255, 92, 92)
münt = (41, 255, 169)

sin = (105, 210, 245)
roh = (133, 245, 105)
pun = (247, 57, 57)
kol = (255, 241, 43)
ora = (255, 149, 43)
roo = (245, 95, 250)

pygame.init()

font = pygame.font.SysFont("Broadway", 110)
font2 = pygame.font.SysFont("DejaVu Sans", 40)
font4 = pygame.font.SysFont("DejaVu Sans", 30)
fontbutton = pygame.font.SysFont("DejaVu Sans", 20)
fonttegevus = pygame.font.SysFont("DejaVu Sans", 15)

# NUPPUDELE:
# OCR A Extended
# DejaVu Sans

# PEALKIRJALE:
# Broadway

def fondid(text, color, size):
    if size == "font":
        textSurface = font.render(text, True, color)
    elif size == "font2":
        textSurface = font2.render(text, True, color)
    elif size == "font4":
        textSurface = font4.render(text, True, color)
    elif size == "nupufont":
        textSurface = fontbutton.render(text, True, color)
    return textSurface, textSurface.get_rect()

laius = 1200
kõrgus = 600
nupu_laius = 100
nupu_kõrgus = 40
numbrinupu_laius = 50
numbrinupu_kõrgus = 40
nupuvärv_a = must
nupuvärv_b = helemust
nuputekstivärv = valge
punktid = 0
kord = 1
näita_punkte = False

Screen = pygame.display.set_mode((laius, kõrgus))  # teeb akna
pygame.display.set_caption("40 kraadi")  # aknale pealkiri

#nuppude loomine
class nupp():
    def __init__(self, rect, värv1, värv2, buttontekst, tulemus):
        self.rect = rect
        self.värv1 = värv1
        self.värv2 = värv2
        self.buttontekst = buttontekst
        self.tulemus = tulemus

    def draw(self):  # kas hiir on peal, muudab värvi
        if kas_hiir_on_nupul(self.rect[0], self.rect[1], self.rect[2], self.rect[3], pygame.mouse.get_pos()[0],
                             pygame.mouse.get_pos()[1]):
            # 0=nupp_x, 1=nupp_y, 2=nupu laius, 3=nupu kõrgus, pygame.mouse.get_pos()[0]=hiir_x, pygame.mouse.get_pos()[1]=hiir_y
            pygame.draw.rect(Screen, self.värv2, self.rect)
        else:
            pygame.draw.rect(Screen, self.värv1, self.rect)
        nuputekst(self.buttontekst, must, self.rect[0], self.rect[1], self.rect[2], self.rect[3])

    def mouse_collision(self, mouse_event):  # kas nuppu vajutati
        if kas_hiir_on_nupul(self.rect[0], self.rect[1], self.rect[2], self.rect[3], mouse_event.pos[0],
                             mouse_event.pos[1]):
            return self.tulemus
        else:
            return


def nuputekst(msg, color, buttonX, buttonY, button_width, button_height, size="nupufont"):
    textSurf, textRect = fondid(msg, nuputekstivärv, size)
    textRect.center = ((buttonX + (button_width / 2)), buttonY + (button_height / 2))
    Screen.blit(textSurf, textRect)


def handle_buttons(buttons, mouse_event):  # 'buttons' asemele läheb nuppude listinimi
    for b in buttons:
        result = b.mouse_collision(mouse_event)  # kontrollib, kas sellele nupule vajutati (kui jah, tagastab tulemuse)
        if result != None:  # kui nupule vajutati, tagastab tulemuse
            return result


def draw_buttons(buttons):
    for b in buttons:
        b.draw()  # kutsub klassist välja def-i


def kas_hiir_on_nupul(nupp_x, nupp_y, nupu_laius, nupu_kõrgus, hiir_x, hiir_y):
    if hiir_x < nupp_x or hiir_y < nupp_y or hiir_x > nupp_x + nupu_laius or hiir_y > nupp_y + nupu_kõrgus:
        return False
    else:
        return True

# NUPULISTID
start_nupud = [nupp((540, 300, nupu_laius, nupu_kõrgus), hall, helehall, "Alusta", "Alusta"),
               nupp((540, 350, nupu_laius, nupu_kõrgus), hall, helehall, "Abi", "Abi"),
               nupp((540, 400, nupu_laius, nupu_kõrgus), hall, helehall, "Välju", "Välju")]

abi_nupud = [nupp((540, 470, nupu_laius, nupu_kõrgus), hall, helehall, "Tagasi", "Tagasi")]

mängijate_arv_nupud = [nupp((575, 250, numbrinupu_laius, numbrinupu_kõrgus), hall, helehall, "2", "2_mängijat"),
                       nupp((575, 300, numbrinupu_laius, numbrinupu_kõrgus), hall, helehall, "3", "3_mängijat"),
                       nupp((575, 350, numbrinupu_laius, numbrinupu_kõrgus), hall, helehall, "4", "4_mängijat"),
                       nupp((575, 400, numbrinupu_laius, numbrinupu_kõrgus), hall, helehall, "5", "5_mängijat"),
                       nupp((575, 450, numbrinupu_laius, numbrinupu_kõrgus), hall, helehall, "6", "6_mängijat")]

tõmbakaartnupp = [nupp((810, 280, nupu_laius + 80, nupu_kõrgus), hall, helehall, "Tõmba kaart", "tõmbakaart")]

kaardinupud = [nupp((850, 250, nupu_laius, nupu_kõrgus), valge, helehall, "Tehtud!", "tehtud"),
               nupp((850, 450, nupu_laius, nupu_kõrgus), valge, helehall, "Jõin!", "jõin")]


def pilt(pildinimi, x, y):
    Screen.blit(pildinimi, (x, y))


def tekst(sõnum, font, värv, x, y):
    teksti_pilt = font.render(sõnum, False, värv)
    Screen.blit(teksti_pilt, (x, y))

#mängijate loomine
class inimene():
    def __init__(self, nimi, punktid, järjekord, värv):
        self.nimi = nimi
        self.punktid = punktid
        self.järjekord = järjekord
        self.värv = värv

    def lisa_punkte(self, arv):
        self.punktid += arv

mängija1 = inimene("Valdek", 0, 1, sin)
mängija2 = inimene("Tambet", 0, 2, roh)
mängija3 = inimene("Neeme", 0, 3, pun)
mängija4 = inimene("Alo", 0, 4, kol)
mängija5 = inimene("Kalev", 0, 5, ora)
mängija6 = inimene("Ilmar", 0, 6, roo)

def mäng():
    pygame.draw.rect(Screen, valge, (600, 0, 600, 600))
    tase = "tõmba"
    draw_buttons(tõmbakaartnupp)
    if result == "tõmbakaart":
        pygame.draw.rect(Screen, hall, (700, 100, 400, 400))
        draw_buttons(kaardinupud)
        tekst("Mängi kassi", fontbutton, must, 750, 150)
        if result == "tehtud" or result == "jõin":
            tase = "tõmba"

tase = "startmenüü"

gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.MOUSEBUTTONUP:

            # JALAD

            if tase == "startmenüü":
                result = handle_buttons(start_nupud, event)
                if result == "Alusta":
                    tase = "mängijate_arv"
                elif result == "Abi":
                    tase = "abi"
                elif result == "Välju":
                    gameExit = True

            elif tase == "abi":
                result = handle_buttons(abi_nupud, event)
                if result == "Tagasi":
                    tase = "startmenüü"

    pygame.display.update()

pygame.quit()
quit()
