#Meet Silvia
#Possible to gain +1 Points with Silvia

#Arrive at Dorm
label Day1_Dorm:
    scene bg dorm
    narrator             "You collapse onto your bed, totally and utterly exhausted. You only had one class and barely lifted anything, yet you feel absolutely spent. That hangover probably didn’t help your energy levels either."
    narrator             "But you’re home now, and you totally lucked out in the dorm lottery on getting a single room, so it’s *just* you. Maybe you can grab a snack from your hoard, take a nap, enjoy the quiet…"
    #Hear music, look for source, see Silvia
    narrator             "Suddenly, a wave pop punk music blasts into your head."
    narrator             "???!!! Where is that coming from?!"
    narrator             "You realize your window is open. Climbing up, you peek out from between your curtains and see a girl leaning against the garage door, probably convinced the area was just isolated enough to hang out."
    narrator             "Your room is situated right on top of your building’s garage, where the custodians take out the garbage and bring in cleaning apparatus every so often. "
    narrator             "And you recognize her! She actually offered you a ride home in her truck when she saw you stumbling around drunk last night at the party, but you declined not wanting to inconvenience her."
    narrator             "You kind of wish you hadn’t. {p}She’s really pretty."
    narrator             "She pulls out a cigarette, sparks it up, and takes a long drag. Judging from the poor music quality, you deduce it’s coming from her phone speaker."
    narrator             "And in an instant, a dank, skunk-esque smell has permeated your whole room. Oh. That’s not a cigarette she’s holding, is it?"
    player               "HEY!" with hpunch
    narrator             "The girl jumps a bit in surprise, turns around, and leers up at you."
    #Start chatting with Silvia
    $ lastSpoke="silvia"
    show silvia base at center with Dissolve(0.5)
    silviaUnknownSpeach  "Hey there!"
    player               "Hi! Your music is kinda loud!"
    silviaUnknownSpeach  "What, do you not like Lynx-182?"
    player               "I mean, they’re pretty good I guess. But, I can hear it from my room, which also now smells a lot like… uh…"
    silviaUnknownSpeach  "Like weed? I’m so sorry dude! I didn’t even consider that could be someone’s room."
    player               "Don’t worry about it! I’ve actually never heard this song before. I like it!"
    #Silvia offers you join her
    silviaUnknownSpeach  "Wanna come down and listen? I was planning on going over to my other spot on the flip side of the building. You can also have some if you want. I kinda owe you for smelling up your room and all."
    narrator             "You had been planning to relax, but you’d never pass up the opportunity to talk to a cute girl. Especially one this chill."
    player               "Yeah, I’m cool with that. I’ll be right down."
    narrator             "Wait… Hm. This window isn’t that high up. You could jump down from here; that would impress her for sure. But you also aren’t the most coordinated person… "
    narrator             "But then on the other hand, it could be worth the risk…"
    $ renpy.choice_for_skipping()
    narrator "What should you do?"
    menu:
        "Risk it and jump down to her from the window like an anime protagonist":
            jump Day1_MeetSilvia_JumpOutWindow
        "Take the safe route and exit through the front door of your building":
            jump Day1_MeetSilvia_ExitNormally
           
#Jump out of the window to join Silvia (+1 Silvia)
label Day1_MeetSilvia_JumpOutWindow:
    narrator      "You open the window and shimmy out the bug screen."
    silviaUnknown "Uh… what are you doing?"
    player        "Coming down, like I said."
    narrator      "You tried to muster that out in a cool and collected tone, but now that your head is half out the window it looks like a much steeper drop than you had anticipated."
    narrator      "No. You have to commit to the bit."
    narrator      "You put your legs through the window one-by-one and sit down on the ledge in order to try and find a slightly lower foothold to anchor on."
    narrator      "You feel a skinny ledge beneath you- a row of bricks jutting out from the building. Ok. Ok yeah you can do this."
    narrator      "You bring the rest of your body out the window, holding your weight firmly against the thin ledge. It looks like you’re about 8 feet up in the air."
    narrator      "You’re like what- 5’5? This is only a little over 2 feet taller than you! It’s fine. This is totally fine."
    narrator      "Now jump.{p}Uh.{p}Ok now JUMP."
    narrator      "Alright. You’re kind of paralyzed in fear now. If you wait any longer, you’re going to look like a complete dumbass."
    narrator      "Ok let’s do it{cps=3}... F{/cps}OR THE CUTE GIRL!"
    player        "Er. Yeah so. Here I come!"
    narrator      "You close your eyes, take a deep breath, and kick off the ledge. Your stomach drops as you fall for way longer than you expect."
    
    show pauseForVPunch with vpunch
    narrator      "As your feet connect to the ground, a surge of sharp pain travels up your feet and into your ankles."
    narrator      "You can feel yours eyes tearing up from the stinging shockwave that should have rendered your feet useless, but you suck it up in desperation."
    narrator      "You pull yourself up, cool as a cucumber."
    
    call UpdateRelationPoints((("silvia", 1), ))
        
    silviaUnknown "DUDE THAT WAS SO RAD?! I didn’t think you were actually going to do it!!!"
    player        "Heh, thanks! Neither did I!"
    
#Exit the building to join Silvia
label Day1_MeetSilvia_ExitNormally:
    narrator "You dab"  
    
    jump DetermineFinalLover