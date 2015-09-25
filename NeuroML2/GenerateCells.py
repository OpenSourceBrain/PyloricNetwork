
from neuroml import *

from pyneuroml import pynml

values = {}

values['AB/PD_1']=[400, 2.5, 6, 50, 10, 100, 0.01, 0.00]
values['AB/PD_2']=[100, 2.5, 6, 50, 5, 100, 0.01, 0.00]

values['AB/PD_3']=[200, 2.5, 4, 50, 5, 50, 0.01, 0.00]
values['AB/PD_4']=[200, 5.0, 4, 40, 5, 125, 0.01, 0.00]
values['AB/PD_5']=[300, 2.5, 2, 10, 5, 125, 0.01, 0.00]
values['LP_1']=[100, 0.0, 8, 40, 5, 75, 0.05, 0.02]
values['LP_2']=[100, 0.0, 6, 30, 5, 50, 0.05, 0.02]
values['LP_3']=[100, 0.0, 10, 50, 5, 100, 0.00, 0.03]
values['LP_4']=[100, 0.0, 4, 20, 0, 25, 0.05, 0.03]
values['LP_5']=[100, 0.0, 6, 30, 0, 50, 0.03, 0.02]
values['PY_1']=[100, 2.5, 2, 50, 0, 125, 0.05, 0.01]
values['PY_2']=[200, 7.5, 0, 50, 0, 75, 0.05, 0.00]
values['PY_3']=[200, 10.0, 0, 50, 0, 100, 0.03, 0.00]
values['PY_4']=[400, 2.5, 2, 50, 0, 75, 0.05, 0.00]
values['PY_5']=[500, 2.5, 2, 40, 0, 125, 0.01, 0.03]
values['PY_6']=[500, 2.5, 2, 40, 0, 125, 0.00, 0.02]

cd_names = ["Na_STG_all", "CaT_STG_all", "CaS_STG_all", "KA_STG_all", "KCa_STG_all", "Kd_STG_all", "H_STG_all", "LeakConductance_all"]


def generate_cell(type, number, cond_densities):
    
    print('Generating cell %s, number %i: %s'%(type, number, cond_densities))
    nml_doc = pynml.read_neuroml2_file('../neuroConstruct/generatedNeuroML2/%s.cell.nml'%type)
    cell = nml_doc.cells[0]
    print('Loaded: %s'%cell.id)
    cell_id = '%s_%i'%(type, number)
    cell.id = cell_id
    nml_doc.id = cell_id
    nml_file = '%s.cell.nml'%cell_id
    
    mp = cell.biophysical_properties.membrane_properties
    
    for i in range(len(cond_densities)):
        cd = cd_names[i]
        value = '%s %s'%(cond_densities[i], 'mS_per_cm2')
        print("  Changing cond dens of %s to %s"%(cd, value))
        for c in mp.channel_densities:
            if c.id == cd:
                c.cond_density = value
            
        
    pynml.write_neuroml2_file(nml_doc, nml_file)

    
if __name__ == "__main__":
    
    for cellref in values.keys():
        [type, number] = cellref.split('_')
        cond_densities = values[cellref]
        generate_cell(type.replace('/','_'), int(number), cond_densities)