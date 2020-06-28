# -*- coding: utf-8 -*-
"""
Created on Tue Jun 2 09:17:18 2020

@author: byron
"""
import pygame
import time
pygame.init()

tam_tela = (width, height) = (600,400)
fps = 120
font = pygame.font.SysFont("monospace",16)



#cores

verde = (18,114,47)
amarelo = (255, 255,0)
azul = (0,0,255)
branco = (255,255,255)


background = pygame.image.load('fundo.jpg')
tela = pygame.display.set_mode(tam_tela)
delay = pygame.time.Clock()
clock  = pygame.time.Clock()


pygame.display.set_caption("SPACE HOCKEY")


class rebatedor():
    def __init__(self,x,y,tam_x, tam_y,cor):
        self.image = pygame.Surface((tam_x, tam_y),pygame.SRCALPHA,32)
        self.rect = self.image.get_rect()
        self.image.fill(cor)
        self.image.convert_alpha()
        
        self.rect.left = x
        self.rect.top = y
        
        self.cor = cor
        self.movimento = [0,0]
        self.velocidade = 8 
        self.pontos = 0 
        
          
    def gera_rebatedor(self):
        tela.blit(self.image,self.rect)
        
    
    def checa_margens(self):
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > height:
            self.rect.bottom = height
            
    def atlza(self):
        self.rect = self.rect.move(self.movimento)
        self.checa_margens()
            
        
        
class bolinha():
    def __init__(self,x,y,tamanho, cor, movimento = [0,0]):
        self.image = pygame.Surface((tamanho, tamanho), pygame.SRCALPHA, 32)
        self.rect = self.image.get_rect()
        self.image.convert_alpha()
        self.rect.centerx = x 
        self.rect.centery = y 
        
        pygame.draw.circle(self.image, cor, (int(self.rect.width/2), int(self.rect.height/2)), int(tamanho/2))
        
        self.movimento = movimento
        self.velocidade_max = 6  
        self.pontuação = 0 
        
        
    def gera_bolinha(self):
        tela.blit(self.image,self.rect)
        
    def atlza(self): 
        if self.rect.top <= 0 or self.rect.bottom >= height:
            self.movimento[1] = -1*self.movimento[1]
        if self.rect.left <= 0 or self.rect.right >= width:
            self.movimento[0] = -1*self.movimento[0]

        if self.movimento[1] > self.velocidade_max:
            self.movimento[1]  = self.velocidade_max

        self.rect = self.rect.move(self.movimento)
        self.checa_margens()
        
            
    
    def checa_margens(self):
        if self.rect.top < 0:
            self.rect.top = 0 
        if self.rect.bottom > height:
            self.rect.bottom = height
        if self.rect.left < 0: 
            self.rect. left = 0 
        if self.rect.right > width:
            self.rect.right = width
            
def pc_mov(bola, pc):
    if bola.movimento[0] > 0:
        if bola.rect.bottom > pc.rect.bottom:
            pc.movimento[1] = pc.velocidade

        elif bola.rect.top < pc.rect.top:
            pc.movimento[1] = -1 * pc.velocidade

        else:
            pc.movimento[1] = 0
            
    else:
        pc.movimento[1] = 0 


        
        
        


def main():
    Pontuação = 0 
    rebates_pc = 0 
    game_over = False
    barrinha = rebatedor(int(width/10),int(height/3),int(width/60),int(height*60/400),verde)
    barrinha_pc = rebatedor(int(width - width/10),int(height/3),int(width/60),int(height*60/400),azul)
    bola = bolinha(width/2, height/2, width/30, amarelo,  [5,5])
    while game_over != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    barrinha.movimento[1] = -1*barrinha.velocidade
                if event.key == pygame.K_RIGHT:
                    barrinha.movimento[1] = barrinha.velocidade
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    barrinha.movimento[1] = 0 


        if pygame.sprite.collide_mask(barrinha,bola):
            Pontuação += 1
            bola.movimento[0] = -1*bola.movimento[0]
            bola.movimento[1] = bola.movimento[1] - barrinha.movimento[1]
            
        

        if pygame.sprite.collide_mask(barrinha_pc,bola):
            rebates_pc +=1 
            bola.movimento[0] = -1*bola.movimento[0]
            bola.movimento[1] = bola.movimento[1] - barrinha_pc.movimento[1]


        pc_mov(bola, barrinha_pc)  
        rebates = font.render("REBATES DO COMPUTADOR: " +str(rebates_pc), True, amarelo)
        tela.blit(rebates,(180,50))
        pontitos = font.render("PONTOS: " + str(Pontuação), True, amarelo)
        tela.blit(pontitos,(250, 350))
        pygame.display.flip()
        
       
       
        if rebates_pc == 100:
            fim = font.render("GAME OVER", True, amarelo)
            tela.blit(fim,(250,200))
            pygame.display.flip()
            time.sleep(4)
            game_over = True
       
        
        barrinha_pc.atlza()
        barrinha.atlza()
        bola.atlza()
        tela.blit(background, (0,0))
        barrinha_pc.gera_rebatedor()
        barrinha.gera_rebatedor()
        bola.gera_bolinha()

        delay.tick(fps)
        
        
    pygame.quit()
    quit()

main()

    
    
                
        
    

    
        
    
        
    
        
    
    
    
    

            

        
        
    
