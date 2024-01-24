from PIL import Image, ImageOps, ImageStat

def Unet(path, size=(256, 256)):
    image = Image.open(path)
    temp = max(image.size)
    mask = Image.new('RGB', (temp, temp), (0,0,0))
    mask.paste(image, (0,0))
    mask = mask.resize(size)
    return mask

def VGG(path, size=(224, 224), MODE='RGB'):
    image = Image.open(path)
    size = size[0]
    if(MODE == 'RGB'): mask = White_background(image, size)
    elif(MODE == 'Mirror'): mask = resize_and_mirror_padding(image, size)
    elif(MODE == 'Mean'): mask = resize_and_mean_color_padding(image, size)
    elif(MODE == 'Transparent'): mask = resize_and_transparent_padding(image, size)
    else: raise ValueError('MODE must be one of RGB, Mirror, Mean, Transparent')
    return mask


def White_background(img, size, fill=0):
    img.thumbnail((size, size), Image.LANCZOS)
    new_img = Image.new("RGB", (size, size), fill)
    x = (size - img.size[0]) // 2
    y = (size - img.size[1]) // 2
    new_img.paste(img, (x, y))

    return new_img

def resize_and_mirror_padding(image, desired_size):
    # 等比例缩放图像
    image.thumbnail((desired_size, desired_size), Image.LANCZOS)

    # 镜像填充
    delta_w = desired_size - image.width
    delta_h = desired_size - image.height
    padding = (delta_w//2, delta_h//2, delta_w-(delta_w//2), delta_h-(delta_h//2))
    return ImageOps.expand(image, padding)

def resize_and_mean_color_padding(image, desired_size):
    # 等比例缩放图像
    image.thumbnail((desired_size, desired_size), Image.LANCZOS)

    # 均值颜色填充
    mean_color = ImageStat.Stat(image).mean
    new_img = Image.new("RGB", (desired_size, desired_size), tuple(map(int, mean_color)))
    new_img.paste(image, ((desired_size - image.width) // 2, (desired_size - image.height) // 2))
    return new_img

def resize_and_transparent_padding(image, desired_size):
    # 等比例缩放图像
    image.thumbnail((desired_size, desired_size), Image.LANCZOS)

    # 透明填充
    new_img = Image.new("RGBA", (desired_size, desired_size), (0, 0, 0, 0))
    new_img.paste(image, ((desired_size - image.width) // 2, (desired_size - image.height) // 2), image)
    return new_img




