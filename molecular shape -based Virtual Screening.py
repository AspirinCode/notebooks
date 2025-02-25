#!/usr/bin/python3.6

import oddt
from oddt.shape import usr, usr_similarity

query = next(oddt.toolkit.readfile('mol2', 'query.mol2'))
database = list(oddt.toolkit.readfile('mol2', 'molecules.mol2'))

results = []
	 query_shape = usr(query)
	 for mol in database:
	     mol_shape = usr(mol)
	     similarity = usr_similarity(query_shape, mol_shape)
	     if similarity > 0.8:
	         results.append(mol)

results
 
for i in range(len(results)):
    results[i].write("mol2",str(i)+".mol2")


