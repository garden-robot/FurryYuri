#Animation for ganing or losing points with someone


#Define icons to show gaining/losing points
image gainLovePointsIcon = "heart.png"
image gainLikePointsIcon = "note.png"
image loseLovePointsIconFull = "heart.png"
image loseLovePointsIconLeft = "heartLeft.png"
image loseLovePointsIconRight = "heartRight.png"
image loseLikePointsIcon = "sadface.png"



init python:
    #Define side images for gaining/losing points with characters
    emmaSideAngry = "characters/emma/emma angry.png"
    emmaSideHappy = "characters/emma/emma happy.png"
    eveSideHappy = "characters/eve/eve happy.png"
    eveSideAngry = "characters/eve/eve angry.png"
    kathleenSideHappy = "characters/kathleen/kathleen happy.png"
    kathleenSideAngry = "characters/kathleen/kathleen angry.png"
    silviaSideHappy = "characters/silvia/silvia happy.png"
    silviaSideAngry = "characters/silvia/silvia angry.png"

    islaySideHappy = "characters/islay/islay happy.png"
    islaySideAngry = "characters/islay/islay angry.png"
    hudsonSideHappy = "characters/hudson/hudson happy.png"
    hudsonSideAngry = "characters/hudson/hudson angry.png"
    
    sideHappyImages0={}
    sideHappyImages0["emma"]=emmaSideHappy
    sideHappyImages0["eve"]=eveSideHappy
    sideHappyImages0["kathleen"]=kathleenSideHappy
    sideHappyImages0["silvia"]=silviaSideHappy
    sideHappyImages0["islay"]=islaySideHappy
    sideHappyImages0["hudson"]=hudsonSideHappy
    
    sideAngryImages0={}
    sideAngryImages0["emma"]=emmaSideAngry
    sideAngryImages0["eve"]=eveSideAngry
    sideAngryImages0["kathleen"]=kathleenSideAngry
    sideAngryImages0["silvia"]=silviaSideAngry
    sideAngryImages0["islay"]=islaySideAngry
    sideAngryImages0["hudson"]=hudsonSideAngry
    
    
    sideHappyImages1=sideHappyImages0
    sideHappyImages2=sideHappyImages0
    sideHappyImages3=sideHappyImages0
    
    sideAngryImages1=sideAngryImages0
    sideAngryImages2=sideAngryImages0
    sideAngryImages3=sideAngryImages0


    gainLovePointsIcon = "heart.png"
    gainLikePointsIcon = "note.png"
    loseLovePointsIconFull = "heart.png"
    loseLovePointsIconLeft = "heartLeft.png"
    loseLovePointsIconRight = "heartRight.png"
    loseLikePointsIcon = "sadface.png"

    
    updatePointsIcons0={}
    updatePointsIcons0["lover"]={}
    updatePointsIcons0["friend"]={}
    updatePointsIcons0["lover"]["gain"]=gainLovePointsIcon
    updatePointsIcons0["lover"]["lose"]={}
    updatePointsIcons0["lover"]["lose"]["full"]=loseLovePointsIconFull
    updatePointsIcons0["lover"]["lose"]["left"]=loseLovePointsIconLeft
    updatePointsIcons0["lover"]["lose"]["right"]=loseLovePointsIconRight
    updatePointsIcons0["friend"]["gain"]=gainLikePointsIcon
    updatePointsIcons0["friend"]["lose"]=loseLikePointsIcon
    
    updatePointsIcons1=updatePointsIcons0
    updatePointsIcons2=updatePointsIcons0
    updatePointsIcons3=updatePointsIcons0



label UpdateRelationPoints(updateTuple):
    
    $ toShow=len(updateTuple)
    $ characterIndex=toShow-1
    while characterIndex>=0:
        python:
            tempChar=updateTuple[characterIndex]
            gainPoints=(tempChar[1]>0)
            entrySide="left"
            if characterIndex%2==0:
                entrySide="right"
            entryHeight=1.0-int(characterIndex/2)*0.5
            
        call doRelationUpdateAnimate(tempChar[0], gainPoints, entrySide, entryHeight, tempChar[1], characterIndex)
        $ characterIndex-=1
        
        
    return
    

