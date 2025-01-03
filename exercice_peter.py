import streamlit as st
import pandas as pd
#from some_module import DeltaGenerator, FormData

#simulation d'une base des donnees d'hotel 
hotels_data={"chambre":["chambre 101", "chambre 102", "chambre 102"], "capacite":[2, 4, 3], "prix_par_nuit":[100, 150, 110], "reserve":[False, False, False]}
# conversion des donnees multidimentionnelles en dataframe ou bidimensionnel
df_hotels = pd.DataFrame(hotels_data)
st.title("Gestion d'hotel")
#AFFICHAGE DES CHAMBRES DISPONIBLES
st.subheader("chambres Disponibles")
available_rooms = df_hotels[df_hotels["reserve"] == False]
st.dataframe(available_rooms)
#DeltaGenerator(_form_data=FormData(form_id='reservation_form'))
# voici le formulaire de reservation
#st.subheader(" resevation d'une chambre")
#with st.form("reservation_form"):
    #nom_client = st.text_input("Nom complet du client")
   # choisir_la_chambre = st.selectbox("quel chambre voulez-vous choisir?",df_hotels["chambre"] [~df_hotels["reserve"]])
    #date_debut = st.text_input("date d'arrivee a l_hotel")
    #date_fin = st.text_input("fin du sejour a l_hotel")
    ## soumission du formulaire
    #submitted = st.form_submit_button("reserver")
    #if submitted:
        #df_hotels.loc[df_hotels['chambre'] == choisir_la_chambre, 'reservee'] = True





