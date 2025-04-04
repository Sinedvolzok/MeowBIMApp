from textual.app import App, ComposeResult
from textual.widgets import Label, Static
from textual.containers import Vertical, Horizontal


class MWAppHeader(Static):
    LOGO = """
          ▄▀▄       ▄▀▄
         ▄█░░█▄▄▄▄▄█░░█▄
         █░░░░░░░░░░░░░█
     ▄▄  █░░  █░░░  █░░█  ▄▄
    █░░█ █░░▄▄▄░▄░▄▄▄░░█ █░░█
    """

    LOGO_TEXT = """
    █▄ ▄█ █▀▀ ▄▀▀▀▄ █  █  █
    █▀▄▀█ █▀▀ █   █ █  █  █
    █   █ █▄▄ ▀▄▄▄▀ ▀▄▄▀▄▄▀
    """

    def compose(self) -> ComposeResult:
        with Vertical():
            with Horizontal():
                yield Label(self.LOGO, id="logo")
                yield Label(self.LOGO_TEXT, id="logoText")
                with Vertical(id="logoDescript"):
                    yield Label("Manager's Environment for Organizing Workflow", classes="title")
                    yield Label("Create Local Copies Run Revit Models And Run Dynamo Scrips", classes="comment")
