import os
import shutil

def easy_rename_img(old_path, new_path, extension='.jpg', Copy=True):
    if not os.path.exists(old_path):
        raise FileExistsError('The path does not exist! You need to check it')

    file_list = os.listdir(old_path)
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    image_list = []
    image_list = [file for file in file_list if file.endswith(extension)]
    image_list.sort()
    l = len(str(len(image_list)))

    for index, image in enumerate(image_list):
        old_image_path = os.path.join(old_path, image)
        new_image_name = str(index).zfill(l) + extension # 0001.jpg
        if Copy:
            new_image_path = os.path.join(new_path, new_image_name)
            shutil.copyfile(old_image_path, new_image_path)
        else:
            new_image_path = os.path.join(old_path, new_image_name)
            os.rename(old_image_path, new_image_path)
    
    print('Easy rename complete!')


if __name__ == '__main__':
    old_path = '/Users/sunshizhe/Downloads/rename'
    new_path = '/Users/sunshizhe/Downloads/example_pic'
    easy_rename_img(old_path, new_path, extension='.jpg', Copy=False)

