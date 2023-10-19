# Project Name

wikipedia airports extractor

# Project Overview

Extracts airport coordinates and corresponding wikipages to those airports

# Getting Started

# Prerequisites

---- If wanting to download files and run scripts ----

Wikipedia dumps --> https://dumps.wikimedia.org/
8GB+ RAM Linux system (Ubuntu, MacOs Monterrey used here), and at least 150GB of storage memory (XML uncompressed files are big :| )


# Installation

First: Download XML dump files from wikimedia


Second: Create and activate virtual environment using virtualenv

$ python -m venv python3-virtualenv
$ source python3-virtualenv/bin/activate

Third: Use package manager pip to install requirements

pip install -r requirements.txt

Optional: Tableau --Used for geo mapping

# Usage

JSON provided with coordinates of 8800+ airport entries (coordinates_output.json). You can import this file into for example Tableau and map the coordinates!!





# Technologies Used

Python3.7
Tableau

# Code Overview

Key Files

airport_coordinate_extractor.py: extracts geohack coordinates from airport wiki page
airport_name_id_extractor.py: extracts article titles and article ids from wikimedia xml dump meta data files (stub-articles*)
filter_csv_list.sh: bash file to further filter titles, to not include relevant data

How to Contribute

Extract more data! Airport wiki pages also include cool metrics such as top destinations, and number of passengers

# issues and Bugs

Not perfect. There are some airports and coordinates not included 

# Changelog

# Acknowledgments

Shout out to Mark Litwintschik --> https://tech.marksblogg.com/

# License

Creative Commons License

# Contact







