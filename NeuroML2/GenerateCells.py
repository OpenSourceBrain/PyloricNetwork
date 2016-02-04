import itertools
from neuroml import *
from pyneuroml import pynml

values = {
    'AB/PD_1': [400, 2.5, 6, 50, 10, 100, 0.01, 0.00],
    'AB/PD_2': [100, 2.5, 6, 50, 5, 100, 0.01, 0.00],
    'AB/PD_3': [200, 2.5, 4, 50, 5, 50, 0.01, 0.00],
    'AB/PD_4': [200, 5.0, 4, 40, 5, 125, 0.01, 0.00],
    'AB/PD_5': [300, 2.5, 2, 10, 5, 125, 0.01, 0.00],
    'LP_1': [100, 0.0, 8, 40, 5, 75, 0.05, 0.02],
    'LP_2': [100, 0.0, 6, 30, 5, 50, 0.05, 0.02],
    'LP_3': [100, 0.0, 10, 50, 5, 100, 0.00, 0.03],
    'LP_4': [100, 0.0, 4, 20, 0, 25, 0.05, 0.03],
    'LP_5': [100, 0.0, 6, 30, 0, 50, 0.03, 0.02],
    'PY_1': [100, 2.5, 2, 50, 0, 125, 0.05, 0.01],
    'PY_2': [200, 7.5, 0, 50, 0, 75, 0.05, 0.00],
    'PY_3': [200, 10.0, 0, 50, 0, 100, 0.03, 0.00],
    'PY_4': [400, 2.5, 2, 50, 0, 75, 0.05, 0.00],
    'PY_5': [500, 2.5, 2, 40, 0, 125, 0.01, 0.03],
    'PY_6': [500, 2.5, 2, 40, 0, 125, 0.00, 0.02]
}

cd_names = ["Na_STG_all", "CaT_STG_all", "CaS_STG_all", "KA_STG_all", "KCa_STG_all", "Kd_STG_all", "H_STG_all", "LeakConductance_all"]

    
for cellref in values:
    [type, number] = cellref.split('_')
    cond_densities = values[cellref]

    type = type.replace('/','_')
    number = int(number)
     
    print('Generating cell %s, number %i: %s'%(type, number, cond_densities))
    nml_doc = pynml.read_neuroml2_file('../neuroConstruct/generatedNeuroML2/%s.cell.nml'%type)
    cell = nml_doc.cells[0]
    print('Loaded: %s'%cell.id)
    cell_ref = '%s_%i'%(type, number)
    #cell.id = cell_id
    nml_doc.id = cell_ref
    nml_file = '%s.cell.nml'%cell_ref
    
    mp = cell.biophysical_properties.membrane_properties
    
    for i in range(len(cond_densities)):
        cd = cd_names[i]
        value = '%s %s'%(cond_densities[i], 'mS_per_cm2')
        print("  Changing cond dens of %s to %s"%(cd, value))
        for c in itertools.chain(mp.channel_densities, mp.channel_density_nernsts):
            if c.id == cd:
                c.cond_density = value
    pynml.write_neuroml2_file(nml_doc, nml_file)
