import pydicom
import os

def anonimitzar_imatge_dicom(ruta_imatge, ruta_desti):
    # Llegir l'arxiu DICOM
    dataset = pydicom.dcmread(ruta_imatge)
    
    # Anonimizar els atributs del pacient
    dataset.PatientID = ""
    dataset.PatientName = ""
    dataset.PatientBirthDate = ""
    dataset.PatientSex = ""
    
    # Guardar l'arxiu DICOM anonimizat en la ruta de destí
    dataset.save_as(ruta_desti)
    
    # Mostrar missatge d'èxit
    print("Imatge anonimitzada guardada amb èxit: " + ruta_desti)

directori_imatges = "C:/Users/Adrià López/Downloads/SR0000/SR0000"
directori_desti = "C:/Users/Adrià López/Desktop/Imatges anonimitzades/"

# Recorrer los archivos en el directorio de imágenes
for arxiu in os.listdir(directori_imatges):
    # Comprobar que el archivo tenga la extensión DICOM (.dcm)
    if arxiu.endswith(".dcm"):
        # Obtener la ruta completa del archivo de imagen
        ruta_imatge = os.path.join(directori_imatges, arxiu)
        
        # Crear la ruta de destino para el archivo anonimizado
        nom_arxiu_anon = os.path.splitext(arxiu)[0] + "_anon.dcm"
        ruta_desti = os.path.join(directori_desti, nom_arxiu_anon)
        
        # Llamar a la función para anonimizar la imagen DICOM y guardarla en la ruta de destino
        anonimitzar_imatge_dicom(ruta_imatge, ruta_desti)