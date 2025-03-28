import arcpy
import os

"""
import_vector_to_gdb
Script to import vector data into a geodatabase, specified by the gdb_path variable. This script then reprojects the vector data into the selected coordinate system.
"""

# Set environment settings
gdb_path = r"C:\Users\folder\example.gdb"  # Path to your geodatabase
arcpy.env.workspace = gdb_path
arcpy.env.overwriteOutput = True

# Define the input vector data (Shapefile or other vector format)
input_vector_data = r"C:\Users\folder\Output.shp" # Change filename and location based on this line

# Extract the name of the shapefile (or other vector format) without the extension
input_name = os.path.splitext(os.path.basename(input_vector_data))[0]

# Import the vector data into the geodatabase
output_fc = arcpy.FeatureClassToFeatureClass_conversion(input_vector_data, gdb_path, input_name)

# Reproject the newly added feature class to a coordinate system consistent with the geodatabase
reprojected_fc = os.path.join(gdb_path, input_name + "_reprojected")
reproject_to_cs = arcpy.SpatialReference("NAD 1983 UTM Zone 10N") # Define the coordinate system to reproject to
arcpy.management.Project(output_fc, reprojected_fc, reproject_to_cs)

print(f"Successfully imported {input_name} into {gdb_path}")
