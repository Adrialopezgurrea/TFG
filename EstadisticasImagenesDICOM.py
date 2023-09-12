import os
import pydicom
import numpy 
import matplotlib.pyplot 

def get_ctdi_vol_from_dicom(dicom_file_path):
    try:
        dataset = pydicom.dcmread(dicom_file_path)  # Lee el archivo DICOM
        ctdi_vol = dataset.get("CTDIvol", None)  # Obtiene el valor de la variable CTDIvol si está presente
        return ctdi_vol
    except Exception as e:
        print(f"Error al leer el archivo {dicom_file_path}: {e}")
        return None

def calculate_statistics(directory_path):
    ctdi_vol_values = []  # Lista para almacenar los valores de CTDIvol
    # Recorre el directorio y todos los subdirectorios usando os.walk
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.lower().endswith(".dcm"):  # Comprueba si el archivo es DICOM
                dicom_file_path = os.path.join(root, file)  # Construye la ruta completa al archivo DICOM
            
                ctdi_vol = get_ctdi_vol_from_dicom(dicom_file_path)  # Obtiene el valor de CTDIvol del archivo DICOM
                
                
                if ctdi_vol is not None:
                    ctdi_vol_values.append(ctdi_vol)  # Agrega el valor de CTDIvol a la lista
                
    return ctdi_vol_values

if __name__ == "__main__":
    directory_path = "Ruta/de/la/carpeta/con/imagenes/DICOM"  # Ruta del directorio que contiene las imágenes DICOM
    ctdi_vol_values = calculate_statistics(directory_path)  # Calcula los valores de CTDIvol
    
    
    if ctdi_vol_values:
        mean_ctdi_vol = numpy.mean(ctdi_vol_values)  # Calcula la media de CTDIvol
        std_ctdi_vol = numpy.std(ctdi_vol_values)  # Calcula la desviación estándar de CTDIvol
        data_range = numpy.max(ctdi_vol_values) - numpy.min(ctdi_vol_values)  # Calcula el rango de CTDIvol
        max_ctdi = numpy.max(ctdi_vol_values)
        min_ctdi = numpy.min(ctdi_vol_values)
        q1_ctdi_vol = numpy.percentile(ctdi_vol_values, 25)  # Calcula el percentil 25 (primer cuartil)
        q3_ctdi_vol = numpy.percentile(ctdi_vol_values, 75)  # Calcula el percentil 75 (tercer cuartil)
        coef_var_ctdi_vol = (std_ctdi_vol / mean_ctdi_vol) * 100  # Calcula el coeficiente de variación
       
    
        print(f"Estadísticas de la maquina "Nombre_Equipo":")
        print(f"Media de CTDIvol: {mean_ctdi_vol}")
        print(f"Desviación estándar de CTDIvol: {std_ctdi_vol}")
        print(f"Rango de CTDIvol: {data_range}")
        print(f"Num màxim de CTDIvol: {max_ctdi}")
        print(f"Num mínim de CTDIvol: {min_ctdi}")
        print(f"Primer cuartil (Q1) de CTDIvol: {q1_ctdi_vol}")
        print(f"Tercer cuartil (Q3) de CTDIvol: {q3_ctdi_vol}")
        print(f"Coeficiente de variación de CTDIvol: {coef_var_ctdi_vol:.2f}%")
    
        

        
        # Crea y muestra un histograma de CTDIvol
        matplotlib.pyplot.hist(ctdi_vol_values, bins=20, edgecolor='black')
        matplotlib.pyplot.xlabel('CTDIvol (mGy)')
        matplotlib.pyplot.ylabel('Frecuencia')
        matplotlib.pyplot.title('Histograma de CTDIvol de la maquina "Nombre_Equipo"')
        matplotlib.pyplot.show()
    else:
        print("No se encontraron imágenes DICOM con la variable CTDIvol.")
