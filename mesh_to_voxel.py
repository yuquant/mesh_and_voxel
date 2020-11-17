# -*- coding: utf-8 -*-
"""
Author : Jason
Github : https://github.com/yuquant
Description :
https://drububu.com/miscellaneous/voxelizer/?out=txt
"""


import numpy as np
import SimpleITK as sitk


def make_voexl_arr(txt_file_path, arr_size):
    tmp_arr = np.zeros(arr_size, dtype=np.uint16)
    with open(txt_file_path, 'r') as f:
        for line in f.readlines():
            num_strs = line.strip("\n").split(',')
            if num_strs:
                try:
                    x, y, z = list(map(int, num_strs))
                    tmp_arr[x+1, y+1, z+1] = 1
                except Exception as e:
                    print(line, e)

    return tmp_arr


def main():
    # txt_file_path = r'D:\projects\mesh_voxel\breast_200.txt'
    txt_file_path = r'D:\360安全浏览器下载\breast_256_stl.txt'
    arr_size = (256, 256, 256)
    arr = make_voexl_arr(txt_file_path, arr_size)
    sitk_img = sitk.GetImageFromArray(arr)
    sitk.WriteImage(sitk_img, r'D:\projects\mesh_voxel\brest_256.nii.gz')


if __name__ == "__main__":
    main()





