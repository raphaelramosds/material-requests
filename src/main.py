import os
import pandas as pd

class BuildData:
  def __init__(self, folder):
    self.folder = folder
    self.all_data = pd.DataFrame()

  def mergeFiles(self):
    files = self.__files()
    for file in files:
      try:
        data = pd.read_csv(file)
        self.all_data = pd.concat([self.all_data, data])
      except pd.errors.ParserError as e:
        with open("erros.log", "a") as log_file:
            log_file.write(f"Error on read file {file}: {str(e)}\n")
    
    self.all_data.to_csv(f"{self.folder}all_data.csv", index=False)

  # --private methods
  def __files(self):
    files = os.listdir(self.folder)
    return [f"{self.folder}{file}" for file in files]
  
if __name__ == "__main__":
  build_data = BuildData("./data/")
  build_data.mergeFiles()
  