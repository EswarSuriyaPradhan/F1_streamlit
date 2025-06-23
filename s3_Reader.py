import boto3
import pandas as pd
import streamlit as st
import io

def load_csv_from_s3(file_key):
    """
    Load a CSV file from S3 using boto3 and return as a pandas DataFrame.
    """
    s3 = boto3.client(
        "s3",
        aws_access_key_id=st.secrets["aws_access_key_id"],
        aws_secret_access_key=st.secrets["aws_secret_access_key"],
        region_name=st.secrets["aws_region"]
    )

    bucket = st.secrets["s3_bucket"]
    obj = s3.get_object(Bucket=bucket, Key=file_key)

    return pd.read_csv(obj["Body"])

