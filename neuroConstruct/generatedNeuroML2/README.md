**Some console commands for running simulations of this model in OSB 3D Explorer**

PyloricPacemakerNetwork.AB_PD_0.electrical.getSimulationTree()
PyloricPacemakerNetwork.AB_PD_0.electrical.SimulationTree.AB_PD[0].v.setWatched(true)
PyloricPacemakerNetwork.LP_0.electrical.getSimulationTree()
PyloricPacemakerNetwork.LP_0.electrical.SimulationTree.LP[0].v.setWatched(true)
PyloricPacemakerNetwork.PY_0.electrical.getSimulationTree()
PyloricPacemakerNetwork.PY_0.electrical.SimulationTree.PY[0].v.setWatched(true)


G.addWidget(0).plotData(PyloricPacemakerNetwork.AB_PD_0.electrical.SimulationTree.AB_PD[0].v)
G.addWidget(0).plotData(PyloricPacemakerNetwork.LP_0.electrical.SimulationTree.LP[0].v)
G.addWidget(0).plotData(PyloricPacemakerNetwork.PY_0.electrical.SimulationTree.PY[0].v)

Project.getActiveExperiment().play({playAll:true})




