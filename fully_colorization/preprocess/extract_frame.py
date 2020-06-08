import argparse
import os
import subprocess
import sys
sys.path.append('..')
from pathlib import Path
from pytorch_pwc.utils import get_names


def extract_video_frames(input_path, output_path):
    path = Path(input_path)

    # Make a folder for the frames, if the folder does not already exist

    subprocess.run(
        [
            "ffmpeg",
            "-i",
            "{}".format(path.as_posix()),
            "{}".format(
                Path(os.path.join(output_path, path.stem + "_%06d.jpg")).as_posix()
            ),
        ]
    )


def parse_args(args):
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        "--input-path",
        dest="input_path",
        help="Path to an MP4 video file",
        type=str,
        required=True,
    )
    arg_parser.add_argument(
        "--output-path",
        default='frames',
        help="Path to an MP4 video file",
        type=str,
        required=True,
    )
    return arg_parser.parse_args(args)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    os.makedirs(args.output_path, exist_ok=True)
    files = get_names(args.input_path)
    for file_path in files:
        extract_video_frames(file_path, args.output_path)
