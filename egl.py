import math
import pygame,sys

#x-y line coordinates

y_cor = 350
x_cor = 200
def draw(win,w,h,font,xyline,fvh,x_line_fv,tvh,x_line_tv,vp_dis,hp_dis,tvl,fvl,gamma,beta,multi):
    #themes
    white = (255,255,255)
    black = (0,0,0)
    blue = (0,0,255)
    green=(0,255,0)
    red = (255,0,0)
    fvy_start = y_cor-hp_dis
    tvy_start = y_cor+vp_dis

    win.fill(white)
    
    pygame.draw.rect(win,black,xyline)
    
#values
    theta_text = font.render(f'gamma = {round(gamma*(180/3.143),1)} degree',1,black)
    text_rect = pygame.Rect(w-300,0,100,100)
    
    phi_text = font.render(f'beta = {round(beta*(180/3.143),1)} degree',1,black)
    text_rect2 = pygame.Rect(w-300,25,100,100)

    fvl_text = font.render(f'fvl = {round(fvl/multi,1)}',1,black)
    text_rect3 = pygame.Rect(w-300,50,100,100)

    tvl_text = font.render(f'tvl = {round(tvl/multi,1)}',1,black)
    text_rect4 = pygame.Rect(w-300,75,100,100)

    #front-view-tl
    pygame.draw.line(win,black,(x_cor,fvy_start),(x_cor+tvl , fvy_start-fvh),4)
    #top-view-tl
    pygame.draw.line(win,black,(x_cor,tvy_start),(x_cor+fvl , tvy_start+tvh),4)
    #tl projections
    pygame.draw.line(win,red,(x_cor+tvl , 0),(x_cor+tvl , h),1)
    pygame.draw.line(win,red,(x_cor+fvl , 0),(x_cor+fvl , h),1)


    #front-view
    pygame.draw.line(win,black,(x_cor,fvy_start),(x_cor+x_line_fv , fvy_start-fvh),4)
    #top-view
    pygame.draw.line(win,black,(x_cor,tvy_start),(x_cor+x_line_tv , tvy_start+tvh),4)


    #proection of end points
    pygame.draw.line(win,blue,(x_cor+x_line_fv , fvy_start-fvh),(x_cor+x_line_tv , tvy_start+tvh),1)
    #projection of start points
    pygame.draw.line(win,blue,(x_cor,fvy_start),(x_cor ,tvy_start),1)


    #projection of line on fv start
    if hp_dis!=0:
        pygame.draw.line(win,green,(0,fvy_start),(w,fvy_start),1)
    #projection of line on tv start
    if vp_dis!=0:
        pygame.draw.line(win,green,(0,tvy_start),(w,tvy_start),1)
    

    #projection of line on fv end
    pygame.draw.line(win,green,(0,fvy_start-fvh),(w,fvy_start-fvh),1)
    #projection of line on tv end
    pygame.draw.line(win,green,(0,tvy_start+tvh),(w,tvy_start+tvh),1)

    #notations
    x_text = font.render('x',1,black)
    text_rect5 = x_text.get_rect()
    text_rect5.centerx,text_rect5.centery = 100-x_text.get_width(),y_cor

    y_text = font.render('y',1,black)
    text_rect6 = y_text.get_rect()
    text_rect6.centerx,text_rect6.centery = w-100+y_text.get_width(),y_cor

    #locuts of b'
    b_text = font.render("locuts of b'",1,black)
    text_rect7 = b_text.get_rect()
    text_rect7.centerx,text_rect7.centery = x_cor+400,(y_cor-(hp_dis+fvh)-15)

    b_text2 = font.render("locuts of b",1,black)
    text_rect8 = b_text2.get_rect()
    text_rect8.centerx,text_rect8.centery = x_cor+400,(y_cor+(vp_dis+tvh)+15)
    #points
    a_p = font.render('a',1,black)
    a_pt = a_p.get_rect()
    a_pt.centerx,a_pt.centery = x_cor-10,(y_cor+vp_dis+15)

    a_f = font.render("a'",1,black)
    a_ft = a_f.get_rect()
    a_ft.centerx,a_ft.centery = x_cor-8,(y_cor-hp_dis-15)

    b1_p = font.render('b1',1,black)
    b1_pt = b1_p.get_rect()
    b1_pt.centerx,b1_pt.centery = x_cor+fvl-10,(tvy_start+tvh+15)

    b1_f = font.render("b1'",1,black)
    b1_ft = b1_f.get_rect()
    b1_ft.centerx,b1_ft.centery = x_cor+fvl-15,(fvy_start-15)

    b2_p = font.render("b2",1,black)
    b2_pt = b2_p.get_rect()
    b2_pt.centerx,b2_pt.centery = x_cor+tvl+15,(tvy_start+15)

    b2_f = font.render("b2'",1,black)
    b2_ft = b2_f.get_rect()
    b2_ft.centerx,b2_ft.centery = x_cor+tvl-10,( fvy_start-fvh-15)

    b_p = font.render('b',1,black)
    b_pt = b_p.get_rect()
    b_pt.centerx,b_pt.centery = x_cor+x_line_fv-10,(tvy_start+tvh+15)

    b_f = font.render("b'",1,black)
    b_ft = b_f.get_rect()
    b_ft.centerx,b_ft.centery = x_cor+x_line_tv-10,(fvy_start-fvh-15)



    #texts
    win.blit(theta_text,text_rect)
    win.blit(phi_text,text_rect2)
    win.blit(fvl_text,text_rect3)
    win.blit(tvl_text,text_rect4)
    win.blit(x_text,text_rect5)
    win.blit(y_text,text_rect6)
    win.blit(b_text,text_rect7)
    win.blit(b_text2,text_rect8)
    win.blit(a_p,a_pt)
    win.blit(a_f,a_ft)
    win.blit(b_p,b_pt)
    win.blit(b_f,b_ft)
    win.blit(b2_p,b2_pt)
    win.blit(b2_f,b2_ft)
    win.blit(b1_p,b1_pt)
    win.blit(b1_f,b1_ft)
    pygame.display.update()

def main():
    global win ,w,h,font
    run = True
    
    
    #inputs
    multi = 3
    tl = int(input(' enter the true length :'))*multi
    theta = int(input('\n enter angle theta (angle with horizontal plane):'))
    phi = int(input('\n enter angle phi (angle with vertical plane):'))
    vp_dis = int(input('\n enter the distance from vertical plane:'))*multi
    hp_dis = int(input('\n enter the distrance from horizontal plane:'))*multi
    pi = 22/7

    #height
    fvh = tl*math.sin((theta/180)*(pi))
    tvh = tl*math.sin((phi/180)*(pi))
    #new length
    tvl = tl*math.cos((theta/180)*(pi))
    fvl = tl*math.cos((phi/180)*(pi))
    
    #pygame
    pygame.init()
    w,h = 1440,800
    win = pygame.display.set_mode((w,h))
    pygame.display.set_caption('egl-project')
    font = pygame.font.Font('freesansbold.ttf', 24)
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



