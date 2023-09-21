import os
from pdf2image import convert_from_path
import pytesseract

def extract_txt_from_img_get_cpf(img):
    text = ''
    try:
        raw_text = pytesseract.image_to_string(img)
        parts = raw_text.split("\n")
        text = parts[0] # CPF
    except Exception as e:
        print(f"Error trying to get text from img {img}: {e}")
    return text

def save_txt(file, path_to_save):
    with open(path_to_save, "w") as file:
        for chave, valor in dict_name_cpf.items():
            file.write(f"{chave}: {valor}\n")

def img_to_pdf(pdf_path):
    try:
        pictures = convert_from_path(pdf_path)
        picture_croped = pictures[0].crop((108,320,310,400))
    except Exception as e:
        print(f"Error trying convert PDF to IMG. PDF path: {pdf_path}: {e}")
    return picture_croped


def main(dir):
    result = {}
    for root, _, files in os.walk(dir):
        for filename in files:
            if filename.endswith(".pdf"):
                pdf_path = os.path.join(root, filename)
                img = img_to_pdf(pdf_path)
                cpf = extract_txt_from_img_get_cpf(img)
                key = filename.replace(".pdf","")
                result[key] = cpf
    return result

if __name__ == "__main__":
    pdfs_path = "./data"
    path_to_save = "./result/name-cpf.txt"
    dict_name_cpf = main(pdfs_path)
    save_txt(dict_name_cpf, path_to_save)

