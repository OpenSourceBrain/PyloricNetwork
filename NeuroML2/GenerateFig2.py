
from neuroml import *

from pyneuroml import pynml
from matplotlib import pyplot as plt
import sys

lems_files = {}
lems_files['a'] = 'LEMS_Fig2a.xml'
lems_files['b'] = 'LEMS_Fig2b.xml'

def generate_panel(ref):
    example_lems_file = lems_files[ref]

    results = pynml.run_lems_with_jneuroml(example_lems_file, nogui=True, load_saved_data=True)
    
    if not '-nogui' in sys.argv:
        print("Plotting results of %s"%ref)
        
        plots = len(results.keys())-1
        f, a = plt.subplots(plots, sharex=True, sharey=True)

        count = 0
        for key in results.keys():

            #plt.xlabel('Time (s)')
            #plt.ylabel('Membrane potential (V)')
            #plt.grid('on')

            if key != 't':
                a[count].plot(results['t'],results[key], label=""+key)
                count+=1

    
if __name__ == "__main__":
    
    generate_panel('a')
    generate_panel('b')

    plt.show()