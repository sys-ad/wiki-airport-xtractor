import json
import requests
from bs4 import BeautifulSoup
import re
import os

def fetch_coordinates_for_wikipedia_page(title, article_id):
    url = f'https://en.wikipedia.org/wiki/?curid={article_id}'
    response = requests.get(url)

    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find the geohack link
        geohack_link = soup.find('a', {'href': re.compile(r'geohack\.toolforge\.org', re.I)})

        if geohack_link:
            # Extract the coordinates from the link text
            coordinates_match = re.search(r'(\d+\.\d+)°([NS])\s*(\d+\.\d+)°([EW])', geohack_link.text)
            
            if coordinates_match:
                latitude = float(coordinates_match.group(1)) * (-1 if coordinates_match.group(2).upper() == 'S' else 1)
                longitude = float(coordinates_match.group(3)) * (-1 if coordinates_match.group(4).upper() == 'W' else 1)

                return {'latitude': latitude, 'longitude': longitude}

    return None

def main():
    with open('filtered_airports.csv', 'r', encoding='utf-8') as csv_file:
        lines = csv_file.readlines()

    output_file_path = 'coordinates_output.json'
    if os.path.exists(output_file_path):
        os.remove(output_file_path)

    with open(output_file_path, 'a+', encoding='utf-8') as out_file:
        for line in lines:
            # Ensure that the split result has exactly two elements
            line_parts = line.strip().split(',')
            if len(line_parts) == 2:
                title, article_id = line_parts
                print(f"Processing: {title}, ID: {article_id}")

                coordinates_info = fetch_coordinates_for_wikipedia_page(title, article_id)

                if coordinates_info:
                    data = {'title': title, 'url': f'https://en.wikipedia.org/wiki/?curid={article_id}', 'coordinates': coordinates_info}
                    out_file.write(json.dumps(data, ensure_ascii=False))
                    out_file.write('\n')
                    print(f"Coordinates found: {coordinates_info}")
                else:
                    print(f"No coordinates found for '{title}' with ID '{article_id}'")
            else:
                print(f"Skipping line: {line}")

if __name__ == "__main__":
    main()

