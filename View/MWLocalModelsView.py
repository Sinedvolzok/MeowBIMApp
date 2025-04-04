from textual.app import ComposeResult
from textual.widgets import Label, Static, Button, Input
from textual.containers import Vertical, Horizontal
from View.MWFilesListView import MWFilesListView


class MWLocalModelsView(Static):

    def compose(self) -> ComposeResult:
        with Vertical():
            yield Label("Local Models", classes="title")
            yield Label("Paste path to folder were you store local models", classes="comment")
            yield Input(placeholder="D:\\Exemple\\Path", classes="input")
            yield Label("Apply actions and inspect models info", classes="comment")
            yield MWFilesListView(classes="models")
            with Horizontal(classes="buttonsHorizontal"):
                yield Static(classes="spacerHorizontal")
                yield Button("Run Actions", classes="button")
