#Animation for ganing or losing points with someone

#Define side images for gaining/losing points with characters
image emmaSideHappy = "characters/emma/emma happy.png"
image emmaSideAngry = "characters/emma/emma angry.png"
image eveSideHappy = "characters/eve/eve happy.png"
image eveSideAngry = "characters/eve/eve angry.png"
image kathleenSideHappy = "characters/kathleen/kathleen happy.png"
image kathleenSideAngry = "characters/kathleen/kathleen angry.png"
image silviaSideHappy = "characters/silvia/silvia happy.png"
image silviaSideAngry = "characters/silvia/silvia angry.png"

image islaySideHappy = "characters/islay/islay happy.png"
image islaySideAngry = "characters/islay/islay angry.png"
image hudsonSideHappy = "characters/hudson/hudson happy.png"
image hudsonSideAngry = "characters/hudson/hudson angry.png"

#Define icons to show gaining/losing points
image gainLovePointsIcon = "heart.png"
image gainLikePointsIcon = "note.png"
image loseLovePointsIcon = "sadface.png"
image loseLikePointsIcon = "sadface.png"




label HideAllSideSprites:
    hide emmaSideHappy
    hide emmaSideAngry
    hide eveSideHappy
    hide eveSideAngry
    hide kathleenSideHappy
    hide kathleenSideAngry
    hide silviaSideHappy
    hide silviaSideAngry
    
    hide islaySideHappy
    hide islaySideAngry
    hide hudsonSideHappy
    hide hudsonSideAngry
    
    hide gainLovePointsIcon
    hide gainLikePointsIcon
    hide loseLovePointsIcon
    hide loseLikePointsIcon
    
    return


label UpdateRelationPoints(updateTuple):
    
    call HideAllSideSprites
    
    $ characterIndex=0
    $ toShow=len(updateTuple)
    while characterIndex<toShow:
        python:
            tempChar=updateTuple[characterIndex]
            gainPoints=(tempChar[1]>0)
            entrySide="left"
            if characterIndex%2==0:
                entrySide="right"
            entryHeight=1.0-int(characterIndex/2)*0.5
            
        call doRelationUpdateAnimate(tempChar[0], gainPoints, entrySide, entryHeight, tempChar[1])
        $ characterIndex+=1
        
        
    return
    

label doRelationUpdateAnimate(getWith, gainPoints, entrySide, entryHeight, gainAmount):
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
        if gainPoints:
            show emmaSideHappy:
                GetPointsAnimation(location[0], location[1])
        else:
            show emmaSideAngry:
                LosePointsAnimation(location[0], location[1])
            
    elif getWith=="eve":
        $ PointsEve+=gainAmount
        if gainPoints:
            show eveSideHappy:
                GetPointsAnimation(location[0], location[1])
        else:
            show eveSideAngry:
                LosePointsAnimation(location[0], location[1])
            
    elif getWith=="kathleen":
        $ PointsKathleen+=gainAmount
        if gainPoints:
            show kathleenSideHappy:
                GetPointsAnimation(location[0], location[1])
        else:
            show kathleenSideAngry:
                LosePointsAnimation(location[0], location[1])
            
    elif getWith=="silvia":
        $ PointsSilvia+=gainAmount
        if gainPoints:
            show silviaSideHappy:
                GetPointsAnimation(location[0], location[1])
        else:
            show silviaSideAngry:
                LosePointsAnimation(location[0], location[1])
            
    else:
        python:
            loveGain=False
        if getWith=="islay":
            $ PointsIslay+=gainAmount
            if gainPoints:
                show islaySideHappy:
                    GetPointsAnimation(location[0], location[1])
            else:
                show islaySideAngry:
                    LosePointsAnimation(location[0], location[1])
                
        elif getWith=="hudson":
            $ PointsHudson+=gainAmount
            if gainPoints:
                show hudsonSideHappy:
                    GetPointsAnimation(location[0], location[1])
            else:
                show hudsonSideAngry:
                    LosePointsAnimation(location[0], location[1])
                    
        else:
            python:
                raise Exception("Invalid character: "+getWith)
                    
        
    if loveGain:
        if gainPoints:
            show gainLovePointsIcon:
                GetPointsIconAnimation(location[0], location[1])
        else:
            show loseLovePointsIcon:
                LosePointsIconAnimation(location[0], location[1])
    else:
        if gainPoints:
            show gainLikePointsIcon:
                GetPointsIconAnimation(location[0], location[1])
        else:
            show loseLikePointsIcon:
                LosePointsIconAnimation(location[0], location[1])
        
    
    return
    



transform GetPointsAnimation(x, y):
    xzoom (abs(x)/x)
    rotate 360-(20*(abs(x)/x))
    xalign x yalign y
    linear 1.0 xalign x-(0.83*(abs(x)/x)) yalign y
    pause 0.15
    linear 0.05 yalign y-0.04
    linear 0.05 yalign y
    pause 0.75
        
    linear 1.0 xalign x yalign y
    
    
    
    
transform GetPointsIconAnimation(x, y):
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


transform LosePointsAnimation(x, y):
    xzoom (abs(x)/x)
    rotate 360-(20*(abs(x)/x))
    xalign x yalign y
    linear 1.0 xalign x-(0.83*(abs(x)/x)) yalign y
    
    block:
        linear 0.1 xalign x-(0.84*(abs(x)/x)) yalign y
        linear 0.1 xalign x-(0.82*(abs(x)/x)) yalign y
        repeat
        
    time 2.0
    
    linear 1.0 xalign x yalign y

transform LosePointsIconAnimation(x, y):
    alpha 0.0
    pause 1.2
    alpha 1.0
    xalign x-(1.025*(abs(x)/x)) yalign y-0.45
    
    parallel:
        pause 1.0
        linear 1.0 alpha 0.0
    parallel:
        linear 2.0 yalign y-0.35

    