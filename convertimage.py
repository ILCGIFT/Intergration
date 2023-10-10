from PIL import Image

# Open the image
image = Image.open("sample.jpg") # Change the filename to your image filename

# Get image size (number of rows and number of columns)
width, height = image.size

# Convert image into pixel matrix
pixel_matrix = []
for y in range(height):
    row = []
    for x in range(width):
        pixel = image.getpixel((x, y))
        # pixels is a tuple (R, G, B) in the case of RGB images
        # For simplicity, the average value of R, G and B can be taken
        grayscale_pixel = sum(pixel) // 3
        row.append(grayscale_pixel) # Add pixel values ​​to the row
    pixel_matrix.append(row) # Add rows to the matrix

df = pd.DataFrame(pixel_matrix)
