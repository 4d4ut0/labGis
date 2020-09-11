import glob

csv = []
for file in glob.glob('*.xml'):
	csvLine = file + ';'
	for line in open(file):
		if line.strip().startswith('<MDI key="STATISTICS_MAXIMUM">'):
			csvLine = csvLine + line.split('>')[1].split('<')[0] + ';'
		elif line.strip().startswith('<MDI key="STATISTICS_MEAN">'):
			csvLine = csvLine + line.split('>')[1].split('<')[0] + ';'
		elif line.strip().startswith('<MDI key="STATISTICS_MINIMUM">'):
			csvLine = csvLine + line.split('>')[1].split('<')[0] + ';'
		elif line.strip().startswith('<MDI key="STATISTICS_STDDEV">'):
			csvLine = csvLine + line.split('>')[1].split('<')[0] + '\n'
	csv.append(csvLine)

csvFile = open('resultado.csv', 'w')

csvFile.writelines('Nome do arquivo; Maximum; Mean; Minimum; STDDEV\n')
csvFile.writelines(csv)