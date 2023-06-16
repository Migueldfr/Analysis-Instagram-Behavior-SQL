import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")
import os 

# Current working directory
dir_path = os.path.dirname(os.path.realpath(__file__))

# Change working directory
os.chdir(dir_path)


def read_data_from_csv():
    likes=pd.read_csv('data/likes.csv')
    return likes


def data_cleaning():
    #DO NOT REMOVE FOLLOWING LINE
    #call remove_unwanted_columns() function to get dataframe
    likes=read_data_from_csv()

    #Remove Unwanted columns
    
    likes.drop(columns=['following or not', 'like type'],inplace=True)

    
    #rename columns, only these columns are allowed in the dataset
    likes.rename(columns={'user ': 'user_id', 'photo': 'photo_id', 'created time': 'created_at'}, inplace=True)

    # 1.	user_id
    # 2.	photo_id
    # 3.	created_at
    
    #export cleaned Dataset to newcsv file named "likes_cleaned.csv"
    likes.to_csv('data/likes_cleaned.csv',index_label='id', index=True)
    return likes


#Do not Delete the Following function
def task_runner():
    data_cleaning()

task_runner()