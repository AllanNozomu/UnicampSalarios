#!/usr/bin/env python
import re
import pandas as pd
import numpy as np

text = ''
with open('output.txt') as f:
    text = f.read()

# Split text by lines
lines = text.split('\n')

# Remove empty lines
lines = [l for l in lines if l.strip() != '']
new_lines = []

# Concatenate the lines because the information of one person in formed by 2 (or 3) lines
i = 0
while i < len(lines):
    if not (lines[i].strip()[0].isdigit()):
        new_lines[-1] = new_lines[-1] + ' ' + lines[i]
        i = i + 1
    new_lines.append(lines[i].strip() + ' ' + lines[i + 1].strip())
    i = i + 2
    
# Regex to parse the information
program = re.compile('(\d+) ([\w \'-.]+) +(\d+,\d\d) +(\d+,\d\d) +(\d*,\d\d) +(\d*,\d\d) +(\d*,\d\d) (.*)')

# Put all the information in a table
table = []
for l in new_lines:
    res = program.match(l)
    if res:
        table.append([res.group(1), res.group(2).split('   ')[0], res.group(2).split('   ')[-1], res.group(3), res.group(4),
            res.group(5), res.group(6), res.group(7), res.group(8).split('   ')[0], res.group(8).split('   ')[-1]]) 
    else:
        print(l)

# Clean the information
# Tranforming floats in to floats, striping the strings, separating if necessary
for r in table:
    r[0] = int(r[0]) 
    r[1] = r[1].strip()
    r[2] = r[2].strip()
    r[3] = float(r[3].replace(',', '.'))
    r[4] = float(r[4].replace(',', '.'))
    r[5] = float(r[5].replace(',', '.'))
    r[6] = float(r[6].replace(',', '.'))
    r[7] = float(r[7].replace(',', '.'))
    if r[8] == r[9]:
        r[8] = r[8][:r[8].index('PAEPE')].strip() 
        r[9] = r[9][r[9].index('PAEPE'):].strip() 
    else:
        r[8] = r[8].strip()
        r[9] = r[9].strip()

# Put the columns names and make an output.csv file
np_table = np.asarray(table)
table_df = pd.DataFrame(np_table)
table_df.columns = ['Matricula', 'Nome', 'Referencia', 'Bruto', 'Indenizacoes', 'Redutor', 'Descontos', 'Liquido', 'Lotacao', 'Cargo']
table_df.to_csv('output.csv')
