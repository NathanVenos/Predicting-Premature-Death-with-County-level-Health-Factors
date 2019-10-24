import pandas as pd

def create_column_dict(path):
    """
    Reads in the two rows of column names from the data set. 
    The first row is a descriptive column name 
    while the second row is simpler unique id.
    Creates a dictionary of the two sets of column names.
    Ignores the first 6 column names,
    which are descriptive in both rows.
    Simplifies the formatting and types of characters 
    within the descriptive column names.
    Returns the dictionary.
    """
    # read in the first two rows
    columns_df = pd.read_csv(path, nrows=1)
    # create the dictionary
    columns_dict = columns_df.iloc[0, 7:].to_dict()
    # swap the keys and values while also removing capitalizations
    columns_dict = dict([(value, key.lower())
                         for key, value in columns_dict.items()])
    # loop through the dictionary to make various string replacements
    str_replace_list = [(' - ', '_'),
                        (' ', '_'),
                        ('-', '_'),
                        ('/', '_'),
                        ('=', '_eqls_'),
                        ('(', ''),
                        (')', ''),
                        ('%', 'pct'),
                        ('+', 'plus'),
                        ('.', '')]
    for key, value in columns_dict.items():
        for replacement in str_replace_list:
            value = value.replace(replacement[0],
                                  replacement[1])
        columns_dict.update({key: value})

    return columns_dict

def column_na_count_df(df):
    """
    Generates a dataframe with one column listing 
    every column in the DataFrame parameter (df),
    and another column with the count of na's in the column.
    """
    na_dict = {}
    for col in df.columns:
        na_count = df[col].isna().sum()
        na_dict.update({col: na_count})
    na_count_df = pd.DataFrame.from_dict(data=na_dict, 
                                         orient='index',
                                         columns=['na_count'])
    na_count_df.reset_index(inplace=True)
    na_count_df.rename(columns={'index': 'column'},
                       inplace=True)
    return na_count_df