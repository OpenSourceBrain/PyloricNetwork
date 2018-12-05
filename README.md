Pyloric Pacemaker Network
=========================

Implementation of the pyloric pacemaker network of the lobster stomatogastric ganglion system of Prinz, Marder, et al.

See http://www.opensourcebrain.org/projects/pyloricnetwork for more
details.

This project contains a neuroConstruct project which generates a version of the pyloric pacemaker model. The channel models have been converted to ChannelML and the network can be exported to:

- [NeuroML v1.8.1](https://github.com/OpenSourceBrain/PyloricNetwork/tree/master/neuroConstruct/generatedNeuroML)
- NEURON
- GENESIS
- MOOSE
- [NeuroML v2beta2](https://github.com/OpenSourceBrain/PyloricNetwork/tree/master/neuroConstruct/generatedNeuroML2)


This is based on work by Aditya Gilra, Boris Marin and Padriag Gleeson.  A unified version of the neuroConstruct model is in the top level [neuroConstruct](https://github.com/OpenSourceBrain/PyloricNetwork/tree/master/neuroConstruct) folder.

----------------------------------

Aditya Gilra's original implementation of the pyloric pacemaker model of the lobster somatogastric ganglion 
system in the [AdityaGilraMOOSEnC](https://github.com/OpenSourceBrain/PyloricNetwork/tree/master/AdityaGilraMOOSEnC) folder.

The 3 cell network is for fig 3d from :
Similar network activity from disparate circuit parameters
Astrid A Prinz, Dirk Bucher & Eve Marder
Nature Neuroscience, 2004.

The cell models and channel mechanisms are from:
Alternative to Hand-Tuning Conductance-Based Models: Construction and Analysis of Databases of Model Neurons
Astrid A. Prinz, Cyrus P. Billimoria, and Eve Marder,
J Neurophysiol 90: 3998–4015, 2003.

The same cell is used as the basis for 3 cells AB_PD, LP and PY with different channel densities,
 connected in the pyloric rhythm generator network specified in Fig 3d of Prinz, Bucher and Marder, 2004 above.
Differences from the original model: Synapses are thresholded rather than graded.

A Python file which can be used to load the NeuroML into MOOSE is at [pyloric_net_MOOSE.py](https://github.com/OpenSourceBrain/PyloricNetwork/blob/master/AdityaGilraMOOSEnC/pyloric_net_MOOSE.py)

----------------------------------

Boris Marin's implementation of the pyloric pacemaker model of the lobster
somatogastric ganglion system was based on, from

Prinz, A. A., Thirumalai, V., & Marder, E. (2003). The functional
consequences of changes in the strength and duration of synaptic
inputs to oscillatory neurons. The Journal of neuroscience : the
official journal of the Society for Neuroscience, 23(3), 943–54.
Retrieved from http://www.ncbi.nlm.nih.gov/pubmed/12574423


[![Build Status](https://travis-ci.org/OpenSourceBrain/PyloricNetwork.svg?branch=master)](https://travis-ci.org/OpenSourceBrain/PyloricNetwork)


### Reusing this model

The code in this repository is provided under the terms of the [software license](LICENSE) included with it. If you use this model in your research, we respectfully ask you to cite the references outlined in the [CITATION](CITATION.md) file.

