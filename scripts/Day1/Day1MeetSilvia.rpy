#Meet Silvia
#Possible to gain +1 Points with Silvia

#Arrive at Dorm
label Day1_Dorm:
    scene bg dorm
    narrator             "You collapse onto your bed, totally and utterly exhausted. You only had one class and barely lifted anything, yet you feel absolutely spent. That hangover probably didn’t help your energy levels either."
    narrator             "But you’re home now, and you totally lucked out in the dorm lottery on getting a single room, so it’s {i}just{/i} you. Maybe you can grab a snack from your stash, take a nap, enjoy the quiet…"
    #Hear music, look for source, see Silvia
    narrator             "Suddenly, a wave pop punk music blasts into your head."
    narrator             "???!!! Where is that coming from?!"
    narrator             "You realize your window is open. Climbing up, you peek out from between your curtains and see a girl leaning against the garage door, probably convinced the area was just isolated enough to hang out."
    narrator             "Your room is situated right on top of your building’s garage, where the custodians take out the garbage and bring in cleaning apparatus every so often. "
    narrator             "And you recognize her! She actually offered you a ride home in her truck when she saw you stumbling around drunk last night at the party, but you declined not wanting to inconvenience her."
    narrator             "You kind of wish you hadn’t. {w}She’s really pretty."
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
    silviaUnknownSpeach  "Wanna come down and listen? We can go over to my other spot on the flip side of the building. Here, let me burn this out really quick… I’m so sorry for smelling up your room!"
    player               "No worries! I’ll keep the window open and I’m sure it’ll air out ok!"
    narrator             "You had been planning to relax, but you’d never pass up the opportunity to talk to a cute girl. Especially one this chill."
    player               "I’m also totally down to hang. I’ll be right out."
    narrator             "Wait… Hm. This window isn’t that high up. You could jump down from here; that would impress her for sure. But you also aren’t the most coordinated person… "
    narrator             "But then on the other hand, it could be worth the risk…"
    $ renpy.choice_for_skipping()
    narrator "What should you do?"
    menu:
        "Risk it and jump down to her like an anime protagonist":
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
    narrator      "Now jump.{w} Uh.{w} Ok now JUMP."
    narrator      "Alright. You’re kind of paralyzed in fear now. If you wait any longer, you’re going to look like a complete dumbass."
    narrator      "Ok let’s do it{cps=3}... F{/cps}OR THE CUTE GIRL!"
    player        "Er. Yeah so. Here I come!"
    narrator      "You close your eyes, take a deep breath, and kick off the ledge. Your stomach drops as you fall for way longer than you expect."
    
    show pauseForVPunch with vpunch
    narrator      "As your feet connect to the ground, a surge of sharp pain travels up your feet and into your ankles."
    if Kathleen_Choice_Day1AskExplination==False:
        narrator      "You really wish you hadn’t done more than 8 reps."
    narrator      "You can feel yours eyes tearing up from the stinging shockwave that should have rendered your feet useless, but you suck it up in desperation."
    narrator      "You pull yourself up, cool as a cucumber."
    
    call UpdateRelationPoints((("silvia", 1), ))
    
    silviaUnknown "DUDE THAT WAS SO RAD?! I didn’t think you were actually going to do it!!!"
    player        "Heh, thanks! Neither did I!"
    
    silviaUnknown "I’m Silvia by the way."
    player        "Nice to meet you Silvia, I’m [playerName]"
    narrator      "You shake her hand jokingly and she laughs in response."
    silvia        "You wanna go to that other spot?"
    player        "Yeah, sure!"
    
label Day1_MeetSilvia_LeaveForSpot:
    narrator      "She puts her phone, still blasting music, in her back pocket and leads the way ahead of you."
    silvia        "You know, you look kind if familiar now that I’m seeing you up close. Have we met before?"
    player        "Yeah, haha I think you offered me a ride home the other night."
    silvia        "OH YEAHHH you were that super drunk person that tripped over yourself on the sidewalk when I was on my way home! You had me pretty worried; I’m glad you made it back ok."
    player        "Thanks… yeah I’m not the best at holding my alcohol, admittedly."
    silvia        "Wish I could say the same! Maybe then I’d be a little more mindful of my drinking."
    player        "Ooooh got any stories?"
    silvia        "Oh jeez… too many to count. I think my crowning moment was that time I blacked out at Christmas mass. My mom got so mad at me but it’s not like I was the one that bought the tequila, you know?"
    narrator      "You snort as you laugh."
    player        "Christmas mass?! You’ve got style, I’ll give you that."
    silvia        "Ha! I get that a lot."
    narrator      "The two of you arrive within an alleyway tucked away behind your dorm building and the one next door. It seems almost labyrinth-like in its placement, in that you probably wouldn’t have ever noticed it had Silvia not led you here."
    narrator      "The walls are totally covered in graffiti, though it’s all drawn in sidewalk chalk. A lot of it seems to be themed around the beginning of the new school year."
    silvia        "Here we are! This is usually my go to spot, but sometimes it gets a bit stuffy."
    player        "Dang, did students draw all of this?"
    silvia        "Yeah, these walls are historic to Oxford U. This place used to be considered the underground meet up spot for DUI bands on campus back in the day. People would spray paint their feelings all up and down these walls."
    silvia        "Eventually, as the university rose in status, the suits at the top figured they couldn’t have their precious institution represented this way, so they started to try to counter it. Underneath that paint are layers and layers of graffiti and subsequent cover up. "
    silvia        "Luckily, the students and school reached a kind of agreement with this chalk alternative. Still not as cool in my opinion."
    player        "So rad! How do you know all of that?"
    silvia        "My dad went here! Told me all about it."
    player        "Neat!"
    silvia        "Speaking of chalk, wanna add something with me? Since we’re here and all. It usually stays up for at least a quarter before it gets hosed down."
    player        "I’m down."
    narrator      "Silvia bends over to grab a few pieces of sidewalk chalk lying at the base of the wall, left for anyone to use you assume. She passes you a blue piece and takes the pink for herself."
    narrator      "What should you draw?"
    
    
#Exit the building to join Silvia
label Day1_MeetSilvia_ExitNormally:
    narrator       "You dab"  
    
    jump GoToEnding