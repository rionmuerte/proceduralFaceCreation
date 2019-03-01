from PIL import Image
import os
import random

class pictureHandler:
    def __init__(self, name):
        self.image = Image.new('RGBA', (64,64))
        self.name = name
    
    def saveImage(self, dir='./createdFaces/'):
        self.image.save(dir+self.name)

    def showImage(self):
        self.image.show()

    def addLayer(self, layer, color):
        destR, destG, destB = color
        pixels = Image.open(layer).load()
        for i in range(64):
            for j in range(64):
                r,g,b,a = pixels[i,j]
                r = int((256-r)/255 * destR)
                g = int((256-g)/255 * destG)
                b = int((256-b)/255 * destB)
                if a > 0:
                    self.image.putpixel((i,j),(r,g,b,a))
        pass
    
    def colorBase(self, colorString, darken=1):
        rh,gh,bh = [int(i,16) for i in colorString.split()]
        r = max(min(int(rh*darken),255),0)
        g = max(min(int(gh*darken),255),0)
        b = max(min(int(bh*darken),255),0)
        return r,g,b

class pictureGenerator:
    def __init__(self):
        self.shapes = ['components/shape/'+ i for i in os.listdir('components/shape/')]
        self.noses = ['components/nose/'+ i for i in os.listdir('components/nose/')]
        self.mouths = ['components/mouth/'+ i for i in os.listdir('components/mouth/')]
        self.mustaches = ['components/mustache/'+ i for i in os.listdir('components/mustache/')]
        self.mustaches.append(None)
        eyes = ['components/eye/eye/'+ i for i in os.listdir('components/eye/eye/')]
        pupils = ['components/eye/pupils/'+ i for i in os.listdir('components/eye/pupils/')]
        self.eyes = [i for i in zip(eyes,pupils)]
        self.beards = ['components/beard/'+ i for i in os.listdir('components/beard/')]
        self.beards.append(None)
        self.haircut = ['components/haircut/'+ i for i in os.listdir('components/haircut/')]
        self.haircut.append(None)
        self.eyebrows = ['components/eyebrows/'+ i for i in os.listdir('components/eyebrows/')]
        f = open('components/skinTones')
        self.skinTones = f.readlines()
        f.close()
        f = open('components/mouthTones')
        self.mouthTones = f.readlines()
        f.close()
        f = open('components/hairTones')
        self.hairTones = f.readlines()
        f.close()
        f = open('components/eyeTones')
        self.eyeTones = f.readlines()
        f.close()
    
    def createRandomPicture(self, name):
        self.ph = pictureHandler(name)
        self._createBaseFace(*self._selectRandomBaseFace())
        self._createEyes(*self._selectRandomEyes())
        self._createHair(*self._selectRandomHair())
        self.ph.saveImage()
        
    def _createBaseFace(self, shape, nose, mouth, skinColor, mouthColor):
        self.ph.addLayer(shape,self.ph.colorBase(skinColor))
        self.ph.addLayer(nose,self.ph.colorBase(skinColor, 1.15))
        self.ph.addLayer(mouth,self.ph.colorBase(mouthColor))   

    def _createEyes(self, eyes, eyeColor):
        eyes,pupils = eyes
        self.ph.addLayer(eyes,self.ph.colorBase('255 255 255'))
        self.ph.addLayer(pupils, self.ph.colorBase(eyeColor))
    
    def _createHair(self, mustache, beard, haircut, eyebrows, hairColor):
        if haircut is not None: self.ph.addLayer(haircut, self.ph.colorBase(hairColor))
        self.ph.addLayer(eyebrows, self.ph.colorBase(hairColor))
        if beard is not None:self.ph.addLayer(beard, self.ph.colorBase(hairColor))
        if mustache is not None: self.ph.addLayer(mustache, self.ph.colorBase(hairColor))

    def _selectRandomBaseFace(self):
        shape = random.choice(self.shapes)
        nose = random.choice(self.noses)
        mouth = random.choice(self.mouths)
        skinColor = random.choice(self.skinTones)
        mouthColor = random.choice(self.mouthTones)
        return shape, nose, mouth, skinColor, mouthColor
    
    def _selectRandomEyes(self):
        eyes = random.choice(self.eyes)
        eyeColor = random.choice(self.eyeTones)
        return eyes, eyeColor

    def _selectRandomHair(self):
        mustache = random.choice(self.mustaches)
        beard = random.choice(self.beards)
        haircut = random.choice(self.haircut)
        eyebrows = random.choice(self.eyebrows)
        color = random.choice(self.hairTones)
        return mustache, beard, haircut, eyebrows, color

if __name__ == "__main__":
    import sys
    pg = pictureGenerator()
    if len(sys.argv) > 1:
        for i in sys.argv[1:]:
            pg.createRandomPicture(i+'.png')
    else:
        pg.createRandomPicture('imge.png')