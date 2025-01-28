from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
import re

# Path to your image file
image_path = "path_of_image"

try:
    # Load and preprocess the image
    image = Image.open(image_path)
    image = image.convert("L")  # Convert to grayscale
    image = image.filter(ImageFilter.SHARPEN)  # Sharpen the image

    # Extract text using pytesseract
    extracted_text = pytesseract.image_to_string(image, config='--psm 7').strip()
    print(f"Extracted Text: {extracted_text}")

    # Sanitize the extracted text
    sanitized_text = re.sub(r"[^0-9+\-*/.() ]", "", extracted_text)
    print(f"Sanitized Text: {sanitized_text}")

    # Evaluate the sanitized expression
    if sanitized_text:
        result = eval(sanitized_text)
        print(f"Result: {result}")
    else:
        print("No valid arithmetic expression found.")

except FileNotFoundError:
    print("Error: Image file not found.")
except Exception as e:
    print(f"Error: {e}")


