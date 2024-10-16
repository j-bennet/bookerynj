from datetime import datetime

from pydantic import BaseModel, FilePath


class ConfigFile(BaseModel):
    created_at: datetime
    file_path: FilePath


if __name__ == "__main__":
    # good
    config_file = ConfigFile(created_at=datetime.now(), file_path="example.py")
    # still works
    config_file = ConfigFile(created_at="2024-01-01", file_path="example.py")

    # pydantic_core._pydantic_core.ValidationError: 1 validation error for ConfigFile
    # file_path
    #   Path does not point to a file [type=path_not_file, input_value='not a file', input_type=str]
    bad_config_file = ConfigFile(created_at=datetime.now(), file_path="not a file")
