import os
import glob
import json
from tqdm import tqdm
rank = os.environ.get('NODE_RANK')

datapath = f'/f_ndata/G/dataset/panda/full_shard_64/part-{rank}'

tmp_json_files = [x for x in glob.glob(datapath + "/*.json")]
success_num = []
for tmp in tqdm(tmp_json_files):
    tmp_json = json.load(open(tmp))
    success_num.append(tmp_json['successes'])
    if tmp_json['successes'] == 0:
        os.remove(tmp)
        print(f"Remove {tmp}")
    # print(tmp_json)
    # break
print(success_num)