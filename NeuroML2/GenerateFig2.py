
from neuroml import *

from pyneuroml import pynml

import sys

def generate_panel(ref):
    example_lems_file = 'LEMS_Fig2.xml'

    results = pynml.run_lems_with_jneuroml_neuron(example_lems_file, nogui=True, load_saved_data=True)
    
    if not '-nogui' in sys.argv:

        from matplotlib import pyplot as plt

        for key in results.keys():

            plt.xlabel('Time (s)')
            plt.ylabel('Membrane potential (V)')
            plt.grid('on')

            if key != 't':
                plt.plot(results['t'],results[key], label=""+key)


    plt.show()
    
if __name__ == "__main__":
    
    generate_panel('a')