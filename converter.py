# Copyright (C) 2023 Warren Usui, MIT License
"""
Take a google sheet and display it as an html file
"""
import os
import datetime
import yaml
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

def get_data_google_sheets(sample_spreadsheet_id, tab_index):
    """
    Code found on https://levelup.gitconnected.com/
                    python-pandas-google-spreadsheet-476bd6a77f2b
    """
    scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
        ]
    credentials = Credentials.from_service_account_file(
            'credentials.json',
            scopes=scopes
        )
    gctxt = gspread.authorize(credentials).open_by_key(sample_spreadsheet_id)
    values = gctxt.get_worksheet(tab_index).get_all_values()
    dfg = pd.DataFrame(values)
    dfg.columns = dfg.iloc[0]
    dfg.drop(dfg.index[0], inplace=True)
    return dfg

def chg_date(msdsy):
    """
    Convert mm/dd/yyyy to month day, year
    """
    return datetime.datetime.strptime(msdsy, "%m/%d/%Y").strftime('%B %d, %Y')

def main_p():
    """
    Main body of code that writes a pandas dataframe after a header containing
    CSS format values.
    """
    # Extract the sheet name from the yaml file
    with open("google_id.yaml", 'r', encoding='utf-8') as ifd:
        google_name = yaml.safe_load(ifd)
    # Get dataframe and html table from Google sheet
    df_ = get_data_google_sheets(google_name["sheet"], 0 )
    tbl = df_.to_html(index=False)
    # Find first and last dates in sheet
    td_fields = tbl.split("<td>")[1:]
    td_flds = list(map(lambda a: a.split("<")[0], td_fields))
    date_flds = list(filter(lambda a: len(a.split('/')) == 3, td_flds))
    # Reformat dates
    drange = list(map(chg_date, [date_flds[0], date_flds[-1]]))
    datetxt = " to ".join(drange)
    # Read html and css headers and add date fields
    with open("header.txt", 'r', encoding='utf-8') as ifd:
        header = ifd.read()
    splt = header.split("DATERANGEGOESHERE")
    headout = datetxt.join(splt)
    splt2 = headout.split("SUBJECTGOESHERE")
    headout = google_name["subject"].join(splt2)
    # Get html file name from first date
    fname = '_'.join(list(map(lambda a: a.strip(','), drange[0].split(' '))))
    fname = os.path.join('html', fname + ".html")
    # Write out data
    with open(fname, 'w', encoding='utf-8') as ofd:
        ofd.write(headout)
        ofd.write(tbl)
        ofd.write("</body></html>")

if __name__ == "__main__":
    main_p()
