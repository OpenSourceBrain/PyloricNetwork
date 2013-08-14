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

simDt =                 0.001

simulators =            ["NEURON"]

numConcurrentSims =     4

varTimestepNeuron =     True
varTimestepTolerance =  0.00001

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
                               varTimestepNeuron =    varTimestepNeuron,
                               varTimestepTolerance = varTimestepTolerance)

    simManager.reloadSims(plotVoltageOnly =   plotVoltageOnly,
                          plotSims =          plotSims,
                          analyseSims =       analyseSims)

    # These were discovered using analyseSims = True above.
    # They need to hold for all simulators
    spikeTimesToCheck = {'JNeurosci_0': [87.6251, 109.231, 133.35, 162.018, 196.502, 238.396, 289.697, 351.571, 1169.24, 1188.6, 1211.41, 1238.87, 1272.36, 1313.78, 1365.76, 1429.21, 2242.39, 2261.71, 2284.47, 2311.89, 2345.32, 2386.67, 2438.49, 2501.63, 3315.11, 3334.43, 3357.19, 3384.61, 3418.03, 3459.38, 3511.2, 3574.33],
                         'JNeurophys_fig9D_0': [101.299, 113.988, 128.354, 144.429, 162.178, 181.757, 202.912, 225.158, 248.198, 271.687, 295.555, 319.531, 343.796, 367.912, 392.476, 416.493, 441.532, 465.076, 491.303, 513.62, 544.234, 563.885, 1565.13, 1577.31, 1591.02, 1606.8, 1624.47, 1644.09, 1665.32, 1687.65, 1710.74, 1734.27, 1758.17, 1782.15, 1806.43, 1830.53, 1855.13, 1879.1, 1904.24, 1927.65, 1954.19, 1976.22, 2008.5, 2027.55, 3028.34, 3040.52, 3054.24, 3070.01, 3087.68, 3107.3, 3128.54, 3150.86, 3173.96, 3197.49, 3221.37, 3245.37, 3269.62, 3293.78, 3318.29, 3342.38, 3367.29, 3391.01, 3416.84, 3439.55, 3468.43, 3488.89],
                         'JNeurophys_fig9E_0': [45.1586, 59.2908, 73.5391, 88.87, 105.564, 123.758, 143.534, 164.947, 188.012, 212.681, 238.888, 266.529, 295.55, 326.008, 358.144, 392.505, 430.276, 475.008, 515.2, 1483.44, 1495.43, 1506.81, 1518.81, 1531.69, 1545.61, 1560.63, 1576.81, 1594.14, 1612.6, 1632.12, 1652.59, 1673.92, 1696.01, 1718.81, 1742.29, 1766.46, 1791.33, 1816.95, 1843.4, 1870.76, 1899.17, 1928.78, 1959.83, 1992.68, 2028.02, 2067.3, 2114.6, 2152.32, 3120.51, 3132.49, 3143.86, 3155.85, 3168.74, 3182.65, 3197.67, 3213.84, 3231.18, 3249.64, 3269.16, 3289.63, 3310.96, 3333.04, 3355.85, 3379.33, 3403.49, 3428.36, 3453.98, 3480.44, 3507.8, 3536.2, 3565.8, 3596.85, 3629.72, 3665.06, 3704.29, 3752.14, 3789.08]}
    
    spikeTimeAccuracy = 0.1

    report = simManager.checkSims(spikeTimesToCheck = spikeTimesToCheck,
                                  spikeTimeAccuracy = spikeTimeAccuracy)

    print report

    return report


if __name__ == "__main__":
    testAll()


