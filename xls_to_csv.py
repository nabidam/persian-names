import pandas as pd


def xls2csv(input_filename, output_filename):
    xls_file = pd.read_excel(input_filename)

    csv_file = output_filename
    xls_file.to_csv(csv_file, index=False, encoding="utf-8")


if __name__ == "__main__":
    xls2csv(input_filename="names_2.xls", output_filename="names_2.csv")
