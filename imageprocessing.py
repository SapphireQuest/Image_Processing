from PIL import Image
import numpy as np

BLACK = [0,0,0] 
WHITE =[255,255,255]
GRAY = [128,128,128]

def single_treshold(pixel_array, width, height, treshold1, treshold2):
    for w in range(width):
        for h in range(height):
            pixel = pixel_array[h][w] 
            r = int(pixel[0])
            g = int(pixel[1])
            b = int(pixel[2])
            avg = (r + g + b)/3
            if treshold2 == -1:
                if(avg >= treshold1):
                    pixel_array[h][w] = WHITE
                else:
                    pixel_array[h][w] = BLACK
            else:
                if avg >= treshold2:
                    pixel_array[h][w] = WHITE
                elif avg < treshold2 and avg > treshold1:
                    pixel_array[h][w] = GRAY
                else:
                    pixel_array[h][w] = BLACK
    return pixel_array




def main():
    img = Image.open('yoda.jpeg').convert('RGB')
    width, height = img.size
    pixel_array = np.array(img)
    pixel_array_copy = pixel_array.copy()
    single_treshold_array = single_treshold(pixel_array_copy, width, height, 128, 192)
    single_treshold_image = Image.fromarray(single_treshold_array.astype(np.uint8), 'RGB')
    single_treshold_image.show()
if __name__ == "__main__":
    main()