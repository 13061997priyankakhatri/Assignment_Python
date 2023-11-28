# # #         #   Jarvis  #
# # # # # pip install pyaudio

# # # # import pyttsx3 #pip install pyttsx3
# # # # import speech_recognition as sr #pip install speechRecognition
# # # # import datetime
# # # # import wikipedia #pip install wikipedia
# # # # import webbrowser
# # # # import os
# # # # import smtplib

# # # # engine = pyttsx3.init('sapi5')
# # # # voices = engine.getProperty('voices')
# # # # # print(voices[1].id)
# # # # engine.setProperty('voice', voices[0].id)


# # # # def speak(audio):
# # # #     engine.say(audio)
# # # #     engine.runAndWait()


# # # # def wishMe():
# # # #     hour = int(datetime.datetime.now().hour)
# # # #     if hour>=0 and hour<12:
# # # #         speak("Good Morning!")

# # # #     elif hour>=12 and hour<18:
# # # #         speak("Good Afternoon!")   

# # # #     else:
# # # #         speak("Good Evening!")  

# # # #     speak("I am Jarvis Sir. Please tell me how may I help you")       

# # # # def takeCommand():
# # # #     #It takes microphone input from the user and returns string output

# # # #     r = sr.Recognizer()
# # # #     with sr.Microphone() as source:
# # # #         print("Listening...")
# # # #         r.pause_threshold = 1
# # # #         audio = r.listen(source)

# # # #     try:
# # # #         print("Recognizing...")    
# # # #         query = r.recognize_google(audio, language='en-in')
# # # #         print(f"User said: {query}\n")

# # # #     except Exception as e:
# # # #         # print(e)    
# # # #         print("Say that again please...")  
# # # #         return "None"
# # # #     return query

# # # # def sendEmail(to, content):
# # # #     server = smtplib.SMTP('smtp.gmail.com', 587)
# # # #     server.ehlo()
# # # #     server.starttls()
# # # #     server.login('youremail@gmail.com', 'your-password')
# # # #     server.sendmail('youremail@gmail.com', to, content)
# # # #     server.close()

# # # # if __name__ == "__main__":
# # # #     wishMe()
# # # #     while True:
# # # #     # if 1:
# # # #         query = takeCommand().lower()

# # # #         # Logic for executing tasks based on query
# # # #         if 'wikipedia' in query:
# # # #             speak('Searching Wikipedia...')
# # # #             query = query.replace("wikipedia", "")
# # # #             results = wikipedia.summary(query, sentences=2)
# # # #             speak("According to Wikipedia")
# # # #             print(results)
# # # #             speak(results)

# # # #         elif 'open youtube' in query:
# # # #             webbrowser.open("youtube.com")
# # # #         elif 'open google' in query:
# # # #             webbrowser.open("google.com")

# # # #         elif 'open stackoverflow' in query:
# # # #             webbrowser.open("stackoverflow.com")   


# # # #         elif 'play music' in query:
# # # #             music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
# # # #             songs = os.listdir(music_dir)
# # # #             print(songs)    
# # # #             os.startfile(os.path.join(music_dir, songs[0]))

# # # #         elif 'the time' in query:
# # # #             strTime = datetime.datetime.now().strftime("%H:%M:%S")    
# # # #             speak(f"Sir, the time is {strTime}")

# # # #         elif 'open code' in query:
# # # #             codePath = "C:\\Users\\nayna\\AppData\\Local\\Programs\\Python\\Python312\\Vedio-2"
# # # #             os.startfile(codePath)

# # # #         elif 'email to priyanka' in query:
# # # #             try:
# # # #                 speak("What should I say?")
# # # #                 content = takeCommand()
# # # #                 to = "naynakhatri999@gmail.com"    
# # # #                 sendEmail(to, content)
# # # #                 speak("Email has been sent!")
# # # #             except Exception as e:
# # # #                 print(e)
# # # #                 speak("Sorry my friend priyanka. I am not able to send this email")    
# # # #         else:
# # # #             print("No query matched")


# # #     #   Love Calculator     #
# # # # import tkinter
# # # from tkinter import *
# # # # import random module
# # # import random
# # # # Creating GUI window
# # # root = Tk()
# # # # Defining the container size, width=400, height=240
# # # root.geometry('400x240')
# # # # Title of the container
# # # root.title('Love Calculator????')

# # # # Function to calculate love percentage
# # # # between the user ans partner


