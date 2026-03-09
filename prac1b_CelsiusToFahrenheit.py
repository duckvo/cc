import requests
import xml.etree.ElementTree as ET  # Fixed import

url = "https://www.w3schools.com/XML/tempconvert.asmx"
temp = float(input("Enter a temp in Celsius:"))

SOAPEnvelop = f"""<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <CelsiusToFahrenheit xmlns="https://www.w3schools.com/xml/">
      <Celsius>{temp}</Celsius>
    </CelsiusToFahrenheit>
  </soap:Body>
</soap:Envelope>"""

headers = {
    "Content-Type": "text/xml; charset=utf-8",  
    "SOAPAction": "https://www.w3schools.com/xml/CelsiusToFahrenheit"
}

response = requests.post(url=url, data=SOAPEnvelop, headers=headers)
root = ET.fromstring(response.text)

for child in root.iter("{https://www.w3schools.com/xml/}CelsiusToFahrenheitResult"):  
    csf = child.text
    print(f"{temp} is equal to {csf}F")
