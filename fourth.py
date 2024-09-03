# After converting image to red and black here you can make it black and white

from PIL import Image

# Load the image
image = Image.open('new.png')  # Replace with your image file

# Convert the image to RGB mode to allow color manipulation
rgb_image = image.convert('RGB')

# Get the image dimensions
width, height = rgb_image.size

# Create a new image to store the result
result_image = Image.new('RGB', (width, height))

def is_red(pixel):
    r, g, b = pixel
    return r > 100 and g < 50 and b < 50  # Threshold for red color

def is_black(pixel):
    r, g, b = pixel
    return r == 0 and g == 0 and b == 0  # Black color

# Process each pixel
for y in range(height):
    for x in range(width):
        pixel = rgb_image.getpixel((x, y))

        if is_red(pixel):
            result_image.putpixel((x, y), (0, 0, 0))  # Convert red to white
        elif is_black(pixel):
            result_image.putpixel((x, y), (255, 255, 255))  # Keep black as black
        else:
            result_image.putpixel((x, y), pixel)  # Keep other colors unchanged

# Save the modified image
result_image.save('output_image.png')
# result_image.show()  # Optionally display the image
