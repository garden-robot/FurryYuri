#Screen to hendle Islay's OwO faces

screen islayOwO(faceExpression, position, isFlipped=False):
    fixed:
        #If islay didnt speak last, darken the sprite
        if lastSpoke=="islay":
            $ imgToUse="characters/islay/islay faceless.png"
        else:
            $ imgToUse=im.MatrixColor("characters/islay/islay faceless.png", im.matrix.brightness(-0.5))
        #Apply a vertical flip
        if not isFlipped:
            $ flip = 1
        else:
            $ flip = -1
        
        #Position Islay and his face if he's standing on the left
        if position=="left":
            #Position Islay
            add imgToUse:
                xalign 0.0 
                yalign 1.0 
                zoom islaySizeScale
                xzoom flip
            #Position the OwO
            if not isFlipped:
                text "{color=#000000}{size=25}[faceExpression]{/size}{/color}":
                    xcenter 0.059
                    ycenter 0.285
            else:
                text "{color=#000000}{size=25}[faceExpression]{/size}{/color}":
                    xcenter 0.113
                    ycenter 0.285
                    
        #Position Islay and his face if he's standing in the center
        if position=="center":
            #Position Islay
            add imgToUse:
                xalign 0.5 
                yalign 1.0
                zoom islaySizeScale
                xzoom flip
            #Position the OwO
            if not isFlipped:
                text "{color=#000000}{size=25}[faceExpression]{/size}{/color}":
                    xcenter 0.471 
                    ycenter 0.285
            else:
                text "{color=#000000}{size=25}[faceExpression]{/size}{/color}":
                    xcenter 0.527 
                    ycenter 0.285
                    
        #Position Islay and his face if he's standing on the right
        if position=="right":
            #Position Islay
            add imgToUse:
                xalign 1.0
                yalign 1.0
                zoom islaySizeScale
                xzoom flip
            #Position the OwO
            if not isFlipped:
                text "{color=#000000}{size=25}[faceExpression]{/size}{/color}":
                    xcenter 0.89 
                    ycenter 0.285
            else:
                text "{color=#000000}{size=25}[faceExpression]{/size}{/color}":
                    xcenter 0.89 
                    ycenter 0.285
            
            
            