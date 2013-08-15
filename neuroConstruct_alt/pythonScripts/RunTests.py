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

projFile = File(os.getcwd(), "../lobster_pyloric_2004.ncx")


##############  Main settings  ##################

simConfigs = []

simConfigs.append("Test3STGcells")

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
    spikeTimesToCheck = {'JNeurosci_0': [82.23, 103.75, 127.69, 156.1, 190.17, 231.38, 281.37, 340.3, 413.55, 1212.07, 1231.3, 1253.95, 1281.2, 1314.38, 1355.27, 1406.01, 1466.13, 2277.88, 2297.05, 2319.65, 2346.84, 2379.95, 2420.74, 2471.33, 2531.18, 3343.22, 3362.38, 3384.97, 3412.16, 3445.27, 3486.05, 3536.64, 3596.48],
                         'JNeurophys_fig9D_0': [92.36, 105.08, 119.43, 135.45, 153.14, 172.63, 193.71, 215.88, 238.85, 262.28, 286.07, 310.0, 334.17, 358.27, 382.69, 406.77, 431.51, 455.31, 480.75, 503.78, 531.25, 552.51, 592.34, 609.76, 1594.49, 1606.65, 1620.29, 1635.98, 1653.56, 1673.1, 1694.27, 1716.52, 1739.56, 1763.02, 1786.85, 1810.77, 1834.99, 1859.03, 1883.55, 1907.48, 1932.48, 1955.93, 1982.12, 2004.37, 2034.79, 2054.46, 3041.39, 3053.55, 3067.19, 3082.88, 3100.46, 3120.0, 3141.17, 3163.42, 3186.46, 3209.92, 3233.75, 3257.67, 3281.89, 3305.93, 3330.45, 3354.38, 3379.38, 3402.83, 3429.02, 3451.27, 3481.68, 3501.36],
                         'JNeurophys_fig9E_0': [42.84, 56.96, 71.17, 86.45, 103.08, 121.2, 140.9, 162.22, 185.18, 209.72, 235.77, 263.23, 292.03, 322.19, 353.93, 387.71, 424.45, 466.4, 510.42, 1476.03, 1487.98, 1499.29, 1511.2, 1524.0, 1537.82, 1552.74, 1568.81, 1586.04, 1604.39, 1623.79, 1644.14, 1665.34, 1687.31, 1709.97, 1733.3, 1757.3, 1781.98, 1807.39, 1833.6, 1860.68, 1888.74, 1917.93, 1948.44, 1980.58, 2014.84, 2052.18, 2094.9, 2137.99, 3103.66, 3115.61, 3126.92, 3138.83, 3151.63, 3165.45, 3180.38, 3196.45, 3213.69, 3232.05, 3251.45, 3271.81, 3293.02, 3315.0, 3337.67, 3361.01, 3385.01, 3409.7, 3435.13, 3461.35, 3488.44, 3516.52, 3545.72, 3576.26, 3608.42, 3642.72, 3680.11, 3722.94, 3765.84]}
    
    spikeTimeAccuracy = 0.1

    report = simManager.checkSims(spikeTimesToCheck = spikeTimesToCheck,
                                  spikeTimeAccuracy = spikeTimeAccuracy)

    print report

    return report


if __name__ == "__main__":
    testAll()


