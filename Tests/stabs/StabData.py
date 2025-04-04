from dataclasses import dataclass
from Core.MWNode import MWNode, MWData


@dataclass
class Stab:
    root = MWNode("Root", MWData("\\some\\link", [{"DAT DATA": ""}]))
    node_1 = MWNode("node_1", MWData("\\some\\link\\node_1", [{"DAT DATA": ""}]))
    node_2 = MWNode("node_2", MWData("\\some\\link\\node_2", [{"DAT DATA": ""}]))
    node_3 = MWNode("node_2", MWData("\\some\\link\\node_3", [{"DAT DATA": ""}]))

    stub_links = ["\\some\\link\\node_1",
                  "\\some\\link\\node_2",
                  "\\some\\link\\node_3"]

    stub_json = {
        "timestamp": "02/14/2025, 11:16:10",
        "result": {
            "name": "Омск.временная",
            "url": "http://172.16.22.20/RevitServerAdminRESTService2022/AdminRESTService.svc/",
            "models": ["0001_ИТР_АР_К10-ОСИ_R22.rvt",
                       "0001_ИТР_АР_К11-ОСИ_R22.rvt"],
            "folders": [
                {
                    "name": "Семейства (временное)",
                    "url": "http://172.16.22.20/RevitServerAdminRESTService2022/AdminRESTService.svc/|Омск.временная",
                    "models": [
                        "Файл семейств_Омск_2_АР.rvt"
                    ],
                    "folders": []
                },
                {
                    "name": "Фасады (пример)",
                    "url": "http://172.16.22.20/RevitServerAdminRESTService2022/AdminRESTService.svc/|Омск.временная",
                    "models": [
                        "0001_ИТР_АР_К10-Фасады_R22.rvt",
                        "0001_ИТР_АР_К11-Фасады_R22.rvt",
                        "0001_ИТР_АР_К12-Фасады_R22.rvt",
                        "0001_ИТР_АР_К13-Фасады_R22.rvt",
                        "0001_ИТР_АР_К9-Фасады_R22.rvt"
                    ],
                    "folders": []
                }
            ]
        }
    }

    stub_responses = {
        "http://srvrvt22/RevitServerAdminRESTService2022/AdminRESTService.svc/|Омск.временная/contents":
            {
                "Path": "Омск.временная",
                "DriveFreeSpace": 1483686658048,
                "DriveSpace": 2736399577088,
                "Files": [
                    "0001_ИТР_АР_К10-ОСИ_R22.rvt",
                    "0001_ИТР_АР_К11-ОСИ_R22.rvt"
                ],
                "Folders": [
                    {
                        "HasContents": True,
                        "LockContext": "None",
                        "LockState": 0,
                        "ModelLocksInProgress": "None",
                        "Name": "Семейства (временное)",
                        "Size": 124912719
                    },
                    {
                        "HasContents": True,
                        "LockContext": "None",
                        "LockState": 0,
                        "ModelLocksInProgress": "None",
                        "Name": "Фасады (пример)",
                        "Size": 566651299
                    }
                ],
                "LockContext": "None",
                "LockState": 0,
                "ModelLocksInProgress": "None",
                "Models": [

                ]
            },
        "http://srvrvt22/RevitServerAdminRESTService2022/AdminRESTService.svc/|Омск.временная|Семейства (временное)/contents":
            {
                "Path": "Омск.временная\\Семейства (временное)",
                "DriveFreeSpace": 1483686658048,
                "DriveSpace": 2736399577088,
                "Files": [

                ],
                "Folders": [

                ],
                "LockContext": "None",
                "LockState": 0,
                "ModelLocksInProgress": "None",
                "Models": [
                    {
                        "LockContext": "None",
                        "LockState": 0,
                        "ModelLocksInProgress": "None",
                        "ModelSize": 119250751,
                        "Name": "Файл семейств_Омск_2_АР.rvt",
                        "ProductVersion": 12,
                        "SupportSize": 5661968
                    }
                ]
            },
        "http://srvrvt22/RevitServerAdminRESTService2022/AdminRESTService.svc/|Омск.временная|Фасады (пример)/contents":
            {
                "Path": "Омск.временная\\Фасады (пример)",
                "DriveFreeSpace": 1483686658048,
                "DriveSpace": 2736399577088,
                "Files": [

                ],
                "Folders": [

                ],
                "LockContext": "None",
                "LockState": 0,
                "ModelLocksInProgress": "None",
                "Models": [
                    {
                        "LockContext": "None",
                        "LockState": 0,
                        "ModelLocksInProgress": "None",
                        "ModelSize": 69379301,
                        "Name": "0001_ИТР_АР_К10-Фасады_R22.rvt",
                        "ProductVersion": 12,
                        "SupportSize": 6819076
                    },
                    {
                        "LockContext": "None",
                        "LockState": 0,
                        "ModelLocksInProgress": "None",
                        "ModelSize": 59815809,
                        "Name": "0001_ИТР_АР_К11-Фасады_R22.rvt",
                        "ProductVersion": 12,
                        "SupportSize": 6338969
                    },
                    {
                        "LockContext": "None",
                        "LockState": 0,
                        "ModelLocksInProgress": "None",
                        "ModelSize": 51890152,
                        "Name": "0001_ИТР_АР_К12-Фасады_R22.rvt",
                        "ProductVersion": 12,
                        "SupportSize": 4970028
                    },
                    {
                        "LockContext": "None",
                        "LockState": 0,
                        "ModelLocksInProgress": "None",
                        "ModelSize": 139632054,
                        "Name": "0001_ИТР_АР_К13-Фасады_R22.rvt",
                        "ProductVersion": 12,
                        "SupportSize": 12342832
                    },
                    {
                        "LockContext": "None",
                        "LockState": 0,
                        "ModelLocksInProgress": "None",
                        "ModelSize": 190031489,
                        "Name": "0001_ИТР_АР_К9-Фасады_R22.rvt",
                        "ProductVersion": 12,
                        "SupportSize": 25431589
                    }
                ]
            }
    }
