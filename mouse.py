import pygame, sys #mengimport modul pygame dan sys
from pygame import rect
from pygame.locals import *
import time

WIDTH, HEIGHT = 400, 400 #mengatur lebar dan tinggi window
pygame.display.set_caption('Smooth Movement') #mengeset judul window

pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()#membuat objek untuk membantu melacak waktu

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Player:
    def __init__(self, x, y): #membuat fungsi constructor dengan memasukan objek self dan parameter x,y
        self.x = int(x)
        self.y = int(y)
        self.rect = pygame.Rect(self.x, self.y, 32, 32)
        self.color = (250, 120, 60)
        self.velX = 0
        self.velY = 0
        self.left_pressed = False #ketika ditekan tombol kiri posisinya awal/default adalah false
        self.right_pressed = False #ketika ditekan tombol kanan posisinya awal/default adalah false
        self.up_pressed = False #ketika ditekan tombol atas posisinya awal/default adalah false
        self.down_pressed = False  #ketika ditekan tombol bawah posisinya awal/default adalah false
        self.speed = 4 #kecepatan objectnya adalah 4
    
    def draw(self, win): #fungsi untuk menggambar object dari rectangle dengan warna orange serta ukuran layar yang sudah ditentukan
        pygame.draw.rect(win, self.color, self.rect)
    
    def update(self): #fungsi update dari objek self, agar bisa bergerak setiap kita tekan tombol, mengikuti titik koordinat dan kecepatan yang telah ditentukan
        self.velX = 0
        self.velY = 0
        if self.left_pressed and not self.right_pressed:  #agar tidak bablas keluar window diset dengan self.x lebih dari 0 
            self.velX = -self.speed
        if self.right_pressed and not self.left_pressed:
            self.velX = self.speed
        if self.up_pressed and not self.down_pressed:
            self.velY = -self.speed
        if self.down_pressed and not self.up_pressed:
            self.velY = self.speed
        #agar nilai koordinat dan kecepatan terus bertambah seiiring tombol ditekan atau object agar dapat begerak 
        self.x += self.velX
        self.y += self.velY

        self.rect = pygame.Rect(int(self.x), int(self.y), 32, 32)


player = Player(WIDTH/2, HEIGHT/2)
#akan menjalankan jika perulangannya True, dan akan menyusun logic-logic pemrogramannya ketika tombol ditekan maka harus menggerakan kondisi apa
font_color = (255,0,127)
font_obj = pygame.font.Font("C:\Windows\Fonts\RAVIE.TTF",25)
text = "ILHAM HIDAYAT CAH MADIUN"
img = font_obj.render(text, True, (BLACK))

rect = img.get_rect()
rect.topleft = (20,20)
cursor = Rect(rect.topright, (3, rect.height))

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.left_pressed = True
            if event.key == pygame.K_RIGHT:
                player.right_pressed = True
            if event.key == pygame.K_UP:
                player.up_pressed = True
            if event.key == pygame.K_DOWN:
                player.down_pressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.left_pressed = False
            if event.key == pygame.K_RIGHT:
                player.right_pressed = False
            if event.key == pygame.K_UP:
                player.up_pressed = False
            if event.key == pygame.K_DOWN:
                player.down_pressed = False
    


    
            if event.type == QUIT:
                    running = False

            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    if len(text)>0:
                        text = text[:-1]

                else:
                    text += event.unicode
                    img = font_obj.render(text, True, PINK)
                    rect.size = img.get_size()
                    cursor.topleft = rect.topright

    win.fill((GREEN))
    pygame.draw.rect(win, (WHITE), player)

    win.blit(img,rect)
    if time.time() % 1 > 0.5:
        pygame.draw.rect(win, GREEN, cursor)
    pygame.display.update()

    player.update()
    pygame.display.flip()

    clock.tick(120)
    pygame.display.update()
    
pygame.quit()
