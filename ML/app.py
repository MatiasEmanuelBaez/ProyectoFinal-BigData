import streamlit as st
import pandas as pd
import random
import csv

st.set_page_config(page_title="Restaurantes", page_icon="♨")

######################### FUNCIONES #########################

### Cargamos las ciudades de las que pueden elegir
lista_ciudades = []

def obtener_ciudades_desde_csv():
    with open('datos//ciudades.csv', 'r', newline='', encoding='utf-8') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv, delimiter=';')
        encabezados = next(lector_csv)
        
        # Filtramos por las ciudades en las cuales tenemos restaurantes recomendados al cliente.
        ciudades_a_mantener = [2, 32, 37, 242, 243, 299, 332, 361, 393]
        filas_filtradas = [fila for fila in lector_csv if int(fila['id_ciudad']) in ciudades_a_mantener]
        
        for fila in filas_filtradas:
            if 'ciudad' in fila:
                lista_ciudades.append(fila['ciudad'])


### Frases de cumplido para la eleccion de ciudades
def obtener_frase_aleatoria():
    frases = [
        "excelente elección!",
        "increíble decisión.",
        "has elegido sabiamente.",
        "bravo por tu elección!",
        "buena decisión!",
        "estupenda elección!",
        "increíblemente bien elegido!",
        "fantástica elección!",
    ]

    return random.choice(frases)

### Cargamos el sistema de recomndación creado en notebook "recomendaciones" y almacenado
def cargar_sis_recomendacion():
    jaccard_csv = pd.read_csv('datos//df_jaccard.csv', sep=';', index_col='nombre')
    return jaccard_csv

### Carga de restaurantes con sus datos
def cargar_restaurantes():

    # Cargamos las categorias a un df
    dfcategorias = pd.read_csv('datos//categorias.csv', index_col='id_categoria')
    dfcategorias = dfcategorias.drop(['Unnamed: 0'], axis=1)

    # Cargamos los restaurantes a un df
    dfrestaurantes = pd.read_csv('datos//restaurantes.csv', index_col='id_restaurante')
    dfrestaurantes = dfrestaurantes.drop(['Unnamed: 0'],axis=1)

    # Cargamos la tabla intermedia
    dfcategoriasrestaurantes = pd.read_csv('datos//categoriasrestaurantes.csv', index_col='id_categoria_restaurante')
    dfcategoriasrestaurantes = dfcategoriasrestaurantes.drop(['Unnamed: 0'],axis=1)
    
    # Cargamos las ciudades a un df
    dfciudades = pd.read_csv('datos//ciudades.csv', index_col='id_ciudad', sep=';')

    # Unimos las categorias con la tabla intermedia y eliminamos columnas que no sirven para el analisis
    dfagrupado = pd.merge(dfcategoriasrestaurantes, dfcategorias, left_on= 'id_categoria', right_on= 'id_categoria', how= 'left')
    dfagrupado = dfagrupado.drop(['id_categoria'], axis=1)

    # Unimos ahora los restaurantes gracias a la tabla intermedia
    dfagrupado = pd.merge(dfagrupado, dfrestaurantes, left_on='id_restaurante', right_on='id_restaurante', how='left')
    dfagrupado = dfagrupado.drop(['identificador_yelp', 'identificador_google', 'latitud', 'longitud'], axis=1)
    
    # Unimos ahora las ciudades
    dfagrupado = pd.merge(dfagrupado, dfciudades, left_on='id_ciudad', right_on='id_ciudad', how='left')
    dfagrupado = dfagrupado.drop(['id_estado'], axis=1)
    
    # Dejamos en el df solo las ciudades que utilizaremos en el sistema de recomendacion
    dfagrupado = dfagrupado[dfagrupado['id_ciudad'].isin([2, 32, 37, 242, 243, 299, 332, 361, 393])]
    
    return dfagrupado

