import pytesseract
import re
import cv2

# Configure Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

EXPIRY_PATTERNS = [
    # Expiry Date patterns
    r"(?:exp(?:iry)?\.?\s*date\s*[:\-]?\s*.*?(\d{2}[\/\-]\d{2}[\/\-][0O]\d{2}))",  # Expiry Date: 20/07/2O24
    r"(?:exp(?:iry)?\.?\s*date\s*[:\-]?\s*.*?(\d{2}[\/\-]\d{2}[\/\-]\d{4}))",      # Expiry Date: 20/07/2024
    r"(?:exp(?:iry)?\.?\s*date\s*[:\-]?\s*.?(\d{2}\s[A-Za-z]{3,}\s[0O]\d{2}))",  # Expiry Date: 20 MAY 2O24
    r"(?:exp(?:iry)?\.?\s*date\s*[:\-]?\s*.?(\d{2}\s[A-Za-z]{3,}\s\d{4}))",      # Expiry Date: 20 MAY 2024
    r"(?:exp(?:iry)?\.?\s*date\s*[:\-]?\s*.*?(\d{4}[\/\-]\d{2}[\/\-]\d{2}))",      # Expiry Date: 2024/07/20

    # Best Before patterns
    r"(?:best\s*before\s*[:\-]?\s*.*?(\d{2}[\/\-]\d{2}[\/\-][0O]\d{2}))",          # Best Before: 20/07/2O24
    r"(?:best\s*before\s*[:\-]?\s*.*?(\d{2}[\/\-]\d{2}[\/\-]\d{4}))",              # Best Before: 20/07/2024
    r"(?:best\s*before\s*[:\-]?\s*.?(\d{2}\s[A-Za-z]{3,}\s[0O]\d{2}))",          # Best Before: 20 MAY 2O24
    r"(?:best\s*before\s*[:\-]?\s*.?(\d{2}\s[A-Za-z]{3,}\s\d{4}))",              # Best Before: 20 MAY 2024

    # Consume Before patterns
    r"(?:consume\s*before\s*[:\-]?\s*.*?(\d{1,2}[A-Za-z]{3,}[0O]\d{2}))",          # Consume Before: 3ODEC2O24
    r"(?:consume\s*before\s*[:\-]?\s*.*?(\d{1,2}[A-Za-z]{3,}\d{2}))",              # Consume Before: 30DEC23
    r"(?:consume\s*before\s*[:\-]?\s*.*?(\d{2}[\/\-]\d{2}[\/\-][0O]\d{2}))",       # Consume Before: 20/07/2O24
    r"(?:consume\s*before\s*[:\-]?\s*.*?(\d{2}[\/\-]\d{2}[\/\-]\d{4}))",           # Consume Before: 20/07/2024
    r"(?:consume\s*before\s*[:\-]?\s*.?(\d{2}\s[A-Za-z]{3,}\s\d{4}))",           # Consume Before: 20 MAY 2024

    # Expired formats
    r"(?:exp\s*[:\-]?\s*.*?(\d{2}[\/\-]\d{2}[\/\-][0O]\d{2}))",                    # Exp: 20/07/2O24
    r"(?:exp\s*[:\-]?\s*.*?(\d{2}[\/\-]\d{2}[\/\-]\d{4}))",                        # Exp: 20/07/2024

    # General date formats
    r"\d{2}[\/\-]\d{2}[\/\-]\d{2,4}",                                             # DD/MM/YYYY or DD-MM-YY
    r"\d{1,2}\s[A-Za-z]{3,}\s\d{2,4}",                                            # 20 MAY 2024
    r"\d{4}[\/\-]\d{2}[\/\-]\d{2}",                                               # YYYY/MM/DD
]

def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    return thresh

def extract_expiry_date(image):
    """Extract expiry date using Tesseract and regex."""
    text = pytesseract.image_to_string(image)
    for pattern in EXPIRY_PATTERNS:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(0)
    return "Expiry date not found"


# # Preprocess image
# def preprocess_image(image):
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     _, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
#     return thresh

# # Extract text with Tesseract
# def extract_text_with_tesseract(image):
#     text = pytesseract.image_to_string(image)
#     return text

# # Find expiry date
# def find_expiry_date(text):
#     for pattern in EXPIRY_PATTERNS:
#         match = re.search(pattern, text, re.IGNORECASE)
#         if match:
#             return match.group(0)
#     return "Expiry date not found"

# Use LayoutLMv3 for structured extraction
# def extract_expiry_with_layoutlm(image_path):
#     image = Image.open(image_path).convert("RGB")
#     inputs = processor(image, return_tensors="pt")
#     outputs = model(**inputs)
#     logits = outputs.logits
#     predictions = torch.argmax(logits, dim=-1).squeeze().tolist()
#     tokens = processor.tokenizer.convert_ids_to_tokens(inputs.input_ids.squeeze())
#     extracted_data = {token: prediction for token, prediction in zip(tokens, predictions)}
#     return extracted_data

