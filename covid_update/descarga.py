import os
import tempfile
from zipfile import ZipFile

import requests
from django.conf import settings


def descargar_datos():
    directorio = os.path.join(
        settings.BASE_DIR,
        settings.DATOS_BASE_DIR,
        settings.CASOS_DIR)
    url = settings.DATOS_URL
    return descargar_zip(url, directorio)


def descargar_catalogos():
    directorio = os.path.join(
        settings.BASE_DIR,
        settings.DATOS_BASE_DIR,
        settings.DESCARGAS_DIR)
    url = settings.DICCIONARIO_DATOS_URL
    return descargar_zip(url, directorio)


def descargar_zip(url, directorio):
    if not os.path.exists(directorio):
        os.makedirs(directorio)

    peticion = requests.get(url)
    with tempfile.TemporaryFile() as archivo_temporal:
        archivo_temporal.write(peticion.content)
        descomprimidos = descomprimir_en_directorio(
            archivo_temporal,
            directorio)

    return descomprimidos


def descomprimir_en_directorio(archivo, directorio):
    descomprimidos = []

    with ZipFile(archivo) as archivo_zip:
        for nombre in archivo_zip.namelist():
            ruta_completa = os.path.join(directorio, nombre)

            if not os.path.exists(ruta_completa):
                archivo_zip.extract(nombre, directorio)
                descomprimidos.append(nombre)

    return descomprimidos
