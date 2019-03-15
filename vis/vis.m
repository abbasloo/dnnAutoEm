clear all; 
clc;
s1 = loadoff('/home/mabbasloo/Documents/carData4/f005_S2000001_1.off');
[Phi1, Lambda1, A1] = calc_lbo(s1, 100);

s60 = loadoff('/home/mabbasloo/Documents/carData4/f005_S2000001_60.off');
[Phi60, Lambda60, A60] = calc_lbo(s60, 100);

s1_xyz = [s1.X, s1.Y, s1.Z]'; 
s1_xyz_t = s1_xyz * Phi1;

s60_xyz = [s60.X, s60.Y, s60.Z]'; 
s60_xyz_t = mtimes(s60_xyz, Phi1);

s60_n_ = mtimes(s60_xyz_t, pinv(Phi1));
s60_n = s60;
s60_n.X = s60_n_(1, :);
s60_n.Y = s60_n_(2, :);
s60_n.Z = s60_n_(3, :);

subplot(1, 2, 1); scatter3(s60.X, s60.Y, s60.Z, '.'); title('point cloud, t=60');
subplot(1, 2, 2); scatter3(s60_n.X, s60_n.Y, s60_n.Z, '.'); title('obtained point cloud, t=60');