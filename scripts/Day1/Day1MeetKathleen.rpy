#Meet Kathleen or Easton
#Possible to gain +1 Points with Kathleen

#Arrive at Rec Center
label Day1_RecCenter:
    scene bg recCenter
    #Look around Rec Center
    narrator "Exercising is the last thing you’d ever want to do, but you promised your hare-ents that you’d try to make use of the gym membership that was included in your tuition."
    narrator "Since you don’t have any class for the rest of the day, you figured it would be a good time to at least try to get acquainted with the gym."
    narrator "As you enter the Sir Oxington Athletics and Recreation centre (or SOAR as some people call it) you’re a little overwhelmed by how many people there are- people of all ages too, like kids and their parents."
    narrator "There’s even a group of obnoxious teenage boys from the high school a few blocks over, probably on a lunch break, and they’re having a coffee chugging contest at one of the tables."
    narrator "Wow, that guy can really chug.{cps=2} {/cps}Oh.{cps=2} {/cps}He just threw up. "
    narrator "That brings you to notice the fact that there's a fairly large food court here too, which must also be attracting the crowd, and is even beckoning you over with its variety of richly greasy scents."
    narrator "You’re a little thankful you just saw that dumb kid vomit coffee, otherwise you’d probably ditch your gym trip and go eat."
    narrator "After beeping into the entrance with your student ID, you realize you forgot to pack gym clothes, so you just decide to hit the weight room as you are. "
    narrator "You’ve never seen so many exercising apparatus in one space before- it’s totally terrifying. The air is thick with sweat and there are buff people left and right, grunting heavily as they pick things up and put things down."
    narrator "You spot an empty area. It’s that kind of weight thing that has a really long bar, those big black discs on the side, and you lie on your back as you lift it up- like in the movies!"
    narrator "You pseudo-confidently strut on over and check the weights on it. There are 10 on each side, adding up to a total of 20 pounds. That should be fine to start!"
    narrator "You lie down on your back underneath. You used to play softball in highschool, and your coach would push your team pretty hard in the exercising realm (or so you thought). It shouldn’t be that hard to get back into the ‘swing’ of things. Haha. That was funny."
    narrator "Time to show these gym rats what’s up!"
    
    #See Easton istead of Kathleen
    if DateableKathleen==False:
        jump Day1_MeetKathleen_MeetEaston
    
    #Start Lifting weights, Kathleen saves you
    narrator "You lift the bar from the rack, and- OH GOSH, OH HOLY HECK YOU CAN’T HOLD IT IT’S SO HEAVY WH OH GOD IT’S FALLING"
    narrator "IT’S FALLING ON YOU"
    narrator "IT’S ON YOUR THROAT"
    narrator "IS THIS HOW IT ENDS"
    narrator "OH YOU’RE GOING TO SUFFoCAte"
    narrator "AAaaaAAjpfp(fje" with hpunch
    narrator "IMGOINGTODIE" with vpunch
    
    $ lastSpoke = "kathleen"
    narrator "GASSSSSSSSP" with hpunch

    show kathleen base at center with Dissolve(0.5)
    narrator        "You cough violently as your savior lifts the bar from your throat."
    narrator        "Y-you’re alive."
    kathleenUnknown "I gotcha."
    player          "*COUGH COUGH WHEEZE*" with vpunch
    kathleenUnknown "Never use the bench press without someone to spot you. Be more careful next time."
    player          "Y-you saved my life! *COUGH*"
    kathleenUnknown "All in a day’s work."
    narrator        "You finally have the strength to stand up, and thank your hero."
    narrator        "When you see her face right side up you realize you definitely saw her at the party last night. She was at the beer pong table the whole time, totally blowing everyone out of the water."
    player          "T-thank you so much for saving me… It was only 20 pounds! Why did it feel so much heavier?!"
    kathleenUnknown "The bar is 45 on its own. So that’s a total of 65 lbs."
    player          "……"
    
    hide kathleen
    show kathleen smirk at center:
        zoom kathleenSizeScale
    narrator        "The girl clucks humorously."
    hide kathleen
    show kathleen base at center
    #Kathleen helps, is introduced
    kathleenUnknown "Do you want me to spot you while you’re here? Maybe give you some training advice? I don’t mind. I have some time right now."
    player          "Uh, yeah! That would be great, actually. I don’t know if you can tell, but I’ve never been in a weight room before."
    if Morning1Choice_Honesty:
        call UpdateRelationPoints((("kathleen", 1), ))
        kathleen "Well you definitely dress like you know your way around one! I thought you were a regular when I first saw you saunter up to the bench press. I’m Kathleen, by the way."
    else:
        kathleenUnknown "Oh, trust me, you hide it really well. I’m Kathleen, by the way."
    player          "I’m [playerName]"
    kathleen        "Alright, [playerName]! What are you looking to train?"
    player          "Uh… like… muscles… and stuff..."
    kathleen        "Nice, that gives me a {i}lot{\i} to work with."
    narrator        "She walks over to a different machine, and you follow closely behind, still wheezing a bit."
    narrator        "This one also has those disc weights hanging on the side, but is smaller and has a flat surface with foot prints on it."
    kathleen        "I’m guessing you’re looking to do a balanced work out, so let’s start with your legs. This thing here is called a leg press. It’ll mostly work out your quads."
    
    $ renpy.choice_for_skipping()
    kathleen        "Figure out a comfortable weight, and do a set of 8 reps. Obviously do less if you feel like you’re in a lot of pain."
    menu:
        "Pretend you understood everything she just said and figure it out as you go":
            jump Day1_MeetKathleen_FiguerOutAsGoAlong
        "Confess that you have no clue what she just said":
            jump Day1_MeetKathleen_AdmitNoIdea
    
