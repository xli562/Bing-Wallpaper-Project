from PIL import Image
import piexif

def commentJPG(path:str, comment:str):
    image = Image.open(path)

    # Create a new EXIF dictionary and add the comment
    exif_dict = {"0th": {}}
    exif_dict["0th"][piexif.ImageIFD.ImageDescription] = comment
    exif_bytes = piexif.dump(exif_dict)

    image.save(path, "jpeg", exif=exif_bytes)
