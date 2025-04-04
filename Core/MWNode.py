from typing import Final
from typing import Protocol
from typing import Final, Self
from typing import TypeAlias
from typing import Callable, Any
from abc import ABC, abstractmethod
from dataclasses import dataclass
import uuid

MWNodeWalkAction: TypeAlias = Callable[[Self], None]
MWNodeGetDataAction: TypeAlias = Callable[[str], {str: Any}]
URL: TypeAlias = str


@dataclass
class MWData:
    url: URL
    raw_data: Any

    def __str__(self):
        return f"Data: ( {self.url}: {self.raw_data} )"


@dataclass
class MWFile:
    name: str


class MWNode(ABC):
    name: str
    node_id: uuid
    parent: Self | None
    node_data: MWData
    files: list[MWFile] | None
    folders: dict[str: Self] | None

    __parent_id_set = set()

    def __init__(self,
                 name: str,
                 node_data: MWData,
                 parent: Self | None = None,
                 files: list[MWFile] | None = None,
                 folders: dict[str, Self] | None = None
                 ):
        self.name = name
        self.node_id = uuid.uuid4()
        self.parent = parent
        self.node_data = node_data
        self.files = files if files is not None else list()
        self.folders = folders if folders is not None else dict()

    def add(self, child: Self) -> None:
        self.folders[child.name] = child

    def walk(self, action: MWNodeWalkAction) -> None:
        if not (self.node_id in MWNode.__parent_id_set):
            MWNode.__parent_id_set.add(self.node_id)
            for child_name in self.folders:
                action(self.folders[child_name])
                self.folders[child_name].walk(action)

    def __str__(self):
        return f"{self.name}: {self.node_data}< children - {len(self.folders)} files: {len(self.files)}"


class MWStorageNode(MWNode):
    __parent_id_set = set()

    def grow_json(self) -> None:
        if not (self.node_id in MWStorageNode.__parent_id_set):
            MWStorageNode.__parent_id_set.add(self.node_id)
            folders_data = self.node_data.raw_data
            for folder_data in folders_data:
                child_data = MWData(folder_data["url"], folder_data["folders"])
                child_node = MWStorageNode(folder_data["name"], child_data, self)
                child_node.files = folder_data["models"]
                self.add(child_node)
                child_node.grow_json()


class MWRequestNode(MWNode):
    __parent_id_set = set()

    def grow_server(self, request: MWNodeGetDataAction, request_url: str) -> None:
        if not (self.node_id in MWRequestNode.__parent_id_set):
            MWRequestNode.__parent_id_set.add(self.node_id)
            request_data = request(request_url)
            folders_data = request_data["Folders"]
            child_url = f"{request_url.replace('/contents', '')}"
            self.files = [x["Name"] for x in request_data["Models"]]
            for folder_data in folders_data:
                request_url = f"{child_url}|{folder_data['Name']}/contents"
                child_data = MWData(child_url, request_url)
                child_node = MWRequestNode(folder_data["Name"], child_data, self)
                self.add(child_node)
                child_node.grow_server(request, request_url)
