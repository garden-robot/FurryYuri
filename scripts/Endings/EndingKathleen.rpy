#Placeholder for Kathleen's Ending

label Ending_Kathleen_Start:
    
    narrator "You Romanced Kathleen!!"
    jump Ending_Kathleen_UpdateSave

#Save that we dated Kathleen
label Ending_Kathleen_UpdateSave:
    $ DateableKathleen=False
    $ persistent.KathleenDateable=False
    $ UpdateCompletedDates()
    
    return