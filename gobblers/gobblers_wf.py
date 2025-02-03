from PyPDF2 import PdfReader
import re

def capture_pattern(text_obj,pattern):
    if text_obj:
        matches = pattern.search(text_obj) 
        #matches = pattern.findall(text_obj)  # Find all matching lines
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
    investment=savings=income=0
    transactions_savings,transactions_income,transactions_investments=[],[],[]
    transactions_expenses=[]
    if text:
        for j, line in enumerate(lines):
            flag_expense=False
            if j + 1 < len(lines): 
                pattern = re.compile(r"Withdrawals/Subtractions.*", re.IGNORECASE)
                if pattern.search(line):
                    master.append(line)
                pattern = re.compile(r"Deposits/Addition.*", re.IGNORECASE)
                if pattern.search(line):
                    master.append(line)
                #RECORDS
                pattern = re.compile(r"Americanexpress.*Transfer.*", re.IGNORECASE)
                if pattern.search(line):
                    investment+=float(lines[j+1].split()[1])
                    record=line+lines[j+1].split()[1]
                    transactions_investments.append(record)
                    flag_expense=True
                pattern = re.compile(r"Verman.*", re.IGNORECASE)
                if pattern.search(line):
                    savings+=float(lines[j+1].split()[2])
                    record=line+lines[j+1].split()[2]
                    transactions_savings.append(record)
                    flag_expense=True
                pattern = re.compile(r"Payroll.*", re.IGNORECASE)
                if pattern.search(line):
                    income+=float(line.split()[-1].replace(",",""))
                    record=line
                    transactions_income.append(record)
                    flag_expense=True
                if not flag_expense:
                    transactions_expenses.append(line)
                    #print("Line is an expense")
            

                
            
        master.append(f"Investment-Amex HYA:{investment}")
        master.append(f"Savings-WellsFargo WF:{savings}")
        master.append(f"Income:{income:0.2f}")
            
            
            
    
    
    print(*master,sep="\n")
    print("DETAILED TRANSACTIONS")
    print("INCOME")
    print(*transactions_income,sep="\n")
    print("INVESTMENTS")
    print(*transactions_investments,sep="\n")
    print("SAVINGS")
    print(*transactions_savings,sep="\n")
    print("EXPENSES")

    for j, line in enumerate(transactions_expenses):
        pattern = re.compile(r"^\d{1,2}/\d{1,2}.*", re.IGNORECASE)
        if pattern.search(line):
            if j + 1 < len(transactions_expenses):
                print(line)
                # print(transactions_expenses[j+1])
            else:
                print(line) 
                
    # print(*transactions_expenses,sep="\n")
    # if pattern.search(text):
    #     print(f"{pattern.search(text).group()}")
        


