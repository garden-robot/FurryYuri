#Meet Emma, or Darren
#Also Meet Hudson and Islay


label Day1_LectureHall:
    scene bg lectureHall
    narrator             "You arrive at your first class of the day: Intro to Art History. You push through the doors of the lecture hall, heaving from all the running you just did. Luckily, the class hasn’t started yet! Phew!"
    narrator             "You scan the packed lecture hall for an empty seat and sit down in one of the front rows. Right as you sit down you hear a mellow voice through the surrounding speakers:"
    islayUnknownSpeach   "Hewwo? OwO Is dis ting on? Yew guis can heaw me, wight?"
    narrator             "The class nods in unison at the lecturer."
    
    $ lastSpoke="islay"
    show islay base at center with Dissolve(0.5)
    hide islay
    show screen islayOwO("^w^", "center")
    islayUnknownSpeach "Hewwo, cwass ^w^ I'm Pwofessow Buwgess and I wiww be guiding you aww awong thwough the histowy of awt >w<" 
    
    hide screen islayOwO
    show islay base at center
    islay        "Fwom the mystewious cave paintings of Wascaux to the Campbeww soup cans of Andy Wawhow, you wiww come to undewstand the wowwd awound you in an uwtimatewy nyew and exciting way."
    islay        "Befowe we begin, I wouwd wike to intwoduce youw TA fow the semestew! (/∀`♥)"
    
    if DateableEmma:
        $ lastSpoke="emma"
        show emma base at right with Dissolve(0.5)
        narrator "A familiar face stands up in front of the class- it’s that girl from the party! The one you uh… accidentally spilled beer on when you tripped over that tree stump… But she was really nice about it. And is super adorable. You had no clue she was so much older than you."
        emma     "Hewwo- I mean uh… Hello everyone! I’m Emma! I’ll be assisting Pwo-Professor Burgess this year. If anyone needs assistance in studying,  proofreading for essays, or you just wanna talk, I’ve posted my office hours on the course webpage."
        emma     "This class is actually the class that inspired me switch over to an Art History major to begin with. I hope you all really enjoy it! Thank you!"
        narrator "The class claps intensely as Emma blushes and sits down back into her seat. Everyone seems to be totally stunned by her modest, yet captivating charm. You included."
        show emma base:
            easein 1.0 xalign 2.0

        if Morning1Choice_Tough:
            narrator "Emma makes eye contact with you and blushes as she sits back down into her seat.  Everyone seems to be totally stunned by her modest, yet captivating charm. Especially you. I mean, she looked right at you!"

    else:
        $ lastSpoke="darren"
        show darren base at right with Dissolve(0.5)
        narrator        "Pwofessor Buwgess gestures and out steps Darren. "
        narrator        "Darren is 5 feet, and 3 inches. He’s the university alpha. He’s a volunteer at a homeless shelter, and he enjoys cooking with loved ones."
        narrator        "You’re not sure how you know all of this but somehow you do. It all floods into your head and it wont stop."
        narrator        "5’3”, alpha, volunteer, likes to cook. The words repeat in your head. 5’3”, alpha, volunteer, likes to cook."
        narrator        "Suddenly, you blink and the world returns to normal, like you just woke up from a dream."
        darren          "-office hours are mondays, at 1:30 to 2:30, I look forward to seeing you all there!"
        player          "(Did I just zone out?)"
        hide islay
        show screen islayOwO("OuO", "center") 
        islayOwOSpeach     "Thank you Dawwen, pwofessionyal as awways! OuO"
        hide screen islayOwO
        show islay base at center 
        darren          "Darren smiles and begins to walk out of the classroom."
        
        #Ease Darren offscreen
        show darren base:
            easein 1.0 xalign 2.0
            
    show islay base at left with move:
        pause 3.0
        fakeBobTalk
    jump Day1_MeetHudson

