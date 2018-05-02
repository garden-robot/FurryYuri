

#Initiate the player
label definePlayer:
    $ playerName="Jude"
    if DebugMode==False:
        $ playerName = renpy.input("What is your name, Magical Boi?")
    define player = Character("[playerName]")
    return

#Define all other characters
init 1:
    define narrator = Character(what_italic=True)
    define actionText = Character("", what_bold=True)

    #   ---Known Characters---
    #Datable
    define emmaSpeach = Character("Emma", what_color="#ef5878", who_color="#ef0739")
    define eveSpeach = Character("Eve", what_color="#d72424", who_color="#a71616")
    define kathleenSpeach = Character("Kathleen", what_color="#6699ff", who_color="#9a9ae5")
    define silviaSpeach = Character("Silvia", what_color="#8cff66", who_color="#2db300")
    
    #Friends
    define islaySpeach = Character("Pwofessow Buwgess")
    define hudsonSpeach = Character("Hudson")
    define adamSpeach = Character("Adam")
    
    # Post-date replacements
    define darren = Character("Darren")
    define joey = Character("Joey")
    define easton = Character("Easton")

    #Minor
    define professorSpeach = Character("Professor")

    #   ---Unknown Characters---    
    #Datable Unknown
    define emmaUnknownSpeach = Character("???", what_color="#ef5878", who_color="#ef0739")
    define eveUnknownSpeach = Character("???", what_color="#d72424", who_color="#a71616")
    define kathleenUnknownSpeach = Character("???", what_color="#6699ff", who_color="#9a9ae5")
    define silviaUnknownSpeach = Character("???", what_color="#8cff66", who_color="#2db300")
    
    #Friends Unknown
    define islayUnknownSpeach = Character("???")
    define hudsonUnknownSpeach = Character("???")
    define adamUnknownSpeach = Character("???")
    
init python:
    style.say_dialogue.slow_cps = 100
    
    lastSpoke=None
    
    #Make the given character bob when they talk
    def animateSpeach(whoName, whoSpeach, what, **kwargs):
        global lastSpoke
        lastSpoke=whoName
        renpy.show(whoName, at_list=[ speakingBob() ])
        whoSpeach(what, **kwargs)
        
    #Special say functions so people bob
    def emma(what, **kwargs):
        animateSpeach("emma", emmaSpeach, what, **kwargs)
    def eve(what, **kwargs):
        animateSpeach("eve", eveSpeach, what, **kwargs)
    def kathleen(what, **kwargs):
        animateSpeach("kathleen", kathleenSpeach, what, **kwargs)
    def silvia(what, **kwargs):
        animateSpeach("silvia", silviaSpeach, what, **kwargs)
    def islay(what, **kwargs):
        animateSpeach("islay", islaySpeach, what, **kwargs)
    def hudson(what, **kwargs):
        animateSpeach("hudson", hudsonSpeach, what, **kwargs)
        
    def professor(what, **kwargs):
        animateSpeach("professor", professorSpeach, what, **kwargs)
    def adam(what, **kwargs):
        animateSpeach("adam", adamSpeach, what, **kwargs)

    def emmaUnknown(what, **kwargs):
        animateSpeach("emma", emmaUnknownSpeach, what, **kwargs)
    def eveUnknown(what, **kwargs):
        animateSpeach("eve", eveUnknownSpeach, what, **kwargs)
    def kathleenUnknown(what, **kwargs):
        animateSpeach("kathleen", kathleenUnknownSpeach, what, **kwargs)
    def silviaUnknown(what, **kwargs):
        animateSpeach("silvia", silviaUnknownSpeach, what, **kwargs)
    def islayUnknown(what, **kwargs):
        animateSpeach("islay", islayUnknownSpeach, what, **kwargs)
    def hudsonUnknown(what, **kwargs):
        animateSpeach("hudson", hudsonUnknownSpeach, what, **kwargs)
        
    def professorUnknown(what, **kwargs):
        animateSpeach("professor", professorUnknownSpeach, what, **kwargs)
    def adamUnknown(what, **kwargs):
        animateSpeach("adam", adamUnknownSpeach, what, **kwargs)
        
    def islayOwOSpeach(what, **kwargs):
        global lastSpoke
        lastSpoke="islay"
        islaySpeach(what, **kwargs)
        
#Make a character bob
transform speakingBob:
    linear 0.05 yoffset -10
    linear 0.05 yoffset 0