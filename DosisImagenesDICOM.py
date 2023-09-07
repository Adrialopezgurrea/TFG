import os
import pydicom

def get_ctdi_vol_from_dicom(dicom_file_path):
    try:
        dataset = pydicom.dcmread(dicom_file_path)
        ctdi_vol = dataset.get("CTDIvol", None)
        return ctdi_vol
    except Exception as e:
        print(f"Error al leer el archivo {dicom_file_path}: {e}")
        return None

def explore_directory(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.lower().endswith(".dcm"):
                dicom_file_path = os.path.join(root, file)
                ctdi_vol = get_ctdi_vol_from_dicom(dicom_file_path)
                if ctdi_vol is not None:
                    print(f"Archivo DICOM: {dicom_file_path}, CTDIvol: {ctdi_vol}")
                else:
                    print(f"Archivo DICOM: {dicom_file_path}, no se encontró la variable CTDIvol.")

if __name__ == "__main__":
    # Ruta del directorio que contiene las imágenes DICOM
    directory_path = "C:/Users/Adrià López/Desktop/TC_PhilipsDescomprimit"
    explore_directory(directory_path)