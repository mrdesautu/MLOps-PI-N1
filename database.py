from peewee import *
import pandas as pd
netflix= pd.read_csv("netflix_csv")
hulu=pd.read_csv("hulu_csv")
disney=pd.read_csv("disney_csv")
amazon=pd.read_csv("amazon")

netflix= MySQLDatabase("netflix_csv",user="root",host="/home/martin/Escritorio/data engenier/netflix_csv.csv",port=3306)

