import cv2
import numpy as np
import os
from PIL import Image
from load import SAVE_DIR, CHANNEL, CHANNEL_NAME

OUTPUT_DIR = "../output"
OUTPUT_FILENAME = f"{OUTPUT_DIR}/{CHANNEL}_average_thumbnail.jpg"
TARGET_SIZE = (480, 270)

def blendThumbs(folder_path, target_size):
    all_images = []
    
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
                file_path = os.path.join(root, file)
                
                try:
                    img_pil = Image.open(file_path).convert('RGB')
                    img_cv = np.array(img_pil) 
                    img_cv = img_cv[:, :, ::-1].copy()
                    
                    resized_img = cv2.resize(img_cv, target_size, interpolation=cv2.INTER_AREA)
                    all_images.append(resized_img)
                    
                except Exception as e:
                    print(f"Skipping file {file}. Error: {e}")
                    continue

    if not all_images:
        print(f"Error: No valid image files found in '{folder_path}'.")
        return

    print(f"Successfully loaded and resized {len(all_images)} thumbnails.")

    sum_image = np.zeros(all_images[0].shape, dtype=np.float64)
    
    for img in all_images:
        sum_image += img

    average_image = (sum_image / len(all_images)).astype(np.uint8)

    cv2.imwrite(OUTPUT_FILENAME, average_image)
    print(f"Average image saved as '{OUTPUT_FILENAME}'")

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

blendThumbs(f"{SAVE_DIR}/{CHANNEL_NAME}", TARGET_SIZE)