from fastapi import FastAPI
import pandas as pd
import numpy as np
import mitosheet 
from database import netflix 

amazon = pd.read_csv(r"Datasets/amazon_prime_titles-score.csv")
disney = pd.read_csv(r"Datasets/disney_plus_titles-score.csv")
hulu = pd.read_csv(r"Datasets/hulu_titles-score (2).csv")
netflix = pd.read_csv(r"Datasets/netflix_titles-score.csv")



app = FastAPI()

@app.get("/")
def index():
    return "hola chico"

@app.get("get_word_count")
def get_word_count(plataforma, keyword):
    if plataforma == "amazon":
        return amazon[amazon["title"].str.contains(keyword)].shape[0]
    elif plataforma == "netflix":
        return netflix[netflix["title"].str.contains(keyword)].shape[0]
    elif plataforma == "disney":
        return disney[disney["title"].str.contains(keyword)].shape[0]
    elif plataforma == "hulu":
        return hulu[hulu["title"].str.contains(keyword)].shape[0]

@app.get("get_score_count")
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

@app.get("get_longest")
def get_longest(plataforma, tipode_duracion, año):
    if plataforma == "netflix":
        pel_duracion= netflix[(netflix["date_added"]== año) & (netflix["duration_int"] == (netflix["diratiom_int"].max())) & ( netflix["duration_type"] == tipode_duracion )]#numero maximo de  
        return pel_duracion["title"]

#http://127.0.0.1:8000

