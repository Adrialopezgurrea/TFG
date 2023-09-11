import pydicom
import os

def anonimizar_imagen_dicom(ruta_imagen, ruta_destino):
    # Leer el arxivo DICOM
    dataset = pydicom.dcmread(ruta_imagen)
    
    # Anonimizar los atributos del paciente
    dataset.PatientID = ""
    dataset.PatientName = ""
    dataset.PatientBirthDate = ""
    dataset.PatientSex = ""
    
    # Guardar el arxivo DICOM anonimizado en la ruta de destno
    dataset.save_as(ruta_destino)
    
    # Mostrar mensaje de exito
    print("Imagen anonimizada guardada con exito: " + ruta_destino)

directorio_imagenes = "Ruta/Carpeta/Imagenes/Sin/Anonimizar" 
directorio_destino = "Ruta/Carpeta/Imagenes/Anonimizadas"

# Recorrer los archivos en el directorio de imágenes
for archivo in os.listdir(directorio_imagenes):
    # Comprobar que el archivo tenga la extensión DICOM (.dcm)
    if archivo.endswith(".dcm"):
        # Obtener la ruta completa del archivo de imagen
        ruta_imagen = os.path.join(directorio_imagenes, archivo)
        
        # Crear la ruta de destino para el archivo anonimizado
        nombre_arxivo_anon = os.path.splitext(archivo)[0] + "_anon.dcm"
        ruta_destino = os.path.join(directorio_destino, nombre_arxivo_anon)
        
        # Llamar a la función para anonimizar la imagen DICOM y guardarla en la ruta de destino
        anonimizar_imagen_dicom(ruta_imagen, ruta_destino)
