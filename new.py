from PIL import Image

# Load the image
image = Image.open('output.png')

# Convert the image to RGB mode to allow color changes
rgb_image = image.convert('RGB')

# Get the image dimensions
width, height = rgb_image.size

def island(x, y, rgb_image):
    stack = [(x, y)]
    
    while stack:
        cx, cy = stack.pop()
        
        # Check if the coordinates are within bounds and if the pixel is white
        if cx < 0 or cy < 0 or cx >= width or cy >= height or rgb_image.getpixel((cx, cy)) != (255, 255, 255):
            continue
        
        # Mark the current pixel as visited by setting it to red
        rgb_image.putpixel((cx, cy), (255, 0, 0))
        
        # Add neighboring pixels to the stack
        stack.append((cx + 1, cy))  # Right
        stack.append((cx - 1, cy))  # Left
        stack.append((cx, cy + 1))  # Down
        stack.append((cx, cy - 1))  # Up
        stack.append((cx + 1, cy + 1))  # Down-right
        stack.append((cx + 1, cy - 1))  # Up-right
        stack.append((cx - 1, cy + 1))  # Down-left
        stack.append((cx - 1, cy - 1))  # Up-left

# Traverse each pixel
for y in range(height):
    for x in range(width):
        pixel = rgb_image.getpixel((x, y))
        if pixel == (255, 255, 255):  # Check if the pixel is white
            island(x, y, rgb_image)  # Change connected white pixels to red

# Save or display the modified image
rgb_image.save('new1.png')
