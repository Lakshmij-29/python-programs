from PIL import Image
from pathlib import Path

source = Path("original_images")
destination = Path("resized_images")
destination.mkdir(exist_ok=True)
for file in source.glob("*"):
    try:
        with Image.open(file) as image:
            image.thumbnail((800, 800))
            image.convert("RGB").save(destination / f"{file.stem}.jpg")
            print("Processed:", file.name)
    except Exception as error:
        print("Skipped:", file.name, error)
