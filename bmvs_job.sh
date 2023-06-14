#!/bin/bash
#SBATCH --job-name=nvdiffrecmc
#SBATCH -p g24
#SBATCH --gres=gpu:1
#SBATCH --qos=normal
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --output="./logs/man-%a-%j.log"
#SBATCH --open-mode=append

scenes=(
bear
clock
dog
durian
jade
man
sculpture
stone
# 37
# 40
# 55
# 63
# 65
# 69
# 83
# 97
)

scene="man"
# scene="${scenes[$SLURM_ARRAY_TASK_ID]}"
###aaa#SBATCH --array="0-3"

echo "====== Scene: $scene ======"

python train.py --config configs/${scene}.json

# python train.py --nvs true --ref_mesh "/homes/sanskar/data/bmvsdtu/llff_data/$scene/" --out_dir $scene --bbox /homes/sanskar/data/bmvsdtu/$scene/neus_mesh.ply

# python train.py --nvs true --ref_mesh "/homes/sanskar/data/nvdiffrec/input/$scene/" --out_dir $scene --bbox /homes/sanskar/data/bmvsdtu/$scene/neus_mesh.ply
