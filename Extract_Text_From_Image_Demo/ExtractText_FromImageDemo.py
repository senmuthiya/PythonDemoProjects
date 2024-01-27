from PIL import Image
import pytesseract

# Set the path to the Tesseract executable (change this path based on your installation)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    try:
        # Open the image file
        image = Image.open(image_path)

        # Use pytesseract to do OCR on the image
        text = pytesseract.image_to_string(image)

        return text

    except Exception as e:
        print(f"Error during text extraction: {e}")
        return None

# Replace 'Test_image.png' with the path to your .png file
image_path = 'Test_image.png'

# Call the function and handle the result
extracted_text = extract_text_from_image(image_path)

if extracted_text is not None:
    print("Extracted Text:")
    print(extracted_text)
else:
    print("Text extraction failed.")

