import shutil
import os
from glob import glob
from tqdm import tqdm




# scenes = ["scan37", "scan40", "scan55", "scan63", "scan65", "scan69", "scan83", "scan97"]
scenes = ["bear", "clock", "dog", "durian", "jade", "man", "sculpture", "stone"]
out_dir = "/homes/sanskar/data/outputs/nvdiffrecMC/bmvs/"

for scene in scenes:
    results = "out/" + scene + "/validate/val_"
    scene_dir = out_dir + scene + "/nvs/"
    os.makedirs(scene_dir, exist_ok=True)
    for i in tqdm(range(50)):
        in_file = results + str(i).zfill(6) + "_opt.png"
        out_file = scene_dir + "pr_image_" + str(i).zfill(4) + ".png"
        try:
            shutil.copyfile(in_file, out_file)
        except:
            pass


# scenes = ["air_baloons", "chair", "hotdog", "jugs"]
# out_dir = "/homes/sanskar/data/outputs/nvdiffrec/synthetic/"

# for scene in scenes:
#     results = "out_synth/nerf_" + scene + "/validate/relight_val_"
#     scene_dir = out_dir + scene + "/relight/"
#     os.makedirs(scene_dir, exist_ok=True)
#     for i in tqdm(range(600)):
#         in_file = results + str(i).zfill(6) + "_opt_hdr.npy"
#         out_file = scene_dir + "pr_image_" + str(i).zfill(4) + ".npy"
#         shutil.copyfile(in_file, out_file)


#     results = "out_synth/nerf_" + scene + "/validate/nvs_val_"
#     scene_dir = out_dir + scene + "/nvs/"
#     os.makedirs(scene_dir, exist_ok=True)
#     for i in tqdm(range(200)):
#         in_file = results + str(i).zfill(6) + "_opt.png"
#         out_file = scene_dir + "pr_image_" + str(i).zfill(4) + ".png"
#         shutil.copyfile(in_file, out_file)


# scenes = ["antman", "apple", "chest", "gamepad", "tpiece", "porcelain_mug", "ping_pong_racket", "wood_bowl"]
# out_dir = "/homes/sanskar/data/outputs/nvdiffrec/objrel/"

# for scene in scenes:
#     results = "out_lock/" + scene + "/validate/relight_val_00000"
#     scene_dir = out_dir + scene + "/relight/"
#     os.makedirs(scene_dir, exist_ok=True)
#     for i in range(9):
#         in_file = results + str(i) + "_opt_hdr.npy"
#         out_file = scene_dir + "pr_image_" + str(i).zfill(4) + ".npy"
#         shutil.copyfile(in_file, out_file)


#     results = "out_lock/" + scene + "/validate/nvs_val_00000"
#     scene_dir = out_dir + scene + "/nvs/"
#     os.makedirs(scene_dir, exist_ok=True)
#     for i in range(3):
#         in_file = results + str(i) + "_opt.png"
#         out_file = scene_dir + "pr_image_" + str(i).zfill(4) + ".png"
#         shutil.copyfile(in_file, out_file)
