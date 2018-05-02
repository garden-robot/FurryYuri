

label Ending_Eve_Start:
    
    narrator "You Romanced Eve!!"
    jump Ending_Eve_UpdateSave

label Ending_Eve_UpdateSave:
    $ DateableEve=False
    $ persistent.EveDateable=False
    $ UpdateCompletedDates()
    
    return