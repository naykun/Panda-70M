import os
import pandas as pd
from math import ceil
from tqdm import tqdm
target_folder = "/f_ndata/G/dataset/panda/full_shard_64/"
os.mkdir(target_folder)
def split_csv(file_path, number_of_splits):
    # Check if the file exists
    if not os.path.isfile(file_path):
        print(f"The file {file_path} does not exist.")
        return

    # Load the CSV file (without loading it entirely into memory)
    csv_file = pd.read_csv(file_path, chunksize=1)
    total_rows = sum(1 for row in csv_file)

    # Calculate the number of rows per split file
    rows_per_split = ceil(total_rows / number_of_splits)

    # Reset the chunksize to the calculated rows per split
    csv_file = pd.read_csv(file_path, chunksize=rows_per_split)

    # Get the base name for the output files
    base_name = os.path.splitext(os.path.basename(file_path))[0]

    # Split the file into chunks and save them
    for i, chunk in tqdm(enumerate(csv_file), total=64):
        output_file = f"{base_name}_{i}.csv"
        output_file = os.path.join(target_folder, output_file)
        chunk.to_csv(output_file, index=False)
        print(f"Created split file: {output_file}")

# Usage
file_path = '/f_ndata/G/dataset/panda/panda70m_training_full.csv' # Replace with your CSV file path
number_of_splits = 64
split_csv(file_path, number_of_splits)
