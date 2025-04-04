from textual import on
from textual.app import ComposeResult
from textual.widgets import Label, Static, Button, Select
from textual.widgets import LoadingIndicator
from textual.containers import Vertical, Horizontal
from textual.widgets import DirectoryTree # Convert to ServerFolderTree
from Model.MWUserInput import Input
# import asyncio


class MWSelectProject(Select):
    user_input = Input()
    projects = []

    def __init__(self):
        super().__init__([], classes="input")
        self.options = None
        self.prompt = "Select Project"

    def add_data(self) -> None:
        self.projects = self.user_input.project_list
        self.options = [(v, v) for v in self.projects]


class MWSelectRevit(Select):
    # user_input = Input()
    revit_versions = ["2019", "2020", "2021", "2022"]

    def __init__(self):
        super().__init__([(v, v) for v in self.revit_versions], classes="input")
        self.prompt = "Select Revit"


class MWRSFoldersView(Static):
    # user_input = Input()
    # revit_versions = user_input.SERVER_NAME_ID_DICT.keys()
    # projects = user_input.project_list
    # projects = ["test", "Солнечный", "Омск-1", "Омск-2"]

    def compose(self) -> ComposeResult:
        with Vertical():
            yield Label("Server Folders", classes="title")
            with Horizontal(id="revitAndProject"):
                with Vertical():
                    yield Label("Select Revit Version", classes="comment")
                    yield MWSelectRevit()
                with Vertical(id="projects"):
                    yield Label("Select project", classes="comment")
                    yield MWSelectProject()
            yield Label("Select files to create local copy", classes="comment")
            yield DirectoryTree("./", classes="models")
            with Horizontal(classes="buttonsHorizontal"):
                yield Static(classes="spacerHorizontal")
                yield Button("Save Local", classes="button")

    @on(MWSelectRevit.Changed)
    def reload_projects(self) -> None:
        self.query_one(MWSelectProject).loading = True
        self.get_projects()

    def get_projects(self) -> None:
        sel = self.query_one(MWSelectProject)
        sel.add_data()
        sel.loading = False
