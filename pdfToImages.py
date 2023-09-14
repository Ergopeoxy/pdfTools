import fitz  # PyMuPDF

pdf_file = "test.pdf"

def extract_images_from_pdf(pdf_file):
    pdf_document = fitz.open(pdf_file)
    images = []
    for page_number in range(pdf_document.page_count):
        print ("Page number",page_number)
        page = pdf_document.load_page(page_number)
        xrefs = page.get_images(full=True)
        print(xrefs)
        for xref in xrefs:
            base_image = pdf_document.extract_image(xref[0])
            image_data = base_image["image"]
            images.append(image_data)
    return images

images = extract_images_from_pdf(pdf_file)
print(len(images))
print(images)
from PIL import Image
import pytesseract

def ocr_images(images):
    extracted_text = ""
    for image_data in images:
        image = Image.frombytes("RGB", image_data.size, image_data.samples)
        text = pytesseract.image_to_string(image)
        extracted_text += text + "\n"
    return extracted_text

extracted_text = ocr_images(images)

print(extracted_text)


import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'
filename = 'test.png'
img1 = np.array(Image.open(filename))
text = pytesseract.image_to_string(img1)

print(text)




doc = fitz.open("test.pdf") # open a document
for page in doc: # iterate the document pages
  text = page.get_text() # get plain text encoded as UTF-8
  print(text)