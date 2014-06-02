__author__ = 'Nathan'

# A simple build script coz it only needs to be simple at the moment :)

import os.path
import shutil

src_dir = "src"
dist_dir = "dist"

try:
    shutil.rmtree(dist_dir)
except:
    os.makedirs(dist_dir)

shutil.copytree(src_dir+"/JugaadClient", dist_dir+"/JugaadClient")