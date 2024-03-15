import cv2

def grayscale(image):

  yuv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
  gray = yuv[:, :, 0]
  return gray

def get_dimensions(image):

  return image.shape[:2] 

def find_min_max_pixel_values(image):

  min_val, max_val, _, _ = cv2.minMaxLoc(image)
  return min_val, max_val


image = cv2.imread("avatar.png")

if image is None:
  print("Error: Could not read image 'avatar.png'")
  exit(1)


gray_image = grayscale(image)


width, height = get_dimensions(image)


min_pixel, max_pixel = find_min_max_pixel_values(gray_image)


print("Grayscale image dimensions: width =", width, ", height =", height)
print("Minimum pixel value:", min_pixel)
print("Maximum pixel value:", max_pixel)


cv2.imshow("Grayscale Image", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
