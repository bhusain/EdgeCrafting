# EdgeCrafting Workflow

![GitHub Logo](EdgeCrafting.png)

## USAGE:

## 1) Pre-processing

Pre-processing includes normalizing of the input Unified Kidney Gene expression matrix (GEM) 

Details for the normalizing code can be accessed at: https://github.com/SystemsGenetics/GEMprep

All data required to run edgecrafting out of the box example is available at https://figshare.com/s/737e8a51dc14084cb461. Perform the following steps to get the data ready:

```
# a. Download UnifiedKidneyData.zip from https://figshare.com/s/737e8a51dc14084cb461
# b. Copy UnifiedKidneyData.zip to folder containing edgecrafting.py
# c. Unzip UnifiedKidneyData.zip to UnifiedKidneyData
```

Note all required files are coded in the ```edgecrafting.py``` as ```./UnifiedKidneyData/{input_file}```

## 2) Data Requirements

EdgeCrafting requires 3 input files described below. For the Kidney data example all required data files are included in UnifiedKidneyData.zip

### I. Normalized Input GEM 

```
Input file: ./UnifiedKidneyData/kidney_GEM.txt
```

kidney_GEM.txt is a tab-delimited file with the following format:

```
                TCGA.KM.8639.01A.11R.2403.07	TCGA.KL.8339.01A.11R.2315.07	TCGA.KN.8419.01A.11R.2315.07  ...
 METTL21B       7.42668570548574	            8.29096998909265	            7.39835596919758              ...
 VSTM2B         8.58047354631563	            8.2084236165314	              7.82455138909605	            ...
.
.
.
```
The 1st row forms the header indicates the name of the tissue samples, wheere as the 1st column indicates the gene name. Each subsequent row is the normalized FPKM values.

### II. Sample metadata labels

```
Input file: ./UnifiedKidneyData/kidney-labels.txt
```
### III. Pre-parsed edges with low MI threshold to reduce computation


## 3) EdgeCrafting Algorithm [Modules B-D]
```
python edgecrafting.py 
```

This code reads in the three input data files mentioned.

```
Output
# a. EgdeCrafting_output.txt: Edgelist of detected gene-pairs, MI values
# b. A Folder containing plots of detected edges as a scatterplot with overlaid blobs
```

### Important Notes:

1) EgdeCraffting_output.txt will include unfiltered MI value. Thresholds are determined in postprocessing.