#If you don't ask for an explination
label Day1_MeetKathleen_FiguerOutAsGoAlong:
    #Start Lifting
    narrator "What are sets? What are reps? A set of 8 reps? Are reps like- a multiple of something? You feel like such an idiot as is, you shouldn’t ask her about it. Ok, ok. You can do this."
    narrator "Just…do what she said and try to do it until something hurts? Maybe she’ll tell you when to stop?"
    narrator "You set up the weights and then sit down."
    kathleen "Yeah, keep your feet about a shoulder’s length apart."
    narrator "You do as she says, take a deep breath, and-"
    narrator "Woah."
    pause 0.2
    narrator "Ok."
    pause 0.2
    narrator "You’ve done 3 now."
    pause 0.2
    narrator "This isn’t so bad! You’re working out!"
    pause 0.2
    narrator "You’ve done 6, you’re starting to struggle a little."
    pause 0.2
    narrator "Ok you’re at 10 and your muscles feel like they’re going to give out."
    pause 0.2
    narrator "11…."
    narrator "Oh jeez. When do you stop? You want to impress her! You want to make up for all the embarrassing things you just did."
    pause 0.2
    narrator "12…"
    narrator "Oh for the love of-"
    #Finish lifting and Kathleen calls you out
    kathleen "Uh, have you been keeping count?"
    narrator "Your knees nearly slam into your chest as the leg press gets the best of you; the weights slam against the machine with a loud and earth-shattering CLANG."
    narrator "The whole gym is looking at the two of you."
    kathleen "Are you alright?!" 
    narrator "Y-Yeah I’m fine..."
    kathleen "Why didn’t you just stick to 8 reps?!"
    player   "I’m sorry, I don’t know what reps and sets are. And I feel so stupid as is, I didn’t want to like… embarrass myself more? But I guess I did anyway." 
    kathleen "Yeah, tell me about it!"
    kathleen "{cps=2}...L{/cps}isten. {p}Don’t ever feel bad or stupid about asking for help. Wouldn’t you rather risk getting embarrassed over seriously injuring yourself?"
    kathleen "I mean, you really could have gotten hurt."
    player   "I think you underestimate how bad I am at dealing with embarrassment."
    kathleen "You’re kind of an idiot, you know that?" 
    player   "I’m well aware!" 
    kathleen " Anyways, to avoid you nearly killing yourself next time: reps are just the amount times you repeat an action."
    kathleen "So like, to do 8 reps is to lift something 8 times. And 1 set of that is to only do it 8 times once during your workout."
    player   "Oh ok! That’s way less complicated than I thought."
    
    jump Day1_Dorm

