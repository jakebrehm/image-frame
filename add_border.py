import argparse
import os
from typing import Optional

from PIL import Image
from tqdm import tqdm


def validate_file(filepath: str) -> str:
    """Determine if the specified filepath is a valid file.
    
    Passes the filepath back through if it is valid, and raises an exception
    if it is not.
    """

    # Attempt to open the file
    try:
        Image.open(filepath, "r")
    except IOError:
        raise argparse.ArgumentTypeError(
            "The specified filepath does not lead to a valid file."
        )
    # Return the filepath if there were no issues
    return filepath


def add_border(
        input_filepath: str,
        output_filepath: Optional[str] = None,
        mode: str = "RGB",
        color: str = "black",
        duration: int = 30,
        padding: int = 10,
        disable_tqdm: bool = False,
    ) -> None:
    """Adds a colored border to the provided file.
    
    Duration is the number of milliseconds between each frame, which defaults
    to 30.
    """

    # Read the contents of the file at the specified input filepath
    original_image = Image.open(input_filepath)

    # Return an error for invalid arguments
    if (original_image.n_frames > 1) and not duration:
        return ValueError("A duration value must be specified for video files.")

    # Get the dimensions of the original file
    original_size = original_image.size

    # Calculate the dimensions of the new file by adding padding
    new_size = tuple(dimension+(2*padding) for dimension in original_size)

    # The position of the original image should be shifted to the bottom right
    top_left_coordinates = (padding, padding)

    # Iterate through each frame and add the colored border to each one
    new_frames = []
    frames = range(original_image.n_frames)
    for frame_number in tqdm(frames, unit="frames", disable=disable_tqdm):
        original_image.seek(frame_number)
        new_frame = Image.new(mode, new_size, color)
        new_frame.paste(original_image, box=top_left_coordinates)
        new_frames.append(new_frame)
    
    # Construct the output filename if one was not provided
    if not output_filepath:
        input_filename, input_extension = os.path.splitext(input_filepath)
        output_filepath = f"{input_filename}-out{input_extension}"
    
    # Save the output file
    if len(new_frames) > 1:
        new_frames[0].save(
            output_filepath,
            append_images=new_frames[1:],
            save_all=True,
            duration=duration,
        )
    else:
        new_frames[0].save(output_filepath)


if __name__ == "__main__":

    # Initialize the command line argument parser
    parser = argparse.ArgumentParser()

    # Add command line argument for input filepath
    parser.add_argument(
        "-i",
        "--input",
        type=validate_file,
        required=True,
        help="Filepath to the image file to add a border to.",
    )
    # Add command line argument for input filepath
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        help=(
            "Filepath to save the output file at. If no name is specified, "
            "'-out' will simply be appended to the input filename."
        )
    )
    # Add command line argument for mode of new image
    parser.add_argument(
        "-m",
        "--mode",
        type=str,
        default="RGB",
        help=(
            "String used by the pillow library to define the type and depth of "
            "a pixel in an image. Defaults to 'RGB', but can be other values "
            "such as 'RGBA' or 'HSV'."
        ),
    )
    # Add command line argument for color of frame
    parser.add_argument(
        "-c",
        "--color",
        type=str,
        default="black",
        help=(
            "The color of the border to add. Can be words such as 'red' or "
            "'green', or can be a hex code. Defaults to 'black'."
        ),
    )
    # Add command line argument for duration
    parser.add_argument(
        "-d",
        "--duration",
        type=int,
        default=30,
        help=(
            "Duration (in milliseconds) between each frame of video-like "
            "images such as gifs. Defaults to 30."
        ),
    )
    # Add command line argument for padding
    parser.add_argument(
        "-p",
        "--padding",
        type=int,
        default=10,
        help=(
            "The padding (in pixels) to add to each side of the image. "
            "Defaults to 10."
        ),
    )
    # Add command line argument for disabling tqdm progress
    parser.add_argument(
        "--disable-progress",
        action="store_true",
        help="Whether or not to disable the progress bar.",
    )

    # Parse and store the provided arguments
    args = parser.parse_args()

    # Add the frame to the image file using the specified parameters
    add_border(
        input_filepath=args.input,
        output_filepath=args.output,
        mode=args.mode,
        color=args.color,
        duration=args.duration,
        padding=args.padding,
        disable_tqdm=args.disable_progress,
    )