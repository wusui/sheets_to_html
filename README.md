# sheets_to_html

Sheets_to_html consists of a text file and a python script that enable one to
produce an html page from the contents of a Google sheets document.

## Recipe ingredient list

What you need:

- converter.py (provided)
- header.txt (provided)
- google.yaml (see Use section below)
- credentials.json (see Setup section below)

## Assumptions

The converter.py script assumes that the data will contain records that
have a date field in them with the format mm/dd/yyyy.

## Prior Art

The get_data_google_sheets python code used in converter.py was extracted from
code publically released by Lucas Ribeiro on this page:

https://levelup.gitconnected.com/python-pandas-google-spreadsheet-476bd6a77f2b

This page is also an excellent source of information on how to set up the connections
for being able to extract the data from Google.

## Setup

- Install python 3 on your system

- Select/create a folder where the data will be collected and saved

- Extract converter.py and header.txt

- mkdir html

- Create the Google credentials needed (see the levelup.gitconnected.com webpage)

The credentials should be saved in credentials.json

The python script will require pandas, and google.oauth2 libraries.  Depending on
your system, you may need more libraries.  I would recommend running the
converter.py script and pip installing what is needed.

## Use

- Create a Google sheet.  Add data

- Create a file named google.yaml containing the following fields:
  - sheet: data added here will be the 44 character long Google sheet name in the URL
  - subject: The text that you will display at the start of the title

- Share (use the sheet SHARE button) and add the email of the client_id in credentials.json

- Run python converter.py

## Results

In html, there should be an html file with the data that you want in it.  You can view
this data in any browser.  The name of the file will be Month_dd_yyyy.html where the
month, day and year values in the file name are the values of the first date found
in the Google sheet.

These steps can be repeated to produce html files for other sheets


