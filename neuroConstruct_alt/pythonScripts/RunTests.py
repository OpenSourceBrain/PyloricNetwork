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
    spikeTimesToCheck = {'JNeurosci_0': [84.19, 105.69, 129.63, 158.06, 192.16, 233.45, 283.57, 342.7, 417.96, 1215.15, 1234.38, 1257.03, 1284.27, 1317.45, 1358.33, 1409.06, 1469.14, 2280.94, 2300.1, 2322.7, 2349.89, 2383.0, 2423.79, 2474.38, 2534.23, 3346.27, 3365.43, 3388.03, 3415.22, 3448.32, 3489.1, 3539.69, 3599.53],
                         'JNeurophys_fig9D_0': [95.75, 108.45, 122.78, 138.79, 156.47, 175.97, 197.04, 219.22, 242.19, 265.62, 289.41, 313.34, 337.51, 361.61, 386.03, 410.1, 434.85, 458.65, 484.1, 507.11, 534.63, 555.86, 596.28, 613.61, 1598.13, 1610.29, 1623.93, 1639.62, 1657.21, 1676.75, 1697.91, 1720.17, 1743.2, 1766.66, 1790.5, 1814.42, 1838.63, 1862.68, 1887.19, 1911.13, 1936.12, 1959.58, 1985.76, 2008.02, 2038.37, 2058.07, 3045.01, 3057.17, 3070.81, 3086.5, 3104.09, 3123.62, 3144.79, 3167.05, 3190.08, 3213.54, 3237.38, 3261.29, 3285.51, 3309.55, 3334.07, 3358.0, 3383.0, 3406.46, 3432.64, 3454.89, 3485.29, 3504.97],
                         'JNeurophys_fig9E_0': [43.81, 57.92, 72.12, 87.4, 104.03, 122.16, 141.86, 163.19, 186.16, 210.72, 236.79, 264.26, 293.07, 323.26, 355.02, 388.83, 425.63, 467.68, 511.51, 1477.11, 1489.06, 1500.38, 1512.29, 1525.09, 1538.91, 1553.84, 1569.91, 1587.14, 1605.5, 1624.9, 1645.26, 1666.47, 1688.44, 1711.11, 1734.45, 1758.45, 1783.14, 1808.56, 1834.77, 1861.86, 1889.93, 1919.13, 1949.66, 1981.81, 2016.1, 2053.47, 2096.27, 2139.23, 3104.92, 3116.86, 3128.17, 3140.08, 3152.88, 3166.71, 3181.63, 3197.71, 3214.95, 3233.31, 3252.72, 3273.08, 3294.29, 3316.27, 3338.94, 3362.28, 3386.29, 3410.98, 3436.41, 3462.63, 3489.73, 3517.81, 3547.02, 3577.56, 3609.73, 3644.04, 3681.44, 3724.3, 3767.16]}
    
    spikeTimeAccuracy = 0.1

    report = simManager.checkSims(spikeTimesToCheck = spikeTimesToCheck,
                                  spikeTimeAccuracy = spikeTimeAccuracy)

    print report

    return report


if __name__ == "__main__":
    testAll()


