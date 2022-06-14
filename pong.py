from random import randint

import pygame

ANCHO_PALETA = 5
ALTO_PALETA = 40

ALTO = 400
ANCHO = 640
MARGEN_LATERAL = 40

TAMANYO_PELOTA = 6
VELO_MAX_PELOTA = 5

PUNTOS_PARTIDA = 3

"""
 -algo de herencia:

 -color, ancho, alto
 -hay cosas fijas como el color y el tamaño

 -metodo de chocar: límite para no salirse de la pantalla
 -metodo moverse: solo hacia arriba y hacia abajo

 -método para interactuar con la pelota
"""

class Paleta(pygame.Rect):

    ARRIBA = True
    ABAJO = False

    def __init__(self, x, y):
        super(Paleta, self).__init__(x, y, ANCHO_PALETA, ALTO_PALETA)
        self.velocidad = 5

    def muevete(self, direccion):
        if direccion == self.ARRIBA:
            self.y = self.y - self.velocidad
            if self.y < 0:
                self.y = 0
        else:
            self.y = self.y + self.velocidad
            if self.y > ALTO - ALTO_PALETA:
                self.y = ALTO - ALTO_PALETA 

class Pelota(pygame.Rect):
    def __init__(self):
        super(Pelota, self). __init__(
            (ANCHO-TAMANYO_PELOTA)/2, (ALTO-TAMANYO_PELOTA)/2, 
            TAMANYO_PELOTA, TAMANYO_PELOTA
            )
        
        self.velocidad_x = 0
        while self.velocidad_x == 0:
            self.velocidad_x = randint(-VELO_MAX_PELOTA, VELO_MAX_PELOTA)
        self.velocidad_y = randint(-VELO_MAX_PELOTA, VELO_MAX_PELOTA)

    def muevete(self):
        self.y = self.y + self.velocidad_y
        self.x = self.x + self.velocidad_x
        if self.y < 0:
            self.y = 0
            self.velocidad_y = -self.velocidad_y
        if self.y > ALTO - TAMANYO_PELOTA:
            self.y = ALTO - TAMANYO_PELOTA
            self.velocidad_y = -self.velocidad_y

    

class Marcador:
    """
    -¿qué?  guardar números, pintar
    -¿dónde? ------
    -¿cómo?  ------
    -¿cuándo? la pelota sale del campo
    """
    def __init__(self):
        self.inicializar()

    def comprobar_ganador(self):
        if self.partida_finalizada:
            return True
        if self.valor[0] == PUNTOS_PARTIDA:
            print("Ha ganado el jugador 1")
            self.partida_finalizada = True
        elif self.valor[1] == PUNTOS_PARTIDA:
            print("Ha ganado el jugador 2")
            self.partida_finalizada = True
        return self.partida_finalizada

    def inicializar(self):
        self.valor = [0, 0]
        self.partida_finalizada = False
"""
-el movimiento es cosa de la paleta
-aumentar o disminuir el valor del eje y posición de la paleta
-quien tiene que capturar el evento de pulsar la tecla es el cucle principal
-redibujar la paleta
"""

class Pong:
    
    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        self.clock = pygame.time.Clock()

        self.jugador1 = Paleta(
            MARGEN_LATERAL,               #coordenada x (left)
            (ALTO-ALTO_PALETA)/2)         #coordenada y (top)   
            

        self.jugador2 = Paleta(
            ANCHO-MARGEN_LATERAL-ANCHO_PALETA,
            (ALTO-ALTO_PALETA)/2)

        self.pelota = Pelota ()
        

    def bucle_principal(self):
        salir = False
        while not salir:
            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        print("Adiós, te has escapado")
                        salir = True                    
                if evento.type == pygame.QUIT:
                    salir = True
            
            estado_teclas = pygame.key.get_pressed()
            if estado_teclas[pygame.K_a]:
                self.jugador1.muevete(Paleta.ARRIBA)
            if estado_teclas[pygame.K_z]:
                 self.jugador1.muevete(Paleta.ABAJO)
            if estado_teclas[pygame.K_k]:
                self.jugador2.muevete(Paleta.ARRIBA)
            if estado_teclas[pygame.K_m]:
                self.jugador2.muevete(Paleta.ABAJO)
            self.pelota.muevete()

            self.colision_paletas()

            self.comprobar_punto()

            self.pantalla.fill((0, 0, 0))

            # for position in range(0, self._ALTO, 40):     #linea discontinua
                # color = (255, 255, 255)        
                # pygame.draw.line(self.pantalla, color, (self._ANCHO/2, position), (self._ANCHO/2, position +10))
               
            pygame.draw.line(self.pantalla, (255, 255, 255), (ANCHO/2, 0), (ANCHO/2, ALTO))        
            pygame.draw.rect(self.pantalla, (255, 255, 255), self.jugador1)
            pygame.draw.rect(self.pantalla, (255, 255, 255), self.jugador2)
            pygame.draw.rect(self.pantalla, (255, 255, 255), self.pelota)

            #refresco de pantalla
            pygame.display.flip()
            self.clock.tick(60)

    def colision_paletas(self):
        """
        -Comprueba si la pelota ha colisionado con la paleta.
        y le cambia la dirección. (pygame.Rect.colliderect(Rect))
        """
        if self.pelota.colliderect(self.jugador1) or self.pelota.colliderect(self.jugador2):
            #self.pelota.velocidad_x = -self.pelota.velocidad_x + randint (-VELO_MAX_PELOTA//2, VELO_MAX_PELOTA//2)
            #if self.pelota.velocidad_x > VELO_MAX_PELOTA:
            self.pelota.velocidad_x = self.pelota.velocidad_x
            self.pelota.velocidad_y = randint(-VELO_MAX_PELOTA, VELO_MAX_PELOTA)


    def comprobar_punto(self,marcador):
        if self.x < 0:
            self.marcador.valor[1] = self.marcador.valor[1]+1
            print(f"El nuevo marcador es {self.marcador.valor}")
            self.pelota.velocidad_x = randint(-VELO_MAX_PELOTA, -1)
            self.iniciar_punto()
        elif self.x > ANCHO:
            self.marcador.valor[1] = self.marcador.valor[1]+1
            print(f"El nuevo marcador es {self.marcador.valor}")
            self.pelota.velocidad_x = randint(1, -VELO_MAX_PELOTA)
            self.iniciar_punto()

    def iniciar_punto(self):
        self.pelota.x = (ANCHO - TAMANYO_PELOTA)/2
        self.pelota.y = (ALTO - TAMANYO_PELOTA)/2
        self.pelota.velocidad_y = randint(-VELO_MAX_PELOTA, VELO_MAX_PELOTA)


if __name__ == "__main__":
    juego = Pong()
    juego.bucle_principal()