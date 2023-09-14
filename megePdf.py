from pypdf import PdfMerger

# pdfs = ['test.pdf', 'file2.pdf', 'file3.pdf', 'file4.pdf']

import os

# Specify the directory path where you want to search for PDF files

directory_path = 'pdfFiles'
directory_path = str(input("where is the directory where your PDF files are located? (default: %s)" % directory_path)) or directory_path

# Get a list of all files in the directory
all_files = os.listdir(directory_path)

# Filter the list to include only PDF files
pdf_files = [file for file in all_files if file.endswith('.pdf')]

# Print the list of PDF files
merger = PdfMerger()
for pdf_file in pdf_files:
    print(pdf_file)
    fulDir = directory_path+'/'+pdf_file
    merger.append(fulDir)

    
finalFileName = str(input("what do you want to call the name of the merged docs to be ? Default :result.pdf ")) or 'result.pdf'
merger.write(directory_path+'/'+finalFileName)
merger.close()


