import sys
import json
import pdfplumber
import re


def extract_texts(pdf_path):

    text = ""
    with pdfplumber.open(pdf_path) as pdf:
      for page in pdf.pages:
        text += page.extract_text()
    return text

def regex_search(text, pattern):
    result = re.findall(pattern, text)
    return result

if __name__ == "__main__":
    pdf_path = sys.argv[1]

    data = extract_texts(pdf_path)

    bodyWorkPattern = re.compile(r"funilaria \d{1,3}.\d{2} \d{1,3}.\d{2} \d{1,3}.\d{2} \d{1,3}.\d{2} \d{1,3}.\d{2} \d{1,3}.\d{2} \d{1,3}.\d{2} \d{1,3}.\d{2}",
                         re.IGNORECASE)
    mechanicalRepairPattern = re.compile(r"mecânica \d{1,3}.\d{2} \d{1,3}.\d{2} \d{1,3}.\d{2} \d{1,3}.\d{2} \d{1,3}.\d{2} \d{1,3}.\d{2} \d{1,3}.\d{2} \d{1,3}.\d{2}",
                         re.IGNORECASE)
    autoUpholsteryPattern = re.compile(r"tapeçaria \d{1,3}.\d{2} \d{1,3}.\d{2} \d{1,3}.\d{2} \d{1,3}.\d{2} \d{1,3}.\d{2} \d{1,3}.\d{2} \d{1,3}.\d{2} \d{1,3}.\d{2}",
                         re.IGNORECASE)
    detailingPattern = re.compile(r"acabamen \d{1,3}.\d{2} \d{1,3}.\d{2} \d{1,3}.\d{2} \d{1,3}.\d{2} \d{1,3}.\d{2} \d{1,3}.\d{2} \d{1,3}.\d{2} \d{1,3}.\d{2}",
                         re.IGNORECASE)
    autoElectricalRepairPattern = re.compile(r"elétrica \d{1,3}.\d{2} \d{1,3}.\d{2} \d{1,3}.\d{2} \d{1,3}.\d{2} \d{1,3}.\d{2} \d{1,3}.\d{2} \d{1,3}.\d{2} \d{1,3}.\d{2}",
                         re.IGNORECASE)
    
    patterns = [
       bodyWorkPattern,
       mechanicalRepairPattern,
       autoUpholsteryPattern,
       detailingPattern,
       autoElectricalRepairPattern
    ]

    # result = regex_search(data, bodyWorkPattern)
    # print(json.dumps(result, ensure_ascii=False))

    for pattern in patterns:
      result = regex_search(data, pattern)
      print(json.dumps(result, ensure_ascii=False))

