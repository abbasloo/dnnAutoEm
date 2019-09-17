clc
clear 

shape = loadoff('/home/mabbasloo/Documents/carCrashData/S2000001/f001_S2000001_1.off');
shape_TRIV = shape.TRIV;
name = '/home/mabbasloo/Documents/carCrashData/meshInfo_S2000001.mat';
parsave(name, shape_TRIV);


shape = loadoff('/home/mabbasloo/Documents/carCrashData/S2000002/f001_S2000002_1.off');
shape_TRIV = shape.TRIV;
name = '/home/mabbasloo/Documents/carCrashData/meshInfo_S2000002.mat';
parsave(name, shape_TRIV);

shape = loadoff('/home/mabbasloo/Documents/carCrashData/S2000003/f001_S2000003_1.off');
shape_TRIV = shape.TRIV;
name = '/home/mabbasloo/Documents/carCrashData/meshInfo_S2000003.mat';
parsave(name, shape_TRIV);

shape = loadoff('/home/mabbasloo/Documents/carCrashData/S2000004/f001_S2000004_1.off');
shape_TRIV = shape.TRIV;
name = '/home/mabbasloo/Documents/carCrashData/meshInfo_S2000004.mat';
parsave(name, shape_TRIV);

function parsave(fn, shape_TRIV)
save(fn, 'shape_TRIV', '-v7.3')
end