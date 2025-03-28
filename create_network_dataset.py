import arcpy
from arcpy import na

"""
create_network_dataset
Creates and builds a network dataset from a feature dataset.
"""

# Set variables
gdb_path = r"C:\folder\example.gdb"  # Path to your geodatabase
# Set environment - change path to location of geodatabase where network analysis will be performed
arcpy.env.workspace = gdb_path
arcpy.env.overwriteOutput = True
feature_dataset_path = f"{gdb_path}\\Paths_FeatureD"  # Path to feature dataset
source_features = ["Paths_Reprojected", "Feature_Class_2"]  # Source feature classes to include from the feature dataset
network_name = "Paths_Network_Name"  # Name and path for the network dataset

# Create Network Dataset
arcpy.na.CreateNetworkDataset(feature_dataset_path, network_name, source_features, "NO_ELEVATION")

# Build Network Dataset
arcpy.na.BuildNetwork(gdb_path)

print("Network Dataset created successfully!")
