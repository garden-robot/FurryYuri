init python:
    #Take info on a sprite and return an image of it darkened
    def darkenSprite(toShowName, spriteType, filterAmount=-0.5):
        output=im.MatrixColor("characters/"+toShowName+"/"+toShowName+" "+spriteType+".png", im.matrix.brightness(filterAmount))
        return output