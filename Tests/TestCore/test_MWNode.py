from unittest import TestCase
from typing import Any
from Core.MWNode import MWData, MWStorageNode, MWRequestNode
from Tests.stabs.StabData import Stab


class TestMWNodeJSON(TestCase):

    def test_add_len(self):
        Stab.root.add(Stab.node_1)
        Stab.root.add(Stab.node_2)
        Stab.node_2.add(Stab.node_3)
        assert len(Stab.root.folders) == 2

    def test_add_links_walk(self):
        links = []

        def add_links(node: MWStorageNode) -> None:
            links.append(node.node_data.url)

        Stab.root.walk(add_links)
        assert links == Stab.stub_links

    def test_grow_root_from_JSON(self):
        # given
        result = Stab.stub_json["result"]
        data = MWData(result["url"], result["folders"])
        root_node_json = MWStorageNode(result["name"], data)
        root_node_json.files = result["models"]

        # when
        root_node_json.grow_json()

        # then
        assert [x for x in root_node_json.folders] == ["Семейства (временное)", "Фасады (пример)"]

    def test_grow_root_from_server(self):
        # given
        base_url_rsp: str = "http://srvrvt22/RevitServerAdminRESTService2022/AdminRESTService.svc/"
        result = Stab.stub_responses[base_url_rsp + "|Омск.временная/contents"]
        data = MWData(base_url_rsp, f"{base_url_rsp}|{result['Path']}/contents")
        root_node_json = MWRequestNode(result["Path"], data)
        root_node_json.files = result["Models"]

        # when
        def get_resp_from_url(url: str) -> {str: Any}:
            result_data = Stab.stub_responses[url]
            return result_data
        root_node_json.grow_server(get_resp_from_url, f"{base_url_rsp}|{result['Path']}/contents")

        # then
        assert [x for x in root_node_json.folders] == ["Семейства (временное)", "Фасады (пример)"]


if __name__ == '__main__':
    test = TestMWNodeJSON()
    test.test_grow_root_from_server()
