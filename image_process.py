from torch.utils.data import Dataset
import os
from utils import *
from torchvision import transforms

transform = transforms.Compose([
    transforms.ToTensor()
])


class UnetDataset(Dataset):
    def __init__(self, path_to_segment, path_to_image):
        self.path_to_segment = path_to_segment
        self.path_to_image = path_to_image
        self.name = os.listdir(path_to_segment)

    def __len__(self):
        return len(self.name)

    def __getitem__(self, index):
        segment_name = self.name[index]
        segment_path = os.path.join(self.path_to_segment, segment_name)
        image_path = os.path.join(self.path_to_image, segment_name)
        segment_image = Unet(segment_path)
        image = Unet(image_path)
        return transform(image), transform(segment_image)


class VGGDataset(Dataset):
    def __init__(self, path):
        self.path = path
        self.name = os.listdir(path)

    def __len__(self):
        return len(self.name)

    def __getitem__(self, index):
        image_name = self.name[index]
        image_path = os.path.join(self.path, image_name)
        image = VGG(image_path, MODE='Mean')
        label = image_name.split('.')[0]  # 0001.jpg -> 0001, customed by yourself.
        return transform(image), label


if __name__ == '__main__':
    data = UnetDataset('/Your project path',
                       '/Your project path')
    data = VGGDataset('/Your project path')
    print(data[0][0].shape)
    print(data[0][1])
    # 将返回的图片保存到example_img
    # data[0][0].save('exampe_img/1.jpg')
