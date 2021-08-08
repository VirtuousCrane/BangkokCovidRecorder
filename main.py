import src.lib as lib
from sys import exit

def main():
    res   = lib.get_data();
    cases = lib.extract_bangkok_data(res);

    print(f"Total Bangkok Infection: {cases}");
    df = lib.get_previous_data();

    if (not lib.has_updated(cases, df.iloc[-1, 1])):
        print("Data still hasn't updated");
        exit();
    print(f"Today's increase: {cases - df.iloc[-1, 1]}");
    lib.save_data(df, cases);

if __name__ == "__main__":
    main();
