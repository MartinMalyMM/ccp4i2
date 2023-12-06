"""
     CTaskShelx.py
     Copyright (C) 2011 University of York, Leiden University

     This library is free software: you can redistribute it and/or
     modify it under the terms of the GNU Lesser General Public License
     version 3, modified in accordance with the provisions of the 
     license to address the requirements of UK law.
 
     You should have received a copy of the modified GNU Lesser General 
     Public License along with this library.  If not, copies may be 
     downloaded from http://www.ccp4.ac.uk/ccp4license.php
 
     This program is distributed in the hope that it will be useful,
     but WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
     GNU Lesser General Public License for more details.
"""

from pipelines.crank2.script import CTaskCrank2

class CTaskShelx(CTaskCrank2.CTaskCrank2):
  TASKNAME = 'shelx'
  TASKVERSION = 0.0
  TASKMODULE='expt_phasing'
  TASKTITLE='Automated structure solution - SHELXC/D/E phasing and building'
  SHORTTASKTITLE='SHELX'
  DESCRIPTION='Experimental phasing pipeline SHELX (run via Crank2)'
  RANK=1

def whatNext(*args,**kwargs):
  return CTaskCrank2.whatNext(*args,**kwargs)
