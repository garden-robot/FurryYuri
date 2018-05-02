#Placeholder for Emma's Ending

label Ending_Emma_Start:
    
    narrator "You Romanced Emma!!"
    jump Ending_Emma_UpdateSave

#Save that we dated Emma
label Ending_Emma_UpdateSave:
    $ DateableEmma=False
    $ persistent.EmmaDateable=False
    $ UpdateCompletedDates()
    
    return