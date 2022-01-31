import pandas as pd
import matplotlib.pyplot as plt
from pyspark.sql.functions import isnan, when, count, col, udf, dayofmonth, dayofweek, month, year, weekofyear


def extract_content(val):
    """     
    This file is extracting definition table data by filtering needed column name and return code and definition of that attribute
    """

    with open('./other_datasets/I94_SAS_Labels_Descriptions.SAS') as f:
        content = f.read()
        content = content.replace('\t', '')

    
    result = content[content.index(val):]
    result = result[:result.index(';')].split('\n')

    result = [i.replace("'", "") for i in result]
    data_pack = [i.split('=') for i in result[1:]]
    data_pack = dict([i[0].strip(), i[1].strip()] for i in data_pack if len(i) == 2)
    df = pd.DataFrame.from_dict(data_pack, orient="index").reset_index()
    df.columns = ["code","definition"]
    return df



