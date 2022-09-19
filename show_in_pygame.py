class show_in_pygame: # использую класс только для красивого использования
    def show_nums(m, sizecl=10, immn=1, Display=None, time=3):
        import pygame as pg
        import time as t
        
        def f(x, y, im, inF):
            colour = [255 if (s := im*immn) > 255 else s]*3
            rect = (x*sizecl, y*sizecl, sizecl, sizecl)
            pg.draw.rect(display, colour, rect)
        
        if Display == None:
            display = pg.display.set_mode((0, 0))
        else:
            display = Display
        
        m = m.copy()
        m.scan_no_ret(f)
        
        pg.display.update()
        t.sleep(time)
        if Display == None:
            pg.quit()
            
    def show_nums_3D(m, sizecl=10, immn=1, Display=None, time=3, Cof3D=1.25):
        import pygame as pg
        import time as t
           
        def f(x, y, im, inF):
            colour = [y**1.1]+[255 if (s := im*immn) > 255 else s]*2 # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! y может превысить 255
            rect = (x*sizecl, y*sizecl-im**Cof3D, sizecl, sizecl)
            pg.draw.rect(display, colour, rect)
            
        if Display == None:
            display = pg.display.set_mode((0, 0))
        else:
            display = Display
            
        m = m.copy()
        m.scan_no_ret(f)
            
        pg.display.update()
        t.sleep(time)
        if Display == None:
            pg.quit()  

        def show_by_func(m, f, sizecl=10, immn=1, Display=None, time=3):
            import pygame as pg
            import time as t
            
            if Display == None:
                display = pg.display.set_mode((0, 0))
            else:
                display = Display
            
            m = m.copy()
            m.scan_no_ret(f, inFunk=display)
            
            pg.display.update()
            t.sleep(time)
            if Display == None:
                pg.quit()

        

    
if __name__ == "__main__":
    from generator import *
    from class_matrix import Matrix
    m = perlin_nose(Matrix(100, 100), 4, (0, 255))
    show_in_pygame.show_nums(m.show(), time=1)