### Recomendación
def recomendacion_restaurant(palabra_clave: str):
    jaccard_csv = cargar_sis_recomendacion()
    dfagrupado = cargar_restaurantes()    
    
    # Filtramos los restaurantes que pertenecen a nuestro cliente
    restaurantes_prop = dfagrupado[dfagrupado['id_restaurante'].isin([8265, 8321, 10158, 10629, 19398, 9499, 8018, 9510, 15316, 4915])]
    # Filtramos por la ciudad que puso el usuario
    restaurantes_prop = restaurantes_prop[restaurantes_prop['ciudad'].isin([txtCiudad])]
    # Ordeno los restaurantes por rating y tomo solo el mejor
    restaurantes_prop = restaurantes_prop.sort_values(by='avg_rating', ascending=False).head(1)
    # Dejamos solo los campos que vamos a necesitar
    restaurantes_prop = restaurantes_prop[['nombre', 'direccion', 'ciudad', 'avg_rating']]
    
    # Tomamos los datos generales y agrupamos para evitar restaurantes duplicados.
    dfagrupado_agrupado = dfagrupado.groupby(['nombre','direccion','ciudad']).agg({'avg_rating': 'mean'}).reset_index()
    
    # Filtrar restaurantes que contienen la palabra clave
    restaurantes_recom = dfagrupado[dfagrupado['nombre'].str.lower().str.contains(palabra_clave, case=False)]
    if restaurantes_recom.empty:
        print(f"No se encontraron restaurantes que contengan '{palabra_clave}'.")
        return []
    
    # Obtener el nombre del restaurante
    restaurantes_recom = restaurantes_recom['nombre'].iloc[0]
    # Obtener recomendaciones usando el nombre del restaurante
    recomendaciones = jaccard_csv[restaurantes_recom].sort_values(ascending=False)
    
    restaurantes_recom = recomendaciones.reset_index()
    # Unimos la recomendacion con el maestro de restaurantes para obtener los datos: direccion, ciudad y avg_rating
    restaurantes_recom = pd.merge(restaurantes_recom, dfagrupado_agrupado, left_on='nombre', right_on='nombre', how='left')
    # Dejamos solo los campos que vamos a necesitar
    restaurantes_recom = restaurantes_recom[['nombre', 'direccion', 'ciudad', 'avg_rating']]
    # Filtramos los resultados para que solo sean 4 recomendados
    restaurantes_recom = restaurantes_recom[restaurantes_recom['ciudad'] == txtCiudad].head(4)
    
    # Agregamos en primer lugar, el restaurante perteneciente a nuestro cliente que tenga mejor avg_reviews
    # Los demas lugares seran verdaderas recomendaciones
    restaurantes_prop = pd.concat([restaurantes_prop, restaurantes_recom]).reset_index(drop=True)
 
    return restaurantes_prop

#########################           #########################

obtener_ciudades_desde_csv()


st.title("♨️ Recomendación Restaurantes")
st.write("🥐 🥨 🍗 🍔 🍕 🌭 🥪 🌮 🌯 🍘 🥟 🍨 🍩 ☕ 🧇 🧋 🍵 🍰 🍡 🍪 🧁 🥗 🦐 🥠 🥞 🍜 🍝 🍙")

st.header("🗺️ ¿En qué ciudad de Florida te encuentras?")
txtCiudad = st.selectbox("Confirma tu ubicación", lista_ciudades)

if txtCiudad !="":
    st.write(txtCiudad,' ,', obtener_frase_aleatoria())


st.header("🍽️ ¿Qué menú se te antoja hoy?")
options = st.text_input("Ej.: Cafe, Smoothies, Pizza, Tacos, Hot Dog, Chicken, Sandwich, Burgers, Seafood, Chinese, Thai, Italian, Argentinian")
button6 = st.button("Recomendar")
if button6:
    st.write(recomendacion_restaurant(options))

st.divider()

st.image('imagenes//SG-logo.png', caption=None, width=150, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
