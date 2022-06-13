import pygame

"""
 -algo de herencia:

 -color, ancho, alto
 -hay cosas fijas como el color y el tamaño

 -metodo de chocar: límite para no salirse de la pantalla
 -metodo moverse: solo hacia arriba y hacia abajo

 -método para interactuar con la pelota
"""

class Paleta(pygame.Rect):
    pass    

class Pong:

    _ALTO = 400
    _ANCHO = 640
    _MARGEN_LATERAL = 40

    _ANCHO_PALETA = 10
    _ALTO_PALETA = 40

    def __init__(self):
        print("Construyendo un objeto pong")
        pygame.init()
        self.pantalla = pygame.display.set_mode((self._ANCHO, self._ALTO))

        self.jugador1 = Paleta(
            self._MARGEN_LATERAL,                     #coordenada x (left)
            (self._ALTO-self._ALTO_PALETA)/2,         #coordenada y (top)   
            self._ANCHO_PALETA,                       #ancho (width)
            self._ALTO_PALETA)                        #alto (height)

        self.jugador2 = Paleta(
            self._ANCHO-self._MARGEN_LATERAL-self._ANCHO_PALETA,
            (self._ALTO-self._ALTO_PALETA)/2,
            self._ANCHO_PALETA,
            self._ALTO_PALETA)

        

    def bucle_principal(self):
        print("Estoy en el bucle principal")
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        return
                if evento.type == pygame.QUIT:
                    return

            for position in range(0, self._ALTO, 40):
                color = (255, 255, 255)        
                pygame.draw.line(self.pantalla, color, (self._ANCHO/2, position), (self._ANCHO/2, position +10))
                # pygame.draw.line(self.pantalla, (255, 0, 0), (self._ANCHO/2, 0), (self._ANCHO/2, self._ALTO))        
            pygame.draw.rect(self.pantalla, (0, 255, 0), self.jugador1)
            pygame.draw.rect(self.pantalla, (0, 0, 255), self.jugador2)
            pygame.display.flip()

if __name__ == "__main__":
    juego = Pong()
    juego.bucle_principal()