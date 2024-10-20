#!/usr/bin/python3
'''
A script that converts markdown to HTML
'''
import sys
import os
import markdown

if __name__ == '__main__':

    # Test that the number of arguments passed is 2
    if len(sys.argv[1:]) != 2:
        print('Usage: ./markdown2html.py README.md README.html',
              file=sys.stderr)
        sys.exit(1)

    # Store the arguments into variables
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Checks that the markdown file exists and is a file
    if not (os.path.exists(input_file) and os.path.isfile(input_file)):
        print(f'Missing {input_file}', file=sys.stderr)
        sys.exit(1)

    with open(input_file, 'r', encoding='utf-8') as file_1:
        md_content = file_1.read()
        html_content = markdown.markdown(md_content)

    with open(output_file, 'w', encoding='utf-8') as file_2:
        file_2.write(html_content)
