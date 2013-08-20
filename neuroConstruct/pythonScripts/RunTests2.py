#
#
#   File to test current configuration of Pyloric project.
#
#   To execute this type of file, type 'nC.bat -python XXX.py' (Windows)
#   or 'nC.sh -python XXX.py' (Linux/Mac). Note: you may have to update the
#   NC_HOME and NC_MAX_MEMORY variables in nC.bat/nC.sh
#
#   Author: Padraig Gleeson
#
#   This file has been developed as part of the neuroConstruct project
#   This work has been funded by the Medical Research Council and the
#   Wellcome Trust
#
#

import sys
import os

try:
    from java.io import File
except ImportError:
    print "Note: this file should be run using nC.bat -python XXX.py' or 'nC.sh -python XXX.py'"
    print "See http://www.neuroconstruct.org/docs/python.html for more details"
    quit()

sys.path.append(os.environ["NC_HOME"]+"/pythonNeuroML/nCUtils")

import ncutils as nc

projFile = File(os.getcwd(), "../PyloricPacemakerNetwork.ncx")


##############  Main settings  ##################

simConfigs = []

simConfigs.append("Test")

simDt =                 0.005
simDtOverride =         {"LEMS":0.001}

simulators =            ["NEURON","LEMS","GENESIS_SI","GENESIS_PHYS","MOOSE_SI","MOOSE_PHYS"]

numConcurrentSims =     4

varTimestepNeuron =     False

plotSims =              True
plotVoltageOnly =       True
runInBackground =       True
analyseSims =           True
verbose =               False

#############################################


def testAll(argv=None):
    if argv is None:
        argv = sys.argv

    print "Loading project from "+ projFile.getCanonicalPath()


    simManager = nc.SimulationManager(projFile,
                                      numConcurrentSims,
                                      verbose)

    simManager.runMultipleSims(simConfigs =           simConfigs,
                               simDt =                simDt,
                               simDtOverride =        simDtOverride,
                               simulators =           simulators,
                               runInBackground =      runInBackground,
                               varTimestepNeuron =    varTimestepNeuron)

    simManager.reloadSims(plotVoltageOnly =   plotVoltageOnly,
                          plotSims =          plotSims,
                          analyseSims =       analyseSims)

    # These were discovered using analyseSims = True above.
    # They need to hold for all simulators
    spikeTimesToCheck = {'Test_CG_0': [103.459, 137.048, 170.888, 204.999, 239.244, 273.559, 307.912, 342.285, 376.67, 411.06, 445.454, 479.85, 514.247, 548.645, 583.042, 617.44, 651.838, 686.236]}
    
    spikeTimeAccuracy = 0.3

    report = simManager.checkSims(spikeTimesToCheck = spikeTimesToCheck,
                                  spikeTimeAccuracy = spikeTimeAccuracy)

    print report

    return report


if __name__ == "__main__":
    testAll()


