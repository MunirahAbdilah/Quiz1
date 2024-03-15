import cv2

def grayscale(image):
  yuv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)

  gray = yuv[:, :, 0]

  return gray

def get_dimensions(image):

image = cv2.imread("avatar.png")

if image is None:
    print("Error: Could not read image 'avatar.png'")
    exit(1)

gray_image = grayscale(image)

width, height = get_dimensions(image)

print("Grayscale image dimensions: width =", width, ", height =", height)

cv2.imshow("Grayscale Image", gray_image)
cv2.waitKey(0) 
cv2.destroyAllWindows()
