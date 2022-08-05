library(tidyverse)
library(parallel)

data_type <- c("hGEuIInf", "hGEuISti") # infection and stimulation

for(this_type in data_type){
	# this_type <- "hGEuIInf"
	print(this_type)

	file_csvs <- list.files(paste0("../reference_data/GEII_updated/", this_type), full.names = T)
	df_all <- lapply(file_csvs, read_csv, col_types = cols(.default = "c")) 
	df_all <- bind_rows(df_all)
	df_all <- df_all %>% select(-X1)
	df_all <- df_all[!(is.na(df_all$entrezID) & is.na(df_all$gene_symbol)),] # remove na values

	dir.create(paste0("../data_entrez_id/", this_type))
	entrez_id_all <- unique(df_all$entrezID)
	entrez_id_all <- entrez_id_all[!is.na(entrez_id_all)]
	lapply(entrez_id_all, function(x){
		file_out <- paste0("../data_entrez_id/", this_type, "/", x, ".csv")
		if(!file.exists(file_out)){
			print(file_out)
			write_csv(df_all[which(df_all$entrezID==x),], file_out)
		}
	})

	dir.create(paste0("../data_gene_symbol/", this_type))
	gene_symbol_all <- unique(df_all$gene_symbol)
	gene_symbol_all <- gene_symbol_all[!is.na(gene_symbol_all)]
	gene_symbol_all <- sort(gene_symbol_all)
	gene_symbol_all <- gsub("/", "_", gene_symbol_all)
	lapply(gene_symbol_all, function(x){
		file_out <- paste0("../data_gene_symbol/", this_type, "/", x, ".csv")
		if(!file.exists(file_out)){
			print(file_out)
			write_csv(df_all[which(df_all$gene_symbol==x),], file_out)
		}
	})
}

