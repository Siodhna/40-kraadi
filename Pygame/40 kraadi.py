import pygame
from random import randint

must = (0, 0, 0)
helemust = (56, 56, 56)
valge = (255, 255, 255)
hall = (105, 105, 105)
helehall = (199, 199, 199)

taustavärv = (255, 250, 191)
kaardivärv = (230, 209, 142)
nupukollane_a = (196, 162, 100)
nupukollane_b = (173, 143, 87)

sin = (237, 140, 140)
roh = (140, 125, 184)
pun = (98, 171, 181)
kol = (199, 217, 163)
ora = (107, 140, 121)
roo = (204, 172, 126)

tegevustelist1 = []
tegevustelist2 = []
tegevused = open("tegevused.txt")
for a in tegevused:
    tegevustelist1 += [a.strip()]

pygame.init()

font = pygame.font.SysFont("Broadway", 110)
font2 = pygame.font.SysFont("DejaVu Sans", 40)
fontnimed = pygame.font.SysFont("Broadway", 25)
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
    elif size == "fontnimed":
        textSurface = fontnimed.render(text, True, color)
    elif size == "font2":
        textSurface = font2.render(text, True, color)
    elif size == "font4":
        textSurface = font4.render(text, True, color)
    elif size == "nupufont":
        textSurface = fontbutton.render(text, True, color)
    elif size == "fonttegevus":
        textSurface = fonttegevus.render(text, True, color)
    return textSurface, textSurface.get_rect()

laius = 1200
kõrgus = 600
nupu_laius = 100
nupu_kõrgus = 40
numbrinupu_laius = 50
numbrinupu_kõrgus = 40
nupuvärv_a = nupukollane_a
nupuvärv_b = nupukollane_b
nuputekstivärv = must
punktid = 0
kord = 1
näita_punkte = False

Screen = pygame.display.set_mode((laius, kõrgus))  # teeb akna
pygame.display.set_caption("40 kraadi")  # aknale pealkiri

# nuppude loomine
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
start_nupud = [nupp((540, 300, nupu_laius, nupu_kõrgus), nupuvärv_a, nupuvärv_b, "Alusta", "Alusta"),
               nupp((540, 350, nupu_laius, nupu_kõrgus), nupuvärv_a, nupuvärv_b, "Abi", "Abi"),
               nupp((540, 400, nupu_laius, nupu_kõrgus), nupuvärv_a, nupuvärv_b, "Välju", "Välju")]

abi_nupud = [nupp((540, 470, nupu_laius, nupu_kõrgus), nupuvärv_a, nupuvärv_b, "Tagasi", "Tagasi")]

mängijate_arv_nupud = [nupp((575, 250, numbrinupu_laius, numbrinupu_kõrgus), nupuvärv_a, nupuvärv_b, "2", "2_mängijat"),
                       nupp((575, 300, numbrinupu_laius, numbrinupu_kõrgus), nupuvärv_a, nupuvärv_b, "3", "3_mängijat"),
                       nupp((575, 350, numbrinupu_laius, numbrinupu_kõrgus), nupuvärv_a, nupuvärv_b, "4", "4_mängijat"),
                       nupp((575, 400, numbrinupu_laius, numbrinupu_kõrgus), nupuvärv_a, nupuvärv_b, "5", "5_mängijat"),
                       nupp((575, 450, numbrinupu_laius, numbrinupu_kõrgus), nupuvärv_a, nupuvärv_b, "6", "6_mängijat")]

tõmbakaartnupp = [nupp((810, 280, nupu_laius + 80, nupu_kõrgus), nupuvärv_a, nupuvärv_b, "Tõmba kaart", "tõmbakaart")]

kaardinupud = [nupp((830, 250, nupu_laius + 40, nupu_kõrgus), nupuvärv_a, nupuvärv_b, "Tehtud!", "tehtud"),
               nupp((830, 450, nupu_laius + 40, nupu_kõrgus), nupuvärv_a, nupuvärv_b, "Rüübatud!", "jõin")]

