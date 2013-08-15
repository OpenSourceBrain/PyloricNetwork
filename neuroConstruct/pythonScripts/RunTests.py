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

projFile = File(os.getcwd(), "../PyloricNetwork.ncx")


##############  Main settings  ##################

simConfigs = []

simConfigs.append("Default Simulation Configuration")

simDt =                 0.01

simulators =            ["NEURON"]

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
                               simulators =           simulators,
                               runInBackground =      runInBackground,
                               varTimestepNeuron =    varTimestepNeuron)

    simManager.reloadSims(plotVoltageOnly =   plotVoltageOnly,
                          plotSims =          plotSims,
                          analyseSims =       analyseSims)

    # These were discovered using analyseSims = True above.
    # They need to hold for all simulators
    spikeTimesToCheck = {'JNeurosci_0': [86.05, 107.52, 131.47, 159.92, 194.07, 235.44, 285.71, 345.09, 424.1, 1218.95, 1238.19, 1260.83, 1288.07, 1321.24, 1362.1, 1412.8, 1472.84, 2284.7, 2303.87, 2326.47, 2353.66, 2386.76, 2427.55, 2478.15, 2538.0, 3350.03, 3369.2, 3391.79, 3418.98, 3452.08, 3492.87, 3543.46, 3603.29],
                         'JNeurophys_fig9D_0': [98.95, 111.64, 125.94, 141.94, 159.62, 179.12, 200.2, 222.38, 245.35, 268.78, 292.57, 316.5, 340.67, 364.77, 389.19, 413.26, 438.01, 461.8, 487.27, 510.27, 537.82, 559.02, 599.9, 617.17, 1601.53, 1613.7, 1627.33, 1643.03, 1660.61, 1680.15, 1701.31, 1723.57, 1746.6, 1770.06, 1793.9, 1817.82, 1842.03, 1866.08, 1890.59, 1914.53, 1939.52, 1962.98, 1989.15, 2011.42, 2041.73, 2061.45, 3048.4, 3060.56, 3074.2, 3089.89, 3107.48, 3127.01, 3148.18, 3170.44, 3193.47, 3216.93, 3240.77, 3264.69, 3288.9, 3312.94, 3337.46, 3361.39, 3386.39, 3409.85, 3436.03, 3458.28, 3488.65, 3508.34],
                         'JNeurophys_fig9E_0': [44.67, 58.76, 72.96, 88.24, 104.88, 123.01, 142.72, 164.06, 187.04, 211.62, 237.7, 265.2, 294.03, 324.24, 356.03, 389.88, 426.73, 468.92, 512.51, 1478.11, 1490.06, 1501.38, 1513.3, 1526.1, 1539.93, 1554.86, 1570.94, 1588.18, 1606.54, 1625.95, 1646.31, 1667.52, 1689.5, 1712.17, 1735.52, 1759.52, 1784.22, 1809.65, 1835.87, 1862.97, 1891.05, 1920.26, 1950.8, 1982.98, 2017.29, 2054.69, 2097.57, 2140.41, 3106.1, 3118.05, 3129.36, 3141.28, 3154.08, 3167.9, 3182.83, 3198.91, 3216.15, 3234.51, 3253.92, 3274.28, 3295.5, 3317.48, 3340.15, 3363.49, 3387.5, 3412.2, 3437.63, 3463.85, 3490.95, 3519.04, 3548.25, 3578.8, 3610.97, 3645.29, 3682.71, 3725.6, 3768.4]}
    
    spikeTimeAccuracy = 0.1

    report = simManager.checkSims(spikeTimesToCheck = spikeTimesToCheck,
                                  spikeTimeAccuracy = spikeTimeAccuracy)

    print report

    return report


if __name__ == "__main__":
    testAll()