label doRelationUpdateAnimate(getWith, gainPoints, entrySide, entryHeight, gainAmount, spriteSet):
    python:
        if entrySide=="left":
            location=(-1.0, entryHeight)
        elif entrySide=="right":
            location=(2.0, entryHeight)
        else:
            raise Exception("Invalid entrySide: "+entrySide)
        loveGain=True
        
        
    if getWith=="emma":
        $ PointsEmma+=gainAmount
    elif getWith=="eve":
        $ PointsEve+=gainAmount
    elif getWith=="kathleen":
        $ PointsKathleen+=gainAmount
    elif getWith=="silvia":
        $ PointsSilvia+=gainAmount
    else:
        $ loveGain=False
        if getWith=="islay":
            $ PointsIslay+=gainAmount
        elif getWith=="hudson":
            $ PointsHudson+=gainAmount
        else:
            $ raise Exception("Invalid character: "+getWith)
    
    
    
    #Animate side sprite
    #If lover or friend
    if loveGain:
        #If gain or lose
        if gainPoints:
            #Gain Animation for Lover
            call PlayGainLoveFromSpriteSet(getWith, location[0], location[1], spriteSet)
        else:
            #lose Animation for Lover
            call PlayLoseLoveFromSpriteSet(getWith, location[0], location[1], spriteSet)
    else:
        #If gain or lose
        if gainPoints:
            #Animation for character
            call PlayGainLikeFromSpriteSet(getWith, location[0], location[1], spriteSet)
        else:
            #Animation for character
            call PlayLoseLikeFromSpriteSet(getWith, location[0], location[1], spriteSet)
                
    #Animation for the icon
    call PlayUpdateIconFromSpriteSet(loveGain, gainPoints, location[0], location[1]+((1.0-location[1])*0.5), spriteSet)
    return
    
label PlayGainLoveFromSpriteSet(getWith, x, y, spriteSet):
    if spriteSet==0:
        show image sideHappyImages0[getWith]:
            GetPointsAnimation(x, y)
    if spriteSet==1:
        show image sideHappyImages1[getWith]:
            GetPointsAnimation(x, y)
    if spriteSet==2:
        show image sideHappyImages2[getWith]:
            GetPointsAnimation(x, y)
    if spriteSet==3:
        show image sideHappyImages3[getWith]:
            GetPointsAnimation(x, y)
    return
    
label PlayLoseLoveFromSpriteSet(getWith, x, y, spriteSet):
    if spriteSet==0:
        show image sideAngryImages0[getWith]:
            LoseLovePointsAnimation(x, y)
    if spriteSet==1:
        show image sideAngryImages1[getWith]:
            LoseLovePointsAnimation(x, y)
    if spriteSet==2:
        show image sideAngryImages2[getWith]:
            LoseLovePointsAnimation(x, y)
    if spriteSet==3:
        show image sideAngryImages3[getWith]:
            LoseLovePointsAnimation(x, y)
    return
    
label PlayGainLikeFromSpriteSet(getWith, x, y, spriteSet):
    if spriteSet==0:
        show image sideHappyImages0[getWith]:
            GetPointsAnimation(x, y)
    if spriteSet==1:
        show image sideHappyImages1[getWith]:
            GetPointsAnimation(x, y)
    if spriteSet==2:
        show image sideHappyImages2[getWith]:
            GetPointsAnimation(x, y)
    if spriteSet==3:
        show image sideHappyImages3[getWith]:
            GetPointsAnimation(x, y)
    return
    
label PlayLoseLikeFromSpriteSet(getWith, x, y, spriteSet):
    if spriteSet==0:
        show image sideAngryImages0[getWith]:
            LoseLikePointsAnimation(x, y)
    if spriteSet==1:
        show image sideAngryImages1[getWith]:
            LoseLikePointsAnimation(x, y)
    if spriteSet==2:
        show image sideAngryImages2[getWith]:
            LoseLikePointsAnimation(x, y)
    if spriteSet==3:
        show image sideAngryImages3[getWith]:
            LoseLikePointsAnimation(x, y)
    return
    
