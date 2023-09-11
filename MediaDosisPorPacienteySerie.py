import os
import pydicom
from collections import defaultdict

# Función para obtener el valor de CTDIvol de un archivo DICOM
def get_ctdi_vol_from_dicom(dicom_file_path):
    try:
        dataset = pydicom.dcmread(dicom_file_path)
        ctdi_vol = dataset.get("CTDIvol", None)
        return ctdi_vol
    except Exception as e:
        return None

# Función para calcular las medias de CTDIvol
def calculate_average_ctdi_vol(directory_path):
    patient_ctdi = defaultdict(list)  # Almacena los valores de CTDIvol por paciente
    
    # Itera a través de los pacientes en el directorio principal
    for patient_dir in os.listdir(directory_path):
        patient_dir_path = os.path.join(directory_path, patient_dir)
        
        # Verifica si el elemento en el directorio principal es un subdirectorio (paciente)
        if os.path.isdir(patient_dir_path):
            
            # Itera a través de las series de cada paciente
            for series_dir in os.listdir(patient_dir_path):
                series_dir_path = os.path.join(patient_dir_path, series_dir)
                
                # Verifica si el elemento en el subdirectorio es un subdirectorio (serie)
                if os.path.isdir(series_dir_path):
                    ctdi_values = []  # Almacena los valores de CTDIvol para la serie
                    
                    # Itera a través de los archivos en la serie
                    for root, dirs, files in os.walk(series_dir_path):
                        for file in files:
                            if file.lower().endswith(".dcm"):
                                dicom_file_path = os.path.join(root, file)
                                ctdi_vol = get_ctdi_vol_from_dicom(dicom_file_path)
                                
                                # Si se encuentra el valor de CTDIvol, agrégalo a la lista
                                if ctdi_vol is not None:
                                    ctdi_values.append(ctdi_vol)
                    
                    if ctdi_values:
                        # Calcula la media de los valores de CTDIvol para la serie y paciente
                        series_average = sum(ctdi_values) / len(ctdi_values)
                        print(f"Media de CTDIvol para paciente {patient_dir}, serie {series_dir} del equipo Somatom Go Top: {series_average}")
                        patient_ctdi[patient_dir].extend(ctdi_values)
    
    # Calcula y muestra las medias de CTDIvol por paciente
    for patient_id, patient_values in patient_ctdi.items():
        patient_average = sum(patient_values) / len(patient_values)
        print(f"Media de CTDIvol para paciente {patient_id} del equipo Somatom Go Top: {patient_average}")

if __name__ == "__main__":
    directory_path = "Ruta/de/la/carpeta/con/imagenes/DICOM"
    calculate_average_ctdi_vol(directory_path)



