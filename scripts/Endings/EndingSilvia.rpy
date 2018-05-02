#Placeholder for Silvia's Ending

label Ending_Silvia_Start:
    
    narrator "You Romanced Silvia!!"
    jump Ending_Silvia_UpdateSave

#Save that we dated Silvia
label Ending_Silvia_UpdateSave:
    $ DateableSilvia=False
    $ persistent.SilviaDateable=False
    $ UpdateCompletedDates()
    
    return