tagasinupp = [nupp((1100, 510, nupu_laius + 20, nupu_kõrgus), nupuvärv_a, nupuvärv_b, "Menüü", "menüü")]


def pilt(pildinimi, x, y):
    Screen.blit(pildinimi, (x, y))


def tekst(sõnum, font, värv, x, y):
    teksti_pilt = font.render(sõnum, False, värv)
    Screen.blit(teksti_pilt, (x, y))

# mängijate loomine
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

            elif tase == "mängijate_arv":
                result = handle_buttons(mängijate_arv_nupud, event)
                if result == "2_mängijat":
                    mängijatearv = 2
                    tase = "tõmba_kaart"
                    näita_punkte = True
                elif result == "3_mängijat":
                    mängijatearv = 3
                    tase = "tõmba_kaart"
                    näita_punkte = True
                elif result == "4_mängijat":
                    mängijatearv = 4
                    tase = "tõmba_kaart"
                    näita_punkte = True
                elif result == "5_mängijat":
                    mängijatearv = 5
                    tase = "tõmba_kaart"
                    näita_punkte = True
                elif result == "6_mängijat":
                    mängijatearv = 6
                    tase = "tõmba_kaart"
                    näita_punkte = True

            elif tase == "tõmba_kaart":
                result = handle_buttons(tõmbakaartnupp, event)
                if result == "tõmbakaart":
                    b = tegevustelist1[randint(0, (len(tegevustelist1) - 1))]
                    tegevustelist1.remove(b)
                    tegevustelist2 += [b]
                    if len(tegevustelist1) == 0:
                        tegevustelist1 = tegevustelist2
                        tegevustelist2 = []
                    pesukaru = b
                    tase = "kaart"

            elif tase == "kaart":
                result = handle_buttons(kaardinupud, event)
                if result == "tehtud":
                    tase = "arvuta_punktid"
                elif result == "jõin":
                    tase = "arvuta_punktid"

    # AJU

    if tase == "arvuta_punktid":
        if result == "tehtud":
            if kord == 1:
                mängija1.lisa_punkte(randint(3, 7))
                kord = 2
                tase = "tõmba_kaart"
            elif kord == 2:
                mängija2.lisa_punkte(randint(3, 7))
                if mängijatearv == 2:
                    kord = 1
                else:
                    kord = 3
                tase = "tõmba_kaart"
            elif kord == 3:
                mängija3.lisa_punkte(randint(3, 7))
                if mängijatearv == 3:
                    kord = 1
                else:
                    kord = 4
                tase = "tõmba_kaart"
            elif kord == 4:
                mängija4.lisa_punkte(randint(3, 7))
                if mängijatearv == 4:
                    kord = 1
                else:
                    kord = 5
                tase = "tõmba_kaart"
            elif kord == 5:
                mängija5.lisa_punkte(randint(3, 7))
                if mängijatearv == 5:
                    kord = 1
                else:
                    kord = 6
                tase = "tõmba_kaart"
            elif kord == 6:
                mängija6.lisa_punkte(randint(3, 7))
                kord = 1
                tase = "tõmba_kaart"

        elif result == "jõin":
            if kord == 1:
                mängija1.lisa_punkte(randint(2, 5))
                kord = 2
                tase = "tõmba_kaart"
            elif kord == 2:
                mängija2.lisa_punkte(randint(2, 5))
                if mängijatearv == 2:
                    kord = 1
                else:
                    kord = 3
                tase = "tõmba_kaart"
            elif kord == 3:
                mängija3.lisa_punkte(randint(2, 5))
                if mängijatearv == 3:
                    kord = 1
                else:
                    kord = 4
                tase = "tõmba_kaart"
            elif kord == 4:
                mängija4.lisa_punkte(randint(2, 5))
                if mängijatearv == 4:
                    kord = 1
                else:
                    kord = 5
                tase = "tõmba_kaart"
            elif kord == 5:
                mängija5.lisa_punkte(randint(2, 5))
                if mängijatearv == 5:
                    kord = 1
                else:
                    kord = 6
                tase = "tõmba_kaart"
            elif kord == 6:
                mängija6.lisa_punkte(randint(2, 5))
                kord = 1
                tase = "tõmba_kaart"

    # KEHA

    if tase == "startmenüü":
        Screen.fill(taustavärv)
        draw_buttons(start_nupud)
        tekst("40 kraadi", font, must, 280, 100)

    elif tase == "abi":
        Screen.fill(taustavärv)
        draw_buttons(abi_nupud)
        tekst("Juhised mänguks:", font, must, 120, 100)
        tekst("Joo end täis.", font2, must, 300, 250)
        tekst("Ürita ellu jääda.", font2, must, 300, 300)

    elif tase == "mängijate_arv":
        Screen.fill(taustavärv)
        tekst("Vali mängijate arv", font2, must, 410, 100)
        draw_buttons(mängijate_arv_nupud)

    elif tase == "tõmba_kaart":
        Screen.fill(taustavärv)
        draw_buttons(tõmbakaartnupp)
        if kord == 1:
            tekst((mängija1.nimi + ", sinu kord!"), font4, must, 750, 30)
        elif kord == 2:
            tekst((mängija2.nimi + ", sinu kord!"), font4, must, 750, 30)
        elif kord == 3:
            tekst((mängija3.nimi + ", sinu kord!"), font4, must, 750, 30)
        elif kord == 4:
            tekst((mängija4.nimi + ", sinu kord!"), font4, must, 750, 30)
        elif kord == 5:
            tekst((mängija5.nimi + ", sinu kord!"), font4, must, 750, 30)
        elif kord == 6:
            tekst((mängija6.nimi + ", sinu kord!"), font4, must, 750, 30)

    if näita_punkte == True:
        if mängijatearv == 2:
            tekst((mängija1.nimi + ":"), font4, must, 100, 135)
            tekst((mängija2.nimi + ":"), font4, must, 100, 435)
            pygame.draw.circle(Screen, mängija1.värv, (300, 150), 50, 0)
            pygame.draw.circle(Screen, mängija2.värv, (300, 450), 50, 0)
            tekst(str(mängija1.punktid), font4, must, 285, 135)
            tekst(str(mängija2.punktid), font4, must, 285, 435)

        elif mängijatearv == 3:
            tekst((mängija1.nimi + ":"), font4, must, 100, 85)
            tekst((mängija2.nimi + ":"), font4, must, 100, 285)
            tekst((mängija3.nimi + ":"), font4, must, 100, 485)
            pygame.draw.circle(Screen, mängija1.värv, (300, 100), 50, 0)
            pygame.draw.circle(Screen, mängija2.värv, (300, 300), 50, 0)
            pygame.draw.circle(Screen, mängija3.värv, (300, 500), 50, 0)
            tekst(str(mängija1.punktid), font4, must, 285, 85)
            tekst(str(mängija2.punktid), font4, must, 285, 285)
            tekst(str(mängija3.punktid), font4, must, 285, 485)

        elif mängijatearv == 4:
            tekst((mängija1.nimi + ":"), font4, must, 80, 135)
            tekst((mängija2.nimi + ":"), font4, must, 80, 435)
            tekst((mängija3.nimi + ":"), font4, must, 330, 135)
            tekst((mängija4.nimi + ":"), font4, must, 350, 435)
            pygame.draw.circle(Screen, mängija1.värv, (250, 150), 50, 0)
            pygame.draw.circle(Screen, mängija2.värv, (250, 450), 50, 0)
            pygame.draw.circle(Screen, mängija3.värv, (500, 150), 50, 0)
            pygame.draw.circle(Screen, mängija4.värv, (500, 450), 50, 0)
            tekst(str(mängija1.punktid), font4, must, 235, 135)
            tekst(str(mängija2.punktid), font4, must, 235, 435)
            tekst(str(mängija3.punktid), font4, must, 485, 135)
            tekst(str(mängija4.punktid), font4, must, 485, 435)

        elif mängijatearv == 5:
            tekst((mängija1.nimi + ":"), font4, must, 80, 135)
            tekst((mängija2.nimi + ":"), font4, must, 80, 435)
            tekst((mängija3.nimi + ":"), font4, must, 330, 135)
            tekst((mängija4.nimi + ":"), font4, must, 260, 285)
            tekst((mängija5.nimi + ":"), font4, must, 350, 435)
            pygame.draw.circle(Screen, mängija1.värv, (250, 150), 50, 0)
            pygame.draw.circle(Screen, mängija2.värv, (250, 450), 50, 0)
            pygame.draw.circle(Screen, mängija3.värv, (500, 150), 50, 0)
            pygame.draw.circle(Screen, mängija4.värv, (375, 300), 50, 0)
            pygame.draw.circle(Screen, mängija5.värv, (500, 450), 50, 0)
            tekst(str(mängija1.punktid), font4, must, 235, 135)
            tekst(str(mängija2.punktid), font4, must, 235, 435)
            tekst(str(mängija3.punktid), font4, must, 485, 135)
            tekst(str(mängija4.punktid), font4, must, 360, 285)
            tekst(str(mängija5.punktid), font4, must, 485, 435)

        elif mängijatearv == 6:
            tekst((mängija1.nimi + ":"), font4, must, 80, 135)
            tekst((mängija2.nimi + ":"), font4, must, 80, 285)
            tekst((mängija3.nimi + ":"), font4, must, 80, 435)
            tekst((mängija4.nimi + ":"), font4, must, 370, 135)
            tekst((mängija5.nimi + ":"), font4, must, 350, 285)
            tekst((mängija6.nimi + ":"), font4, must, 350, 435)
            pygame.draw.circle(Screen, mängija1.värv, (250, 150), 50, 0)
            pygame.draw.circle(Screen, mängija2.värv, (250, 300), 50, 0)
            pygame.draw.circle(Screen, mängija3.värv, (250, 450), 50, 0)
            pygame.draw.circle(Screen, mängija4.värv, (500, 150), 50, 0)
            pygame.draw.circle(Screen, mängija5.värv, (500, 300), 50, 0)
            pygame.draw.circle(Screen, mängija6.värv, (500, 450), 50, 0)
            tekst(str(mängija1.punktid), font4, must, 235, 135)
            tekst(str(mängija2.punktid), font4, must, 235, 285)
            tekst(str(mängija3.punktid), font4, must, 235, 435)
            tekst(str(mängija4.punktid), font4, must, 485, 135)
            tekst(str(mängija5.punktid), font4, must, 485, 285)
            tekst(str(mängija6.punktid), font4, must, 485, 435)

    if mängija1.punktid >= 10:
        võitja = mängija1.nimi
        tase = "mängläbi"

    if mängija2.punktid >= 10:
        võitja = mängija2.nimi
        tase = "mängläbi"

    if mängija3.punktid >= 50:
        võitja = mängija3.nimi
        tase = "mängläbi"

    if mängija4.punktid >= 50:
        võitja = mängija4.nimi
        tase = "mängläbi"

    if mängija5.punktid >= 50:
        võitja = mängija5.nimi
        tase = "mängläbi"

    if mängija6.punktid >= 50:
        võitja = mängija6.nimi
        tase = "mängläbi"

    if tase == "mängläbi":
        Screen.fill(taustavärv)
        tekst(("Mäng läbi! Võitis " + võitja + "."), font4, must, 400, 100)

    pygame.display.update()

pygame.quit()
quit()
