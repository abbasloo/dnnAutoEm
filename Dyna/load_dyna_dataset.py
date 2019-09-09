# -*- coding: utf-8 -*-
#Copyright (c) [2015] [Gerard Pons-Moll]
#

from argparse import ArgumentParser
from os import mkdir
from os.path import join, exists
import h5py
import sys
import os
import numpy as np


def write_mesh_as_obj(fname, verts, faces):
    with open(fname, 'w') as fp:
        for v in verts:
            fp.write('v %f %f %f\n' % (v[0], v[1], v[2]))
        for f in faces+1:  # Faces are 1-based, not 0-based in obj files (add tmp.shape.TRIV = tmp.shape.TRIV + ones(size(tmp.shape.TRIV)) in extract_lbo.m)
            fp.write('f %d %d %d\n' % (f[0], f[1], f[2]))


if __name__ == '__main__':

    sids = ['50004', '50020', '50021', '50022', '50025'] # female
    #sids = ['50002', '50007', '50009', '50026', '50027'] # male
    pids = ['hips', 'knees', 'light_hopping_stiff', 'light_hopping_loose',
            'jiggle_on_toes', 'one_leg_loose', 'shake_arms', 'chicken_wings',
            'punching', 'shake_shoulders', 'shake_hips', 'jumping_jacks',
            'one_leg_jump', 'running_on_spot']

    parser = ArgumentParser(description='Save sequence meshes as obj')
    parser.add_argument('--path', type=str, default='/home/mabbasloo/Documents/Dyna/data/dyna_dataset_f.h5',
                        help='dataset path in hdf5 format') # '/home/mabbasloo/Documents/Dyna/data/dyna_dataset_m.h5' male
    parser.add_argument('--seq', type=str, default=pids,
                        choices=pids, help='sequence name')
    parser.add_argument('--sid', type=str, default=sids,
                        choices=sids, help='subject id')
    parser.add_argument('--tdir', type=str, default='/home/mabbasloo/Documents/Dyna/data/f/',
                        help='target directory') #'/home/mabbasloo/Documents/Dyna/data/m/' male
    args = parser.parse_args()

    for i in range(len(sids)):
        for j in range(len(pids)):
            sidseq = args.sid[i] + '_' + args.seq[j]
            with h5py.File(args.path, 'r') as f:
                if sidseq not in f:
                    print('Sequence %s from subject %s not in %s' % (args.seq[j], args.sid[i], args.path))
                    #f.close()
                    #sys.exit(1)
                else:
                    verts = f[sidseq].value.transpose([2, 0, 1])
                    faces = f['faces'].value

            #tdir = join(args.tdir, sidseq)
            tdir = args.tdir
            #if not exists(tdir):
            #    mkdir(tdir)

            # Write to an obj file
            c = 0
            for iv, v in enumerate(verts):
                #fname = join(tdir, '%05d' % iv)
                fname = tdir + args.sid[i] + '_' + args.seq[j] + '_' + np.str(c)
                c = c + 1
                print('Saving mesh %s' % fname)
                write_mesh_as_obj(fname + '.obj', v, faces)
                os.system('/home/mabbasloo/meshconv ' + fname + '.obj ' + '-c off -o ' + fname)


