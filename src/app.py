import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from dotenv import load_dotenv
import spotipy  # Ensure this import is present  
from spotipy.oauth2 import SpotifyClientCredentials  
import requests
from dotenv import load_dotenv
load_dotenv()  

  
client_id = os.environ.get("CLIENT_ID")  
client_secret = os.environ.get("CLIENT_SECRET")  

 




token_url = "https://accounts.spotify.com/api/token"  

payload = {  
    "grant_type": "client_credentials",  
    "client_id": client_id,  
    "client_secret": client_secret  
}  


response = requests.post(token_url, data=payload)  

 
if response.status_code == 200:  
    
    token_info = response.json()  
    access_token = token_info['access_token']  
    print(f"Access Token: {access_token}")  
else:  
    print(f"Error: {response.status_code}, {response.text}") 


   

artist_id = "4Z8W4fKeB5YxbusRsdQVPb"  
top_tracks_url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?market=US"  

headers = {  
    "Authorization": f"Bearer {access_token}"  
}  

popular = []  
durat = []  
response = requests.get(top_tracks_url, headers=headers)  

if response.status_code == 200:  
    data = response.json()  

    for track in data["tracks"]:  
        name = track["name"]  
        popularity = track["popularity"]  
        popular.append(popularity)  # Append the actual popularity value  
        duration = track["duration_ms"] / 1000  # Convert duration to seconds  
        durat.append(duration)  

        print(name, popularity, duration)  
else:  
    print("No track found or an error occurred")  

 
df = pd.DataFrame({  
    "Popularity": popular,  
    "Duration (s)": durat  
})  
 
scatter_plot = sns.scatterplot(data=df, x="Popularity", y="Duration (s)")  

 
plt.title("Track Popularity vs. Duration")  
plt.xlabel('Popularity')  
plt.ylabel('Duration (s)') 

 
fig = scatter_plot.get_figure()  
fig.savefig("scatter_plot.png")  
plt.show()
