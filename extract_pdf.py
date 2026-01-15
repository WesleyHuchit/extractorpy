import sys
import json
import pdfplumber
import re
from io import BytesIO


def extract_texts():
    pdf_bytes = sys.stdin.buffer.read()

    text = ""
    # with pdfplumber.open(pdf_bytes) as pdf:
    with pdfplumber.open(BytesIO(pdf_bytes)) as pdf:
      for page in pdf.pages:
        text += page.extract_text()
    return text

def regex_search(text, pattern):
    result = re.findall(pattern, text)
    return result

if __name__ == "__main__":
    # pdf_path = sys.argv[1]

    data = extract_texts()

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

    # patterns = [
    #    ('bodyWork', bodyWorkPattern),
    #    ('mechanicalRepair', mechanicalRepairPattern),
    #    ('autoUpholstery', autoUpholsteryPattern),
    #    ('detailing', detailingPattern),
    #    ('autoElectricalRepair', autoElectricalRepairPattern)
    # ]


    # result = regex_search(data, bodyWorkPattern)
    # print(json.dumps(result, ensure_ascii=False))

    allResults = []

    for pattern in patterns:
      result = regex_search(data, pattern)
      allResults.append(result)

    print(json.dumps(allResults, ensure_ascii=False))
