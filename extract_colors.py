from PIL import Image


def extract_dominant_colors(image_path, num_colors=20):
    """
    Extract the dominant colors from an image using the PIL (Pillow) library.

    Parameters:
    - image_path (str): Path to the image file.
    - num_colors (int): Number of dominant colors to extract. Default is 20.

    Returns:
    - list[tuple]: A list of RGB tuples representing the dominant colors.
    """
    # Open the image
    img = Image.open(image_path)

    # Resize for faster processing (keeping aspect ratio)
    img = img.resize((100, int((img.height / img.width) * 100)))

    # Convert the image to RGB
    img = img.convert('RGB')

    # Get color data
    pixel_data = list(img.getdata())

    # Use frequency analysis to get most common colors
    color_freq = {}
    for color in pixel_data:
        if color in color_freq:
            color_freq[color] += 1
        else:
            color_freq[color] = 1

    sorted_colors = sorted(color_freq.items(), key=lambda x: x[1], reverse=True)

    # Return top 'num_colors' colors
    return [color[0] for color in sorted_colors[:num_colors]]


# Test the function with the provided image
dominant_colors = extract_dominant_colors('image.jpeg')
