from fastapi import FastAPI
import pandas as pd
import numpy as np 
from database import netflix 
from database import hulu 
from database import disney 
from database import amazon 


amazon = pd.read_csv(r"amazon_csv")
disney = pd.read_csv(r"disney_csv")
hulu = pd.read_csv(r"hulu_csv")
netflix = pd.read_csv(r"netflix_csv")


app = FastAPI()
#prueba de API

@app.get("/")
def index():
    return "hola chico"


# cuenta cantidad de peliculas que tienen la palabra ingresada como parametro, por plataforma. 


@app.get("/get_word_count")
def get(plataforma, keyword):
    if plataforma == "amazon":
        return amazon[amazon["title"].str.contains(keyword)].shape[0]
    elif plataforma == "netflix":
        return netflix[netflix["title"].str.contains(keyword)].shape[0]
    elif plataforma == "disney":
        return disney[disney["title"].str.contains(keyword)].shape[0]
    elif plataforma == "hulu":
        return hulu[hulu["title"].str.contains(keyword)].shape[0]


#pelicula con mayor score por plataforma, por año  
@app.get("/get_score_count")
def get(plataforma, score, año):
    if plataforma == "amazon":
        df = amazon[amazon["type"]== "movie" & (amazon["score"]>score) & (amazon["release_year"]== año)]
        return df.shape[0]
    elif plataforma == "netflix":
        df = netflix[netflix["type"]== "movie" & (netflix["score"]>score) & (netflix["release_year"]== año)]
        return df.shape[0]
    elif plataforma == "hulu":
        df = hulu[hulu["type"]== "movie" & (hulu["score"]>score) & (hulu["release_year"]== año)]
        return df.shape[0]
    elif plataforma == "disney":
        df = disney[disney["type"]== "movie" & (disney["score"]>score) & (disney["release_year"]== año)]
        return df.shape[0]




#pelicula que mas duró
def get(plataforma, tipode_duracion, año):
    if plataforma == "netflix":
        pel_duracion= netflix[(netflix["date_added"]== año) & 
                              (netflix["duration_int"] == (netflix["diratiom_int"].max())) &
                              ( netflix["duration_type"] == tipode_duracion )]#numero maximo de  
        return pel_duracion["title"]
    elif plataforma == "amazon":
        pel_duracion= amazon[(amazon["date_added"]== año) & 
                              (amazon["duration_int"] == (amazon["diratiom_int"].max())) &
                              ( amazon["duration_type"] == tipode_duracion )]#numero maximo de  
        return pel_duracion["title"]
    elif plataforma == "hulu":
        pel_duracion= hulu[(hulu["date_added"]== año) & 
                              (hulu["duration_int"] == (hulu["diratiom_int"].max())) &
                              ( hulu["duration_type"] == tipode_duracion )]#numero maximo de  
        return pel_duracion["title"]
    elif plataforma == "diney":
        pel_duracion= disney[(disney["date_added"]== año) & 
                              (disney["duration_int"] == (disney["diratiom_int"].max())) &
                              ( disney["duration_type"] == tipode_duracion )]#numero maximo de  
        return pel_duracion["title"]
    
    
    #ordenar por score mas alto 
def get(plataforma):
    if plataforma == "netflix":
        df_sec= netflix[netflix["score"] == "+18"]  
        df_sec2=df_sec.sort()
        return df_sec2[netflix["title"][1]]
    elif plataforma == "amazon":
        df_sec= amazon[amazon["score"] == "+18"]  
        df_sec2=df_sec.sort()
        return df_sec2[amazon["title"][1]]
    elif plataforma == "hulu":
        df_sec= hulu[hulu["score"] == "+18"]  
        df_sec2=df_sec.sort()
        return df_sec2[hulu["title"][1]]
    elif plataforma == "disney":
        df_sec= disney[disney["score"] == "+18"]  
        df_sec2=df_sec.sort()
        return df_sec2[disney["title"][1]]
#aqui falta el comando para llamar al segundo elemento de la columna title de las plataformas.     


#aqui se concatenaron los 4 data frame y se realizo un recuento de la cantidad de elementos
#que en todos los dataframe cumole con el "rating" en la columna asi nombrada. 
df_total=pd.concat([netflix,disney,hulu,amazon],axis=0)
@app.get("get_ratin_count")
def get(rating):
    df_total1=df_total[(df_total["rating"]== rating)]
    return df_total1.shape[0]







#direccion que nos ofrece fast api
#http://127.0.0.1:8000

