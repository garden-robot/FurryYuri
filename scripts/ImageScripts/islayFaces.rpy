
screen islayOwO(faceExpression, position, isFlipped=False):
    fixed:
        if lastSpoke=="islay":
            $ imgToUse="characters/islay/islay faceless.png"
        else:
            $ imgToUse=im.MatrixColor("characters/islay/islay faceless.png", im.matrix.brightness(-0.5))
        if not isFlipped:
            $ flip = 1
        else:
            $ flip = -1
        if position=="left":
            add imgToUse:
                xalign 0.0 
                yalign 1.0 
                zoom islaySizeScale
                xzoom flip
            if not isFlipped:
                text "{color=#000000}{size=25}[faceExpression]{/size}{/color}":
                    xcenter 0.059
                    ycenter 0.285
            else:
                text "{color=#000000}{size=25}[faceExpression]{/size}{/color}":
                    xcenter 0.113
                    ycenter 0.285
        if position=="center":
            add "characters/islay/islay faceless.png":
                xalign 0.5 
                yalign 1.0
                zoom islaySizeScale
                xzoom flip
            if not isFlipped:
                text "{color=#000000}{size=25}[faceExpression]{/size}{/color}":
                    xcenter 0.471 
                    ycenter 0.285
            else:
                text "{color=#000000}{size=25}[faceExpression]{/size}{/color}":
                    xcenter 0.527 
                    ycenter 0.285
        if position=="right":
            add "characters/islay/islay faceless.png":
                xalign 1.0
                yalign 1.0
                zoom islaySizeScale
                xzoom flip
            if not isFlipped:
                text "{color=#000000}{size=25}[faceExpression]{/size}{/color}":
                    xcenter 0.89 
                    ycenter 0.285
            else:
                text "{color=#000000}{size=25}[faceExpression]{/size}{/color}":
                    xcenter 0.89 
                    ycenter 0.285
            
            
            