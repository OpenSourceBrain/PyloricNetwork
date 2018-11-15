
from neuroml import *

from pyneuroml import pynml
from matplotlib import pyplot as plt
import sys

lems_files = {s: 'LEMS_Fig2%s.xml'%s for s in 'abcd'}

def generate_panel(ref):
    example_lems_file = lems_files[ref]

    print("Running file: %s"%example_lems_file)
    results = pynml.run_lems_with_jneuroml(example_lems_file, nogui=True, load_saved_data=True)
    
    if not '-nogui' in sys.argv:
        print("Plotting results of %s"%ref)
        
        plots = len(results.keys())-1
        f, a = plt.subplots(plots, sharex=True, sharey=True)

	#AB on top
        a[0].plot(results['t'], results[[k for k in results if 'AB' in k][0]])
        
        count = 1
        for key in sorted(results):
            if key != 't' and 'AB' not in key:
                a[count].plot(results['t'],results[key], label=""+key)
                count+=1

    
if __name__ == "__main__":
    
    generate_panel('a')
    generate_panel('b')
    generate_panel('c')
    generate_panel('d') # need to find "good"initial conditions - bistable

    plt.show()
