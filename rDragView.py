#!/usr/bin/env python

import os
import sys

from utils import parserfunc
from get_lcm import read_lcm_obj, run_pydragon
from vtu_tools import create_vtu


if __name__ == '__main__':
   """
      Create vtu objects for visualisation of DRAGON5 flux with Paraview. Currently 
      works for SN 2D/D in Cartesian and hexagonal geometries. Default run assumes 
      that the required LCM objects are in the directory from where this is run. 
   """

   ### CALL TO PARSER FUNC TO PICK UP INPUT VARIABLES FROM COMMAND LINE
   input_args = parserfunc() 

   ### FETCH CALC TYPE, TEST NAME, AND VERBOSE LEVEL
   calc_type = input_args.calc_type[0]
   test_name = input_args.test_name[0]
   verbose = input_args.verbose[0]

   test_name = test_name if test_name is not None else 'test'

   ### SET DIR PATHS
   dir_pwd  = os.getcwd()
   if verbose > 1:
      print('>>>>>>> CURRENT DIRECTORY:\n', dir_pwd)
      print('-'*74 + '\n')

   ### READ LCM OBJECTS OR RUN DRAGON FIRST AND GET LCM OBJECTS
   if calc_type == 'view':
      Geom, Mcro, Trck, Flux = read_lcm_obj(verbose)
   elif calc_type == 'dragon_view':
      Geom, Mcro, Trck, Flux = run_pydragon(test_name,verbose)

   ### CREATE MATERIAL AND FLUX VTU FILES
   create_vtu(Geom, Mcro, Trck, Flux, test_name, verbose)

   sys.exit('\nReached end of script.')
