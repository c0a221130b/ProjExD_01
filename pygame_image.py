import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img1 = pg.image.load("ex01/fig/pg_bg.jpg") #練習1 背景画像surfaceの生成
    bg_img2 = pg.image.load("ex01/fig/pg_bg.jpg")#演習2 画像生成
    bg_img2 = pg.transform.flip(bg_img2, True, False)#演習２ 画像反転
    tmr = 0
    
    '''練習2'''
    kk_img = pg.image.load("ex01/fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    
    '''練習3&演習1'''
    kk_imgs_ori = [pg.transform.rotozoom(kk_img, i, 1.0) for i in range(1, 11)]
    kk_imgs = kk_imgs_ori
    for i in range(len(kk_imgs_ori)-1, -1, -1):
        kk_imgs.append(kk_imgs_ori[i])
    
    print(len(kk_imgs))
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
            
        '''練習6'''
        x = tmr%3200
        #print(-x, 1600-x, 3200-x)
        screen.blit(bg_img1, [-x, 0])
        screen.blit(bg_img2, [1600-x, 0])
        screen.blit(bg_img1, [3200-x, 0])#練習4 背景画像の表示
        
        '''練習5 こうかとん羽ばたく'''
        screen.blit(kk_imgs[tmr%20], [300, 200])
        
        pg.display.update()
        tmr += 1        
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()