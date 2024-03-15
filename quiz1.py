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

def normalize_image(image, min_val, max_val):

  if min_val == max_val:
    return image / 255.0 
  else:
    return (image - min_val) / (max_val - min_val)


image = cv2.imread("avatar.png")

if image is None:
  print("Error: Could not read image 'avatar.png'")
  exit(1)

# Convert ke grayscale
gray_image = grayscale(image)

# dimensions gambar
width, height = get_dimensions(image)

# nilai minimum and maximum pixel
min_pixel, max_pixel = find_min_max_pixel_values(gray_image)

# Normalisasi
normalized_image = normalize_image(gray_image.copy(), min_pixel, max_pixel)

print("Grayscale image dimensions: width =", width, ", height =", height)
print("Minimum pixel value:", min_pixel)
print("Maximum pixel value:", max_pixel)


cv2.imshow("Grayscale Image", gray_image)
cv2.imshow("Normalized Image", normalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
