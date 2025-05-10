#week14

import requests # pip install pytz done in terminal 
from lxml import etree # lxml installed in terminal as well, fix the lxml problem below 
from datetime import datetime
import pytz

#Function to fetch XML data
def fetch_xml_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status() 
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching XML data: {e}")
        return None

# Function for debugging
def pretty_print_xml(xml_data):
    try:
        dom = etree.fromstring(xml_data)
        print(etree.tostring(dom, pretty_print=True).decode('utf-8'))
    except etree.XMLSyntaxError as e:
        print(f"XML Parsing Error: {e}")

# Function to extract information
def parse_xml(xml_data):
    try:
        
        root = etree.fromstring(xml_data)
        pages_info = []
        
        # Loop through each page in the XML and extract info
        for page in root.findall('.//page'):
            page_info = {}
            title = page.find('title').text
            revision = page.find('revision')
            timestamp = revision.find('timestamp').text
            page_info['title'] = title
            page_info['timestamp'] = timestamp
            
          
            utc_time = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%SZ')
            local_time = utc_time.replace(tzinfo=pytz.utc).astimezone(pytz.timezone('America/New_York'))  # Adjust for your local timezone
            page_info['local_time'] = local_time.strftime('%Y-%m-%d %H:%M:%S')

            pages_info.append(page_info)

        return pages_info
    except etree.XMLSyntaxError as e:
        print(f"XML Parsing Error: {e}")
        return None

# Function to display the extracted page information 
def display_sorted_pages(pages_info):
    if not pages_info:
        print("No valid data to display.")
        return
    
    sorted_pages = sorted(pages_info, key=lambda x: x['timestamp'], reverse=True)
    
    print(f"{'Title':<50} {'Last Revision Date (Local Time)'}")
    print("="*80)
    for page in sorted_pages:
        print(f"{page['title']:<50} {page['local_time']}")

# Main function to control the flow
def main():
    # URL of the Special:Export for Category:Applied_Programming, why is link not working sometimes
    url = 'https://en.wikiversity.org/wiki/Category:Applied_Programming' 
    
    # Fetch XML data
    xml_data = fetch_xml_data(url)
    
    if xml_data:
        print("XML data fetched successfully.")
        pretty_print_xml(xml_data)  # Print XML for debugging
        pages_info = parse_xml(xml_data)
        
        if pages_info:
            display_sorted_pages(pages_info)
        else:
            print("Failed to parse the XML data.")  #code is failing to parse the XML data, fix this later
    else:
        print("Failed to fetch the XML data.")


if __name__ == "__main__":
    main()



