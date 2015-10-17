**Some console commands for running simulations of this model in OSB 3D Explorer**

PyloricPacemakerNetwork.AB_PD_0.electrical.getSimulationTree();
PyloricPacemakerNetwork.LP_0.electrical.getSimulationTree();
PyloricPacemakerNetwork.PY_0.electrical.getSimulationTree();

Project.persist();

PyloricPacemakerNetwork.AB_PD_0.electrical.SimulationTree.AB_PD[0].v.setWatched(true);
PyloricPacemakerNetwork.LP_0.electrical.SimulationTree.LP[0].v.setWatched(true);
PyloricPacemakerNetwork.PY_0.electrical.SimulationTree.PY[0].v.setWatched(true);

Project.getActiveExperiment().simulatorConfigurations['PyloricPacemakerNetwork.electrical'].setTimeStep('0.00005'); Project.getActiveExperiment().simulatorConfigurations['PyloricPacemakerNetwork.electrical'].setLength('1');


G.addWidget(0).plotData(PyloricPacemakerNetwork.AB_PD_0.electrical.SimulationTree.AB_PD[0].v)
G.addWidget(0).plotData(PyloricPacemakerNetwork.LP_0.electrical.SimulationTree.LP[0].v)
G.addWidget(0).plotData(PyloricPacemakerNetwork.PY_0.electrical.SimulationTree.PY[0].v)

G.addBrightnessFunction(PyloricPacemakerNetwork.AB_PD_0.electrical, PyloricPacemakerNetwork.AB_PD_0.electrical.SimulationTree.AB_PD[0].v, function(x){return (x+0.06)/0.01;});

Project.getActiveExperiment().play({playAll:true})




