#First scene of the game. Wake up, choose clothing for the day
#Possible to gain +1 with Emma, or Eve, or Kathleen, or Silvia

#Wake up, get read to leave
label Morning1_Intro:
    scene bg room
    narrator "DING DING DINGA DING DING DINGA DINGA DING DING DINGA DINGA -click-" with vpunch
    player   "Ugh.... headache…. Great…"
    player   ".. ???!"
    player   "Oh dang! It’s 8:20 AM! I have a class in ten minutes!"
    narrator "You get up, and quickly decide what you want to wear."
    
    #Get Dressed
    $ renpy.choice_for_skipping()
    player   "Oh jeez, gotta rush… What look should I go for?"
    menu:
        "Sporty":
            jump Morning1_IntroSporty
        "Indie":
            jump Morning1_IntroIndie
        "Tough":
            jump Morning1_IntroTough
        "Girly":
            jump Morning1_IntroGirly
    
#Dress Sporty
label Morning1_IntroSporty:
    player   "Sporty it is!"
    if DateableKathleen:
        narrator "You open your dresser and pull out some sports leggings and a T shirt."
        python:
            PointsKathleen+=1
    else:
        narrator "You open your dresser and find... nothing. You thought you owned some sports leggings and a T shirt, but aparently not?"
        player   "I guess it's a plain shirt and jeans for me..."
        
    python:
        Morning1Choice_Sporty=True
    jump Morning1_IntroChoiceDone
    
#Dress Indie
label Morning1_IntroIndie:
    player   "Indie it is!!"
    narrator "You open your dresser and pull out a baggy sweater and a pair of old jeans torn at the knee."
    narrator "You have always passed it off as style, but in actuality you tore them after crashing your bike into a dumpster."
    narrator "No one has to know that though."
    python:
        Morning1Choice_Indie=True
        PointsSilvia+=1
    jump Morning1_IntroChoiceDone
    
#Dress Though
label Morning1_IntroTough:
    player   "Tough it is!"
    narrator "You open up your dresser and spot what you want immediately."
    narrator "A shirt with a design of a Pirate Ship surfing on an active volcano, as the captain stands valiantly at the helm and punches a Lava-Shark right in the nose. How could you have considered any other option? This will be your aesthetic for life."
    python:
        Morning1Choice_Tough=True
        PointsEmma+=1
    jump Morning1_IntroChoiceDone
    
#Dress Girly
label Morning1_IntroGirly:
    player   "Girly it is then~"
    narrator "You open your dresser and see a cute, knee-length black skirt with white stripes and a blue blouse. You then go to the closet and grab some thigh-highs to complete your outfit. This was written by a transgirl who is trying so hard to be girly but thinks literally everything femme is beautiful and looks good >_>"
    python:
        Morning1Choice_Girly=True
        PointsEve+=1
    jump Morning1_IntroChoiceDone
    
#Leave for class
label Morning1_IntroChoiceDone:
    narrator "After hastily shoving your laptop in your bag and a quick look in the mirror, a you stumble out of the front door of your dorm room knowing you wouldn’t have enough time for breakfast or basic hygiene. Probably not a good idea considering your mild hangover."
    narrator "You really shouldn’t have gone to that party yesterday- but now that you’re in university, you figured it was important to get out a little more and make some friends. Even if you threw up a little in the process. You still aren’t sure if that was the cheap beer, or the anxiety."
    narrator "But you did meet some nice people- and some cute girls… Maybe you’ll run into some of them today?"
    jump Day1_LectureHall
   