label PlayUpdateIconFromSpriteSet(isLover, gainPoints, x, y, spriteSet):
    if isLover:
        if gainPoints:
            if spriteSet==0:
                show image updatePointsIcons0["lover"]["gain"]:
                    GainLovePointsIconAnimation(x, y)
            if spriteSet==1:
                show image updatePointsIcons1["lover"]["gain"]:
                    GainLovePointsIconAnimation(x, y)
            if spriteSet==2:
                show image updatePointsIcons2["lover"]["gain"]:
                    GainLovePointsIconAnimation(x, y)
            if spriteSet==3:
                show image updatePointsIcons3["lover"]["gain"]:
                    GainLovePointsIconAnimation(x, y)
        else:
            if spriteSet==0:
                show image updatePointsIcons0["lover"]["lose"]["full"]:
                    LoseLovePointsIconAnimationFull(x, y)
                show image updatePointsIcons0["lover"]["lose"]["left"]:
                    LoseLovePointsIconAnimationLeft(x, y)
                show image updatePointsIcons0["lover"]["lose"]["right"]:
                    LoseLovePointsIconAnimationRight(x, y)
            if spriteSet==1:
                show image updatePointsIcons1["lover"]["lose"]["full"]:
                    LoseLovePointsIconAnimationFull(x, y)
                show image updatePointsIcons1["lover"]["lose"]["left"]:
                    LoseLovePointsIconAnimationLeft(x, y)
                show image updatePointsIcons1["lover"]["lose"]["right"]:
                    LoseLovePointsIconAnimationRight(x, y)
            if spriteSet==2:
                show image updatePointsIcons2["lover"]["lose"]["full"]:
                    LoseLovePointsIconAnimationFull(x, y)
                show image updatePointsIcons2["lover"]["lose"]["left"]:
                    LoseLovePointsIconAnimationLeft(x, y)
                show image updatePointsIcons2["lover"]["lose"]["right"]:
                    LoseLovePointsIconAnimationRight(x, y)
            if spriteSet==3:
                show image updatePointsIcons3["lover"]["lose"]["full"]:
                    LoseLovePointsIconAnimationFull(x, y)
                show image updatePointsIcons3["lover"]["lose"]["left"]:
                    LoseLovePointsIconAnimationLeft(x, y)
                show image updatePointsIcons3["lover"]["lose"]["right"]:
                    LoseLovePointsIconAnimationRight(x, y)
    else:
        if gainPoints:
            if spriteSet==0:
                show image updatePointsIcons0["friend"]["gain"]:
                    GainLikePointsIconAnimation(x, y)
            if spriteSet==1:
                show image updatePointsIcons1["friend"]["gain"]:
                    GainLikePointsIconAnimation(x, y)
            if spriteSet==2:
                show image updatePointsIcons2["friend"]["gain"]:
                    GainLikePointsIconAnimation(x, y)
            if spriteSet==3:
                show image updatePointsIcons3["friend"]["gain"]:
                    GainLikePointsIconAnimation(x, y)
        else:
            if spriteSet==0:
                show image updatePointsIcons0["friend"]["lose"]:
                    LoseLikePointsIconAnimation(x, y)
            if spriteSet==1:
                show image updatePointsIcons1["friend"]["lose"]:
                    LoseLikePointsIconAnimation(x, y)
            if spriteSet==2:
                show image updatePointsIcons2["friend"]["lose"]:
                    LoseLikePointsIconAnimation(x, y)
            if spriteSet==3:
                show image updatePointsIcons3["friend"]["lose"]:
                    LoseLikePointsIconAnimation(x, y)
                    
    return


transform GetPointsAnimation(x, y):
    xzoom (abs(x)/x)
    rotate 360-(20*(abs(x)/x))
    xalign x yalign y
    linear 1.0 xalign x-(0.83*(abs(x)/x))
    pause 0.15
    linear 0.05 yalign y-0.04
    linear 0.05 yalign y
    
    time 3.0
    linear 1.0 xalign x
    
    
