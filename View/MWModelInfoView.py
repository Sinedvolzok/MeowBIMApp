from textual.app import ComposeResult
from textual.widgets import Label, Static, Button
from textual.containers import Vertical, Horizontal
from textual.widgets import MarkdownViewer


model_info = """\
# Markdown Viewer

This is an example of Textual's `MarkdownViewer` widget.


## Features

Markdown syntax and extensions are supported.

- Typography *emphasis*, **strong**, `inline code` etc.
- Headers
- Lists (bullet and ordered)
- Syntax highlighted code blocks
- Tables!

## Tables

Tables are displayed in a DataTable widget.

| Name            | Type   | Default | Description                        |
| --------------- | ------ | ------- | ---------------------------------- |
| `show_header`   | `bool` | `True`  | Show the table header              |
| `fixed_rows`    | `int`  | `0`     | Number of fixed rows               |
| `fixed_columns` | `int`  | `0`     | Number of fixed columns            |
| `zebra_stripes` | `bool` | `False` | Display alternating colors on rows |
| `header_height` | `int`  | `1`     | Height of header row               |
| `show_cursor`   | `bool` | `True`  | Show a cell cursor                 |

"""


class MWModelInfoView(Static):

    def compose(self) -> ComposeResult:
        with Vertical():
            yield Label("Model Info", classes="title")
            yield Label("Information about model", classes="comment")
            yield MarkdownViewer(model_info,
                                 show_table_of_contents=False,
                                 classes="models")
            with Horizontal(classes="buttonsHorizontal"):
                yield Static(classes="spacerHorizontal")
                yield Button("Save Info", classes="button")
