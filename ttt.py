import pygame
import numpy

pygame.init()
win=pygame.display.set_mode((500,600))
pygame.display.set_caption("Tic-Tac-Toe")

board=pygame.image.load('board0.jpg')
xPhoto=pygame.image.load('X.jpg')
OPhoto=pygame.image.load('0.jpg')


hert=[]
hert0=[]
photo=[]
photo0=[]
xScore=0
oScore=0
for _ in range(3):
    hert0.append(False)
    photo0.append(0)
for _ in range(3):
    hert.append(hert0)
    photo.append(photo0)

tiv=0
wins=False
margat=0
xKamO=0
hert=numpy.array(hert)
photo=numpy.array(photo)
run=True
def Win(photo, xScore, oScore):
    wining=False
    cord=[]
    for i in range(3):
        if photo[i][1]==photo[i][2] and photo[i][1]==photo[i][0] and photo[i][1]!=0:
            wining=True
            xKamO=photo[i][1]
            cord=numpy.array([[i,0],[i,1],[i,2]])
        if photo[2][i]==photo[1][i] and photo[2][i]==photo[0][i] and photo[1][i]!=0:
            cord=numpy.array([[0,i],[1,i],[2,i]])
            xKamO = photo[1][i]
            wining=True

    if photo[1][1]==photo[2][2] and photo[1][1]==photo[0][0] and photo[1][1]>0:
        wining = True
        xKamO = photo[1][1]
        cord=numpy.array([[0,0],[1,1],[2,2]])
    if photo[2][0] ==photo[1][1] and photo[1][1] == photo[0][2] and photo[1][1] > 0:
        cord = numpy.array([[0, 2], [1, 1], [2, 0]])
        xKamO = photo[1][1]
        wining = True
    return wining,cord,xScore,oScore

def clear(hert,photo,tiv):
    for i in range(3):
        for j in range(3):
            hert[i][j] = False
            photo[i][j] = 0
    tiv = 0
    return hert,photo,tiv

def print_text(text, Xpos, Ypos):
    textrect=text.get_rect()
    textrect.center=(Xpos,Ypos)
    win.blit(text,textrect)


def mouse_click(pos, hert, tiv, photo):
    if pos[0] >= 0 and pos[0] < 167:
        xPos = 0
    elif pos[0] >= 167 and pos[0] < 334:
        xPos = 1
    elif pos[0] >= 334 and pos[0] <= 500:
        xPos = 2
    if pos[1]>=0 and pos[1]<167:
        yPos=0
    elif pos[1]>=167 and pos[1]<334:
        yPos=1
    elif pos[1]>=334 and pos[1]<=500:
        yPos=2
    else:
        yPos=3
    if yPos<3:
        if hert[xPos][yPos]==False:
            hert[xPos][yPos]=True
            tiv+=1
            if tiv%2==1:
                photo[xPos][yPos]=1
            else:
                photo[xPos][yPos]=2
    return hert,photo,tiv

qanak=0
while run:
    win.blit(board,(0,0))
    qanak=0
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type == pygame.MOUSEBUTTONUP and wins==False:
            pos = pygame.mouse.get_pos()
            hert,photo,tiv=mouse_click(pos, hert, tiv, photo)
    if not(wins):
        for i in range(3):
            for j in range(3):
                if hert[i][j]==True:
                    qanak+=1
                    if photo[i][j]==1:
                        win.blit(xPhoto,(5+167*i,5+167*j))
                    elif photo[i][j]==2:
                        win.blit(OPhoto,(5+167*i,5+167*j))
    else:
        for i in range(3):
            for j in range(3):
                if hert[i][j]==True:
                    tr=False
                    if margat%2==0:
                        for var in range(3):
                            if i==cord[var][0] and j==cord[var][1]:
                                xKamO=photo[i][j]
                                tr=True
                    if not(tr):
                        if photo[i][j] == 1:
                            win.blit(xPhoto, (5 + 167 * i, 5 + 167 * j))
                        elif photo[i][j] == 2:
                            win.blit(OPhoto, (5 + 167 * i, 5 + 167 * j))
        margat+=1
        pygame.time.delay(200)
        if margat>=6:
            if xKamO==1:
                xScore+=1
            else:
                oScore+=1
            wins=False
            hert,photo,tiv=clear(hert,photo,tiv)
            margat=0
    pygame.time.delay(33)
    wins,cord,xScore,oScore=Win(photo,xScore,oScore)
    if qanak==9 and wins==False:
        hert,photo,tiv=clear(hert,photo,tiv)

    font = pygame.font.Font('freesansbold.ttf', 30)
    text = font.render("Player1: " + str(xScore),True,(255,255,255))
    print_text(text, 500//4, 550)
    text = font.render("Player2: " + str(oScore),True,(255,255,255))
    print_text(text, 1500 // 4, 550)
    pygame.display.update()




pygame.quit()