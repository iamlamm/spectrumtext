from typing import List, Tuple, Union
from .pychroma import Pychroma
from .exceptions import ColorError

ColorInput = Union[str, Tuple[str, Union[str, Tuple[int, int, int]]]]


class Printer:
    @staticmethod
    def print_colored(
        text: str, color: Union[str, Tuple[int, int, int]], background: bool = False
    ) -> None:
        try:
            print(Pychroma.colored_text(text, color, background))
        except ColorError as e:
            print(f"Warning: {str(e)}. Printing without color.")
            print(text)
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}. Printing without color.")
            print(text)

    @staticmethod
    def print_rainbow(text: str) -> None:
        rainbow_colors = [
            "#FF0000",
            "#FF7F00",
            "#FFFF00",
            "#00FF00",
            "#0000FF",
            "#8B00FF",
        ]
        for i, char in enumerate(text):
            color = rainbow_colors[i % len(rainbow_colors)]
            print(Pychroma.colored_text(char, color), end="")
        print()

    @staticmethod
    def print_multi_colored(*args: ColorInput) -> None:
        print(Printer.format_multi_colored(*args))

    @staticmethod
    def format_multi_colored(*args: ColorInput) -> str:
        result = []
        default_color = "\033[0m"  # Default to reset color
        for arg in args:
            if isinstance(arg, tuple):
                text, color = arg
            else:
                text, color = arg, default_color
            try:
                result.append(Pychroma.colored_text(str(text), color))
            except ColorError as e:
                print(f"Warning: {str(e)}. Using default color for '{text}'.")
                result.append(str(text))
            except Exception as e:
                print(f"An unexpected error occurred: {str(e)}. Using default color for '{text}'.")
                result.append(str(text))
        return " ".join(result)
