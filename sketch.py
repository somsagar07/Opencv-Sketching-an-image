import cv2
import sys
image = cv2.imread(r"image/fl.jpeg")
if image is None:
    print("can not find image")
    sys.exit()
# gray scale
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#invert gray image
grayImageInv = 255 - grayImage
# gaussian blur
grayImageInv = cv2.GaussianBlur(grayImageInv, (21, 21), 0)
#blend using color dodge
output = cv2.divide(grayImage, 255-grayImageInv, scale=256.0)
#edge 
gray = cv2.medianBlur(grayImage, 1)
edges = cv2.adaptiveThreshold(gray, 10, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
color = cv2.bilateralFilter(output, 5, 75, 75)
#output
final_output = cv2.bitwise_and(color, color, mask=edges)
cv2.namedWindow("pencilsketch", cv2.WINDOW_AUTOSIZE)
cv2.imshow("pencilsketch", final_output)
#press esc to exit the program
cv2.waitKey(0)
cv2.destroyAllWindows()