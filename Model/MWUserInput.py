from Services.MWDataService import fetch_data
from dataclasses import dataclass, field
# import asyncio


@dataclass
class Input:
    server: str = field(default="2022")
    project: str = field(default="Солнечный")
    # local_folder: Path

    SERVER_NAME_ID_DICT: dict[str: str] = field(init=False, repr=False, default_factory=lambda: {"2022": "srvrvt22"})

    @property
    def base_url(self) -> str:
        return f"http://{self.SERVER_NAME_ID_DICT[self.server]}//RevitServerAdminRESTService{self.server}/AdminRESTService.svc/"

    @property
    def project_list(self) -> [str]:
        # raw_data = fetch_data(f"{self.base_url}|/contents")
        # folders = [x["Name"] for x in raw_data['Folders']]
        return ["Солнечный", "Дождливый", "Ветренный"]

    @property
    def resp_url(self) -> str:
        return f"{self.base_url}|{self.project}/contents"