#Ask Kathleen to explain
label Day1_MeetKathleen_AdmitNoIdea:
    call UpdateRelationPoints((("kathleen", 1), ))
    #Kathleen explains, start lifting
    narrator "You set up the weights and prepare to start working out but then you realize you should probably suck up your anxiety and ask Kathleen what sets and reps are."
    player   "I’m so sorry to waste more of your time and I don’t mean to be annoying but what are reps and sets? "
    kathleen "Hey, don’t ever feel bad about asking for help. I’d always rather you risk seeming annoying over getting hurt. Also, you’re not annoying."
    kathleen "Anyways, reps are just the amount times you repeat an action. So like, to do 8 reps is to lift something 8 times. And 1 set of that is to only do it 8 times once during your workout."
    narrator "Oh, ok! So just do this thing 8 times then!"
    player   "Got it! Thank you!"
    kathleen "No prob, bob. Now press those legs!"
    narrator "You set up the weights and then sit down."
    kathleen "Yeah, keep your feet about a shoulder’s length apart."
    narrator "You do as she says, take a deep breath, and-"
    narrator "Woah"
    pause 0.2
    narrator "Ok."
    pause 0.2
    narrator "You’ve done 3 now."
    pause 0.2
    narrator "This isn’t so bad! It almost feels kind of… good. You really never thought you’d ever say that about working out."
    pause 0.2
    narrator "You’re at 6, and you’re struggling a bit. But you push on forwards."
    pause 0.2
    narrator "7… C’mon, c’mon…"
    pause 0.2
    narrator "8!"
    #Finish lifting
    narrator "You slowly bring your legs forward, letting the weights settle gently against the machine."
    kathleen "Wow, good form! You did it!"
    player   "I couldn’t have done it without you!"
    narrator "Kathleen’s breath catches in her throat and she looks away nervously. She then takes out her phone to check it."
    kathleen "Hey, uh I’m really sorry but I forgot that I had to turn in an application that’s due by tomorrow. My calendar just reminded me."
    player   "Oh uh, maybe we could work out again sometime?"
    kathleen "Oh- uh yeah. That’d be cool."
    player   "Could I get your Furbook?"
    kathleen "Sure."
    narrator "You run over to your bag, tear off a small piece of paper from a notebook, fish for a pen, then run back with both in hand."
    narrator "Kathleen tentatively writes her number on the scrap, and then hands it back to you."
    narrator "Why is she on edge all of a sudden?"
    kathleen "Yeah so, I’ll catch you around maybe."
    player   "Totally! I mean, for the love of Dog- I can’t be trusted in here on my own."
    kathleen "Haha, yeah see ya."
    narrator "She gives you a quick smile and wave before picking up her duffle bag and heading out."
    narrator "Now, you could keep exercising, but frankly that moment where you almost died has traumatized you a bit. Maybe that’s enough for today."
    
    jump Day1_Dorm
    
#Meet Easton instead of Kathleen
label Day1_MeetKathleen_MeetEaston:
    show easton at right with Dissolve(0.5)
    narrator "You grab the bar and begin to lift, but as you do you're hit with the feeling that someone in this room doesn't belong. You lift the bar a little more, and as you do someone across from you starts to stand up. "
    narrator "As he does, the name Easton pops into your head and you become hyper aware of your surroundings. This guy… is Easton, and he’s been staring at you ever since you walked into the center."
    narrator "You start to sweat, but out of fear. "
    narrator "Who the flock is Easton? Easton is a single guy on the wrestling squad who’s going through a bit of an edgy streak."
    narrator "Why did he suddenly start to stand up, then stop? Easton likes to act all tough but he’s actually a softie underneath, you just need to give him a chance."
    narrator "Why the flock is he staring at me?? "
    narrator "An image flashes into your mind of someone who’s bloody, and beaten. Like they were trying to fight back in a situation where they couldn't possibly win."
    narrator "Easton slowly sits back down, almost as if he’s waiting for you to start lifting the bar again."
    narrator "You get up and run, trying to get back to the safety of your dorm. Easton watches as you leave."
    
    jump Day1_Dorm