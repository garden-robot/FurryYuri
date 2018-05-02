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
        
    def GetLoveOrder():
        output=[]
        tempList=[PointsEmma+0.3, PointsEve+0.2, PointsKathleen+0.1, PointsSilvia]
        
        tempList.sort()
        for i in tempList[::-1]:
            c=0
            for ii in [PointsEmma+0.3, PointsEve+0.2, PointsKathleen+0.1, PointsSilvia]:
                if i==ii:
                    if c==0:
                        output+=["Emma"]
                    if c==1:
                        output+=["Eve"]
                    if c==2:
                        output+=["Kathleen"]
                    if c==3:
                        output+=["Silvia"]
                c+=1
                
        return output
                
label GoToEnding:
    
    $ lover=GetLoveOrder()[0]
        
    if lover=="Emma":
        jump Ending_Emma_Start
    if lover=="Eve":
        jump Ending_Eve_Start
    if lover=="Kathleen":
        jump Ending_Kathleen_Start
    if lover=="Silvia":
        jump Ending_Silvia_Start