#Miscellaneous animation functions/positions used in the game

#Defines custom postions
init:
    $ leftMiddle = Position(xcenter=0.25, ypos=1.0)

#Pause while the screen shakes
image pauseForVPunch:
    pause 1.5
    
#Make a character bob
transform speakingBob:
    linear 0.05 yoffset -10
    linear 0.05 yoffset 0
    
# Make a sprite bob up and down at random
transform fakeBobTalk:
    block:
        #Wait between bobs
        block:
            choice:
                pause 2
            choice:
                pause 2.5
            choice:
                pause 3
            choice:
                pause 3.5

        #1/3 chance to get a second bob
        block:
            choice:
                speakingBob
                pause 0.1
            choice:
                pass
            choice:
                pass
                
        speakingBob
        repeat
    
#Make a sprite turn around back and forth at random
transform randomLookAround:
    pause 3
    block:
        xzoom -1
        choice:
            pause 0.7
        choice:
            pause 2.5
        choice:
            pause 3
        xzoom 1
        choice:
            pause 0.7
        choice:
            pause 2.5
        choice:
            pause 3
        repeat