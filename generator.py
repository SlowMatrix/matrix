from class_matrix import Matrix

def perlin_nose(m, difpower=1, diapozon=(0, 1)):
    m.pattern("random", diapozon)
    m.dif(difpower)
    return m
            
if __name__ == "__main__":
    import pygame
    m = perlin_nose(Matrix(10, 10), 1, (0, 10))
    m.show()
    
    