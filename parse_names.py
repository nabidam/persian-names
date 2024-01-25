from enum import Enum
import pandas as pd
import json
import math

from utils import clean_arabic_chars, clean_irabs


class Gender(Enum):
    male = "MALE"
    female = "FEMALE"
    unknown = "UNKNOWN"


def parse_csv(input_filename):
    df = pd.read_csv(input_filename)

    json_data = dict({})

    if "first_name" in df.columns:
        name_column = "first_name"
    elif "Naam" in df.columns:
        name_column = "Naam"
    else:
        return None

    for _, row in df.iterrows():
        name = clean_irabs(clean_arabic_chars(row[name_column]))

        gender = Gender.unknown
        if "Pesar" in df.columns and not math.isnan(row["Pesar"]):
            gender = Gender.male
        elif "Dokhtar" in df.columns and not math.isnan(row["Dokhtar"]):
            gender = Gender.female

        row_data = {"name": name, "gender": gender.value}

        json_data[name] = row_data

    return json_data


if __name__ == "__main__":
    names_1_jsondata = parse_csv(input_filename="names_1.csv")
    names_2_jsondata = parse_csv(input_filename="names_2.csv")

    names_json_data = {**names_1_jsondata, **names_2_jsondata}

    names = json.dumps(names_json_data, ensure_ascii=False)
    filename = "names.json"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(names)

    print(f"First file contains {len(names_1_jsondata)} names.")
    print(f"Second file contains {len(names_2_jsondata)} names.")
    print(f"Finally {len(names_json_data)} distinct names parsed.")
