#Screen to hendle Islay's OwO faces

init python:
    islayOwO=None

init 1 python:
    islayFacelessSizes=(int(123*islaySizeScale),int(352*islaySizeScale))
    #Take info on a sprite and return an image of it darkened
    def makeIslayOwO(faceExpression = "OwO", doFlip=False):
        global islayFacelessSizes, islayOwO, lastSpoke
        facelessIslay=im.Scale("characters/islay/islay faceless.png", islayFacelessSizes[0], islayFacelessSizes[1])
        owoText=Text("{color=#000000}{size=25}"+faceExpression+"{/size}{/color}")
        textSize=owoText.size()
        if doFlip:
            facelessIslay=im.Flip(facelessIslay, horizontal=doFlip)
            textPos=(143-int(textSize[0]/2), 100-int(textSize[1]/2))
        else:
            textPos=(75-int(textSize[0]/2), 100-int(textSize[1]/2))
            
        if lastSpoke!="islay":
            facelessIslay=im.MatrixColor(facelessIslay, im.matrix.brightness(-0.5))
            
        output=LiveComposite(
            (islayFacelessSizes[0], islayFacelessSizes[1]),
            (0, 0), facelessIslay,
            textPos, owoText,
            )
        
        islayOwO=output
            
        return output