# # # def calculate_love():
# # # 	# value will contain digits between 0-9
# # # 	st = '0123456789'
# # # 	# result will be in double digits
# # # 	digit = 2
# # # 	temp = "".join(random.sample(st, digit))
# # # 	result.config(text=temp)


# # # # Heading on Top
# # # heading = Label(root, text='Love Calculator - How much is he/she into you')
# # # heading.pack()

# # # # Slot/input for the first name
# # # slot1 = Label(root, text="Enter Your Name:")
# # # slot1.pack()
# # # name1 = Entry(root, border=5)
# # # name1.pack()

# # # # Slot/input for the partner name
# # # slot2 = Label(root, text="Enter Your Partner Name:")
# # # slot2.pack()
# # # name2 = Entry(root, border=5)
# # # name2.pack()

# # # bt = Button(root, text="Calculate", height=1,
# # # 			width=7, command=calculate_love)
# # # bt.pack()

# # # # Text on result slot
# # # result = Label(root, text='Love Percentage between both of You:')
# # # result.pack()

# # # # Starting the GUI
# # # root.mainloop()

# #         #   Face recognision    #
# # import cv2

# # #Loading The Cascade File
# # face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# # #Reading the Input Image
# # # image= cv2.imread('1.jpg')
# # image= cv2.imread('1.png')

# # #Resizing the Image
# # img = cv2.resize(image,None,fx=0.3,fy=0.3)

# # #Converting the image into grayscale image
# # imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # #Detecting The Faces
# # faces = face_cascade.detectMultiScale(imgGray, 1.2, 5)

# # #Pointing The Faces
# # for (x,y,w,h) in faces:
# # 	cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)

# # #Displaying The Output Image
# # cv2.imshow('img', img)
# # cv2.waitKey()

#         #   Flappy Bird     #
# import random # For generating random numbers
# import sys #To exit the program
# import pygame #pip install pygame
# from pygame.locals import * 
# # Global Variables for the game
# FPS = 32
# SCREENWIDTH = 289
# SCREENHEIGHT = 511
# SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
# GROUNDY = SCREENHEIGHT * 0.8
# GAME_SPRITES = {}
# GAME_SOUNDS = {}
# PLAYER = 'gallery/sprites/bird.png'
# BACKGROUND = 'gallery/sprites/background.png'
# PIPE = 'gallery/sprites/pipe.png'

# def welcomeScreen():

#     playerx = int(SCREENWIDTH/5)
#     playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2)
#     messagex = int((SCREENWIDTH - GAME_SPRITES['message'].get_width())/2)
#     messagey = int(SCREENHEIGHT*0.13)
#     basex = 0
#     while True:
#         for event in pygame.event.get():
#             # if user clicks on cross button, close the game
#             if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
#                 pygame.quit()
#                 sys.exit()

#             # If the user presses space or up key, start the game for them
#             elif event.type==KEYDOWN and (event.key==K_SPACE or event.key == K_UP):
#                 return
#             else:
#                 SCREEN.blit(GAME_SPRITES['background'], (0, 0))    
#                 SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))    
#                 SCREEN.blit(GAME_SPRITES['message'], (messagex,messagey ))    
#                 SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))    
#                 pygame.display.update()
#                 FPSCLOCK.tick(FPS)

# def mainGame():
#     score = 0
#     playerx = int(SCREENWIDTH/5)
#     playery = int(SCREENWIDTH/2)
#     basex = 0

#     # Create 2 pipes for blitting on the screen
#     newPipe1 = getRandomPipe()
#     newPipe2 = getRandomPipe()

#     # List of upper pipes
#     upperPipes = [
#         {'x': SCREENWIDTH+200, 'y':newPipe1[0]['y']},
#         {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y':newPipe2[0]['y']},
#     ]
#     # List of lower pipes
#     lowerPipes = [
#         {'x': SCREENWIDTH+200, 'y':newPipe1[1]['y']},
#         {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y':newPipe2[1]['y']},
#     ]

#     pipeVelX = -4

#     playerVelY = -9
#     playerMaxVelY = 10
#     playerMinVelY = -8
#     playerAccY = 1

#     playerFlapAccv = -8 # velocity while flapping
#     playerFlapped = False # It is true only when the bird is flapping


#     while True:
#         for event in pygame.event.get():
#             if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
#                 pygame.quit()
#                 sys.exit()
#             if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
#                 if playery > 0:
#                     playerVelY = playerFlapAccv
#                     playerFlapped = True
#                     GAME_SOUNDS['wing'].play()


#         crashTest = isCollide(playerx, playery, upperPipes, lowerPipes) # This function will return true if the player is crashed
#         if crashTest:
#             return     

