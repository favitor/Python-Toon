import cv2
import sys
import numpy as np
import argparse

FLAGS = None
IMG = 'image'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image',
                type=str,
                help='Path to the image.')

#Could read the image without the argparse, using the command below
#img = cv2.imread("yourimage.jpg")
img = cv2.imread(FLAGS.image)


#Get the image height and width
height = img.shape[0]
width = img.shape[1]

#Divide the image into 2 faces
width_cutoff = width // 2
face1 = img[:, :width_cutoff]
face2 = img[:, width_cutoff:]


#Select a effect
effect_type = int(input('''[1] Sketch
[2] Stylize
Choose a effect: '''))

if effect_type == 1:
    #Can limit the amount of shade in the output by varying the shade_factor in the function cv2.pencilSketch.
    editedface = cv2.pencilSketch(face2, sigma_s=60, sigma_r=0.07, shade_factor=0.06)

elif effect_type == 2:
    editedface = cv2.stylization(face2, sigma_s=60, sigma_r=0.07)

else:
    print("Error, please try again.")  


#Putting all together
vis = np.concatenate((face1, editedface), axis=1)
cv2.imshow("Final Image", vis)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Saving
save_img = input(str("Do you want save the image? [Y/N]: "))
if save_img == 'y' or 'Y':
    name = input(str("Enter a image name(without the extencion): "))
    cv2.imwrite(name+".jpg", vis)
    print("Image saved.")

else:
    print("End...")
