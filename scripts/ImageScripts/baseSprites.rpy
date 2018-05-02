#All images for base sprites 

init python:
    #Time to wait before any special animations (such as blinks) occur
    waitTime_specialIdleAnimation=1.0 

#Emma
image emma base:
    zoom emmaSizeScale
    baseAnimation("emma")
    
#Eve
image eve base:
    zoom eveSizeScale
    baseAnimation("eve")

#Kathleen
image kathleen base:
    zoom kathleenSizeScale
    baseAnimation("kathleen")

#Silvia
image silvia base:
    zoom silviaSizeScale
    baseAnimation("silvia")

#Islay
image islay base:
    zoom islaySizeScale
    baseAnimation("islay")

#Hudson
image hudson base:
    zoom hudsonSizeScale
    baseAnimation("hudson")
        
#Generic animaton for all base sprites
transform baseAnimation(characterName):
    
    #Determine if sprite should be darkened out
    ConditionSwitch(
    'lastSpoke != "'+characterName+'"', darkenSprite(characterName, "base"),
    "True", "characters/"+characterName+"/"+characterName+" base.png"
    )
    
    pause waitTime_specialIdleAnimation
    makeBlink(characterName)