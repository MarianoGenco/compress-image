from PIL import Image
import os

downloadsFolder = "C:/Users/..."  #Insert Path Folder

if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + filename)

        try:
            if extension in [".JPG", ".JPEG", ".PNG", ".jpg", ".jpeg", ".png"]:
                picture = Image.open(downloadsFolder + filename)
                picture.save(downloadsFolder + "comp_" + filename, optimize=True, quality=60)
                picture = Image.open(downloadsFolder + filename)
                picture.close()
                os.remove(downloadsFolder + filename)
                print(name + extension)
        except:
            continue            