#         #check for score
#         playerMidPos = playerx + GAME_SPRITES['player'].get_width()/2
#         for pipe in upperPipes:
#             pipeMidPos = pipe['x'] + GAME_SPRITES['pipe'][0].get_width()/2
#             if pipeMidPos<= playerMidPos < pipeMidPos +4:
#                 score +=1
#                 print(f"Your score is {score}") 
#                 GAME_SOUNDS['point'].play()


#         if playerVelY <playerMaxVelY and not playerFlapped:
#             playerVelY += playerAccY

#         if playerFlapped:
#             playerFlapped = False            
#         playerHeight = GAME_SPRITES['player'].get_height()
#         playery = playery + min(playerVelY, GROUNDY - playery - playerHeight)

#         # Moving Pipes
#         for upperPipe , lowerPipe in zip(upperPipes, lowerPipes):
#             upperPipe['x'] += pipeVelX
#             lowerPipe['x'] += pipeVelX

#         # Adding Pipes
#         if 0<upperPipes[0]['x']<5:
#             newpipe = getRandomPipe()
#             upperPipes.append(newpipe[0])
#             lowerPipes.append(newpipe[1])

#         # Removing Pipes
#         if upperPipes[0]['x'] < -GAME_SPRITES['pipe'][0].get_width():
#             upperPipes.pop(0)
#             lowerPipes.pop(0)
        
#         # Blitting The Sprites
#         SCREEN.blit(GAME_SPRITES['background'], (0, 0))
#         for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
#             SCREEN.blit(GAME_SPRITES['pipe'][0], (upperPipe['x'], upperPipe['y']))
#             SCREEN.blit(GAME_SPRITES['pipe'][1], (lowerPipe['x'], lowerPipe['y']))

#         SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
#         SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
#         myDigits = [int(x) for x in list(str(score))]
#         width = 0
#         for digit in myDigits:
#             width += GAME_SPRITES['numbers'][digit].get_width()
#         Xoffset = (SCREENWIDTH - width)/2

#         for digit in myDigits:
#             SCREEN.blit(GAME_SPRITES['numbers'][digit], (Xoffset, SCREENHEIGHT*0.12))
#             Xoffset += GAME_SPRITES['numbers'][digit].get_width()
#         pygame.display.update()
#         FPSCLOCK.tick(FPS)

# def isCollide(playerx, playery, upperPipes, lowerPipes):
#     if playery> GROUNDY - 25  or playery<0:
#         GAME_SOUNDS['hit'].play()
#         return True
    
#     for pipe in upperPipes:
#         pipeHeight = GAME_SPRITES['pipe'][0].get_height()
#         if(playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width()):
#             GAME_SOUNDS['hit'].play()
#             return True

#     for pipe in lowerPipes:
#         if (playery + GAME_SPRITES['player'].get_height() > pipe['y']) and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width():
#             GAME_SOUNDS['hit'].play()
#             return True

#     return False

# def getRandomPipe():
#     pipeHeight = GAME_SPRITES['pipe'][0].get_height()
#     offset = SCREENHEIGHT/3
#     y2 = offset + random.randrange(0, int(SCREENHEIGHT - GAME_SPRITES['base'].get_height()  - 1.2 *offset))
#     pipeX = SCREENWIDTH + 10
#     y1 = pipeHeight - y2 + offset
#     pipe = [
#         {'x': pipeX, 'y': -y1}, #upper Pipe
#         {'x': pipeX, 'y': y2} #lower Pipe
#     ]
#     return pipe






# if __name__ == "__main__":
#     # This will be the main point from where our game will start
#     pygame.init() # Initialize all pygame's modules
#     FPSCLOCK = pygame.time.Clock()
#     pygame.display.set_caption('Flappy Bird by CodeWithHarry')
#     GAME_SPRITES['numbers'] = ( 
#         pygame.image.load('gallery/sprites/0.png').convert_alpha(),
#     )

#     GAME_SPRITES['message'] =pygame.image.load('gallery/sprites/message.png').convert_alpha()
#     GAME_SPRITES['base'] =pygame.image.load('gallery/sprites/base.png').convert_alpha()
#     GAME_SPRITES['pipe'] =(pygame.transform.rotate(pygame.image.load( PIPE).convert_alpha(), 180), 
#     pygame.image.load(PIPE).convert_alpha()
#     )

