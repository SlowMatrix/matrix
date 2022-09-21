class Matrix_display:
    def __init__(self, display, matrix, update_function=None):
        self.display = display
        self.matrix = matrix
        
    def update_display(self):
        if self.func != None:
            self.matrix.scan(self.func, murra = True)
    
    def cluse(self):
        pg.quit()

class show_in_pygame: # использую класс только для красивого использования
    def show_nums(m, sizecl=10, immn=1, Display=None, time=3):
        import pygame as pg
        import time as t
        
        def f(x, y, im, display):
            colour = [255 if (s := im*immn) > 255 else s]*3
            rect = (x*sizecl, y*sizecl, sizecl, sizecl)
            pg.draw.rect(display, colour, rect)
        
        show_in_pygame.show_by_func(m, f, Display, time)
        
    def show_nums_3D(m, sizecl=10, immn=1, Display=None, time=3, Cof3D=1.25):
        import pygame as pg
        def f(x, y, im, display):
            colour = [y**1.1]+[im]+[255 if (s := im*immn) > 255 else s]
            colour = [i if i <= 255 and i > 0 else 255 for i in colour]
            rect = (x*sizecl, y*sizecl-im**Cof3D, sizecl, sizecl)
            pg.draw.rect(display, colour, rect)
        
        show_in_pygame.show_by_func(m, f, Display, time)
        
    def show_by_func(m, f, Display=None, time=3):
        import pygame as pg
        import time as t
           
        if Display == None:
            display = pg.display.set_mode((0, 0))
        else:
            display = Display
            
        m = m.copy()
        m.scan_no_ret(f, inFunk=display)
            
        
        if Display == None:
            pg.display.update()
            t.sleep(time)
            pg.quit()
            

        

    
if __name__ == "__main__":
    from generator import *
    from class_matrix import Matrix
    m = perlin_nose(Matrix(100, 100), 9, (0, 255))
    show_in_pygame.show_nums(m, time=1)
    show_in_pygame.show_nums_3D(m, time=1, Cof3D=1.001)