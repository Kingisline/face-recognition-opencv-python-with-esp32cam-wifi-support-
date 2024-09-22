import cv2
import urllib.request
import numpy as np
from PIL import Image
from io import BytesIO

# Example ESP32-CAM URL (replace with your actual ESP32 IP address)
esp32_url = 'http://192.168.31.138/cam-hi.jpg'  # Replace with actual IP

try:
    # Fetch the image from ESP32-CAM
    print(f"Fetching image from {esp32_url}...")
    response = urllib.request.urlopen(esp32_url)
    img_data = response.read()

    # Convert the byte data to a PIL Image
    img = Image.open(BytesIO(img_data))
    print("Image fetched successfully!")

    # Convert the PIL Image to a NumPy array for OpenCV
    img_np = np.array(img)

    # Convert the image from RGB to BGR (OpenCV format)
    img_cv2 = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

    # Resize the image to 480x640
    resized_img = cv2.resize(img_cv2, (640, 480))

    # Convert the resized image to grayscale
    grayscale_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)

    # Display the processed image using OpenCV
    cv2.imshow("Processed Image", grayscale_img)

    # Wait for a key press and close the display window
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except Exception as e:
    print(f"Error: {e}")
