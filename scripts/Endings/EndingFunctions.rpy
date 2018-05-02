init python:
    #Updates the persistent counter as to how many dates you've done 
    def UpdateCompletedDates():
        newValue=0
        if persistent.EmmaDatable==True:
            newValue+=1
        if persistent.EveDatable==True:
            newValue+=1
        if persistent.KathleenDatable==True:
            newValue+=1
        if persistent.SilviaDatable==True:
            newValue+=1
        persistent.CompletedDates=newValue
        
        
label DetermineFinalLover:
        
    if PointsEmma>PointsEve and PointsEmma>PointsKathleen and PointsEmma>PointsSilvia:
        jump Ending_Emma_Start
    if PointsEve>PointsEmma and PointsEve>PointsKathleen and PointsEve>PointsSilvia:
        jump Ending_Eve_Start
    if PointsKathleen>PointsEmma and PointsKathleen>PointsEve and PointsKathleen>PointsSilvia:
        jump Ending_Kathleen_Start
    if  PointsSilvia>PointsEmma and PointsSilvia>PointsEve and PointsSilvia>PointsKathleen:
        jump Ending_Silvia_Start