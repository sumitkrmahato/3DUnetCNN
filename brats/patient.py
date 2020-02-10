import os

from brats.train_isensee2017 import config
from unet3d.prediction import run_validation_case, load_old_model
import tables

itk_snap_location = '/home/sumit/Github/Medical_Imaging/itksnap-3.6.0-20170401-Linux-x86_64/bin/itksnap'
hdf5_file = config["data_file"]
data_file = tables.open_file(hdf5_file, "r")
patients_data = os.path.abspath("test_data")

def show_patient_mri(data_index):
    file_path = os.path.join(patients_data, data_file.root.subject_ids[data_index].decode('utf-8'))
    file_path = os.path.join(file_path, "data_flair.nii.gz")
    # OPen image in ITK-SNAP software
    command = itk_snap_location + " -g " + file_path
    os.system(command)

def show_segmentation(data_index):
    #index = 104 #Patient data index, accept from user

    model_file = config["model_file"]
    model = load_old_model(model_file)
    output_dir = os.path.abspath("test")

    if 'subject_ids' in data_file.root:
        case_directory = os.path.join(output_dir, data_file.root.subject_ids[data_index].decode('utf-8'))
    else:
        case_directory = os.path.join(output_dir, "validation_case_{}".format(data_index))
    run_validation_case(data_index=data_index, output_dir=case_directory, model=model, data_file=data_file,
                        training_modalities=config["training_modalities"], output_label_map=True, labels=config["labels"],
                        threshold=0.5, overlap=16, permute=False)
    seg_file = os.path.join(case_directory, "prediction.nii.gz")
    file_path = os.path.join(patients_data, data_file.root.subject_ids[data_index].decode('utf-8'))
    file_path = os.path.join(file_path, "data_flair.nii.gz")
    command = itk_snap_location + " -g " + file_path + " -s " + seg_file
    os.system(command)

def generate_segmentation_all():
    model_file = config["model_file"]
    model = load_old_model(model_file)
    output_dir = os.path.abspath("prediction_all")

    for data_index in range(167):
        if 'subject_ids' in data_file.root:
            case_directory = os.path.join(output_dir, data_file.root.subject_ids[data_index].decode('utf-8'))
        else:
            case_directory = os.path.join(output_dir, "validation_case_{}".format(data_index))
        run_validation_case(data_index=data_index, output_dir=case_directory, model=model, data_file=data_file,
                            training_modalities=config["training_modalities"], output_label_map=True,
                            labels=config["labels"],
                            threshold=0.5, overlap=16, permute=False)



if __name__ == "__main__":
    index = 104
    #show_patient_mri(index)
    #show_segmentation(index)
    generate_segmentation_all()