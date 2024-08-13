Cancer-Eye - GLOBOCAN 2020 database - Input, pre-processing ( ViT-Patch), feature selection(Fisher-score), classification(K-means), Output(CSV-report(F1-score metrics))

Features:

- Medical imaging
- Behaviour
- Health records
- Clinical records
- Research
- Pandemic control
- Diagnosis
- Drug discovery

## Choosing model

VIT-patch vision transformer with JAX, PyTorch 
- https://huggingface.co/docs/transformers/model_doc/vit
- https://huggingface.co/google/vit-base-patch16-224


## How to train a model on custom data-set?

How to rain VIT-patch?

- https://github.com/kentaroy47/vision-transformers-cifar10

## How to train model for classification and reporting:

https://medium.com/@yanis.labrak/how-to-train-a-custom-vision-transformer-vit-image-classifier-to-help-endoscopists-in-under-5-min-2e7e4110a353

## cancer data for the model

https://www.uicc.org/news/globocan-2020-global-cancer-data
https://www.uicc.org/


````bash
Here's the hierarchical table organized in an evolutionary way, focusing on open-source software for each level of organism simulation:
Evolutionary Level	Simulation Focus	Suggested Open-Source Software	Methods/Techniques
1. DNA	Genetic sequence modeling, mutations, evolution	Biopython, GROMACS, Nextflow, Clustal Omega	Sequence alignment, Molecular Dynamics, NGS
2. RNA	Transcription, splicing, RNA folding, expression analysis	RNAfold, Galaxy, DESeq2 (RStudio)	RNA-Seq, Transcriptomics, Structural prediction
3. Proteins	Protein folding, structure-function relationship	ROSETTA (academic use), PyMOL (open-source version), ChimeraX	Homology modeling, Molecular Dynamics, Docking
4. Ligands	Ligand binding, docking, drug design	AutoDock Vina, OpenBabel, RDKit	Virtual Screening, Docking, QSAR, SAR
5. Enzymes	Enzyme kinetics, catalysis, pathway modeling	COPASI, SBML, CellDesigner	Kinetic modeling, Metabolic flux analysis
6. Organelles	Organelle dynamics, function, interaction	Virtual Cell (VCell), Blender (for 3D modeling)	Systems biology, Spatial modeling
7. Cells	Cellular processes, signaling pathways, proliferation	COPASI, CellDesigner, E-Cell	ODEs/PDEs, Agent-based modeling, FBA
8. Histones	Chromatin structure, epigenetic regulation	ChromHMM, Cistrome	Chromatin modeling, Epigenomics, Histone mark analysis
9. Tissues/Organs	Tissue dynamics, organ development, function simulation	OpenSim, FEBio, Blender (for 3D modeling)	Finite Element Analysis, Biomechanical modeling
10. Organ Systems	Systemic interaction, homeostasis, physiological response	OpenCOR, OpenMM	Systems biology, Whole-body modeling, Physiological simulations
11. Organism	Whole-organism behavior, evolutionary dynamics	NetLogo, MASON, Repast	Agent-based modeling, Evolutionary simulations
````
