## Aditya Gilra, NCBS, Bangalore, July 2013

"""
Generate the generatedNeuroML folder and files using neuroConstruct 1.6.1:
Export NeuroML 1.8.1 Level 3 (not as a single file, but as multiple files).
make and make install the buildQ branch of MOOSE after checking it out as below:
svn co https://moose.svn.sourceforge.net/svnroot/moose/moose/branches/buildQ/ moose
Finally, run
python STG_net_hsolve.py
"""

import os
os.environ['NUMPTHREADS'] = '1'
import sys
sys.path.append('../../../python')

import moose
from moose.utils import *
from moose.neuroml.NeuroML import NeuroML

from pylab import *

simdt = 10e-6 # s
plotdt = 10e-6 # s
runtime = 10.0 # s
cells_path = '/cells' # neuromlR.readNeuroMLFromFile creates cells in '/cells'

def runSTGNeuroML_L123(filename):
    neuromlR = NeuroML()
    populationDict, projectionDict = \
        neuromlR.readNeuroMLFromFile(filename)
    soma1_path = populationDict['AB_PD'][1][0].path+'/Soma_0'
    soma1Vm = setupTable('somaVm',moose.Compartment(soma1_path),'Vm')
    soma2_path = populationDict['LP'][1][0].path+'/Soma_0'
    soma2Vm = setupTable('somaVm',moose.Compartment(soma2_path),'Vm')
    soma3_path = populationDict['PY'][1][0].path+'/Soma_0'
    soma3Vm = setupTable('somaVm',moose.Compartment(soma3_path),'Vm')
    #somaCa = setupTable('somaCa',moose.CaConc(soma_path+'/CaPool_STG'),'Ca')
    #somaIKCa = setupTable('somaIKCa',moose.HHChannel(soma_path+'/KCa_STG'),'Ik')
    #somaCaE = setupTable('somaCaE',moose.HHChannel(soma_path+'/CaT_STG/nernst'),'E')
    ## Am not able to plot KDr gating variable X when running under hsolve
    #KDrX = setupTable('ChanX',moose.HHChannel(soma_path+'/Gran_KDr_98'),'X')

    print "Reinit MOOSE ... "
    resetSim(['/elec',cells_path], simdt, plotdt, simmethod='hsolve')

    print "Running ... "
    moose.start(runtime)
    tvec = arange(0.0,runtime+2*plotdt,plotdt)
    tvec = tvec[ : soma1Vm.vec.size ]
    plot(tvec,soma1Vm.vec,label='AB_PD',color='g',linestyle='dashed')
    plot(tvec,soma2Vm.vec,label='LP',color='r',linestyle='solid')
    plot(tvec,soma3Vm.vec,label='PY',color='b',linestyle='dashed')
    legend()
    title('Soma Vm')
    xlabel('time (s)')
    ylabel('Voltage (V)')
    print "Showing plots ..."
    show()

filename = "generatedNeuroML/Generated.net.xml"
if __name__ == "__main__":
    if len(sys.argv)>=2:
        filename = sys.argv[1]
runSTGNeuroML_L123(filename)
