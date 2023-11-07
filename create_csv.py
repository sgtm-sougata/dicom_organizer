import os
import pydicom
import csv

def create_patient_info_csv(root_folder):
    # Dictionary to store patient information
    patient_info = {}

    # Walk through the directory tree
    for dirpath, dirnames, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.endswith('.dcm'):
                filepath = os.path.join(dirpath, filename)
                try:
                    # Load the DICOM file
                    dcm = pydicom.dcmread(filepath)

                    # Extract required information
                    patient_id = str(dcm.get("PatientID"))
                    study_date = str(dcm.get("StudyDate"))
                    series_desc = str(dcm.get("SeriesDescription"))

                    # If the combination of Patient ID and Study Date exists, update the Series Description
                    key = (patient_id, study_date)
                    if key in patient_info:
                        patient_info[key].add(series_desc)
                    else:
                        patient_info[key] = {series_desc}

                except pydicom.errors.InvalidDicomError:
                    print(f"Invalid DICOM file: {filepath}")

    # Write the information to a CSV file
    with open('patient_info.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Patient ID', 'Study Date', 'Series Description'])

        for (patient_id, study_date), series_desc in patient_info.items():
            csv_writer.writerow([patient_id, study_date, ', '.join(series_desc)])


