import pygame as pg

#inicia o pygame e seta a janela com sua resolução
pg.init()
window = pg.display.set_mode(size=(640, 480))

#mantém a janela aberta
while True:
    # checa todos os eventos
    for event in pg.event.get():
        if event == pg.QUIT:
            pg.quit() #fecha a janela
            quit() #fecha o pygame