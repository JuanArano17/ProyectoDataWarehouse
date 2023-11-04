import random
import xml.etree.ElementTree as ET
from xml.dom import minidom

def prettify(elem):
    """Return a pretty-printed XML string for the Element."""
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="    ")

def generate_start_end_dates():
    start_month = random.randint(1, 12)
    start_day = random.randint(1, 28)
    end_month = random.choice([m for m in range(start_month, 13)])
    if end_month == start_month:
        end_day = random.choice([d for d in range(start_day, 29)])
    else:
        end_day = random.randint(1, 28)
    return f"2022-{start_month}-{start_day}", f"2022-{end_month}-{end_day}"

def generate_credit_limit(customer_fk):
    if 1 <= customer_fk <= 500:
        return random.randint(10000, 1000000)
    elif 500 < customer_fk <= 800:
        return random.randint(500000, 10000000)
    else:
        return random.randint(1000000, 50000000)

def generate_record(record_count):
    records = ET.Element("records")
    for i in range(1, record_count + 1):
        record = ET.SubElement(records, "record")
        ET.SubElement(record, "Product_PK").text = str(i)
        ET.SubElement(record, "Product_ID").text = str(random.randint(1, record_count))
        customer_fk = random.randint(1, 1000)
        ET.SubElement(record, "Customer_FK").text = str(customer_fk)
        product_type_fk = random.randint(1, 9)
        ET.SubElement(record, "Product_Type_FK").text = str(product_type_fk)
        start_date, end_date = generate_start_end_dates()
        ET.SubElement(record, "Start_Date").text = start_date
        ET.SubElement(record, "End_Date").text = end_date

        if product_type_fk in [1, 3, 4, 6]:
            ET.SubElement(record, "Interest_Rate").text = "0"
        else:
            interest_rate = round(random.uniform(0, 200), 2)
            ET.SubElement(record, "Interest_Rate").text = str(interest_rate).replace('.', ',')

        if product_type_fk in [2, 5, 8]:
            ET.SubElement(record, "Credit_Limit").text = "0"
        else:
            ET.SubElement(record, "Credit_Limit").text = str(generate_credit_limit(customer_fk))

    xml_str = prettify(records)
    with open("FactFinancialProducts.xml", "w") as f:
        f.write(xml_str)

if __name__ == "__main__":
    record_count = int(input("Introduce la cantidad de registros a generar: "))
    generate_record(record_count)