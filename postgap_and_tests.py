#! /usr/bin/env python

"""

Copyright [1999-2018] EMBL-European Bioinformatics Institute

Licensed under the Apache License, Version 2.0 (the "License")
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

		 http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""

"""

	Please email comments or questions to the public Ensembl
	developers list at <http://lists.ensembl.org/mailman/listinfo/dev>.

	Questions may also be sent to the Ensembl help desk at
	<http://www.ensembl.org/Help/Contact>.

"""

import sys
import os
import subprocess

def main():


	firstTime=True
	parameters=""
	outputFile=""
	swOutput =0
	for a in sys.argv:
		if not firstTime:
			parameters += a + " "
			
			if swOutput == 1:
				outputFile = a
				swOutput=0

			if a == "--output":
				swOutput=1
			
		firstTime=False

	parameters = parameters.rstrip()
	strExe = "./POSTGAP.py " + parameters	
	subprocess.call(['bash','-c', strExe])

	if outputFile != "":
		fullPathOutputFile = os.path.abspath(outputFile)
		actualPath = os.getcwd()
		os.chdir(actualPath + "/tests")
		strTests ="./runner.py " + fullPathOutputFile
		subprocess.call(['bash','-c', strTests])
		
		
	
if __name__ == "__main__":
	main()


