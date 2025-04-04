from textual.app import App, ComposeResult
from textual.containers import Vertical, Horizontal
from View.MWAppHeader import MWAppHeader
from View.MWRSFoldersView import MWRSFoldersView
from View.MWLocalModelsView import MWLocalModelsView
from View.MWModelInfoView import MWModelInfoView


class MWApp(App):

    CSS_PATH = "grid_layout_auto.tcss"

    def compose(self) -> ComposeResult:
        with Vertical(id="app-rows"):
            yield MWAppHeader(classes="header")
            with Horizontal(classes="column"):
                yield MWRSFoldersView(id="foldersVertical")
                yield MWLocalModelsView(id="modelsVertical")
                yield MWModelInfoView(id="modelInfoVertical")


if __name__ == '__main__':
    app = MWApp()
    app.run()