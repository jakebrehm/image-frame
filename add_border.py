import os
from typing import Optional

from PIL import Image
from tqdm import tqdm


def add_border(
        input_filepath: str,
        output_filepath: Optional[str] = None,
        mode: str = "RGB",
        color: str = "black",
        duration: int = 30,
        padding: int = 10,
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
    for frame_number in tqdm(range(original_image.n_frames)):
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
    add_border(input_filepath="test.png")