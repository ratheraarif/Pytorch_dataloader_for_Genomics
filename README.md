# Genome Sequence Processing Script

This script computes model sequences from the genome and extracts DNA coverage values.  
It requires a FASTA file and a targets file.

## Usage




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

1. Create a new folder called `output`.
2. Inside `output`, generate a folder named `h5py`.
3. The `h5py` folder contains the following datasets:
   - `train` – for training
   - `valid` – for validation
   - `test` – for testing
