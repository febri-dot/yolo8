# from roboflow import Roboflow

# # Initialize Roboflow with your API key
# rf = Roboflow(api_key="")  # 👈 Replace with your actual API key

# # Access the project and version
# project = rf.workspace("buv-team").project("payload-detection")
# dataset = project.version(7).download("yolov8")

from roboflow import Roboflow

rf = Roboflow(api_key="")
project = rf.workspace("buv-team").project("payload-detection")
dataset = project.version(7).download("yolov8", location="datasets")

