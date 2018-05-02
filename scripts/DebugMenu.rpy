
label DebugMainMenu:
    
    #Option to enable alternate dates
    menu:
        "Enable Alt. Dates":
            $ DateableEmma=False
            $ DateableEve=False
            $ DateableKathleen=False
            $ DateableSilvia=False
        "Normal Playthrough":
            pass
         
    #Option to jump to a later point in the game
    menu:
        "Start at Begining":
            jump Morning1_Intro
        "Jump to":
            jump debugPickDay
    
#Pick the day to skip to
label debugPickDay:
    menu:
        "Day 1":
            jump debugDay1_jump
        "Day 2":
            jump debugDay2_jump
            
    return
    
#Jump where in day 1
label debugDay1_jump:
    menu:
        "Lecture Hall (Meet Emma/Islay/Hudson)":
            jump Day1_LectureHall
        "Computer Room (Meet Eve)":
            jump Day1_ComputerLab
        "Rec Center (Meet Kathleen)":
            jump Day1_RecCenter
        "Dorm (Meet Silvia)":
            jump Day1_Dorm
    return
      
#Jump where in day 2      
label debugDay2_jump:
    return