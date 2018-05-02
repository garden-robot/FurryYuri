#Meet Eve, or Joey



label Day1_ComputerLab:
    
    scene bg computerLab
    show hudson base at center
    
    hudson   "I think this is it?"
    narrator "You and Hudson step into a large, open concept room, ordered by rows of desks, computers, and office chairs."
    narrator "The room is dimly lit by a few ceiling lights, and is depressingly windowless as it is located on the bottom most floor. Celing tiles missing You see now why the lab here has earned its title: “The Dungeon”. "
    
    if DateableEve==False:
        jump Day1_MeetEve_MeetJoey
    
    $ lastSpoke="eve"
    show eve base at right with Dissolve(0.5)
    eveUnknown "Uh, hi..."
    narrator   "Haven’t you seen this girl before?"
    narrator   "...Oh, of course! The party! You remember you saw her leave like, 10 minutes into the night. She’s wearing the same adorable sweater, too."
    show hudson base at center:
        xzoom -1 #Hudson faces Eve
    hudson     "Hiya!"
    eveUnknown "Sorry uh, do you need help with anything?"
    hudson     "Yeah!"
    eveUnknown "...So… uh…"
    hudson     ":D"
    eveUnknown "What do you… need help with… {eveSmall}(sorry){/eveSmall}"
    hudson     "Oh, yeah! My laptop won’t turn on."
    eveUnknown "Uhm, let me take a look then."
    
    show eve base:
        ease 1.0 xalign 0.5
    show hudson base:
        ease 1.0 xalign 0.0
    
    narrator   "The small girl trips over herself as she tries to sit into the closest desk chair." #TODO: ask just if this should have a vpunch 
    
    show eve embarassed at center #TODO: Get this sprite
    show hudson base at left
    eveUnknown "Jeez.... {eveSmall}(Oh goodness I’m so embarrassed I could die).{/eveSmall}"
    narrator   "Hudson pulls out his laptop from his backpack."
    show eve base at center
    hudson     "Here it is! I named her Stella. :)"
        
    eveUnknown "Hi, Stella. I’m Eve."
    narrator   "Eve fiddles around with some of the buttons on Stella, before turning her over and unscrewing the bottom cover."
    eve        "How long have you had her for?"
    hudson     "I got her yesterday! :3"
    eve        "{size=+5}Yesterday?!{/size} {eveSmall}(Oh, wow, I said that super loud…){/eveSmall} Uhm, did you drop it or spill anything on it?"
    hudson     "Not at all! Stella’s my first ever laptop so I tried to make sure I was extra careful. :("
    eve        "Hm… Everything looks totally normal on the inside. Strange."
    narrator   "Eve carefully screws the bottom back on."
    #TODO: Ask jamie about name Professor
    eve        "Hey, Professor? Can you take a look at this?" 
    $ renpy.choice_for_skipping()
    narrator   "A person, you assume the professor heading the lab, shuffles over from the other side of the room. As they help Hudson, you and Eve sit off to the side together."
    show hudson base at left:
        xzoom 1
        pause 3.0
        fakeBobTalk
        
    menu:
        "Try and strike up a conversation":
            jump Day1_MeetEve_Conversation
        "Wait for Eve to say something":
            jump Day1_MeetEve_Wait

label Day1_MeetEve_Conversation:
    call UpdateRelationPoints((("eve", 1), ))
    player "How has your day been going?"
    eve    "Oh… {eveSmall}(!!!){/eveSmall} It’s been fine. I’ve just been with computers all day. And I like computers."
    player "Yeah? How long have you worked here for?"
        
    jump Day1_MeetEve_AfterChoice1

label Day1_MeetEve_Wait:
    narrator "The two of you sit there, listening to the Professor’s survey Hudson about his laptop."
    eve      "Uh… {eveSmall}(what do I do...) Uhm are you… having a nice….)))) oh…….. Are you having a nice day?{/eveSmall}"
    player   "Yeah, I am! It’s my first day of university, actually. How long have you worked here for?"
    jump Day1_MeetEve_AfterChoice1
    
label Day1_MeetEve_AfterChoice1:
    eve      "I don’t… work here… {eveSmall}(gosh that sounded rude){/eveSmall} I mean, I’m a student volunteer… In my second year…  Today’s my first day in the lab."
    narrator "You glance over at Hudson and the Professor as they call over another person to help them solve the mystery of Hudson’s broken laptop."
    player   "That’s exciting! What program are you in?"
    eve      "Computer science. How about you?"
    player   "Haha, whoops. I guess that should have been obvious. I’m undeclared, for now. Hopefully."
    eve      "Oh, that’s cool…"
    narrator "Silence."
    player   "What do you like most about computers?"
    eve      "..Oh, uh, a lot of things… {eveSmall}(I guess I like how straightforward everything is, and how you can essentially like, bend reality? I mean I can just imagine anything and bring it to life on a computer. I don’t know…){/eveSmall}"
    
    $ renpy.choice_for_skipping()
    narrator "You can sense Eve is getting more nervous. Should you…"
    menu:
        "Encourage her to speak up":
            jump Day1_MeetEve_SpeakUp
        "Let her keep talking.":
            jump Day1_MeetEve_LetHerTalk
            
