import numpy as np
import os



comp = ['S2000001', 'S2000002', 'S2000003',
	'S2000004', 'S2000040', 'S2000041',
	'S2000046', 'S2000047', 'S2000048', 
	'S2000049', 'S2000054', 'S2000055', 
	'S2000056', 'S2000062', 'S2000071', 
	'S2000072', 'S2000149']

target = 1515*1.0
ratio = [target/1714, target/1736, target/1519, target/1705]

#time = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
#time = [1]

name = 'Truckdataminf' # runs from 001 to 299

#code = ['001', '002', '003', '004', '005']
#code = ['001']

for c in range(1, 299+1):
	nameHere = name + '{:03d}'.format(c) 
	for cp in range(1):
		log = 'open d3plot "/home/ndv/stud/data/Truck/' + nameHere + '/d3plot"' + '\n'
		log += 'selectpart on ' + comp[cp] + '/0' + '\n'
		for i in range(1, 60+1):
			log += 'output "/home/mabbasloo/Documents/carData4/f' + '{:03d}'.format(c) + '_' + comp[cp] + '_' + np.str(i) + '.stl" ' + np.str(i) + ' 7 0 0' + '\n'
		log += 'stop'
		file = open('/home/mabbasloo/Documents/carData4/Data.cfile','w') 
		file.write(log) 
		file.close()
		os.system('/home/mabbasloo/Documents/lsprepost4.0_centos6/lspp4 Data.cfile')
		for i in range(1, 60+1):
			fname = '/home/mabbasloo/Documents/carData4/f' + '{:03d}'.format(c) + '_' + comp[cp] + '_' + np.str(i)
			os.system('/home/mabbasloo/meshconv ' + fname + '.stl ' + '-c obj -o ' + fname)
			#os.system('/home/mabbasloo/simplify ' + fname + '.obj ' + fname + '.obj ' + np.str(ratio[cp]))
			os.system('/home/mabbasloo/meshconv ' + fname + '.obj ' + '-c off -o ' + fname)
