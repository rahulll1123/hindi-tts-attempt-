
#M1
# import playsound as ps
# ps.playsound("tts_create\output.mp3")
# ps.playsound("tts_create\output2.mp3",block=False)#Does not play
# ps.playsound("tts_create\output2.mp3")# there is shutter between two play

#M2
import pygame,sys,time
pygame.mixer.init()
pygame.mixer.music.load('testgtt/output2.mp3')
pygame.mixer.music.play(loops=2)
input("enter to exit")
pygame.mixer.music.unload()