label Day1_MeetEve_SpeakUp:
    player "You can speak up a little bit more. I don’t bite."
    
    call UpdateRelationPoints((("eve", -1), ))
        
    narrator "Eve averts her eyes away from you, even more uncomfortable than she looked before."
    narrator "Oh gosh, I’m sorry."
    eve      "{eveSmall}(…){/eveSmall}"
    player   "I think that’s so… interesting! I’ve never thought about it that way before. I wish I knew more about it."
    
    jump Day1_MeetEve_AfterChoice2

label Day1_MeetEve_LetHerTalk:
    eve      "{eveSmall}(Like, if the world was a computer, then code would be the laws of physics that holds everything together. And it’s a skill that anyone can pick up. It’s cool, I guess.){/eveSmall}"
    player   "Wow."
    eve      "I’m… so sorry…"
    player   "Please don’t be sorry. I think that’s really incredible. Passion really brings out the beauty in people"
    narrator "Eve holds her tail in her hand, and squeezes it nervously. You think you saw her smile? "
    call UpdateRelationPoints((("eve", 1), ))
    
    player   "I think that’s so interesting though! I’ve never thought about it that way before. I wish I knew more about it."
    jump Day1_MeetEve_AfterChoice2

label Day1_MeetEve_AfterChoice2:
    narrator            "It seems as if the three people surrounding Hudson’s laptop have now multiplied to six."
    eve                 "Well uhm… If you want to learn more about code I could give you some pointers sometime. If we’re talking in C specifically, I could give you some *. {eveSmall}(haha.){/eveSmall}"
    narrator            "She’s giggling softly, but… you don’t get it."
    player              "Learn code? That sounds so rad! I’d totally be down sometime."
    eve                 "U-Uh {eveSmall}(really?){/eveSmall} Yeah I can message you my availability in the lab, if you want to add me on FurBook."
    narrator            "Eve gingerly grabs your hand and writes her name on your wrist."
    eve                 "Oh s-s-sorry if that was weird, I just-"
    $ lastSpoke = "professor"
    show hudson base at left:
        xzoom 1
        randomLookAround
        
    professorSpeach     "I just don’t- I don’t understand what the darn problem is!" with hpunch
    professorSpeach     "There’s nothing wrong with this laptop! So why won’t it turn on?!"
    narrator            "The four other students that the Professor called over to help are all in  disarray as they frantically google the laptop model manuel on their phones and argue with one another over the possible issue."
    narrator            "Hudson stands by, wagging his tail hopefully."
    $ lastSpoke = "eve"
    show hudson base at left
    show eve base at leftMiddle with move
    show hudson base at left:
        xzoom -1
    narrator            "Eve turns away from you and walks over to the mess of people."
    eve                 "Uhm Hudson… So when your laptop was working, did it charge properly?"
    hudson              "Charge? What do you mean? :o"
    eve                 "{eveSmall}(what?){/eveSmall}... You know like… you plug in your laptop into the wall when it’s low on battery?"
    hudson              "Plug it in? I thought the point of a laptop was that you didn’t have to plug it in!"
    eve                 "There you have it guys."
    narrator            "The group of students stare blankly at Hudson, who only offers a confused smile in return."
    eve                 "So that cord that came with your laptop? Use it to plug this into a wall and it should work."
    hudson              "Ah ok! Thanks for fixing Stella, Eve! I really appreciate it. :D"
    narrator            "Hudson gives Eve a warm hug, who only cautiously accepts."
    narrator            "The students, clearly irritated, scatter and return to their respective desks. The Professor follows suit, the life having left their eyes."
    hudson              "Alright, well, I gotta get to class now. I’ll see you all later!"
    player              "And I’ve gotta go to the Rec Center, so I’ll walk with you. Bye, Eve! Thanks for the help!"
    show  eve:
        xzoom -1
    eve                 "Bye! It was really nice meeting you. {eveSmall}(Hopefully we’ll see eachother again soon...){/eveSmall}"
    
    jump Day1_RecCenter
    


label Day1_MeetEve_MeetJoey:
    show joey base at right with Dissolve(0.5)
    narrator "You see someone sitting at a desk. He doesn't look familiar, but somehow you know his name is Joey, and he’s a student volunteer here."
    hudson   "Hey! "
    narrator "Joey turns to look at Hudson in a way that feels scripted, like he’s been waiting for this."
    hudson   "Can you umm… help me out? :<\nMy laptop isn't working"
    joey     "Of course!"
    narrator "You lock eyes with Joey and suddenly you're hit with a flash of memories. You remember a phone call with someone. You don’t know who you were talking to, but you start to feel panicked."
    narrator "The voice on the phone starts playing in your head. It belong to a twenty-something girl, and though she sounds memorable you can’t put a face to it."
    narrator "Thinking about it puts you in physical pain, but you feel compelled to try and remember.{p}Suddenly memories of screaming wash over you, and a phantom pain hits your stomach, snapping you back into reality."
    narrator "You… don’t know what happened. Looking abound the room, Hudson is still talking with Joey."
    hudson   "So if I plug Stella in, she’ll be ok? :D"
    joey     "Yup, plug ’er in, let her charge, and in time she should be good to go."
    narrator "Joey is eyeing you"
    hudson   "Wow, Gee thanks!"
    narrator "Joey nods and turns towards you. You start to feel sick to your stomach, and feel the need to get out of here, now. Thankfully, Hudson blindsides Joey with a hug."
    player   "I um… need  to get going. I’m ganna head to the rec-center, see you later Hudson!"
    narrator "You don’t wait for a response, bolting out of the lab as quick as you can."
    
    jump Day1_RecCenter
    