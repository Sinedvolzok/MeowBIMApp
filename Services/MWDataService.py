from returns.result import Result, Success, Failure
from typing import Final, Any
import os
import requests
import uuid


class OutdatedDataError(Exception):
    def __init__(self, message="Storage data has expired!"):
        super().__init__(message)

    def __str__(self):
        return f"{self.message}"


class MWUserOperation:
    USER_NAME: Final[str]
    USER_COMPUTER_NAME: Final[str]
    OPERATION_GUID: Final[str]

    def __init__(self):
        self.USER_NAME = os.environ.get('USERNAME')
        self.USER_COMPUTER_NAME = os.environ.get('COMPUTERNAME')
        self.OPERATION_GUID = str(uuid.uuid4())


def fetch_data(url: str) -> {str: Any}:
    user_operation: MWUserOperation = MWUserOperation()
    r = requests.get(url, headers={
        "User-Name": user_operation.USER_NAME,
        "User-Machine-Name": user_operation.USER_COMPUTER_NAME,
        "Operation-GUID": user_operation.OPERATION_GUID
    })
    # if r:
    #     print("Success!")
    # else:
    #     raise Exception(f"Non-success status code: {r.status_code}")
    # raw_data = r.json()
    return raw_data


def update_storage(new_data, storage_file_path):
    with open(storage_file_path, 'w', encoding='utf-8') as f:
        result = {"time_stamp": datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), "result": new_data}
        json.dump(result, f, ensure_ascii=False, indent=4)


def fetch_data_from_storage(file_path) -> ([str], [str]):
    with open(file_path, "r", encoding='utf-8') as f:
        raw_data = json.load(f)
        result = raw_data["result"]
        storage_date = raw_data["time_stamp"]
        if datetime.now() - timedelta(days=1) < datetime.strptime(storage_date, "%m/%d/%Y, %H:%M:%S"):
            return result
        else:
            raise OutdatedDataError


def fetch_json_from(json_dict: {str: str}) -> ([str], [str]):
    folders, files = ([x for x in json_dict["children"]], [x for x in json_dict["files"]])
    return folders, files
