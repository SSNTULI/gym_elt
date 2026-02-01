import pandas as pd
import requests
import sys
from tqdm import tqdm

def continent(country_var):
    country_space_rm = country_var.replace(" ", "%20")
    country_API = f"https://restcountries.com/v3.1/name/{country_space_rm}"
    resp = requests.get(country_API, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    return data[0]["continents"][0]

def main(csv_input):
    df = pd.read_csv(csv_input)

    dtype_dict = {
        "Index": "Int64",
        "Customer Id": "string",
        "First Name": "string",
        "Last Name": "string",
        "Company": "string",
        "City": "string",
        "Country": "string",
        "Phone 1": "string",
        "Phone 2": "string",
        "Email": "string",
        "Website": "string"
    }

    df = df.astype(dtype=dtype_dict)
    df["Subscription Date"] = pd.to_datetime(df["Subscription Date"])

    # Create column first
    df["continent"] = None

    for i in tqdm(range(len(df))):
        try:
            df.at[i, "continent"] = continent(df.at[i, "Country"])
        except:
            df.at[i, "continent"] = "Unknown"
    

    df.to_csv("output.csv", index=False)

if __name__ == "__main__":
    main(sys.argv[1])
