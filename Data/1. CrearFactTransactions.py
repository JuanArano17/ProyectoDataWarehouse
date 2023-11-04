import random
import xml.etree.ElementTree as ET
from datetime import date, timedelta
from xml.dom.minidom import parseString

def random_date_in_2022():
    start_date = date(2022, 1, 1)
    end_date = date(2022, 12, 31)
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

def transaction_amount_range(customer_fk):
    if 1 <= customer_fk <= 500:
        return "{:.2f}".format(random.uniform(1000, 300000)).replace(".", ",")
    elif 501 <= customer_fk <= 800:
        return "{:.2f}".format(random.uniform(150000, 1500000)).replace(".", ",")
    elif 800 <= customer_fk <= 1000:
        return "{:.2f}".format(random.uniform(300000, 10000000)).replace(".", ",")

def generate_xml_records(num_records):
    root = ET.Element("records")
    
    for pk in range(1, num_records + 1):
        record = ET.SubElement(root, "record")
        
        ET.SubElement(record, "Transaction_PK").text = str(pk)
        ET.SubElement(record, "Transaction_ID").text = str(random.randint(1, num_records))
        customer_fk = random.randint(1, 1000)
        ET.SubElement(record, "Customer_FK").text = str(customer_fk)
        ET.SubElement(record, "Account_FK").text = str(random.randint(1, 1000))
        ET.SubElement(record, "Transaction_Type_FK").text = str(random.randint(1, 5))
        ET.SubElement(record, "Transaction_Amount").text = str(transaction_amount_range(customer_fk))
        ET.SubElement(record, "Transaction_Date").text = random_date_in_2022().strftime('%Y-%m-%d')
        ET.SubElement(record, "Branch_FK").text = str(random.randint(1, 10))
    
    rough_string = ET.tostring(root, encoding="UTF-8", method="xml")
    reparsed = parseString(rough_string)
    return reparsed.toprettyxml(indent="\t")

num_records = int(input("Ingrese la cantidad de registros a generar: "))
xml_data = generate_xml_records(num_records)

# Si desea guardar el XML en un archivo:
with open("FactTransactions.xml", "w") as f:
    f.write(xml_data)