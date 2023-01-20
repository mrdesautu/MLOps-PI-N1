

                          TRABAJO FINAL DATA ENGENIER - HENRY

  El trabajo presente se ha dividido en cuatro procesos  para su planteamiento y resolucion. considerando cada uno necesario para avanzar siguiente. El mismo ha planteado un desafio, por su complejidad, asi como por la novedad de la tarea para quien suscribe. 

1) limpieza se datos
 la misma se baso en cinco tareas, las cuales seran descritas a continuacion:

  A-se instanciaron los dataframe, realizando de  lectura de los csv coorespondientes y posterior determinacion de tipos de datos, correspondiente a cada columna. Se decidio mantener los cuatro data frame por separado. 
  
  Se creo una nueva columna con una funcion de python, que suma la primera letra de la variable (con el nombre de la plataforma)acorde a cada plataforma, con el numero que se encuentra en la columna show id correspondiente a cada uno de los dataframe. 
  
  B-luego se realizo un remplazo de los datos nulos de la columna rating, la misma indica los la nomenclatura utilizada en las peliculas y series para determinar para que rangos etareos es apta. se cambiaron los valores nulos por un str " G" (se la minimizo posteriormente) (aqui tuve una dificultad ya que no se puede usar la funcion fillna, pero si la funcion replace)  
  
  C-posteriormente con al funcion to_datetime se ordenaron el formato de las fechas de la manera AAAA-MM-DD
  
  D-posteriormente con la funcion split se realizo la division de las columnas en duration_int (de naturaleza entero) y duration_type esta contiene si es temporada, o pelicula.de naturaleza str. de esta manera se obtiene dos columnas diferenciadas por tipo, dando mas funcionalidad al dataset.  
  
   asi mismo se procedio a remplazar los str "Season" y "Seasons" de la columna duration_type. para normalizar el str denominador y poder contabilizar todos dentro del mismo grupo.
  
  E-por ultimo de realiza una conversion de todos los string, mediante la funcion lower, manejando todos los str en minusculas. para evitar interferencias en la modildad de los str. 
  se realizo el guardado de los csv con la funcion to_csv componiendo el nombre con el nombrede la plataforma sumando un _CSV. diferenciandolo de los datos originales. 
  
  

2) Confeccion de preguntas solicitadas:
 Como siguiente accion se comenzó a confeccionar las preguntas, para ello se utilizó el lenguaje de python, asi como las librerias a  el afines como pandas y numpy. aunque no se alcanzo una funcionalidad optima de todas ellas, se describiran los razonamientos logicos utilizados en su confeccion. se describirá brevemente la solicitud, su interpretacion, y la hipotesis utilizada para responder a la solicitud. 

  A-Esta nos pide la cantidad de veces que una palabra aparece en los titulos de una plataforma determinada. 
  para ello se creo una funcion que tome como parametro, una plataforma, segmentando significativamente los datos, y que en su titulo contenga (no importa el lugar, o si esta acompañada de otras palabras) la palabraque se ha cargado en el parametro keyword.
  para ello se uso una funcion if, la misma tiene como condicion coincidir con el nombre de la plataforma ingresada, y que la palabra se encuentre en cualquier posicion de su titulo, al filtrar estos dos parametros define un objeto (definido por todas las filas que cumplen con el parametro solicitado anteriormente). y mediante la funcion shape, se realiza el recuento de las filas (ya que la funcion esta especificada en [0])otorgando la cantidad de filas en el dataframe que cumplen con las condiciones definidas en la funcion. 

  B-cantidad de peliculas por plataforma con un puntaje mayor a XX en determinado año.
  para este pedido se realizo una funcion que recibiese 3 parametros 1=la plataforma; 2=el puntaje, score, y por ultimo el año.  para ello se armo un condicial que cumpliese con las sigueintes esoecificaciones, el nombre de la plataforma, indicando el dataframe a utlizar, ya que aun los mantenemos separados. que el valor de la columna "score" sea mayor al numero ingresado. 3=que el año que figura en al columna "release_year"coincida con el año ingresado en el parametro ingresado. Para finalizar se uso al funcion Shape[0], la cual contabiliza la cantidad de filas, dentro del objeto en el que colocamos la filas que cumplen con los criterios designados. 

  C-la segunda pelicula con mayor partitura para una plataforma determinada, sgun el oorden alfabetico de los titulos.
  los parametros a ingresar deben ser dos
  primero se debe hacer una condicion que clasifique perliculas vs series, quedandonos solo con peliculas. 
  
  D-pelicula que mas duro segun el año, plataforma y tipo de duracion. 
  parametros plataforma y año. sobre estas debemos evaluar cuales tienen la mayor duracion. devolviendo el titulo de la pelicula que mas minutos duro en ese año. 
  
  E-cantidad de series y peliculas por raiting
  para el modo de trabajo elegido, aqui el desafio estara en juntar los 4 dataframe , para en ellos contabilizar cuantos cumplen con la funcion de tener eñ rating mas alto.
  


