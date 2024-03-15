import cv2

def grayscale(image):
  yuv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)

  gray = yuv[:, :, 0]

  return gray

image = cv2.imread("avatar.png")

gray_image = grayscale(image)

cv2.imshow("Grayscale Image", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()