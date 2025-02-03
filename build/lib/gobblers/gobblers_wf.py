from PyPDF2 import PdfReader
import re

def capture_pattern(text_obj,pattern):
    if text_obj:
        matches = pattern.findall(text_obj)  # Find all matching lines
        if matches:
            return matches

def gobwf():
    print("Gobbling")
    print("Ingesting WF Files")
    master=[]
    reader = PdfReader(r"C:\projects\python\billAnalyzer\data\WFDec2024.pdf")
    page_num=3
    page = reader.pages[page_num-1]
    text=page.extract_text()
    lines = text.split("\n")
    if text:
        print(lines[16])
        # for j, line in enumerate(lines):
        #     print(line)
    # pattern = re.compile(r"Withdrawals/Subtractions.*", re.IGNORECASE)
    # master+=capture_pattern(text,pattern)
    # pattern = re.compile(r"Deposits/Addition.*", re.IGNORECASE)
    # master+=capture_pattern(text,pattern)
    # pattern = re.compile(r"Americanexpress.*Transfer.*", re.IGNORECASE)
    # master+=capture_pattern(text,pattern)
    # print(master)
    #print(text)
    # if pattern.search(text):
    #     print(f"{pattern.search(text).group()}")
        


