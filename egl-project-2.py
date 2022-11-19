import math
import pygame,sys
from egl import draw

#x-y line coordinates

y_cor = 350
x_cor = 200

def main():
    global win ,w,h,font
    run = True
    
    
    #inputs
    multi = 3
    tl = int(input(' enter the true length :'))*multi
    
    vp_dis = int(input('\n enter the distance from vertical plane:'))*multi
    hp_dis = int(input('\n enter the distrance from horizontal plane:'))*multi
    pi = 22/7

    #input height
    fvh = (int(input('enter the distance above hp :'))*multi)-hp_dis
    tvh = (int(input('enter the distance infront of vp :'))*multi)-vp_dis

    #calculating angles 
    theta = math.asin(fvh/tl)
    phi = math.asin(tvh/tl)
    #new length
    tvl = tl*math.cos(theta)
    fvl = tl*math.cos(phi)
    
    #pygame
    pygame.init()
    w,h = 1000,800
    win = pygame.display.set_mode((w,h))
    pygame.display.set_caption('egl-project')
    font = pygame.font.Font('freesansbold.ttf', 20)
    xyline = pygame.Rect(100,y_cor,w-200,2)
    try:
        #new angles
        gamma = math.asin(fvh/fvl)
        beta = math.asin(tvh/tvl)
        #angle
        x_line_fv = fvl * math.cos(gamma)
        x_line_tv = tvl * math.cos(beta)

        while run:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            draw(win,w,h,font,xyline,fvh,x_line_fv,tvh,x_line_tv,vp_dis,hp_dis,tvl,fvl,gamma,beta,multi)
    except ValueError:
        pygame.quit()
        print('INPUTS ARE INVALID AND ARE NOT POSSIBLE')
        main()
        
        
        

if __name__ == '__main__':
    main()



