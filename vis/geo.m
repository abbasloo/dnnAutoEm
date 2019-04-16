clc
clear all;

nLBO = 500;
%extract_lbo('/home/mabbasloo/Documents/carData4/', '/home/mabbasloo/Documents/carData4/data/lbo', nLBO);

%extract_xyz('/home/mabbasloo/Documents/carCrashData/S2000004/', '/home/mabbasloo/Documents/carCrashData/S2000004/data/');

tmp = struct;
tmp.shape = loadoff('/home/mabbasloo/Documents/carCrashData/S2000004/f001_S2000004_30.off');
[Phi, Lambda, A] = calc_lbo(tmp.shape, nLBO);
name = '/home/mabbasloo/Documents/carCrashData/f001_S2000004_30.mat';
parsave(name, Phi, Lambda, A);

function parsave(fn, Phi, Lambda, A)
save(fn, 'Phi', 'Lambda', 'A', '-v7.3')
end