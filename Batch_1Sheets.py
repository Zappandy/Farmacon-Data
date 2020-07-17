import os
import pandas as pd
import re


headers = {"Connection on LinkedIn": [], "First Name": [], "Last Name": [], "Title": [],
           "Email": [], "Phone": [], "Company Name": [], "Company Website": [],
           "Street Address": [], "Country": [], "City": [], "State": [], "Zip": [], "Phones 1": [],
           "Notes": []}

master_df = pd.DataFrame(headers)


def Wuxi_sheet(df):
    """
    pandas dataframe --> pandas dataframe
    Wuxi_sheet(df) --> dataframe has now naming data, email et al.
    :param df: Master Farmacon dataframe
    :return: Updated data frame
    """
    df_copy = df.copy()
    fileRegex = re.compile(r"^(Farmacon)(.*)(Wuxi.csv)$")
    for file in os.listdir():
        if fileRegex.search(file):
            sheet = pd.read_csv(file).copy()
            break
    list(sheet.keys())  # ['First Name', 'Last Name', 'Title', 'Company']
    for head in sheet.head(0):
        if head in df_copy.head(0): #and df_copy[head].empty:
            df_copy[head] = sheet[head]
        else:
            df_copy["Company Name"] = sheet[head]
    return df_copy


def MeridianCTSpeakers_Sheet(df):
    """
    pandas dataframe --> pandas dataframe
    Wuxi_sheet(df) --> dataframe has now naming data, email et al.
    :param df: Master Farmacon dataframe
    :return: Updated data frame
    """
    df_copy = df.copy()
    fileRegex = re.compile(r"^(Farmacon)(.*)(Meridian CT Speakers.csv)$")
    for file in os.listdir():
        if fileRegex.search(file):
            sheet = pd.read_csv(file).copy()
            break
    list(sheet.keys())  # ['First Name', 'Last Name', 'Title', 'Company']
    for head in sheet.head(0):
        if head in df_copy.head(0): #and df_copy[head].empty:
            df_copy[head] = sheet[head]
        else:
            df_copy["Company Name"] = sheet[head]
    return df_copy
