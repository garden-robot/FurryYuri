# The script of the game goes in this file.

init python:
    #Debug Related
    DebugMode=False
    
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
    
#The start of the game
label start:
    jump Setup_Variables
    
#Setup variables needed for the game
label Setup_Variables:
    
    #Add Debug Privaleges
    if DebugMode==False:
        $config.hard_rollback_limit = 0
    else:
        $config.hard_rollback_limit = 999999999999
        
    #Define who has been dated. Used to prevent paradoxes when loading an old game
    $ DateableEmma=persistent.EmmaDateable
    $ DateableEve=persistent.EveDateable
    $ DateableKathleen=persistent.KathleenDateable
    $ DateableSilvia=persistent.SilviaDateable
    $ DatesComplete=persistent.CompletedDates
    
    call definePlayer #Character creation
    
    #More debug stuff
    if DebugMode:
        jump DebugMainMenu
    jump Morning1_Intro
    
#Deletes Saved date
label DeleteSave:
    #Clear who has been dated
    $ persistent.EmmaDateable=True
    $ persistent.EveDateable=True
    $ persistent.KathleenDateable=True
    $ persistent.SilviaDateable=True
    $ persistent.CompletedDates=0
    call screen main_menu
    
    