import pygame

class MenosGrande: 
    '''Class which defines character MenosGrande'''
    standing = [pygame.image.load('menos_grande/stance_sprite/0.png'), pygame.image.load('menos_grande/stance_sprite/1.png'), pygame.image.load('menos_grande/stance_sprite/2.png'), pygame.image.load('menos_grande/stance_sprite/3.png'), pygame.image.load('menos_grande/stance_sprite/4.png')]
    walkingRight = [pygame.image.load('menos_grande/walk_sprite/5.png'), pygame.image.load('menos_grande/walk_sprite/6.png'), pygame.image.load('menos_grande/walk_sprite/7.png'), pygame.image.load('menos_grande/walk_sprite/8.png'), pygame.image.load('menos_grande/walk_sprite/9.png'), pygame.image.load('menos_grande/walk_sprite/10.png'), pygame.image.load('menos_grande/walk_sprite/11.png'), pygame.image.load('menos_grande/walk_sprite/12.png'), pygame.image.load('menos_grande/walk_sprite/13.png')]
    walkingLeft = [pygame.transform.flip(image, True, False) for image in walkingRight]
    
    def __init__(self, x, y, width, height): 
        self.x = x 
        self.y = y 
        self.width = width 
        self.height = height 
        self.vel = 5 
        self.left = False 
        self.walkCount = 0 

    def walkLeft(self, window): 
        if self.walkCount + 1 >= 27: 
            self.walkCount = 0 
        
        self.x -= self.vel
        window.blit(self.walkingLeft[self.walkCount//3], (self.x, self.y)) 

        self.walkCount += 1

    def walkRight(self, window): 
        if self.walkCount + 1 >= 27: 
            self.walkCount = 0 
        
        self.x += self.vel
        window.blit(self.walkingRight[self.walkCount//3], (self.x, self.y)) 
        self.walkCount += 1

    def pace(self, window, left_border, right_border):
        if self.x - self.vel <= left_border and self.left:
            self.left = False
        elif self.x + self.vel >= right_border and not(self.left): 
            self.left = True 

        if self.left: 
            self.walkLeft(window)
        else: 
            self.walkRight(window)
        


    