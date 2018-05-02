

label Ending_Kathleen_Start:
    
    narrator "You Romanced Kathleen!!"
    jump Ending_Kathleen_UpdateSave

label Ending_Kathleen_UpdateSave:
    $ DateableKathleen=False
    $ persistent.KathleenDateable=False
    $ UpdateCompletedDates()
    
    return