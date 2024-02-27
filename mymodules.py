from pandas import ExcelWriter

def test():
    print("test")

def percentage(df):
    t = df.value_counts(normalize=True) * 100
    return t

def write_dataframes_to_excel(sheets_dict, filename='..\data\processed\test.xlsx'):
    # Create a Pandas Excel writer using XlsxWriter as the engine
    writer = ExcelWriter(filename, engine='xlsxwriter')

    # Write each DataFrame to a different worksheet
    for sheet_name, df in sheets_dict.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)

    # Close the Pandas Excel writer and output the Excel file
    writer.close()

def refresh_ID_list(sheets_dict, df_staging):
    # Get the list of IDs from the staging dataframe
    ids_left = df_staging['ID'].tolist()

    # Iterate over the other sheets
    for sheet_name, df in sheets_dict.items():
        # Filter the dataframe by the IDs and update the dictionary
        sheets_dict[sheet_name] = df[df['ID'].isin(ids_left)]
    # Return the updated dictionary
    return sheets_dict

