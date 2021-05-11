import os
import re
from typing import List, Tuple
from glob import glob


def get_train_files(machine_id: str) -> List[str]:
    fname_lst = glob(
        os.path.join("..", "store", "audios", "train", f"normal_id_{machine_id}_*")
    )
    return fname_lst[:8]


def get_test_files() -> List[str]:
    fname_lst = []
    for machine_id in ["00", "02", "04", "06"]:
        for label in ["normal", "anomaly"]:
            fnames = glob(
                os.path.join(
                    "..",
                    "store",
                    "audios",
                    "test",
                    f"{label}_id_{machine_id}_*",
                )
            )

            fname_lst.append(fnames[0])
            fname_lst.append(fnames[1])

    return fname_lst


def get_support_file(fname: str, folder: str) -> str:
    parts = fname.split(os.path.sep)
    dir_root = os.path.join(parts[0], parts[1], folder, parts[3])
    label, machine_id, audio_id = get_info(parts[4])
    if folder == "images":
        name = f"{label}_id_{machine_id}_0000{audio_id}.png"
    elif folder == "json":
        name = f"{label}_id_{machine_id}_0000{audio_id}.json"
    return os.path.join(dir_root, name)


def get_img(fname: str) -> str:
    return get_support_file(fname, "images")


def get_json(fname: str) -> str:
    return get_support_file(fname, "json")


def get_info(fname: str) -> Tuple[str, str, str]:
    info = re.search(r"(normal|anomaly)_id_(\d{2})_\d{4}(\d{4})", fname)
    label, machine_id, audio_id = info.groups()
    return label, machine_id, audio_id
