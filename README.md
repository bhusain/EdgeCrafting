# EdgeCrafting Workflow

![GitHub Logo](EdgeCrafting.png)

## USAGE:

## 1) Pre-processing

Pre-processing includes normalizing of the input Unified Kidney Gene expression matrix (GEM) 

Details for the normalizing code can be accessed at: https://github.com/SystemsGenetics/GEMprep

All data required to run edgecrafting out of the box example is available at https://doi.org/10.6084/m9.figshare.17701247. Perform the following steps to get the data ready:

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

TCGA.KM.8639.01A.11R.2403.07	kich-tumor-tcga
TCGA.KL.8339.01A.11R.2315.07	kich-tumor-tcga
GTEX.ZYFD.1526.SM.5NQ7T	      kidney-gtex
GTEX.12WSG.0826.SM.5EQ5A	kidney-gtex
TCGA.CJ.5680.11A.01R.1541.07	kirc-normal-tcga
TCGA.CZ.5453.11A.01R.1503.07	kirc-normal-tcga
.
.
.
```

kidney-labels.txt is a tab-delimited file detailing the metadata for the tissue samples that include the following categories: 

```
a. kich-tumor-tcga
b. kich-normal-tcga
c. kidney-gtex
d. kirc-normal-tcga
e. kirc-tumor-tcga
f. kirp-normal-tcga
g. kirp-tumor-tcga
```

### III. Pre-parsed edges with low MI threshold to reduce computation:

kidney_blob_25.txt is a comma-delimited file that contains the edgelist as depicted by Module B. The file format includes: {gene1ID} {gene2ID} {gene1Name} {gene2Name} {MIValue}. The included file (kidney_blob_25.txt) contains a pre-parsed edge-list with only edges that meet the criteria of the selected MI value threshold of 0.97. Pre-parsing the file is not a requirement, and an input containing {gene1ID} {gene2ID} {gene1Name} {gene2Name} would be sufficient.

```
Input file: ./UnifiedKidneyData/kidney_blob_25.txt

973,2272,RNASEH2C,SYNE4,0.995
3886,5388,PHIP,GPR110,0.954
0,2272,METTL21B,SYNE4,0.996
2911,5388,TMEM102,GPR110,0.954
488,2991,C19orf55,TMPRSS2,0.988
.
.
.
```

## 3) EdgeCrafting Algorithm [Modules C-D]
```
python edgecrafting.py 
```

This code reads in the three input data files mentioned above. It requires folder UnifiedKidneyData to be in the same directory as edgecrafting.py. 

```
Output
# a. kidney_blob.csv: Edgelist of detected gene-pairs, MI values
# b. A Folder containing plots of detected edges as a scatterplot with overlaid blobs 
[Need to uncomment line: fig.savefig('./'+str(data.columns.values[i]) + '_' + str(data.columns.values[j]) + '.png')]
```
