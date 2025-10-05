out_put="./train_data"  # define the output folder

python basenji_data_h5.py \
    -p 15 \
    -w 128 \
    -l 196608 \
    -s 0.1 \
    -v chr2,chr18,chr22 \
    -t chr1 \
    --crop 40960 \
    --local \
    -o $out_put \
    ./data/hg19.ml.fa \
    ./data/heart_wigs.txt

python process_h5.py $out_put/h5py/