from pygame import mixer
   
mixer.init()
mixer.music.load("Alex Cohen - Good Old Times.mp3")
mixer.music.play()
while mixer.music.get_busy() == True:
	continue