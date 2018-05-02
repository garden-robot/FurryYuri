

label Ending_Emma_Start:
    
    narrator "You Romanced Emma!!"
    jump Ending_Emma_UpdateSave

label Ending_Emma_UpdateSave:
    $ DateableEmma=False
    $ persistent.EmmaDateable=False
    $ UpdateCompletedDates()
    
    return