transform LoseLovePointsAnimation(x, y):
    xzoom (abs(x)/x)
    rotate 360-(20*(abs(x)/x))
    xalign x yalign y
    linear 1.0 xalign x-(0.83*(abs(x)/x))
    time 3.0
    
    linear 1.0 xalign x
    
    
transform LoseLikePointsAnimation(x, y):
    xzoom (abs(x)/x)
    rotate 360-(20*(abs(x)/x))
    xalign x yalign y
    linear 1.0 xalign x-(0.83*(abs(x)/x))
    
    block:
        linear 0.1 xalign x-(0.84*(abs(x)/x))
        linear 0.1 xalign x-(0.82*(abs(x)/x))
        repeat
        
    time 3.0
    
    linear 1.0 xalign x yalign y
    
    
transform GainLovePointsIconAnimation(x, y):
    alpha 0.0
    pause 1.2
    alpha 1.0
    xalign x-(1.025*(abs(x)/x)) yalign y-0.4
    parallel:
        ease 0.3 xalign x-(1.01*(abs(x)/x))
        ease 0.3 xalign x-(1.04*(abs(x)/x))
        repeat
    parallel:
        linear 2.0 yalign y-0.5
    parallel:
        pause 1.0
        linear 1.0 alpha 0.0
    
transform GainLikePointsIconAnimation(x, y):
    alpha 0.0
    pause 1.2
    alpha 1.0
    xalign x-(1.025*(abs(x)/x)) yalign y-0.4
    parallel:
        ease 0.3 xalign x-(1.01*(abs(x)/x))
        ease 0.3 xalign x-(1.04*(abs(x)/x))
        repeat
    parallel:
        linear 2.0 yalign y-0.5
    parallel:
        pause 1.0
        linear 1.0 alpha 0.0

#Full heart that shakes
transform LoseLovePointsIconAnimationFull(x, y):
    alpha 0.0
    pause 1.0
    alpha 1.0
    xalign x-(1.025*(abs(x)/x)) yalign y-0.45
    
    block:
        linear 0.1 xoffset -4
        linear 0.1 xoffset 4
        repeat
    time 1.8
    alpha 0.0
    
#Left side of the heart when broken
transform LoseLovePointsIconAnimationLeft(x, y):
    alpha 0.0
    time 1.8
    alpha 1.0
    parallel:
        heartSwingSpin(-1)
    parallel:
        heartSwingMove(-1, x, y)
        
    #Drop offscreen
    pause 0.3
    easeout 0.2 yoffset 750

#Right side of the heart when broken
transform LoseLovePointsIconAnimationRight(x, y):
    alpha 0.0
    time 1.8
    alpha 1.0
    parallel:
        heartSwingSpin(1)
    parallel:
        heartSwingMove(1, x, y)
        
    #Drop offscreen
    pause 0.2
    easeout 0.2 yoffset 750
        
        
transform LoseLikePointsIconAnimation(x, y):
    alpha 0.0
    pause 1.2
    alpha 1.0
    xalign x-(1.025*(abs(x)/x)) yalign y-0.45
    
    parallel:
        pause 1.0
        linear 1.0 alpha 0.0
    parallel:
        linear 2.0 yalign y-0.35


transform heartSwingSpin(sign):
    easein 0.45 rotate 210*sign #Needs to be 30 less at all times
    easein 0.5 rotate 150*sign
    easein 0.5 rotate 180*sign
    easein 0.5 rotate 165*sign

transform heartSwingMove(sign, x, y):
    anchor(0.0, 0.0)
    around(int((x-1.025*(abs(x)/x))*config.screen_width)-int(19+19*(abs(x)/x)), int((y-0.45)*config.screen_height))
    angle 30*sign
    radius 17
    
    easein 0.45 angle 240*sign #Needs to be 30 more at all times
    easein 0.5 angle 180*sign
    easein 0.5 angle 210*sign
    easein 0.5 angle 195*sign

    