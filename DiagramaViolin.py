# Importación de las bibliotecas necesarias
import os                    # Para trabajar con archivos y directorios
import pydicom               # Para leer archivos DICOM
import matplotlib.pyplot as plt  # Para trazar gráficos
import seaborn              # Para trazar un gráfico de violín

# Función para obtener el valor de CTDIvol de un archivo DICOM
def get_ctdi_vol_from_dicom(dicom_file_path):
    try:
        # Lee el archivo DICOM en la ruta especificada
        dataset = pydicom.dcmread(dicom_file_path)
        
        # Obtiene el valor de CTDIvol del archivo DICOM (si existe)
        ctdi_vol = dataset.get("CTDIvol", None)
        return ctdi_vol
    except Exception as e:
        # Maneja cualquier error que pueda ocurrir al leer el archivo DICOM
        print(f"Error al leer el archivo {dicom_file_path}: {e}")
        return None

# Función para encontrar archivos DICOM en un directorio y sus subdirectorios
def find_dicom_files(directory_path):
    dicom_files = []  # Lista para almacenar las rutas de los archivos DICOM encontrados
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.lower().endswith(".dcm"):  # Comprueba si el archivo tiene la extensión .dcm
                dicom_files.append(os.path.join(root, file))  # Agrega la ruta del archivo a la lista
    return dicom_files

if __name__ == "__main__":
    # Definición de rutas a los directorios principales de los archivos DICOM
    directory_path1 = "Ruta/Carpeta/Imagenes/Dicom/1"
    directory_path2 = "Ruta/Carpeta/Imagenes/Dicom/2"
    directory_path3 = "Ruta/Carpeta/Imagenes/Dicom/3"
    
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
            labels = ['Philips', 'Siemens_Force', 'Siemens_Go_Top'] #Aqui van los nombres de los equipos a comparar, he dejado los que usé yo
            all_ctdi_vol_values = [ctdi_vol_values_file1, ctdi_vol_values_file2, ctdi_vol_values_file3]
            
            # Crear un gráfico de violín utilizando Seaborn
            seaborn.violinplot(data=all_ctdi_vol_values)
            plt.xticks(ticks=[0, 1, 2], labels=labels)
            plt.xlabel('Equipos')
            plt.ylabel('CTDIvol(mGy)')
            plt.title('Comparación de CTDIvol entre Equipos')
            plt.show()
        else:
            print("Al menos uno de los archivos no tiene valor de CTDIvol.")
    else:
        print("No se encontraron archivos DICOM en los directorios principales.")

