# EdgeCrafting

![GitHub Logo](EdgeCrafting.png)

## USAGE:

## 1) Pre-processing

Pre-processing includes normalizing of the input Unified Kidney Gene expression matrix (GEM) 

Details for the normalizing code can be accessed at: https://github.com/SystemsGenetics/GEMprep

The normalized UnifiedKidneyGEM is available upon request. 


## 2) EdgeCrafting Algorithm [Modules A-D]
```
python EdgeCrafting.py 
```

This code reads in the GEM (GTEx_v7_brain_subGEM-log-no.txt) and outputs a file (NetExtractor_output.txt) which contains GeneA_name, GeneB_name, MI value, Inter-cluster score value.

The code is parallelized for multiprocesses and runs on 20 threads. Modify based on resources available.

### Important Notes:

1) EgdeCraffting_output.txt will include unfiltered MI and S values. Thresholds are determined in postprocessing.