label Day1_MeetHudson:
    hudsonUnknownSpeach "I can’t believe the the University Alpha is our TA! Can you?"
    hide emma
    hide darren
    narrator      "You turn to meet the eyes of the furson talking to you."
    
    show hudson base at center with Dissolve(0.5)
    hudsonUnknown "It’s pretty cool! I never thought I’d ever get to talk to her, but now I can just walk into her office whenever!"
    hudsonUnknown "... Oh sorry, I didn’t realize I was talking out loud. I’m Hudson! What’s your name?"
    player        "I’m [playerName]. Nice to meet you!"
    hudson        "Hi there, [playerName]! It’s nice to meet you too! ..."
    narrator      "Hudson pawses."
    hudson        "Not to be inappropriate- I really don’t want to be offensive when I ask this but… are you… a human?"
    narrator      "You nod."
    player        "Don’t worry! I get that question a lot. I think I’m like, the last human around or something."
    narrator      "Hudson’s ears perk up."
    hudson        "Woah, really?! That’s so cool! Don’t you have like, human parents or something? :o"
    narrator      "The Pwofessow continues to lecture, so you lower your voice a bit."
    player        "Maybe? I was found on someone’s doorstep when I was a baby. Was eventually adopted by a family of hares."
    hudson        "Oh gosh, I’m sorry if I’m being pushy or inappropriate. I’ve just never seen a human before. :x"
    player        "Again, I get it a lot! It’s a pretty good icebreaker. Or ice bweakew as I should say."
    narrator      "Hudson starts to giggle."
    jump Day1_ProfessorInteraction
    
label Day1_ProfessorInteraction:
    
    hide islay
    show screen islayOwO(";`O´", "left", True)
    
    
    islayOwOSpeach "HEY! (;`O´)o " with vpunch
    hide screen islayOwO
    show islay base at left:
        xzoom -1
    narrator    "Pwofessow Buwgess appwoaches."
    
    
    #ease Hudson offscreen as Islay moves to center
    show hudson:
        easein 1.0 xalign 2.0
    show islay base at center with move
    hide hudson
    
    hide islay
    show screen islayOwO("`ε´", "center", True)
    islayOwOSpeach    "And youw nyame is? <( `ε´ )z"
    player   "Oh uh- it’s [playerName]"
    
    $ renpy.choice_for_skipping()
    islayOwOSpeach    "Ok [playerName], since you wewe paying such cwose attention, what is the appwoximate yeaw that the Venyus of Wiwwendowf was scuwpted?"
    menu:
        "Sneakily search the answer on your phone.":
            jump Day1_ProfessorInteraction_CheckPhone
        "Admit your fault like a tough kid.":
            jump Day1_ProfessorInteraction_ActTough
    
label Day1_ProfessorInteraction_CheckPhone:
    
    narrator "You quickly and almost motionlessly take your phone out of your pocket and swipe type Venyus of Wiwwendowf into your search engine, Poodle, but no results show up. Oh jeez- how do you spell it?!"
    show screen islayOwO("e_e", "center", True)
    islayOwOSpeach "...That’s what I thought. I’ve got my eye on you [playerName]. e_e"
    hide screen islayOwO
    show islay base at center:
        xzoom -1
    if DateableEmma:
        narrator "In your peripherals, you notice a dejected and slightly annoyed Emma sigh and continue to type on her laptop."
        call UpdateRelationPoints((("emma", -1), ("islay", -1)))
    else:
        call UpdateRelationPoints((("islay", -1), ))
    
    hudsonSpeach "Sorry [playerName]. :( I didn’t mean to get you in trouble."
    narrator "Your face burns red hot in embarrassment as Pwofessow Buwgess continues to lecture."
    jump Day1_ClassEnd
    
label Day1_ProfessorInteraction_ActTough:
    narrator "You stand up."
    hide screen islayOwO
    show islay base at center:
        xzoom -1
    player   "You know what, I’m a first year. This is my first art history class ever. I’m going to learn a lot of information, and not all of it is going to stick in the beginning."
    player   "But I’m a hard worker, I’m going to make use of our TA’s office hours, and I’m going to ace this class. Sorry I wasn’t paying my fullest attention, pwofessow."
    narrator "You sit back down again."
    
    if DateableEmma:
        narrator "You see Emma in the corner of your eye, seemingly impressed with your courage and honesty."
    
    hide islay
    show screen islayOwO("☆ω☆*", "center", True)
    islayOwOSpeach    "Wow, such passion. (☆ω☆*)I'm excited to see youw gwowth, [playerName]. Aww is fowgiven."
    
    if DateableEmma:
        call UpdateRelationPoints((("islay", 1), ("emma", 1)))
    else:
        call UpdateRelationPoints((("islay", 1),))
    
    hudsonSpeach   "Wow, that was soooo inspiring. You make me wanna be a better student, [playerName]! And it’s only the first day of classes! :D"
    hide screen islayOwO
    show islay base at center:
        xzoom -1
    narrator "As Professow Buwgess continues his lecture, the room is filled with inspired murmurs from your colleagues."
    jump Day1_ClassEnd
    
