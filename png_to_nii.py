import glob
import imread
import imageio
import numpy  as np
import nibabel as nib

list_files = glob.glob("/home/sumit/Github/Medical_Imaging/glioma cases/dhanunjaya full study/flair axials/*.jpg")
list_files.sort()
nifti_mat = []
for i,fname in enumerate(list_files):
    #print(fname)
    x = imageio.imread(fname)
    nifti_mat.append(x)
    #nifti_mat(:,:, i)
nifti_mat = np.asarray(nifti_mat)
print(type(nifti_mat))
print(nifti_mat.shape)
#arr_reshaped = np.transpose(nifti_mat, (1, 2, 0))
arr_reshaped = np.transpose(nifti_mat, (1,2,3,0))
print(type(nifti_mat))
print(arr_reshaped.shape)
filename = "durgarao_flair_3d.nii"
#imageio.imwrite(filename, arr_reshaped)
img = nib.Nifti1Image(arr_reshaped, None) #check if anything is to be gibven as affine paraeter
nib.save(img, filename)
