from PIL import Image
import pytesseract
import warnings
import PyPDF2

def get_text_from_image(file_name):
    # Include tesseract executable in your path
    pytesseract.pytesseract.tesseract_cmd = r"tesseract\tesseract.exe"
     
    # Create an image object of PIL library
    image = Image.open('pic.jpg')
     
    # pass image into pytesseract module
    # pytesseract is trained in many languages
    image_to_text = pytesseract.image_to_string(image, lang='rus')
    return image_to_text

def get_text_from_pdf(file_name):
    pdf = PyPDF2.PdfReader(open(file_name, "rb"))
    text_content = ""
    for page in pdf.pages:
        text_content += page.extract_text()
    if text_content == "": warnings.warn('Your pdf is not readable. Convert it to image and try again')
    return text_content

def get_text(file_name):
    if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
        text_content = get_text_from_image(file_name)
    elif file_name.lower().endswith(('.pdf')):
        #print("pdf")
        text_content = get_text_from_pdf(file_name)
    else:
        warnings.warn('file is neither an image nor a pdf')
    return text_content
        
 
