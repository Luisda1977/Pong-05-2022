from ssl import ALERT_DESCRIPTION_BAD_CERTIFICATE_HASH_VALUE
import pygame

ANCHO_PALETA = 5
ALTO_PALETA = 40

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
            print("Muevete arriba")
        else:
            print("Muevete abajo") 

"""
-el movimiento es cosa de la paleta
-aumentar o disminuir el valor del eje y posición de la paleta
-quien tiene que capturar el evento de pulsar la tecla es el cucle principal
redibujar la paleta

"""

class Pong:

    _ALTO = 400
    _ANCHO = 640
    _MARGEN_LATERAL = 40



    def __init__(self):
        print("Construyendo un objeto pong")
        pygame.init()
        self.pantalla = pygame.display.set_mode((self._ANCHO, self._ALTO))

        self.jugador1 = Paleta(
            self._MARGEN_LATERAL,                     #coordenada x (left)
            (self._ALTO-ALTO_PALETA)/2)         #coordenada y (top)   
            

        self.jugador2 = Paleta(
            self._ANCHO-self._MARGEN_LATERAL-ANCHO_PALETA,
            (self._ALTO-ALTO_PALETA)/2)
        

        

    def bucle_principal(self):
        print("Estoy en el bucle principal")
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        salir = True
                    elif evento.key == pygame.K_a:
                        self.jugador1.muevete(Paleta.ARRIBA)
                    elif evento.key == pygame.K_z:
                        self.jugador1.muevete(Paleta.ABAJO)
                    elif evento.key == pygame.K_k:
                        self.jugador2.muevete(Paleta.ARRIBA)
                    elif evento.key == pygame.K_m:
                        self.jugador1.muevete(Paleta.ABAJO)


                if evento.type == pygame.QUIT:
                    return

            # for position in range(0, self._ALTO, 40):     #linea discontinua
                # color = (255, 255, 255)        
                # pygame.draw.line(self.pantalla, color, (self._ANCHO/2, position), (self._ANCHO/2, position +10))
            pygame.draw.line(self.pantalla, (255, 0, 0), (self._ANCHO/2, 0), (self._ANCHO/2, self._ALTO))        
            pygame.draw.rect(self.pantalla, (0, 255, 0), self.jugador1)
            pygame.draw.rect(self.pantalla, (0, 0, 255), self.jugador2)
            pygame.display.flip()

if __name__ == "__main__":
    juego = Pong()
    juego.bucle_principal()