from textual.app import ComposeResult
from textual.widgets import ListItem, ListView, Label


class MWFilesListView(ListView):

    files = ["24.006-Р_ИТР_АР_С-1_R22_deniskozlov1.rvt",
             "24.006-Р_ИТР_АР_С-2_R22_deniskozlov1.rvt",
             "24.006-Р_ИТР_АР_С-3_R22_deniskozlov1.rvt",
             "24.006-Р_ИТР_АР_С-4_R22_deniskozlov1.rvt",
             "24.006-Р_ИТР_АР_С-5_R22_deniskozlov1.rvt",
             "24.006-Р_ИТР_АР_С-6_R22_deniskozlov1.rvt",
             "24.006-Р_ИТР_АР_С-7_R22_deniskozlov1.rvt",
             "24.006-Р_ИТР_АР_С-8_R22_deniskozlov1.rvt",
             "24.006-Р_ИТР_АР_С-9_R22_deniskozlov1.rvt"]

    _items: list[ListItem] = []

    def __init__(self, classes: str | None):
        super().__init__()
        self.classes = classes

    def compose(self) -> ComposeResult:
        for file in self.files:
            self._items.append(ListItem(Label(file)))
        return self._items