label Day1_ClassEnd:
    hide islay with moveoutleft
    narrator "The class comes to a close, and students left and right begin to pack up their belongings."
    
    $ lastSpoke="hudson"
    show hudson base at center with Dissolve(0.5)
    hudson   "Hey, do you have any other classes today? I have one an hour and a half after this one ends, and I have to bring my computer to the Tech Lab to get it fixed in time. Do you wanna come with?"
    
    if DateableEmma:
        $ renpy.choice_for_skipping()
        narrator "You don’t have any other classes today, but you were thinking of talking to Emma before you left. Although there is quite a long line of eager people to talk to her as is..."
        menu:
            "Make Hudson wait for you while you go talk to Emma.":
                jump Day1_MeetEmma
            "Forget it and leave with Hudson.":
                jump Day1_LeaveWithHudson
    else:
        player "Sure! Sounds like fun."
        jump Day1_LeaveWithHudson
            
label Day1_LeaveWithHudson:
    hudson "Yay! Let’s go!"
    jump Day1_ComputerLab
    
label Day1_MeetEmma:
    hudson   "Alright buddy! I’ll wait by the back door, ok?"
    narrator "Hudson takes off towards to exit, while you approach the daunting line of Emma Admirers."
    hide hudson with Dissolve(0.5)
    scene bg lectureHall
    with fade
    
    narrator "Finally, you’ve reached the front. The room is totally empty, except for you and Emma."
    $ lastSpoke="emma"
    show emma base at center with Dissolve(0.5)
    
    $ renpy.choice_for_skipping()
    emma     "Fancy seeing you here, huh [playerName]? Look out for any tree stumps!"
    python:
        madeWittyComeback=True
    menu:
        "Retort with a witty comeback":
            jump Day1_MeetEmma_WittyComeback
        "Laugh it off":
            jump Day1_MeetEmma_LaughItOff
    
label Day1_MeetEmma_WittyComeback:
    player "The University Alpha remembered my name? Wow, I must be important!"
    emma   "Hard to forget someone who spills beer all over your favourite top."
    player "Heh, sorry about that. At least I got the opportunity to talk to you."
    
    # Animation for gaining points with emma
    call UpdateRelationPoints((("emma", 1), ))
    emma   "Emma blushes as she picks up her things and begins to walk towards the exit. She then looks at you from over her shoulder as if a beckon to follow." #TODO: Maybe expression
    
    jump Day1_MeetEmma_End
    
label Day1_MeetEmma_LaughItOff:
    emma     "Emma picks up her things and begins to walk towards the exit. She then looks at you from over her shoulder as if a beckon to follow."
    python:
        madeWittyComeback=False
        
    jump Day1_MeetEmma_End
    
label Day1_MeetEmma_End:
    emma   "So uh… Are you an art history major too? Or just filling an elective?"
    player "Who knows! Undeclared, baby!"
    emma   "Yeah, you don’t need to rush it- everyone figures it out at their own pace. I was in Environmental Science before switching over to Art History. You can imagine how my parents reacted to that."
    
    narrator   "You both step outside"
    scene bg outside
    emmaSpeach "I’ve got some Alpha work to do- my day is packed with meetings. Good luck with everything. If you need any help, you should stop by my office hours sometime. Don’t bring any drinks. "
    narrator   "She winks at you as she turns away towards the university centre."
    
    if madeWittyComeback:
        narrator "Now it’s your turn to blush."
    else:
        narrator "Your blush really hard. Oh my gosh, she’s cute."
        
    player   "Ha ha- oh uh yeah totally! No drinks ever. I’ll never look at any kind of drink again. I’ll start a drink embargo. A die-of-dehydration type of drink embargo-"
    narrator "And she’s gone."
    hide emma with Dissolve(0.5)
    
    narrator "You are such a useless lesbian."
    jump Day1_Outside

label Day1_Outside:
    $ lastSpoke="hudson"
    show hudson base at center with Dissolve(0.5)
    narrator "Hudson approaches you, wagging his tail excitedly."
    hudson   "How’d it go! :D"
    player   "Oh heh, yeah it uh… It went well. She’s cool. Uh… wanna get going to the computer lab now? "
    hudson   "Sure, let’s go!"
    jump Day1_ComputerLab
    
