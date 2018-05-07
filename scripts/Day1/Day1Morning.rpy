#First scene of the game. Wake up, choose clothing for the day
#Possible to gain +1 with Emma, or Eve, or Kathleen, or Silvia

#Wake up, get read to leave
label Morning1_Intro:
    scene bg room
    narrator "DING DING DINGA DINGA DING DING DINGA DINGA DING DING DINGA DINGA -click-" with vpunch
    
    
    player   "Ugh.... headache…. Great…"
    player   ".. ???!"
    player   "Oh jeez! It’s 8:20 AM! I have a class in ten minutes!"
    narrator "You get up, and quickly decide what you want to wear."
    
    #Get Dressed
    $ renpy.choice_for_skipping()
    player   "Ok ok ok, gotta rush… What look should I go for?"
    menu:
        "Look for something comfy.":
            jump Morning1_IntroHonesty
        "Look for something stylish.":
            jump Morning1_IntroFlair
        "Look through your weird shirt collection.":
            jump Morning1_IntroGuts
        "Look for something femme.":
            jump Morning1_IntroCompassion
    
#Dress Sporty
label Morning1_IntroHonesty:
    if DateableKathleen:
        narrator "You open your dresser and pull out some sports leggings and a T shirt."
    else:
        narrator "You open your dresser and find... nothing. You thought you owned some sports leggings and a T shirt, but aparently not?"
        player   "I guess it's a plain shirt and jeans for me..."
        
    python:
        Morning1Choice_Honesty=True
    jump Morning1_IntroChoiceDone
    
#Dress Indie
label Morning1_IntroFlair:
    narrator "You open your dresser and pull out a baggy sweater and a pair of old jeans torn at the knee."
    narrator "You have always passed it off as style, but in actuality you tore them after crashing your bike into a dumpster.{p}No one has to know that though."
    python:
        Morning1Choice_Flair=True
    jump Morning1_IntroChoiceDone
    
#Dress Though
label Morning1_IntroGuts:
    narrator "You open up your dresser and dig through your prised collection of cotton oddities. And then you spot the perfect shirt- ol’ reliable."
    narrator "As you unfold it, you take a moment to appreciate its glorious design- a Pirate Ship sailing against lava spurting from an active volcano. Its captain stands valiantly at the helm as she punches a Lava-Shark right in the nose. "
    narrator "Perfect. A flawless work of art. How could you have considered anything else?"
    
    python:
        Morning1Choice_Guts=True
    jump Morning1_IntroChoiceDone
    
#Dress Girly
label Morning1_IntroCompassion:
    narrator "You open your dresser and see a cute little mint dress that you bought last summer. "
    python:
        Morning1Choice_Compassion=True
    jump Morning1_IntroChoiceDone
    
#Leave for class
label Morning1_IntroChoiceDone:
    narrator "After hastily shoving your laptop in your bag and a quick look in the mirror, a you stumble out of the front door of your dorm room knowing you wouldn’t have enough time for breakfast or basic hygiene. Probably not a good idea considering your mild hangover."
    narrator "You really shouldn’t have gone to that party yesterday but now that you’re in university, you figured it was important to get out a little more and make some friends."
    narrator "Even if you threw up a little in the process. You still aren’t sure if that was the cheap beer, or the anxiety."
    narrator "But you did meet some nice people- and some cute girls… Maybe you’ll run into some of them today?"
    jump Day1_LectureHall
   

