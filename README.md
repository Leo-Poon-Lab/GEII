## host Gene Expression under Influenza virus infection or Interferon stimulation (GEII)
*Yi Cao, Haogao Gu, Leo Poon*


### Online version
XXX

### Citation
XXX

### About
Host Gene Expression under Influenza virus infection or Interferon stimulation (GEII) database is a user-friendly tool for study host gene expression during diverse subtypes of influenza virus infection or interferon stimulation across multiple cell types. GEII integrates high throughput datasets generated from RNA-seq and microarray from public databases such SRA, GEO and IRD. 

### Usage and Glossary Information
GEII recognize NCBI entrez ID (recommended) or gene symbol as input and return output containing information about gene annotations, originates, infection or stimulation conditions, expression fold change and relevant statistics. 

***entrezID***: NCBI gene entrez ID, unique digit or digits that assigned to gene as identifier. 

***gene_symbo***l: NCBI gene symbol, gene name based on short-form abbreviation.

***bioproject***: Bioproject number in SRA database.

***res_design***: research design is about the strategy applied to uploaded datasets. Note: Research design used in this database may be different from original study as datasets in one bioprojct that have no relevance to the aim of this study had been removed. 

***host_type***: tissues or cells used as host for infection.

***virus_strain***: influenza subtypes used for infection.

***stimulator***: If it is under condition of interferon stimulation, type of interferon used in the stimulation.

***concentration***: If it is under condition of interferon stimulation, the concentration used in the stimulation.

***M.O.I***: Multiplicity of infection used in infection.

***H.P.I***: Hour post infection.

***H.P.S***: Hour post stimulation.

***baseMean***: The average of the normalized count values, dividing by size factors, taken over all samples[^1].

***lfcSE***: The standard error estimate for the log2 fold change estimate[^1].

***stat***: The value of the test statistic for the gene or transcript[^1].

***log2FoldChange***: For RNA-seq dataset, the effect size estimate. This value indicates how much the gene or transcript's expression seems to have changed between the comparison and control groups. This value is reported on a logarithmic scale to base 2[^1]. For microarray dataset, Log2-fold change between two experimental conditions[^2].

***pvalue***: P-value of the test for the gene or transcript[^1].

***padj***: Adjusted P-value for multiple testing for the gene or transcript[^1].

***probe_seq***: Probe sequences used to detect gene expression. Note: In microarray dataset, multiple probes may be used to detect one gene’s expression. 

***t***: Moderated t-statistic[^2].

***B***: B-statistic or log-odds that the gene is differentially expressed[^2].


### Acknowledgements
GEII database is funded by XXX. 


[^1]: Michael Love, Simon Anders and Wolfgang Huber. Beginner’s guide to using the DESeq2 package. May 13, 2014.
[^2]: Gordon K. Smyth, Matthew Ritchie, Natalie Thorne, James Wettenhall and Wei Shi. limma: Linear Models for Microarray Data User’s Guide. 3 April 2010.
