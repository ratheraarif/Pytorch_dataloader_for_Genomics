

# Genome Sequence Processing Script

*In the same style as [Enformer](https://www.nature.com/articles/s41592-021-01252-x), [AlphaGenome](https://www.biorxiv.org/content/10.1101/2025.06.25.661532v1), and [Borzoi](https://www.nature.com/articles/s41588-024-02053-6)*

this script is designed to prepare genomic datasets and create a PyTorch DataLoader for downstream modeling from Bigwig or narrowpeaks files. While all of these models are originally trained in TensorFlow and use TFRecord files, which are incompatible with PyTorch, this script provides a bridge by enabling PyTorch-ready data pipelines to train deep learning models depending upon your use case. It supports flexible sequence cropping, downsampling, handling of unmappable regions etc.


#### please make sure you have all the packages installed specified in 'requirements.txt'


# Data Preparation Instructions

## Step 1: Download Test Data
Run the Jupyter notebook `step1.ipynb` to download all necessary test data.  
This ensures you have the correct datasets before proceeding.

## Step 2: Generate Training Data
Run the shell script:

```bash
sh generate_data.sh
```

This script will:

1. Create a new folder called `train_data`.
2. Inside `train_data`, generates a folder named `h5py`.
3. The `h5py` folder contains the following datasets:
   - `all_train.h5` – for training
   - `all_valid.h5` – for validation
   - `all_test.h5` – for testing
  
### please remove the -s(downsample) option from `generate_data.sh` to generate all data. I have used -s .1 as a quick test to process the data fast(just for the test)


## options for `basenji_data_h5.py`



| Option                     | Description                                  | Default    |
| -------------------------- | -------------------------------------------- | ---------- |
| `<fasta_file>`             | Input genome FASTA file                      | -          |
| `<targets_file>`           | Input targets / coverage file                | -          |
| `-b`                       | Set blacklist nucleotides to baseline value  | None       |
| `-c, --crop`               | Crop base pairs from each end                | 0          |
| `-d`                       | Round values to given decimals               | None       |
| `-f`                       | Generate cross fold split                    | None       |
| `-g`                       | Genome assembly gaps BED file                | None       |
| `-l`                       | Sequence length                              | 131072     |
| `--limit`                  | Limit to segments overlapping BED file       | None       |
| `--local`                  | Run jobs locally instead of SLURM            | False      |
| `-o`                       | Output directory                             | `data_out` |
| `-p`                       | Number of parallel processes                 | None       |
| `--peaks`                  | Create contigs only from peaks               | False      |
| `--restart`                | Continue progress from midpoint              | False      |
| `-s`                       | Down-sample the segments                     | 1.0        |
| `--st, --split_test`       | Exit after split                             | False      |
| `--stride, --stride_train` | Stride to advance train sequences            | 1.0        |
| `--stride_test`            | Stride to advance valid/test sequences       | 1.0        |
| `-t`                       | Proportion of data for testing               | 0.05       |
| `-w`                       | Sum pool width                               | 128        |
| `-v`                       | Proportion of data for validation            | 0.05       |


## step 3: create pytorch data loaders
##### open the `data_loader.ipynb` for creating the pytorch dataloaders with options for shift augmentation, reverse complement augmentation etc

