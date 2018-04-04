import sys
import os
import shutil
from subprocess import call
###############################################################################

version_nb="0.0.1"

'''
***********************************************
v''' + version_nb + '''
author: Sarah-Beth Amos (sarah-beth.amos@bioch.ox.ac.uk)
git: https://github.com/sbtaamos/MSM_analysis

'''

### Preprocessing of MSM data

# In order to use the MSM script you will need to strip out all the data that 
# we don't want - i.e. coordinates other than that of our disordered region of
# interest. This script produces .xtc and .gro files for both the loop C-alpha 
# atoms and full sidechain residues.  
# 
# This script can be automated for many replicates by using automate.sh (TODO)

###############################################################################

### USAGE: python Preprocess_MSM.py TPR XTC loop_residues

### e.g. python Preprocess_MSM.py md.sim.tpr md.sim.xtc 25-75

###############################################################################



# set inputs

inp1, inp2, inp3 = sys.argv[1], sys.argv[2], sys.argv[3]



# make a lipid index file - select 'r xxx' for an individual lipid, 'r xxx xxx xxx xxx' for a group, where xxx is the residue number.

os.system("echo 'del 0\n' 'del 1-45\n' 'r %s & a CA\n' 'r %s \n' 'q\n'|"%(inp3, inp3)+"gmx_avx make_ndx -f %s -o selections.ndx"%(inp1))

# convert the trajectories

# r & a CA
os.system("echo '1\n'|"+"gmx_avx trjconv -s %s -f %s -n selections.ndx -o r_%s_CA.xtc -nice -15"%(inp1, inp2, inp3))

# r 
os.system("echo '2\n'|"+"gmx_avx trjconv -s %s -f %s -n selections.ndx -o r_%s.xtc -nice -15"%(inp1, inp2, inp3))