3) Armado de apis, realizacion de consulta online

Para ello fue necesario crear un archivo .py, al mismo se lo denomino main.py . este archivo contendria la importacion de fastapi, su preceso de instanciado en un objeto llamado app. el cual sera evocado mediante un "decorado" consignado por la varibale @app (app =nombre que se le otorgo a la variable) 
cada funcion se definio posterior a su vinculacion mediante este metodo. colocando las diferentes funciones creadas anteriormente en jupyter. 
luego de esta confeccion, mediante la consola se realiza un entorno virtual, mediante la descarga de fastapi y uvicorn, se descargan las librerias necesarias, para que se cargen en el contenedor que dokerizará nuestra libreria fastapi, para mayor eficiencia del sistema. 
para activar nuestro entorno virtual usaremos la funcion :
source tutorial-env/bin/activate
esto nos permitirá entrar a nuestro entorno virtual. Antes de usar nuestra funcion debemos ubicarnos en la carpeta que hemos creado donde poseemos todos los archivos (main.py, bases de datos varias, etc).
posteriormente levantamos la api, mediante la funcion 
uvicorn main:app --reload
esta detectara los cambios para actualizar cualquier cambio realizado en el archivo (este debe guardarse para que el cambio se refleje en el sistema)
asi mismo nos entregará una ubicacion especifica a la cual, mientras se encuentre activo el proceso, podremos invocar la funcion definida mediente el codigo especificado en la "decoracion" de la api (Ej. si el decorado es @app.get ("asd"). asd es el la direccion a ingresar posterior a la direccion otorgada para ejecutar la funcion y que desde un navegador podamos obtener el resultado que la funcion arroja. 


4) utilizacion de Deta. 
pero no podemos estar usando todo el tiempo la terminal de la computadora, es por ello que utilizaremos deta, para ello debemos seguir una serie de pasos...
a- instalar deta
b- crear una cuenta en deta
c- asi mismo debemos crear un txt con el nombre requirement que contenga la palabra fastapi
d- ingresar a deta desde la terminal (ubicandonos en la carpeta que contiene el main.py)  con la funcion deta loing lo cual nos enviara a la pagina para realizar el ingreso al usuario.
e- lueg colocaremos  deta new. entiendo que esta funcion creara un repositorio virtual del archivo.py que se encuetre en la carpeta que nos pocisionamos. 
otorgandonos en este proceso una direccion, que podemos colocar en un navegador y ejecutar la funcion definida en nuestro archivo.py (en nuestro caso es main.py). pudiendo ejecutarlo sin necesidad de que subamos la api desde nuestra terminal. 
f- se uso la funcion deta auth disable, esta hace publico el acceso a la informacion.



link video explicativo de youtube:



gracias por su tiempo!




