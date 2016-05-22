from strip import *
import time

s = Strip().strip
s.setBrightness(20)

colorWipe(s, Color(50,50,50))
colorWipe(s, black)

# Flag 1
s.setPixelColor(0, red)
s.setPixelColor(1, yellow)
s.setPixelColor(2, red)

# Set 1
setNumber = 1


vo = 8
# Flag 2
s.setPixelColor(vo+3+1, red)
s.setPixelColor(vo+3+2, blue)
s.setPixelColor(vo+3+3, white)



# Set team 1
s.setPixelColor(4, setColors[0])
s.setPixelColor(5, black)
s.setPixelColor(6, black)


# Set team 2
s.setPixelColor(vo+2, setColors[0])
s.setPixelColor(vo+1, black)
s.setPixelColor(vo, black)

s.show()


game1 = 0
game2 = 0
for i in range (6):
    even = i%2
    if even == 0:
        service = 4
    else :
        service = vo+2
    #    game2 = game2  + 1

    game1 = i
    s.setPixelColor(4, setColors[game1])
    s.setPixelColor(vo+2, setColors[game2])
    s.show()
    t = 0
    while t < 3:
        t = t+1
        blinkPixel(s, service, 200)

game1 = 0
game2 = 0
pixel1= 5
pixel2 = vo +1
for i in range (6):
    even = i%2
    if even == 0:
        service = pixel1
    else :
        service = pixel2
     #   game2 = game2  + 1

    game1 = i
    s.setPixelColor(pixel1, setColors[game1])
    s.setPixelColor(pixel2, setColors[game2])
    s.show()
    t = 0
    while t < 3:
        t = t+1
        blinkPixel(s, service, 300)

game1 = 0
game2 = 0
pixel1= 6
pixel2 = vo 
for i in range (6):
    even = i%2
    if even == 0:
        service = pixel1
    else :
        service = pixel2
     #   game2 = game2  + 1

    game1 = i
    s.setPixelColor(pixel1, setColors[game1])
    s.setPixelColor(pixel2, setColors[game2])
    s.show()
    t = 0
    while t < 3:
        t = t+1
        blinkPixel(s, service, 300)

