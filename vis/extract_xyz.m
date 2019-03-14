function extract_xyz(srcpath, dstpath)

fnames = dir(fullfile(srcpath, '*.off'));
for i = 1 : length(fnames)
    fprintf('Processing %s\n', fnames(i).name)
    shape = loadoff(fullfile(srcpath, fnames(i).name));
    shape_xyz = [shape.X, shape.Y, shape.Z]';
    namesplit = strsplit(fnames(i).name, '.');
    name = strcat(namesplit{1}, '.mat');
    parsave(fullfile(dstpath, name), shape_xyz');
end
end

function parsave(fn, shape_xyz)
save(fn, 'shape_xyz', '-v7.3')
end