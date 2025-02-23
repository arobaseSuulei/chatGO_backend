import os
from supabase import create_client, Client
from transformers import pipeline




url = "https://pxyqknxfvimxdcmplbff.supabase.co" 
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InB4eXFrbnhmdmlteGRjbXBsYmZmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjkzMDM4NjIsImV4cCI6MjA0NDg3OTg2Mn0.cuq3c8ejHCSky7BcV1qlj76_QYWcYXYiAbvDolxN6Uk"  # Remplace avec ta clé API
supabase: Client = create_client(url, key)

# Appel à la table "chatGO-analyzer" et récupération des données
response = supabase.table("chatGO-analyzer").select("msg,id").execute()

classifier = pipeline("sentiment-analysis")

    # Afficher la réponse pour tester et boucler
for i in response.data:
    print ('debut')
    print(i['msg'])
    #model="nlptown/bert-base-multilingual-uncased-sentiment"
       


    
    res = classifier(i['msg'])
    
    for item in res:
        print(item['label'])
        response = (
        supabase.table("chatGO-analyzer")
        .update({"sentiment": item['label'] })
        .eq("id",i['id'])
        
        .execute()
)