#     # Game sounds
#     GAME_SOUNDS['die'] = pygame.mixer.Sound('gallery/audio/die.wav')
#     GAME_SOUNDS['hit'] = pygame.mixer.Sound('gallery/audio/hit.wav')
#     GAME_SOUNDS['point'] = pygame.mixer.Sound('gallery/audio/point.wav')
#     GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('gallery/audio/swoosh.wav')
#     GAME_SOUNDS['wing'] = pygame.mixer.Sound('gallery/audio/wing.wav')

#     GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
#     GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()

#     while True:
#         welcomeScreen()
#         mainGame() 

        #   Snake    #
author = 'CodeWithHarry'

#Importing The Modules
import pygame
import random
import os

#Initialization
pygame.mixer.init()
pygame.init()


#Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
snakegreen = (35, 45, 40)

#Game Backgrounds
# bg1 = pygame.image.load("Screen/bg.jpg")
bg2 = pygame.image.load("Screen/bg2.jpg")
intro = pygame.image.load("Screen/intro1.png")
outro = pygame.image.load("Screen/outro.png")

#Creating The window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

#Game Title
pygame.display.set_caption("Snake By CodeWithHarry")
pygame.display.update()

#Music
pygame.mixer.music.load('music/wc.mp3')
pygame.mixer.music.play(100)
pygame.mixer.music.set_volume(.6)

#Variables For The Game
clock = pygame.time.Clock()
font = pygame.font.SysFont('Harrington', 35)

def text_screen(text, color, x, y):
   screen_text = font.render(text, True, color)
   gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow, color, snk_list, snake_size):
   for x,y in snk_list:
       pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


#Welcome Screen

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.blit(intro, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.fadeout(200)
                    pygame.mixer.music.load('music/bgm.mp3')
                    pygame.mixer.music.play(100)
                    pygame.mixer.music.set_volume(.6)
                    gameloop()
        pygame.display.update()
        clock.tick(60)

# Game Loop
def gameloop():

# Game specific variables
   exit_game = False
   game_over = False
   snake_x = 45
   snake_y = 55
   velocity_x = 0
   velocity_y = 0
   snk_list = []
   snk_length = 1

#Highscore Build
   if(not os.path.exists("highscore.txt")):
       with open("highscore.txt", "w") as f:
           f.write("0")
   with open("highscore.txt", "r") as f:
            highscore = f.read()

#Food
   food_x = random.randint(20, screen_width / 2)
   food_y = random.randint(20, screen_height / 2)

#Game Variables
   score = 0
   init_velocity = 5
   snake_size = 30
   fps = 60
   while not exit_game:
       if game_over:
           with open("highscore.txt", "w") as f:
               f.write(str(highscore))

#GameOverScreen

           gameWindow.blit(outro, (0, 0))
           text_screen("Score: " + str(score ), snakegreen, 385, 350)
           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   exit_game = True
               if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_RETURN:
                       welcome()
       else:
           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   exit_game = True
               if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_RIGHT:
                       velocity_x = init_velocity
                       velocity_y = 0
                   if event.key == pygame.K_LEFT:
                       velocity_x = - init_velocity
                       velocity_y = 0
                   if event.key == pygame.K_UP:
                       velocity_y = - init_velocity
                       velocity_x = 0
                   if event.key == pygame.K_DOWN:
                       velocity_y = init_velocity
                       velocity_x = 0
                   if event.key == pygame.K_q:
                        score +=10
           snake_x = snake_x + velocity_x
           snake_y = snake_y + velocity_y
           if abs(snake_x - food_x)<12 and abs(snake_y - food_y)<12:
               score +=10
               food_x = random.randint(20, screen_width / 2)
               food_y = random.randint(20, screen_height / 2)
               snk_length +=5
               if score>int(highscore):
                   highscore = score
           gameWindow.blit(bg2, (0, 0))
           text_screen("Score: " + str(score) + "  Highscore: "+str(highscore),  snakegreen, 5, 5)
           pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
           head = []
           head.append(snake_x)
           head.append(snake_y)
           snk_list.append(head)


           if len(snk_list)>snk_length:
               del snk_list[0]
           if head in snk_list[:-1]:
               game_over = True
               pygame.mixer.music.load('music/bgm1.mp3')
               pygame.mixer.music.play(100)
               pygame.mixer.music.set_volume(.6)
           if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
               game_over = True
               pygame.mixer.music.load('music/bgm2.mp3')
               pygame.mixer.music.play(100)
               pygame.mixer.music.set_volume(.6)
           plot_snake(gameWindow, black, snk_list, snake_size)
       pygame.display.update()
       clock.tick(fps)
   pygame.quit()
   quit()
welcome()
