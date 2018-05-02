#Placeholder for Eve's Ending

label Ending_Eve_Start:
    
    narrator "You Romanced Eve!!"
    jump Ending_Eve_UpdateSave

#Save that we dated Eve
label Ending_Eve_UpdateSave:
    $ DateableEve=False
    $ persistent.EveDateable=False
    $ UpdateCompletedDates()
    
    return