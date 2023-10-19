import csv
import gzip
from glob import glob
import xml.etree.ElementTree as ET

def extract_articles_with_keyword(xml_file, keyword='airport'):
    for event, element in ET.iterparse(xml_file, events=('end',)):
        if element.tag.endswith('page'):
            title_tag = element.find(".//{http://www.mediawiki.org/xml/export-0.10/}title")
            id_tag = element.find(".//{http://www.mediawiki.org/xml/export-0.10/}id")

            title = title_tag.text if title_tag is not None else ''
            article_id = id_tag.text if id_tag is not None else ''

            if keyword.lower() in title.lower():
                yield title, article_id

def pluck_wikipedia_titles(pattern='enwiki-*.xml.gz', out_file='airport_titles.csv'):
    with open(out_file, 'a+', encoding='utf-8', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['title', 'id'])  

        for gz_filename in sorted(glob(pattern), key=lambda a: int(a.split('-')[1].split('.')[0]), reverse=True):
            print(gz_filename)
            with gzip.open(gz_filename, 'rt', encoding='utf-8') as xml_file:
                for title, article_id in extract_articles_with_keyword(xml_file):
                    print(f"Processing: {title}")
                    csv_writer.writerow([title, article_id])


