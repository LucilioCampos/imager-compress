from PIL import Image, ImageDraw, ImageFont
import os

print('*** Program Started ***')
"""
  Necessário criar duas pastas, uma chamada input e outra output no 
  mesmo diretório do arquivo compress.py.

  Inserir todas as imagens no diretório input 
  Rodar o script python3 compress.py ou python compress.py


  Após o término os arquivos comprenssados ficaram disponivies no pasta output

  Caso rode o script uma segunda vez, os arquivos novos sobrescreverão os arquivos
  contidos na pasta output que tiverem o mesmo nome
  
"""

def get_filepaths(directory):

  file_paths = []

  for root, directories, files in os.walk(directory):
    for filename in files:
      filepath = os.path.join(root, filename)
      file_paths.append(filepath)

  return file_paths

input_files = get_filepaths("input/")
output_files = get_filepaths("output/")

image_path_input = 'input/'
image_path_output = 'output/'

contador = 0
print("\n *** Aguarde Processando e Convertendo as imagens ***")
print("\n\ *** Total de arquivos: {} ***\n\n\n\n".format(len(input_files)))
for file in input_files:
  image_name_output =  "compressed" + file.split("/")[1]
  im = Image.open(file).convert('RGB')
  im.load()
  
  im.save(image_path_output + image_name_output ,optimize=True,quality=80)
  contador += 1
  print("\nArquivo processado: {}, total de arquivos processados {}".format(file.split("/")[1], contador))



print('\n*** {} Imagens Processadas com sucesso! ***'.format(len(output_files)))