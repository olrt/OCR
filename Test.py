import pdf2image, os, re
from datetime import datetime

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

textFilename = "temp.txt"
pdfFilename = "Result_TestPg1.pdf"
word = "Potassium"
#word = "Sodium"

# Convert PDF to image
def pdf_to_img(pdf_file):
    return pdf2image.convert_from_path(pdf_file)

# Extract text from converted image and write to text file
def ocr_core(file):
    text = pytesseract.image_to_string(file)
    return text
    
def extractStrToTextFile(text,textFilename):
    if os.path.exists(textFilename):
        os.remove(textFilename)
    f = open(textFilename, "a")
    f.write(text)
    f.close()
    return True

def extractPatientDetails(textFilename):
    with open(textFilename, "r") as f:
        lines = f.readlines()
        for row in lines:
            if row.find("ex: ") != -1:
                wordIndex = row.find("ex: ")
                strLine = row[wordIndex+4:]
                arrayTemp = strLine.split("/")
                arrayData = []
                dateFormat = "%d-%b-%Y"
                for data in arrayTemp:
                    data = data.strip()
                    print (data)
                    try:
                        dt = datetime.strptime(data, dateFormat)
                        bool(dt)
                        dt = dt.date()
                        arrayData.append(dt)
                    except ValueError:
                        if not arrayData:
                            arrayData.append(None)
                        elif " years" in data:
                            data = data.replace(" years","")
                            arrayData.append(int(data))
                        elif len(arrayData) == 1:
                            arrayData.append(None)
                        elif "Male" in data:
                            arrayData.append("Male")
                        elif "Female" in data:
                            arrayData.append("Female")
    return arrayData

def extractResults(textFilename, word):
    with open(textFilename, "r") as f:
        lines = f.readlines()
        for row in lines:
            if row.find(word) != -1:
                wordIndex = row.find(word)
                strLine = row[wordIndex:]
                extractResult = re.search(r'[0-9.]+', strLine)
                #print(extractResult)
                strResult = extractResult.group(0)
                if strResult.isdigit():
                    result = int(strResult)
                else:
                    result = float(''.join(strResult))
    return result

#def print_pages(pdf_file):
#    images = pdf_to_img(pdf_file)
#    for pg, img in enumerate(images): 
#        print(ocr_core(img))

#print_pages('Result_TestPg1.pdf')

images=pdf_to_img(pdfFilename)
for pg, img in enumerate(images): 
    text=ocr_core(img)
extractStrToTextFile(text,textFilename)
print (extractResults(textFilename, word))
print ("***********************************")
print (text)
print ("***********************************")
print (extractPatientDetails(textFilename))