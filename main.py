#Imports the Libraries
import cv2
import numpy as np

# Save the inputted image
img = cv2.imread('can.png', cv2.IMREAD_COLOR)

# Convert input image to grayscale.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur image (uses a 3 * 3 kernel)
gray_blurred = cv2.blur(gray, (3, 3))

# Detect the circles using Hough Circles.
detected_circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, param2 = 30, minRadius = 1, maxRadius = 10000)

# Check if circles are detected to avoid errors.
if detected_circles is not None:
	# Convert the parameters of the circle: center point and radius, into integers.
	detected_circles = np.uint16(np.around(detected_circles))

	# Display the circles and their center points
	for pt in detected_circles[0, :]:
		# Collect and save the parameters for each circle.
		a, b, r = pt[0], pt[1], pt[2]

		# Outline the circle.
		cv2.circle(img, (a, b), r, (214, 69, 197), 4) # Color is a light purple and the width of the outline is 4

		# Draw a small that fills itself in for the center point.
		cv2.circle(img, (a, b), 4, (255, 0, 0), 6) #Center point is blue and is very thick with a small radius to make sure it's filled in.
		#Display the can with the overlay
		cv2.imshow("Detected Circle", img)
		cv2.waitKey(0)
