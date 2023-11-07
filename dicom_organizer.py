
import os
import pydicom
import shutil
from create_csv import create_patient_info_csv
# Path to the root directory containing DICOM files
root_folder = os.path.join(os.getcwd(), "data")

# Function to get DICOM tags
def get_tag_value(dcm, tag):
    if tag in dcm:
        return str(dcm[tag].value)
    else:
        return "Unknown"

# Walk through the directory tree
for dirpath, dirnames, filenames in os.walk(root_folder):
    for filename in filenames:
        if filename.endswith('.dcm'):
            filepath = os.path.join(dirpath, filename)
            try:
                # Load the DICOM file
                dcm = pydicom.dcmread(filepath)

                # Extract required information
                patient_id = get_tag_value(dcm, "PatientID")
                study_date = get_tag_value(dcm, "StudyDate")
                series_desc = get_tag_value(dcm, "SeriesDescription")

                # Create directories if they don't exist
                patient_dir = os.path.join(root_folder, patient_id)
                study_dir = os.path.join(patient_dir, study_date)
                series_dir = os.path.join(study_dir, series_desc)

                os.makedirs(series_dir, exist_ok=True)

                # Move the DICOM file to the appropriate directory
                new_filepath = os.path.join(series_dir, filename)
                shutil.move(filepath, new_filepath)

            except pydicom.errors.InvalidDicomError:
                print(f"Invalid DICOM file: {filepath}")

print("DICOM files organized successfully.")
create_patient_info_csv(root_folder)
print("Create Patient Info csv successfully")