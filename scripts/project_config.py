from pathlib import Path


class Config:

  Root_Path = Path("./")
  Repository = "https://github.com/Caphace-Ethan/Breast-Cancer-Diagnosis"
  Data_path = Root_Path / "data"
  Image_path = Data_path / "img"

  scripts_path = Root_Path / "scripts"



