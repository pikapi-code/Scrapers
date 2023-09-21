
import requests
from bs4 import BeautifulSoup

websites = [
    'https://www.incometax.gov.in/iec/foportal/help/how-to-file-itr4-form-sugam',
    'https://www.incometax.gov.in/iec/foportal/help/e-filing-itr4-form-sugam-faq',
    'https://www.incometax.gov.in/iec/foportal/help/individual-business-profession#returnsandforms' 
]

for url in websites:
    response = requests.get(url)

    if response.status_code == 200:
        # Content was received sucessfully
        page_content = response.text

        soup = BeautifulSoup(page_content, 'html.parser')

        # Find all text content within the HTML
        all_text = ' '.join(soup.stripped_strings)

        title = all_text.split('|')[0]
        title = title.strip()
        text = title + ' \n ' + "".join(all_text.split(title)[2:])
        text = text.split('Page Last Reviewed or Updated:')[0]
        text = text.split('Footer')[0]
        
        # Create a filename based on the title
        filename = f"{title}.txt"

        # Save the text as a TXT file
        with open('downloads/'+filename, 'w', encoding='utf-8') as file:
            file.write(text)

        print(f"Saved {filename}")

    else:
        print('Failed to retrieve the web page')
