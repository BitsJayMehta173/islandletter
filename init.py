
from PIL import Image

# Open an image file
image = Image.open('a.png')

# Convert image to grayscale
gray_image = image.convert('L')

# Apply a threshold to get a binary image (black and white)
threshold = 128
bw_image = gray_image.point(lambda x: 0 if x < threshold else 255, '1')

# Save the black-and-white image
bw_image.save('output.png')

# Optionally, traverse each pixel (same as before)
pixels = bw_image.load()
width, height = bw_image.size

for y in range(height):
    for x in range(width):
        pixel = pixels[x, y]
        print(f"Pixel at ({x}, {y}): {'Black' if pixel == 0 else 'White'}")
