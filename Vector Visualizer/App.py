from tkinter import font
from turtle import width
import pygame
import random
from Vector import *

pygame.init()
screenWidth, screenHeight = 500, 675
white = (255, 255, 255)
gray = (55, 55, 55)
vectorFont = pygame.font.SysFont('Segoe UI Bold', 25)
UIFont = pygame.font.SysFont('Segoe UI', 15)
gridSubdivisions = 14  # Use only even numbers
black = (0, 0, 0)
origin = [0, 0]  # Real center coordinate
unitSize = screenWidth/gridSubdivisions
midScreen = screenWidth/2

def colorGenerator():
    randomColor = (random.randint(85, 255), random.randint(85, 255), random.randint(85, 255))
    return randomColor

def renderer(screen, vector):
    # Assigns the letter tag to a vector
    coordTag = vectorFont.render(vector.tag, True, white)
    pygame.draw.line(screen, vector.color, vector.absoluteOrigin,vector.absoluteDirection, width=2)
    if(vector.origin == (0, 0)):
        pygame.draw.circle(screen, vector.color,vector.absoluteDirection, 8)
    else:
        pygame.draw.circle(screen, vector.color,vector.absoluteDirection, 4)
    if vector.tag != "Axis":
        screen.blit(coordTag, ((vector.absoluteDirection[0]+5, vector.absoluteDirection[1]-25)))
    else:
        screen.blit(coordTag, ((((vector.absoluteOrigin[0]+vector.absoluteDirection[0])/2), (vector.absoluteOrigin[1]+vector.absoluteDirection[1])/2)))
    return

def interfaceRenderer(screen):
    textList = ["Press a number key to execute an operation with random vectors.", "1) Generate Vectors",
                "2) Normalize Vectors", "3) Vector Addition", "4) Vector Substraction", "5) Vector Projection"]
    pygame.draw.line(screen, white, (0, midScreen), (screenWidth, midScreen))
    pygame.draw.line(screen, white, (midScreen, 0), (midScreen, screenWidth))
    for i in range(1, gridSubdivisions+1):  # Render grid
        if i != gridSubdivisions/2:
            pygame.draw.line(screen, gray, (0, i * unitSize),(screenWidth, i * unitSize))
            pygame.draw.line(screen, gray, (i * unitSize, 0),(i * unitSize, screenWidth))
    for index, string in enumerate(textList):
        interfaceText = UIFont.render(string, True, white)
        screen.blit(interfaceText, (unitSize, (screenWidth+20*index)+25))

def vectorGenerator():
    vectorA = Vector(origin, [random.randint(-5.0, 5.0),
                     random.randint(-5.0, 5.0)], unitSize, midScreen, (255, 0, 0), "A")
    vectorB = Vector(origin, [random.randint(-5.0, 5.0),
                     random.randint(-5.0, 5.0)], unitSize, midScreen, (255, 0, 0), "B")
    return vectorA, vectorB

def main():
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    pygame.display.set_caption('Vector Visualizer Ver. 0.1')
    isRunning = True

    while isRunning:
        screen.fill(black)
        interfaceRenderer(screen)  # Rendering interface elements
        for event in pygame.event.get():  # Key presses
            if event.type == pygame.QUIT:
                isRunning = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:  # Generating two random vectors
                    vectorA, vectorB = vectorGenerator()
                if event.key == pygame.K_2:  # Normalizing generated vectors
                    vectorA.normalize(unitSize, midScreen)
                    vectorB.normalize(unitSize, midScreen)
                if event.key == pygame.K_3:  # Addition
                    vectorA, vectorB = vectorGenerator()
                    vectorR = vectorA.add(vectorB, unitSize, midScreen)
                if event.key == pygame.K_4:  # Substraction
                    vectorA, vectorB = vectorGenerator()
                    vectorR = vectorA.substract(vectorB, unitSize, midScreen)
                if event.key == pygame.K_5:  # Projection
                    vectorA, vectorB = vectorGenerator()
                    vectorR, vectorD = vectorA.project(vectorB, unitSize, midScreen)
        renderer(screen, vectorArray)
        pygame.display.update()
