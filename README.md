# DICOM File Organizer

## Project Overview
The DICOM File Organizer is an open-source Python script designed to organize DICOM files based on Patient ID, Study Date, and Series Description. This tool utilizes the `pydicom` library to extract relevant information from DICOM files and organizes them into a structured folder hierarchy, making it easier to manage and access medical imaging data.

## Usage
Follow these steps to use the DICOM File Organizer:

### Prerequisites
- Python 3.x installed
- Install the required libraries using:



### Instructions
1. **Clone the repository or download the Python script.**
2. **Prepare your DICOM data:**
  - Ensure your DICOM files are organized within a root folder.
3. **Update the Python script:**
  - Modify the `root_folder` variable in the script with the path to your root DICOM data folder.
4. **Run the Python script:**
  - Execute the script in your terminal or Python environment.
  ```
  python dicom_organizer.py
  ```
5. **Review the output:**
  - The script will organize the DICOM files into a folder structure based on Patient ID, Study Date, and Series Description.
  - It will also generate a CSV file summarizing the DICOM file information with Patient ID, Study Date, and Series Description columns.

### Generated CSV File
The script will generate a CSV file named `patient_info.csv` containing the following columns:
- Patient ID
- Study Date
- Series Description (Multiple descriptions separated by commas for each unique Patient ID and Study Date combination)

### Note
- Ensure that the DICOM files contain the necessary tags: `PatientID`, `StudyDate`, and `SeriesDescription` for proper organization and CSV generation.
- Adjust the code if your DICOM files have different tag information.

## Contributing
Contributions to this open-source project are welcome. To contribute, follow these steps:
- Fork the repository
- Create your feature branch (`git checkout -b feature/YourFeature`)
- Commit your changes (`git commit -am 'Add your feature'`)
- Push to the branch (`git push origin feature/YourFeature`)
- Create a pull request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- The DICOM File Organizer script was created using the `pydicom` library.

