import pandas as pd

#----------------------------
#STEP1 - Update Bom File
#----------------------------

# Load CSV
file_path = '../production/bom.csv'
df = pd.read_csv(file_path)

# First column name
first_col = df.columns[0]

# Find index of the row where the first column is 'MODULE1'
match_index = df.index[df[first_col] == 'MODULE1'].tolist()

if match_index:
    idx = match_index[0]
    original_row = df.iloc[[idx]].copy()
    duplicate_row = df.iloc[[idx]].copy()

    # Update names
    original_row.iloc[0, 0] = 'MODULE1A'
    duplicate_row.iloc[0, 0] = 'MODULE1B'

    # Replace original with updated rows
    top = df.iloc[:idx]
    bottom = df.iloc[idx + 1:]
    df = pd.concat([top, original_row, duplicate_row, bottom], ignore_index=True)

    # Overwrite file
    df.to_csv(file_path, index=False)
    print(f"MODULE1 split into MODULE1A + MODULE1B.")
else:
    print("No row with MODULE1 found.")

#----------------------------
#STEP2 - Update Position File
#----------------------------

# Load CSV
file_path = '../production/positions.csv'
df = pd.read_csv(file_path)

# First column name
first_col = df.columns[0]

# Find index of the row where the first column is 'MODULE1'
match_index = df.index[df[first_col] == 'MODULE1'].tolist()

if match_index:
    idx = match_index[0]
    original_row = df.iloc[[idx]].copy()
    duplicate_row = df.iloc[[idx]].copy()

    # Update names
    original_row.iloc[0, 0] = 'MODULE1A'
    duplicate_row.iloc[0, 0] = 'MODULE1B'

    # Update second column by subtracting 34
    second_col = df.columns[1]
    try:
        duplicate_row.iloc[0, 1] = float(duplicate_row.iloc[0, 1]) - 15.24
    except ValueError:
        print(f"⚠️ Can't subtract from second column: not a number -> '{duplicate_row.iloc[0, 1]}'")
        exit(1)

    # Replace original with updated rows
    top = df.iloc[:idx]
    bottom = df.iloc[idx + 1:]
    df = pd.concat([top, original_row, duplicate_row, bottom], ignore_index=True)

    # Overwrite file
    df.to_csv(file_path, index=False)
    print(f"MODULE1 split into MODULE1A + MODULE1B. Value adjusted by -15.24. File '{file_path}' overwritten.")
else:
    print("No row with MODULE1 found.")
    





