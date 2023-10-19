#!/bin/bash


input_csv_file="airport_titles.csv"
output_csv_file="filtered_airports.csv"

grep -v -Ei 'List|class|movie|book|template|airports|Category|Portal|File|Featured|incursion|incident|Wikipedia|radio' "$input_csv_file" > "$output_csv_file"
