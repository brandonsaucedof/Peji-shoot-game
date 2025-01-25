from operator import truediv
from pickle import TRUE
from re import X
from tkinter import Y
import pygame
pygame.font.init()
pygame.init()
#-----------------------------------------------------------
#pantalla
P_ancho = 1000
P_alto = 600
pantalla = (P_ancho , P_alto) 
win = pygame.display.set_mode((pantalla)) 
pygame.display.set_caption("Peji-Shoot") 
clock = pygame.time.Clock()
#-----------------------------------------------------------
#editar
negro = (0, 0, 0) 
blanco = (255, 250, 255)
fps = 120
ancho , alto = 100 , 200
#-----------------------------------------------------------
#editar texto
creditos = "by: ELi, Brandy, Alex"
contador = 1
last_count = pygame.time.get_ticks()
game_over = 0 
display_surface = pygame.display.set_mode((P_ancho, P_alto))
fuente = pygame.font.SysFont("OCR A Extended" , 30)
F_creditos = pygame.font.SysFont("OCR A Extended" , 20)
#-----------------------------------------------------------
#fondo
fondo = pygame.image.load("boliche.jpg")
#-----------------------------------------------------------
#peji quieto
class Player(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y):
		super().__init__()
		self.attack_animation = True
		self.sprites = []
		self.sprites.append(pygame.image.load("jugadorAnimacionEspera1.png"))
		self.sprites.append(pygame.image.load("jugadorAnimacionEspera2.png"))
		self.sprites.append(pygame.image.load("jugadorAnimacionEspera3.png"))
		self.sprites.append(pygame.image.load("jugadorAnimacionEspera4.png"))
		self.sprites.append(pygame.image.load("jugadorAnimacionEspera5.png"))
		self.sprites.append(pygame.image.load("jugadorAnimacionEspera6.png"))
		self.sprites.append(pygame.image.load("jugadorAnimacionEspera7.png"))
		self.current_sprite = 0
		self.image = self.sprites[self.current_sprite]

		self.rect = self.image.get_rect()
		self.rect.topleft = [pos_x,pos_y]

	def attack(self):
		self.attack_animation = True

	def update(self,speed):
		if self.attack_animation == True:
			self.current_sprite += speed
			if int(self.current_sprite) >= len(self.sprites):
				self.current_sprite = 0
				self.attack_animation = True

		self.image = self.sprites[int(self.current_sprite)]
