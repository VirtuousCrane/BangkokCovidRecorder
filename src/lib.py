import requests
import pandas as pd
from datetime import date

def get_data() -> dict[list[dict[str, str]]]:
    res = requests.get("https://covid19.th-stat.com/json/covid19v2/getSumCases.json");
    return res.json();

def extract_bangkok_data(data: dict[list[dict[str, str]]]) -> int:
    return int(data["Province"][0]["Count"]);

def get_previous_data() -> pd.DataFrame:
    df = pd.read_csv("./src/data/bangkok_data.csv");
    return df;

def has_updated(t_data: int, y_data: int) -> bool:
    if (t_data == y_data):
        return False;
    return True;

def save_data(df: pd.DataFrame, cases: int) -> bool:
    today = date.today();
    df.loc[len(df.index)] = [today, cases, cases - df.iloc[-1, 1]];
    data_stream = df.to_csv(index=False);

    f = open("./src/data/bangkok_data.csv", "w");
    f.write(data_stream);
    f.close();

    return True;
