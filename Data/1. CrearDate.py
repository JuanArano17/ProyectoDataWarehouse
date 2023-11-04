import xml.etree.ElementTree as ET
from datetime import datetime, timedelta

def create_xml_file():
    # Crear la raíz del XML
    records = ET.Element("records")

    # Fecha inicial y fecha final
    start_date = datetime(2021, 1, 1)
    end_date = datetime(2022, 12, 31)

    delta = timedelta(days=1)

    while start_date <= end_date:
        # Crear registro para cada día
        record = ET.SubElement(records, "record")
        
        # Agregar la información de Date, Day, Month y Year al registro
        date_element = ET.SubElement(record, "Date")
        date_element.text = f"{start_date.year}-{start_date.month}-{start_date.day}"
        
        day_element = ET.SubElement(record, "Day")
        day_element.text = str(start_date.day)
        
        month_element = ET.SubElement(record, "Month")
        month_element.text = str(start_date.month)
        
        year_element = ET.SubElement(record, "Year")
        year_element.text = str(start_date.year)
        
        # Mover al siguiente día
        start_date += delta

    # Escribir el XML a un archivo
    tree = ET.ElementTree(records)
    with open("records.xml", "wb") as f:
        tree.write(f, encoding="UTF-8", xml_declaration=True)

if __name__ == "__main__":
    create_xml_file()