#---------------------------------------------------------------
#peji muerte
class MUERTEPEJI (pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.muerte_animation = True
        self.sprites = []

        self.sprites.append(pygame.image.load("muerteMain1.png"))
        self.sprites.append(pygame.image.load("muerteMain2.png"))
        self.sprites.append(pygame.image.load("muerteMain3.png"))
        self.sprites.append(pygame.image.load("muerteMain4.png"))
        self.sprites.append(pygame.image.load("muerteMain5.png"))
        self.sprites.append(pygame.image.load("muerteMain6.png"))
        self.sprites.append(pygame.image.load("muerteMain7.png"))
        self.sprites.append(pygame.image.load("muerteMain8.png"))
        self.sprites.append(pygame.image.load("muerteMain9.png"))
        self.sprites.append(pygame.image.load("muerteMain10.png"))
        self.sprites.append(pygame.image.load("muerteMain11.png"))
        self.sprites.append(pygame.image.load("muerteMain12.png"))
        self.sprites.append(pygame.image.load("muerteMain13.png"))
        self.sprites.append(pygame.image.load("muerteMain14.png"))
        self.sprites.append(pygame.image.load("muerteMain15.png"))
        self.sprites.append(pygame.image.load("muerteMain16.png"))
        self.sprites.append(pygame.image.load("muerteMain17.png"))
        self.sprites.append(pygame.image.load("muerteMain18.png"))
        self.sprites.append(pygame.image.load("muerteMain19.png"))
        self.sprites.append(pygame.image.load("muerteMain20.png"))
        self.sprites.append(pygame.image.load("muerteMain21.png"))
        self.sprites.append(pygame.image.load("muerteMain22.png"))
        self.sprites.append(pygame.image.load("muerteMain23.png"))
        self.sprites.append(pygame.image.load("muerteMain24.png"))
        self.sprites.append(pygame.image.load("muerteMain25.png"))
        self.sprites.append(pygame.image.load("muerteMain26.png"))
        self.sprites.append(pygame.image.load("muerteMain27.png"))
        self.sprites.append(pygame.image.load("muerteMain28.png")) 
        self.sprites.append(pygame.image.load("muerteMain29.png"))
        self.sprites.append(pygame.image.load("muerteMain30.png"))
        self.sprites.append(pygame.image.load("muerteMain31.png"))
        self.sprites.append(pygame.image.load("muerteMain32.png"))
        self.sprites.append(pygame.image.load("muerteMain33.png"))
        self.sprites.append(pygame.image.load("muerteMain34.png"))
        self.sprites.append(pygame.image.load("muerteMain35.png"))
        self.sprites.append(pygame.image.load("muerteMain36.png"))
        self.sprites.append(pygame.image.load("muerteMain37.png"))
        self.sprites.append(pygame.image.load("muerteMain38.png"))
        self.sprites.append(pygame.image.load("muerteMain39.png")) 
        self.sprites.append(pygame.image.load("muerteMain40.png"))  

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def muerte(self):
        self.muerte_animation = True

    def update(self,speed):
        if self.muerte_animation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.muerte_animation = TRUE
        self.image = self.sprites[int(self.current_sprite)]
#---------------------------------------------------------------
#peji disparo
class Disparo (pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.disparo_animation = False
        self.sprites = []

        self.sprites.append(pygame.image.load("shootAndCapa1.png"))
        self.sprites.append(pygame.image.load("shootAndCapa2.png"))
        self.sprites.append(pygame.image.load("shootAndCapa3.png"))
        self.sprites.append(pygame.image.load("shootAndCapa4.png"))
        self.sprites.append(pygame.image.load("shootAndCapa5.png"))
        self.sprites.append(pygame.image.load("shootAndCapa6.png"))
        self.sprites.append(pygame.image.load("shootAndCapa7.png"))
        self.sprites.append(pygame.image.load("shootAndCapa8.png"))
        self.sprites.append(pygame.image.load("shootAndCapa9.png"))
        self.sprites.append(pygame.image.load("shootAndCapa10.png"))
        self.sprites.append(pygame.image.load("shootAndCapa11.png"))
        self.sprites.append(pygame.image.load("shootAndCapa12.png"))
        self.sprites.append(pygame.image.load("shootAndCapa13.png"))
        self.sprites.append(pygame.image.load("shootAndCapa14.png"))
        self.sprites.append(pygame.image.load("shootAndCapa15.png"))
        self.sprites.append(pygame.image.load("shootAndCapa16.png"))
        self.sprites.append(pygame.image.load("shootAndCapa17.png"))
        self.sprites.append(pygame.image.load("shootAndCapa18.png"))
        self.sprites.append(pygame.image.load("shootAndCapa19.png"))
        self.sprites.append(pygame.image.load("shootAndCapa20.png"))
        self.sprites.append(pygame.image.load("shootAndCapa21.png"))
               
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def disparo(self):
        self.disparo_animation = True

    def update(self,speed):
        if self.disparo_animation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.disparo_animation = False

        self.image = self.sprites[int(self.current_sprite)]
#----------------------------------------------------------
#paco quieto
class Npc(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y):
		super().__init__()
		self.npc_animation = True
		self.sprites = []

		self.sprites.append(pygame.image.load("policiaStand1.png"))
		self.sprites.append(pygame.image.load("policiaStand2.png"))
		self.sprites.append(pygame.image.load("policiaStand3.png"))
		self.sprites.append(pygame.image.load("policiaStand4.png"))
		self.sprites.append(pygame.image.load("policiaStand5.png"))
		self.sprites.append(pygame.image.load("policiaStand6.png"))

		self.current_sprite = 0
		self.image = self.sprites[self.current_sprite]

		self.rect = self.image.get_rect()
		self.rect.topleft = [pos_x,pos_y]

	def npc(self):
		self.npc_animation = True

	def update(self,speed):
		if self.npc_animation == True:
			self.current_sprite += speed
			if int(self.current_sprite) >= len(self.sprites):
				self.current_sprite = 0
				self.npc_animation = True

		self.image = self.sprites[int(self.current_sprite)]
#----------------------------------------------------------
#paco disparo
class Disparo_paco (pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.disparo2_animation = True
        self.sprites = []

        self.sprites.append(pygame.image.load("policiaDisparo1.png"))
        self.sprites.append(pygame.image.load("policiaDisparo2.png"))
        self.sprites.append(pygame.image.load("policiaDisparo3.png"))
        self.sprites.append(pygame.image.load("policiaDisparo4.png"))
        self.sprites.append(pygame.image.load("policiaDisparo5.png"))
        self.sprites.append(pygame.image.load("policiaDisparo6.png"))
        self.sprites.append(pygame.image.load("policiaDisparo7.png"))
        self.sprites.append(pygame.image.load("policiaDisparo8.png"))
        self.sprites.append(pygame.image.load("policiaDisparo9.png"))
        self.sprites.append(pygame.image.load("policiaDisparo10.png"))
        self.sprites.append(pygame.image.load("policiaDisparo11.png"))
        self.sprites.append(pygame.image.load("policiaDisparo12.png"))
        self.sprites.append(pygame.image.load("policiaDisparo13.png"))
        self.sprites.append(pygame.image.load("policiaDisparo14.png"))
        self.sprites.append(pygame.image.load("policiaDisparo15.png"))
        self.sprites.append(pygame.image.load("policiaDisparo16.png"))
        self.sprites.append(pygame.image.load("policiaDisparo17.png"))
        self.sprites.append(pygame.image.load("policiaDisparo18.png"))
        self.sprites.append(pygame.image.load("policiaDisparo19.png"))
        self.sprites.append(pygame.image.load("policiaDisparo20.png"))
        self.sprites.append(pygame.image.load("policiaDisparo21.png"))
        self.sprites.append(pygame.image.load("policiaDisparo22.png"))
        self.sprites.append(pygame.image.load("policiaDisparo23.png"))
        self.sprites.append(pygame.image.load("policiaDisparo24.png"))
        self.sprites.append(pygame.image.load("policiaDisparo25.png"))
        self.sprites.append(pygame.image.load("policiaDisparo26.png"))
        self.sprites.append(pygame.image.load("policiaDisparo27.png"))
        self.sprites.append(pygame.image.load("policiaDisparo28.png")) 

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def disparo2(self):
        self.disparo2_animation = True

    def update(self,speed):
        if self.disparo2_animation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.disparo2_animation = True

        self.image = self.sprites[int(self.current_sprite)]
#----------------------------------------------------------
#paco muerte
class punto(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.muerte1_animation = True
        self.sprites = []
        self.sprites.append(pygame.image.load("rip1.png"))


        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def disparo2(self):
        self.muerte1_animation = True

    def update(self,speed):
        if self.muerte1_animation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.muerte1_animation = True

        self.image = self.sprites[int(self.current_sprite)]       
#----------------------------------------------------------
#dibujar pantalla
def draw_bg():
	win.blit(fondo, [0, 0])

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    win.blit(img, (x, y))
#-----------------------------------------------------------
#sonido
disparo1 = pygame.mixer.Sound("disparo.wav")
disparo3 = pygame.mixer.Sound("disparo2.wav")
ambiente = pygame.mixer.Sound("nashe+.wav")
winner = pygame.mixer.Sound("peji_winner.wav")
fail = pygame.mixer.Sound("peji_fail.wav")
#-----------------------------------------------------------
# Agrupar sprites
pejiquieto = pygame.sprite.Group()
player = Player(100,400)
pejiquieto.add(player)

disparopeji = pygame.sprite.Group()
disparo=Disparo(107,286)
disparopeji.add(disparo)

pacoquieto = pygame.sprite.Group()
npc1=Npc(650,300)
pacoquieto .add(npc1)

disparopaco = pygame.sprite.Group()
disparo2=Disparo_paco(650,300)
disparopaco.add(disparo2)

muertepeji = pygame.sprite.Group()
muertepej=MUERTEPEJI(65,286)
muertepeji.add(muertepej)

muertepaco = pygame.sprite.Group()
muerte1=punto(800,500)
muertepaco.add(muerte1)
#-----------------------------------------------------------
#bucle
Victory=True
muerte = False
bucle = True
ambiente.play(3)
while bucle:
    clock.tick(fps)
    pygame.time.delay(50)
#-----------------------------------------------------------
# Contador    
    draw_bg()

    if contador == 0:
        tiempo = pygame.time.get_ticks()

    if contador < 4:
        draw_text('¡¿Estas listo?!', fuente, blanco, int(P_ancho / 2.15 - 110), int(P_alto / 2 + 5))
        draw_text(str(contador), fuente, blanco, int(P_ancho / 2.019 - 10), int(P_alto / 2 + 50))
        count_timer = pygame.time.get_ticks()
        if count_timer - last_count > 1000:
            contador += 1
            last_count = count_timer

    if contador == 4:
        draw_text('DISPARA!!!!', fuente, blanco, int(P_ancho / 2 - 110), int(P_alto / 2 + 5))

        count_timer = pygame.time.get_ticks()
        if count_timer - last_count > 1000:
            contador += 1
            last_count = count_timer 
        
    if contador >= 4 and muerte==True :
        draw_text('PEJI WINNER !!!!', fuente, blanco, int(P_ancho / 2 - 110), int(P_alto / 2 + 5))
        count_timer = pygame.time.get_ticks()
        if count_timer - last_count > 1000:
            contador += 1
            last_count = count_timer
        disparopeji.draw(win)
        disparopeji.update(0.5)

    if Victory == True:
        count_timer = pygame.time.get_ticks()
        if count_timer - last_count > 1000:
            contador += 1
            last_count = count_timer 
        pacoquieto.draw(win)
        pacoquieto.update(0.5)
        pejiquieto.draw(win)
        pejiquieto.update(0.5)
       
    if muerte == True:
        count_timer = pygame.time.get_ticks()
        if count_timer - last_count > 1000:
            contador += 1
            last_count = count_timer 
        muertepaco.draw(win)
        muertepaco.update(0.5)
                    
    if contador>=4 and contador < 5  :
        Victory=False
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            
            muerte =True   
            disparo.disparo()                                     
            disparo1.play()
            winner.play()

            count_timer = pygame.time.get_ticks() 
            if count_timer - last_count > 1500:
                contador += 1
                last_count = count_timer 
            contador = 7      
        else:
            
            Victory=False
            muerte = False
            
    if contador == 5 and Victory == False:
        disparo3.play()
        fail.play()
        
        count_timer = pygame.time.get_ticks()
        if count_timer - last_count > 1500:
            contador += 1
            last_count = count_timer
        disparopaco.draw(win)
        disparopaco.update(1)
        muertepeji.draw(win)
        muertepeji.update(1) 

    if contador == 5:
        draw_text('PEJI FAIL !!!!', fuente, blanco, int(P_ancho / 2 - 110), int(P_alto / 2 + 5))
        count_timer = pygame.time.get_ticks()
        if count_timer - last_count > 10000:
            contador += 1
            last_count = count_timer



#-----------------------------------------------------------
#dibujar
    image = pygame.Surface((ancho,alto))    
    pygame.display.flip()
#-----------------------------------------------------------
#continuar bucle
    credit = F_creditos.render((creditos) , 1 , (blanco))
    win.blit(credit, (730, 28))

    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT:    
            quit()
    pygame.display.update()
pygame.quit()    