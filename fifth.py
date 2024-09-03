# made the island array from the red and black
# now we have completed the code and now normalizing is left to be done
from PIL import Image

# Load the image
image = Image.open('new.png')  # Replace with your image file

# Convert the image to RGB mode
rgb_image = image.convert('RGB')

# Get the image dimensions
width, height = rgb_image.size

# Create a result image to visualize changes (optional)
result_image = Image.new('RGB', (width, height), (255, 255, 255))

def is_black(pixel):
    r, g, b = pixel
    return r == 0 and g == 0 and b == 0  # Black color

def flood_fill(x, y, rgb_image, visited, island):
    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()
        if (cx, cy) in visited or not (0 <= cx < width and 0 <= cy < height):
            continue
        pixel = rgb_image.getpixel((cx, cy))
        if not is_black(pixel):
            continue
        visited.add((cx, cy))
        island.append((cx, cy))
        result_image.putpixel((cx, cy), (255, 0, 0))  # Mark the pixel as part of an island

        # Check neighboring pixels
        stack.extend([
            (cx + 1, cy), (cx - 1, cy),
            (cx, cy + 1), (cx, cy - 1),
            (cx + 1, cy + 1), (cx + 1, cy - 1),
            (cx - 1, cy + 1), (cx - 1, cy - 1)
        ])

# List to store islands
island_array = []

# Set to keep track of visited pixels
visited = set()

stop=False
# Traverse each pixel
for y in range(height):
    for x in range(width):
        if (x, y) not in visited and is_black(rgb_image.getpixel((x, y))):
            island = []
            flood_fill(x, y, rgb_image, visited, island)
            island_array.append(island)
            stop=True
            break
    if stop==True:
        break
    
# Save or display the modified image (optional)
result_image.save('new3.png')
result_image.show()  # Optionally display the result image

# Print the island array
for i, island in enumerate(island_array):
    print(f"Island {i + 1}: {island}")
