import pygame
import numpy

pygame.init()
win=pygame.display.set_mode((500,600))
pygame.display.set_caption("Tic-Tac-Toe")

board=pygame.image.load('board0.jpg')
xPhoto=pygame.image.load('X.png')
OPhoto=pygame.image.load('0.png')
Menu_bg=pygame.image.load('backg.png')
victory_sound=pygame.mixer.Sound('victory.wav')
GameMusic=pygame.mixer.music.load('MusicTTT.mp3')
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)

x_draw=0
music_paused=False
hert=[]
hert0=[]
photo=[]
photo0=[]
xScore=0
oScore=0
Start=0
qanak=0
win_sound=True
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

def print_text(text, Xpos, Ypos, tcolor, fontSize):
    font = pygame.font.Font('freesansbold.ttf', fontSize)
    text_p=font.render(text,True,tcolor)
    textrect=text_p.get_rect()
    textrect.center=(Xpos,Ypos)
    win.blit(text_p,textrect)


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



class Button:
    def __init__(self, width, height, active_color, inactive_color):
        self.width=width
        self.height=height
        self.active_clr=active_color
        self.inactive_clr=inactive_color

    def draw(self, x, y, text, action):
        Click=False
        mPos=pygame.mouse.get_pos()
        for event in ev:
            if event.type == pygame.MOUSEBUTTONUP:
                Click=True
        pygame.draw.rect(win, self.inactive_clr, (x, y, self.width, self.height))
        if x<mPos[0]<x+self.width:
            if y<mPos[1]<y+self.height:
                pygame.draw.rect(win,self.active_clr, (x,y,self.width,self.height))
                if Click:
                     if text=="Exit":
                         action=0;
                     elif text=="One Player":
                        action=1
                     else:
                         action=2
                     pygame.time.delay(100)
        if text!="Exit":
            print_text(text,x+140,y+60, (255,255,255), 30)
        else:
            print_text(text,x+25,y+25,(255,255,255),15)
        return action


def find_empties(hert):
    empty_boxes=[]
    xPos_empty=[]
    yPos_empty=[]
    for i in range(3):
        for j in range(3):
            if hert[i][j]==False:
                xPos_empty.append(i)
                yPos_empty.append(j)
    empty_boxes.append(xPos_empty)
    empty_boxes.append(yPos_empty)
    return empty_boxes

def photo_0to2(hert,photo,xPos,yPos):
    photo[xPos][yPos]=2
    hert[xPos][yPos]=True
    return hert,photo,True



def OX_2_1(hert,photo,x):
    exist=False
    for i in range(3):
        if photo[i][0]==0:
            if photo[i][1]==x and photo[i][2]==x:
                hert,photo,exist=photo_0to2(hert,photo,i,0)
                break
        if photo[i][1]==0:
            if photo[i][0]==x and photo[i][2]==x:
                hert,photo,exist=photo_0to2(hert,photo,i,1)
                break
        if photo[i][2]==0:
            if photo[i][0]==x and photo[i][1]==x:
                hert,photo,exist=photo_0to2(hert,photo,i,2)
                break
        if photo[0][i]==0:
            if photo[1][i]==x and photo[2][i]==x:
                hert,photo,exist=photo_0to2(hert,photo,0,i)
                break;
        if photo[1][i]==0:
            if photo[0][i]==x and photo[2][i]==x:
                hert, photo, exist = photo_0to2(hert, photo, 1, i)
                break;
        if photo[2][i]==0:
            if photo[1][i]==x and photo[0][i]==x:
                hert,photo,exist=photo_0to2(hert,photo,2,i)
                break;
    if not(exist):
        for i in range(3):
            if photo[i][i]==0:
                k=0
                for j in range(3):
                    if photo[j][j]==x:
                        k+=1
                if k==2:
                    hert, photo, exist = photo_0to2(hert, photo, i, i)
                    break;
            if photo[i][2-i]==0:
                k=0
                for j in range(3):
                    if photo[j][2-j]==x:
                        k+=1
                if k==2:
                    hert, photo, exist = photo_0to2(hert, photo, i, 2-i)
                    break;

    return hert,photo,exist

def comp_queue(hert,photo):
    empty_boxes=find_empties(hert)
    if len(empty_boxes[0])>=8:
        if not(hert[1][1]):
            hert,photo,exist=photo_0to2(hert, photo, 1, 1)
        else:
            xPos=(numpy.random.randint(2))*2
            yPos=(numpy.random.randint(2))*2
            hert, photo, exist = photo_0to2(hert, photo, xPos, yPos)

    else:
        hert,photo,exist=OX_2_1(hert,photo,2)
        if not(exist):
            hert, photo, exist = OX_2_1(hert, photo, 1)
            if not(exist):
                k=numpy.random.randint(len(empty_boxes[0]))
                hert[empty_boxes[0][k]][empty_boxes[1][k]]=True
                photo[empty_boxes[0][k]][empty_boxes[1][k]]=2
    return hert,photo


while run:
    pygame.time.delay(25)
    ev=pygame.event.get()
    for event in ev:
        if event.type==pygame.QUIT:
            run=False
    if Start>0:
        exit_button=Button(50,50,(50,50,20),(0,0,0))
        win.blit(board,(0,0))
        qanak=0
        if Start==2 or (Start==1 and tiv%2==0):
            FrameCount=0
            '''click=pygame.mouse.get_pressed()
            if click[0]==1 and wins==False and x_draw>=0:'''
            for event in ev:
                if event.type == pygame.MOUSEBUTTONUP and x_draw>0 and wins==False:
                    pos = pygame.mouse.get_pos()
                    hert,photo,tiv=mouse_click(pos, hert, tiv, photo)
        elif wins==False:
            FrameCount+=1
            if FrameCount>=20:
                hert,photo=comp_queue(hert,photo)
                tiv+=1
        x_draw=1
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
            if win_sound:
                win_sound=False
                pygame.mixer.Sound.play(victory_sound)
                pygame.mixer.music.pause()
                music_paused=True
            for i in range(3):
                for j in range(3):
                    if hert[i][j]==True:
                        tr=False
                        if (margat//15)%2==0:
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
            if margat>=90:
                if xKamO==1:
                    xScore+=1
                else:
                    oScore+=1
                wins=False
                win_sound=True
                hert,photo,tiv=clear(hert,photo,tiv)
                pygame.mixer.music.unpause()
                music_paused = False
                margat=0
        wins,cord,xScore,oScore=Win(photo,xScore,oScore)

        Start=exit_button.draw(446,5,"Exit",Start)

        if (qanak==9 and wins==False) or Start==0:
            win_sound = True
            pygame.time.delay(100)
            hert,photo,tiv=clear(hert,photo,tiv)

        if Start==2:
            print_text("Player1: " + str(xScore), 500//4, 550, (255,255,255), 30)
            print_text("Player2: " + str(oScore), 1500 // 4, 550, (255,255,255), 30)
        else:
            print_text("Player: " + str(xScore), 500 // 4, 550, (255, 255, 255), 30)
            print_text("Mr Koshy: " + str(oScore), 1500 // 4, 550, (255, 255, 255), 30)

    else:
        if music_paused:
            music_paused = False
            pygame.mixer.music.unpause()
        pygame.mixer.Sound.stop(victory_sound)
        wins=False
        x_draw=0
        xScore=0
        oScore=0
        margat=0
        win.blit(Menu_bg,(0,0))
        button=Button(300,120,(0,0,0),(0,255,255))
        Start=button.draw(100, 100, "One Player", Start)
        Start=button.draw(100, 350, "Two Player", Start)
    pygame.display.update()




pygame.quit()