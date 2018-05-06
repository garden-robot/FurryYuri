#Code related to making characters blink

init python:    
    #Get the amount of time to pause between blinks
    def getPauseTime(trans, st, at):
        waitTimes=[0.2, 1.5, 2.7, 3.3, 4.0, 6.0, 6.5, 7.2, 7.5, 7.7, 8.0]
        trans.pauseFor=waitTimes[renpy.random.randint(0, len(waitTimes)-1)]
        return None
    
    #Wait for a period of time
    def waitPauseTime(trans, st, at):
        if st<=trans.pauseFor:
            return 0
        else:
            return None
            
#Animaton to make a character close their eyes, and open them back up
transform makeBlink(characterName):
    ConditionSwitch(
    'lastSpoke != "'+characterName+'"', darkenSprite(characterName, "base"),
    "True", "characters/"+characterName+"/"+characterName+" base.png"
    )
    startBlink(characterName)
    repeat
    
#Initiates a blink
transform startBlink(characterName):
    randomizeBlinkWait
    animateBlink(characterName)

#Picks a random amount of time to wait until the next blink
transform randomizeBlinkWait:
    function getPauseTime
    function waitPauseTime
    
#Changes a characters sprite to the blinking frames
transform animateBlink(characterName):
    #Darken them if they arnt talking
    ConditionSwitch(
    'lastSpoke != "'+characterName+'"', darkenSprite(characterName, "blinking"),
    "True", "characters/"+characterName+"/"+characterName+" blinking.png"
    )
    pause 0.2