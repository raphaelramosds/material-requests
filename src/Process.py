from sklearn.preprocessing import LabelEncoder
import pandas as pd

class ProcessData:
  def __init__(self, filePath):
    self.delimiter = ';'
    self.filePath = filePath
    self.folder = './data'
    self.data = self.__readFile()


  def execute(self):
    self.__getOnlyMaterialRequests()
    self.__clearUnnecessaryCollumns()
    self.__setBinaryStatus()
    self.__categorizeCollumn('status')
    self.__categorizeCollumn('convenio')
    self.__categorizeCollumn('almoxarifado')
    self.__generateFileWithNewData()

  # -- private methods

  def __generateFileWithNewData(self):
    self.data.to_csv(f"{self.folder}/processed_data.csv", index=False)

  def __categorizeCollumn(self, column):
    label_encoder = LabelEncoder()
    self.data[column] = label_encoder.fit_transform(self.data[column])

  def __setBinaryStatus(self):
    self.data = self.data[self.data['status'].isin(['NEGADA', 'AUTORIZADA', 'LIQUIDADA', 'EM_LIQUIDACAO', 'COMPRA'])]

  def __clearUnnecessaryCollumns(self):
    self.data = self.data.drop([
      'numero',
      'ano',
      'requisicao',
      'data',
      'observacoes',
      'grupo_material',
      'tipo_requisicao',
      'unidade_custo',
      'id_unidade_custo'
      'unidade_requisitante'
    ], axis=1)

  def __getOnlyMaterialRequests(self):
    self.data = self.data[self.data['tipo_requisicao'] == 'REQUISIÇÃO DE MATERIAL']

  def __readFile(self):
    return pd.read_csv(self.filePath, delimiter=self.delimiter)
    

if __name__ == '__main__':
  ProcessData('./data/all_data.csv').execute()