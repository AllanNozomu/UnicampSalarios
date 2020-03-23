# UnicampSalarios
Extracting data of Unicamp (Campinas State University) salaries from http://www.dgrh.unicamp.br/remuneracao/transparencia-novembro-2018.pdf

# Motivations
I dit it because I was studying PDF information extraction and wanted something that has a lot of data

# How to use
All the information is already in the repository.
But if you would like to know how I did this, follow this instructions

## Pre-requisites
- Python3
- Pip
- VirtualEnv
- pdftotext

## Steps

### General setup
Create a new virtual environment for python3, activate it and install all the dependencies.

I used [numpy](http://www.numpy.org/), [pandas](https://pandas.pydata.org/) and [PyPDF2](https://pythonhosted.org/PyPDF2/) to help me deal with the data.

```bash
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
```

### Cleanning the pdf

First, you need to download the pdf file.

```bash
curl -O http://www.dgrh.unicamp.br/remuneracao/transparencia-novembro-2018.pdf
```
The first page of this pdf is unecessary. And it have some text and unecessary information at the border. The `remove_borders.py` script will remove the first page and remove some borders from pdf. It will generate this [output.pdf](https://github.com/AllanNozomu/UnicampSalarios/blob/master/output.pdf) file containing only the table.

```bash
python remove_borders.py
```

### Pdf to txt
This part I would like to create a text file containing the information extracted from pdf.

I could use [tabula](https://tabula.technology/) to extract the information, but I decided to not. 

Because I think pdftotext is a more straightfoward solution, so I used it. The -layout parameter of pdftotext is very important to separate all the data and make it appear separated by lines. This command generated this file [output.txt](https://raw.githubusercontent.com/AllanNozomu/UnicampSalarios/master/output.txt)

```bash
pdftotext -layout output.pdf
```

### Txt to csv
Finally, in this part, I will tranform the data from output.txt to [output.txt](https://raw.githubusercontent.com/AllanNozomu/UnicampSalarios/master/output.csv).

I needed to make some cleanning:
1. Read all the data and separate it by lines (\n)
1. Remove the empty lines and trim all the lines removing desnecessary whitespaces.
1. Concatenate the information of each person. Because the information came in 2 (and sometimes 3) lines.
1. Using regex to make a pattern, separate all the information into a matrix
1. Cleanned the data. trim the strings, convert to float the numbers and separate some specific data.
1. Used numpy and pandas to save the csv.

All the process is in commentaries in the code.
```bash
python clean_text.py
```
