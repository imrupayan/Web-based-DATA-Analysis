import streamlit as st
import numpy as np
import pandas as pd


st.title("My Organized Dashboard")
st.set_page_config(layout="wide")
# st.sidebar().title("file uploder")
file= st.file_uploader("Upload a csv or excel file", type=["csv"])
if file:
    df = pd.read_csv(file)
else:
    st.write("Your file is not uploaded")
    st.stop()

#df = pd.read_csv(r"C:\Users\rupay\Downloads\Telegram Desktop\Chocolate Sales (2).csv")


def all_features(feature, data_frame):
    temp_data= data_frame.copy()
    if feature=="Handeling missing Data":
        missing_data_handel = st.selectbox("How do you want to handel?",
                                    ["Do nothing","Drop that Row","With Mean","With Median","With Standard Deviation","With Mode",
                                        "Data From Previous Row","Data From Next Row"])
        

        if missing_data_handel=="Do nothing":
            return temp_data

        elif missing_data_handel=="Drop that Row":
            temp_data.dropna(inplace=True)
            return temp_data

        


        elif missing_data_handel=="With Mean":
            temp_data.fillna(df.mean(numeric_only=True), inplace=True)
            return temp_data
                
        elif missing_data_handel=="With Median":
            temp_data.fillna(df.median(numeric_only=True), inplace=True)
            return temp_data
            


        elif missing_data_handel=="With Standard Deviation":
            temp_data.fillna(df.std(numeric_only=True), inplace=True)
            return temp_data


        elif missing_data_handel=="With Mode":
            temp_data.fillna(df.mode(numeric_only=True), inplace=True)
            return temp_data


        elif missing_data_handel=="Data From Previous Row":
            temp_data.ffill(inplace=True)
            return temp_data

        
        elif missing_data_handel=="Data From Next Row":
            temp_data.bfill(inplace=True)
            return temp_data


        


    elif feature=="Groupwise Filter":
        group_filter= st.selectbox("Select a Column", temp_data.columns)
        group=temp_data.groupby(group_filter)
        unique_group=temp_data[group_filter].unique()
        select_a_group=st.selectbox("Select a group", unique_group )
        get_that_group=group.get_group(select_a_group)
        return get_that_group
    elif feature=="Statistical Summary":
        summary =temp_data.describe()
        return summary
    elif feature=="Rename Group":
        pass
#df = pd.read_csv(r"C:\Users\rupay\Downloads\Telegram Desktop\Chocolate Sales (2).csv")

col_left, col_right = st.columns([1, 5])


with col_left:
    features=st.selectbox("Let's do something",["Handeling missing Data","Groupwise Filter","Statistical Summary","Rename Group"])
    new_df = all_features(features,df)
with col_right:

    data_frame= st.dataframe(new_df)






    
#column_filter = st.selectbox("select column", )


#select_tool= st.selectbox("select statistics:", ["mean","median","mode"])
#st.write(stat_func(column_filter,select_tool))







