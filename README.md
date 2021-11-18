# EdgeCrafting Workflow

![GitHub Logo](EdgeCrafting.png)

## USAGE:

## 1) Pre-processing

Pre-processing includes normalizing of the input Unified Kidney Gene expression matrix (GEM) 

Details for the normalizing code can be accessed at: https://github.com/SystemsGenetics/GEMprep

The normalized UnifiedKidneyGEM is available upon request. 

## 2) Data Requirements

```
# a. Normalized Input GEM - Example: kidney_GEM.txt
# b. Sample metadata labels - Example: kidney-labels.txt
# c. Pre-parsed edges with low MI threshold to reduce computation
```

## 3) EdgeCrafting Algorithm [Modules B-D]
```
python edgecrafting.py 
```

This code reads in the three input data files mentioned.

```
Output
# a. EgdeCraffting_output.txt: Edgelist of detected gene-pairs, MI values
# b. A Folder containing plots of detected edges as a scatterplot with overlaid blobs
```

### Important Notes:

1) EgdeCraffting_output.txt will include unfiltered MI value. Thresholds are determined in postprocessing.
