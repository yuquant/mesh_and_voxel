# -*- coding: utf-8 -*-
"""
Author : Jason
Github : https://github.com/yuquant
Description : 
"""
from skimage import measure
import SimpleITK as sitk


def convert_nii_to_obj(nii_path, obj_output_path):
    image = sitk.ReadImage(nii_path)
    image_arr = sitk.GetArrayFromImage(image)
    verts, faces, normals, values = measure.marching_cubes_lewiner(image_arr, 0, spacing=(1.2, 0.625,0.625))
    faces += 1
    with open(obj_output_path, 'w') as thefile:
        for item in verts:
            thefile.write("v {0} {1} {2}\n".format(item[0], item[1], item[2]))

        for item in normals:
            thefile.write("vn {0} {1} {2}\n".format(item[0], item[1], item[2]))

        for item in faces:
            thefile.write("f {0}//{0} {1}//{1} {2}//{2}\n".format(item[0], item[1], item[2]))


def main():
    nii_path = r'D:\projects\mesh_voxel\label_base.nii.gz'
    obj_output_path = r'D:\projects\mesh_voxel\breast.obj'
    convert_nii_to_obj(nii_path, obj_output_path)


if __name__ == "__main__":
    main()
