out_put="./outputs2"  # define the output folder

python3 basenji_data_h5.py \
    -p 15 \
    -w 128 \
    -l 196608 \
    -v chr2,chr18,chr22 \
    -t chr1 \
    --crop 40960 \
    --local \
    -o $out_put \
    ./hg19.ml.fa \
    ./heart_wigs.txt

python3 process_h5.py out_put/h5py/