import os
import pydicom
import matplotlib.pyplot as plt
import seaborn 

# Función para obtener el valor de CTDIvol de un archivo DICOM
def get_ctdi_vol_from_dicom(dicom_file_path):
    try:
        dataset = pydicom.dcmread(dicom_file_path)
        ctdi_vol = dataset.get("CTDIvol", None)
        return ctdi_vol
    except Exception as e:
        print(f"Error al llegir l'arxiu {dicom_file_path}: {e}")
        return None

# Función para encontrar archivos DICOM en un directorio y sus subdirectorios
def find_dicom_files(directory_path):
    dicom_files = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.lower().endswith(".dcm"):
                dicom_files.append(os.path.join(root, file))
    return dicom_files

if __name__ == "__main__":
    # Rutas a los directorios principales de los archivos DICOM
    directory_path1 = "C:/Users/Adrià López/Desktop/TC_PhilipsDescomprimit"
    directory_path2 = "C:/Users/Adrià López/Desktop/Somatom.Force_Descomprimit/Anonims"
    directory_path3 = "C:/Users/Adrià López/Desktop/Somatom.Go.Top_Descomprimit/Anonims"
    
    # Buscar archivos DICOM en cada directorio
    dicom_files1 = find_dicom_files(directory_path1)
    dicom_files2 = find_dicom_files(directory_path2)
    dicom_files3 = find_dicom_files(directory_path3)
    
    # Verificar que haya al menos un archivo DICOM en cada directorio
    if len(dicom_files1) >= 1 and len(dicom_files2) >= 1 and len(dicom_files3) >= 1:
        ctdi_vol_values_file1 = []
        ctdi_vol_values_file2 = []
        ctdi_vol_values_file3 = []
        
        # Obtener los valores de CTDIvol de cada archivo DICOM en los directorios
        for dicom_file in dicom_files1:
            ctdi_vol = get_ctdi_vol_from_dicom(dicom_file)
            if ctdi_vol is not None:
                ctdi_vol_values_file1.append(ctdi_vol)
        
        for dicom_file in dicom_files2:
            ctdi_vol = get_ctdi_vol_from_dicom(dicom_file)
            if ctdi_vol is not None:
                ctdi_vol_values_file2.append(ctdi_vol)
        
        for dicom_file in dicom_files3:
            ctdi_vol = get_ctdi_vol_from_dicom(dicom_file)
            if ctdi_vol is not None:
                ctdi_vol_values_file3.append(ctdi_vol)
        
        # Verificar que haya valores de CTDIvol en cada archivo
        if len(ctdi_vol_values_file1) > 0 and len(ctdi_vol_values_file2) > 0 and len(ctdi_vol_values_file3) > 0:
            # Etiquetas para los archivos en el gráfico
            labels = ['Philips', 'Siemens_Force', 'Siemens_Go_Top']
            all_ctdi_vol_values = [ctdi_vol_values_file1, ctdi_vol_values_file2, ctdi_vol_values_file3]
            
            # Crear un violin plot utilizando Seaborn
            seaborn.violinplot(data=all_ctdi_vol_values)
            plt.xticks(ticks=[0, 1, 2], labels=labels)
            plt.xlabel('Equips')
            plt.ylabel('CTDIvol(mGy)')
            plt.title('Comparació de CTDIvol entre Equips')
            plt.show()
        else:
            print("Almenys un dels arxius no té valor de CTDIvol.")
    else:
        print("No s'han trobat arxius DICOM en els directoris principals.")
