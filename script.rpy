# The script of the game goes in this file.


init python:
    DebugMode=False
    
    if DebugMode==False:
        config.hard_rollback_limit = 0
    
    #Relationship Points
    PointsEmma=0
    PointsEve=0
    PointsKathleen=0
    PointsSilvia=0
    PointsIslay=0
    PointsHudson=0
    
    #If someone is availible to date
    if persistent.EmmaDateable==None:
        persistent.EmmaDateable=True
    if persistent.EveDateable==None:
        persistent.EveDateable=True
    if persistent.KathleenDateable==None:
        persistent.KathleenDateable=True
    if persistent.SilviaDateable==None:
        persistent.SilviaDateable=True
    if persistent.CompletedDates==None:
        persistent.CompletedDates=0
        
    
    
    #Character scale variables
    emmaSizeScale=1.75
    eveSizeScale=1.75
    kathleenSizeScale=1.75
    silviaSizeScale=1.5
    islaySizeScale=1.75
    hudsonSizeScale=1.75
    
    #What the player picked on Day 1
    Morning1Choice_Sporty=False
    Morning1Choice_Indie=False
    Morning1Choice_Tough=False
    Morning1Choice_Girly=False
    
    
label start:
    
    $ DateableEmma=persistent.EmmaDateable
    $ DateableEve=persistent.EveDateable
    $ DateableKathleen=persistent.KathleenDateable
    $ DateableSilvia=persistent.SilviaDateable
    $ DatesComplete=persistent.CompletedDates
    
    jump Setup_Variables
    
label Setup_Variables:
    call definePlayer
    if DebugMode:
        jump DebugMainMenu
    jump Morning1_Intro
    
    
label DeleteSave:
    
    $ persistent.EmmaDateable=True
    $ persistent.EveDateable=True
    $ persistent.KathleenDateable=True
    $ persistent.SilviaDateable=True
    $ persistent.CompletedDates=0
    
    jump main_menu_label
    
label main_menu_label:
    
    call screen main_menu
        
    #call screen preferences
    