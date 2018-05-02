
label DebugMainMenu:
    
#    menu:
#        "Disable Debug Mode":
#            $ DebugMode=False
#            jump Morning1_Intro
#        "Enable Debug Mode":
#            pass
    
    
    
    menu:
        "Enable Alt. Dates":
            call enableAltDates
        "Normal Playthrough":
            pass
                
    menu:
        "Start at Begining":
            jump Morning1_Intro
        "Jump to":
            jump debugPickDay
    
    
label debugPickDay:
    menu:
        "Day 1":
            jump debugDay1_jump
        "Day 2":
            jump debugDay2_jump
            
    return
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
    
label enableAltDates:
    
    $ DateableEmma=False
    $ DateableEve=False
    $ DateableKathleen=False
    $ DateableSilvia=False
    
    return 
            
label debugDay2_jump:
    return