

label Ending_Silvia_Start:
    
    narrator "You Romanced Silvia!!"
    jump Ending_Silvia_UpdateSave

label Ending_Silvia_UpdateSave:
    $ DateableSilvia=False
    $ persistent.SilviaDateable=False
    $ UpdateCompletedDates()
    
    return