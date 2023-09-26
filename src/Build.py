import os
import pandas as pd

class BuildData:
  def __init__(self, folder):
    self.folder = folder
    self.all_data = []

  def mergeFiles(self):
    files = self.__files()
    for file in files:
      try:
        print(f".::Read file {file}...")
        data = pd.read_csv(file, on_bad_lines='skip', delimiter=';')
        self.all_data.append(data)
        print(f".::File read! Data with lenght {len(self.all_data)}.\n")
      except pd.errors.ParserError as e:
        print(f"Error on read file {file}: {str(e)}\n")
    
    pd.concat(self.all_data).to_csv(f"{self.folder}/../all_data.csv", index=False)

  # --private methods
  def __files(self):
    files = os.listdir(self.folder)
    return [f"{self.folder}/{file}" for file in files]
  
if __name__ == "__main__":
  build_data = BuildData("./data/raw_data")
  build_data.mergeFiles()