import h5py
import numpy as np
import glob
import sys
import os
from natsort import natsorted

data_dir = sys.argv[1] if len(sys.argv) > 1 else "."

for pattern, output in [("train*", "all_train"), ("valid*", "all_valid"), ("test*", "all_test")]:
    files = natsorted(glob.glob(f"{data_dir}/{pattern}.h5"))
    if not files:
        continue
    
    data_list, target_list = [], []
    for f in files:
        with h5py.File(f, 'r') as h5f:
            data_list.append(h5f["sequence"][:])
            target_list.append(h5f["target"][:])
    
    with h5py.File(f"{data_dir}/{output}.h5", "w") as h5f_out:
        h5f_out.create_dataset("sequence", data=np.concatenate(data_list))
        h5f_out.create_dataset("target", data=np.concatenate(target_list))
    
    print(f"Created {output}.h5 from {len(files)} files")
    
    # Remove original files
    for f in files:
        os.remove(f)
        print(f"  Removed {os.path.basename(f)}")
    
print("\nCleanup complete!")