import PyPDF2
import os

merger = PyPDF2.PdfMerger()  # Mesclar os pdf

lista_arquivos = os.listdir("arquivos") # Listar os arquivos que tem dentro de uma pasta
lista_arquivos.sort() # Ordenar os arquivos
print(lista_arquivos)

for arquivo in lista_arquivos:  # Arquivo é a variavel do nome do arquivo (cv - t.i...)
    if ".pdf" in arquivo: # se tem pdf no nome do arquivo
        merger.append(f"arquivos/{arquivo}") # Adicionar o arquivo que está sendo lido no mesclador

merger.write("Curriculo.pdf") # Salvar o pdf final