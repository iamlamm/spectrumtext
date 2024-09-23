import re
from typing import Tuple, Union
from .exceptions import ColorError


class Pychroma:
    @staticmethod
    def hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
        hex_color = hex_color.lstrip("#")
        if not re.match(r"^[0-9A-Fa-f]{6}$", hex_color):
            raise ColorError(f"Invalid hex color code: {hex_color}")
        return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))

    @staticmethod
    def validate_rgb(rgb: Tuple[int, int, int]) -> None:
        if not all(isinstance(c, int) and 0 <= c <= 255 for c in rgb):
            raise ColorError(
                f"Invalid RGB values: {rgb}. Each value should be an integer between 0 and 255."
            )

    @staticmethod
    def colored_text(
        text: str, color: Union[str, Tuple[int, int, int]], background: bool = False
    ) -> str:
        try:
            if isinstance(color, str):
                if color.startswith("\033"):
                    return f"{color}{text}\033[0m"
                rgb = Pychroma.hex_to_rgb(color)
            else:
                Pychroma.validate_rgb(color)
                rgb = color
            color_code = f"\033[{'48' if background else '38'};2;{rgb[0]};{rgb[1]};{rgb[2]}m"
            return f"{color_code}{text}\033[0m"
        except ColorError as e:
            print(f"Warning: {str(e)}. Using default color.")
            return text
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}. Using default color.")
            return text
