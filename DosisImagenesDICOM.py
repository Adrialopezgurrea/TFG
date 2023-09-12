import os
import pydicom

# Función para obtener el valor de CTDIvol de un archivo DICOM
def get_ctdi_vol_from_dicom(dicom_file_path):
    try:
        dataset = pydicom.dcmread(dicom_file_path)  # Lee el archivo DICOM
        ctdi_vol = dataset.get("CTDIvol", None)  # Obtiene el valor de CTDIvol del archivo DICOM
        return ctdi_vol
    except Exception as e:
        # Maneja cualquier error que pueda ocurrir al leer el archivo DICOM
        print(f"Error al leer el archivo {dicom_file_path}: {e}")
        return None

# Función para explorar un directorio en busca de archivos DICOM y obtener los valores de CTDIvol
def explore_directory(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.lower().endswith(".dcm"):  # Verifica si el archivo tiene la extensión .dcm (formato DICOM)
                dicom_file_path = os.path.join(root, file)  # Obtiene la ruta completa del archivo DICOM
                ctdi_vol = get_ctdi_vol_from_dicom(dicom_file_path)  # Obtiene el valor de CTDIvol del archivo DICOM
                if ctdi_vol is not None:
                    print(f"Archivo DICOM: {dicom_file_path}, CTDIvol: {ctdi_vol}")  # Imprime la información
                else:
                    print(f"Archivo DICOM: {dicom_file_path}, no se encontró la variable CTDIvol.")  # Imprime si no se encontró CTDIvol

if __name__ == "__main__":
    # Ruta del directorio que contiene las imágenes DICOM
    directory_path = "C:/Users/Adrià López/Desktop/TC_PhilipsDescomprimit"
    explore_directory(directory_path)  # Llama a la función para explorar el directorio y procesar los archivos DICOM
