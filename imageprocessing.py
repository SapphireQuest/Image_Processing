from PIL import Image
import numpy as np
import time

BLACK = [0,0,0] 
WHITE =[255,255,255]
GRAY = [128,128,128]

def treshold(pixel_array, width, height, treshold1, treshold2):
    for w in range(width):
        for h in range(height):
            pixel = pixel_array[h][w] 
            r = int(pixel[0])
            g = int(pixel[1])
            b = int(pixel[2])
            avg = (r + g + b)//3
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


def histogram_equalization(pixel_array,width, height):
    histogram = [0] * 256
    for w in range(width):
        for h in range(height):
            pixel = pixel_array[h][w] 
            histogram[pixel] += 1

    CDF = [0] * 256
    CDF[0] = histogram[0]
    for i in range(1, 256):
        CDF[i] = CDF[i-1] + histogram[i]
    for i in range (0, 256):
        if CDF[i] != 0:
            CDF_min = CDF[i]
            break
    new_shades = [0] * 256
    for i in range (0, 256):
        new_value = ((CDF[i] - CDF_min) / (CDF[255] - CDF_min)) * 255
        new_shades[i] = int(round(new_value))
    for w in range(width):
        for h in range(height):
            pixel = pixel_array[h][w]
            new_color = new_shades[pixel]
            pixel_array[h][w] = new_color
    return pixel_array

def basic_mask(pixel_array,width,height, mask_size=71):
    blurred_array = pixel_array.copy()
    offset = mask_size//2
    total_pixel_in_mask = mask_size*mask_size

    for w in range(offset, width - offset):
        for h in range(offset,height - offset):
            box_sum = 0
            for box_h in range(h - offset, h + offset + 1):
                for box_w in range(w - offset, w + offset + 1):
                    box_sum += int(pixel_array[box_h][box_w])
            blurred_array[h][w] = box_sum//total_pixel_in_mask

    return blurred_array


def summed_area_table(pixel_array, widht, height, mask_size=71):
    pass
     

def main():
    img = Image.open('yoda.jpeg').convert('RGB')
    width, height = img.size
    pixel_array = np.array(img)

    # ------ TASK 2 -------
    #pixel_array_treshold = pixel_array.copy()
    #treshold_array = treshold(pixel_array_treshold, width, height, 128, -1)
    #treshold_image = Image.fromarray(treshold_array.astype(np.uint8), 'RGB')
    #treshold_image.show()

    # -------- TASK 3 ---------
    #grayscale_image = Image.open('yoda.jpeg').convert('L')
    #equalized_pixel_array = np.array(grayscale_image)
    #equalized_array = histogram_equalization(equalized_pixel_array,width, height)
    #grayscale_image.show()
    #equalized_image = Image.fromarray(equalized_array.astype(np.uint8), 'L')
    #equalized_image.show()

   # ----- TASK 4 -----
    grayscale_image_road = Image.open('road.jpg').convert('L')
    mask_pixel_array = np.array(grayscale_image_road)
    width_road, height_road = grayscale_image_road.size 
    
    start_time = time.time()
    blurred_array = basic_mask(mask_pixel_array,width_road, height_road)
    stop_time = time.time()
    exec_time = stop_time - start_time
    print("Basic mask time: ")
    print(exec_time)
    blured_image = Image.fromarray(blurred_array.astype(np.uint8), 'L')
    blured_image.show()
    
    summed_area_table(mask_pixel_array,width_road, height_road)


if __name__ == "__main__":
    main()