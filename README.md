# GEOG-428-BeSpoke-Solutions
Python scripts developed by Team BeSpoke Solutions as part of deliverables for GEOG 428: Advanced Topics in GIS at the University of Victoria. Scripts written by Jenni Buskas with help from Oliver James and Vanessa Clark.

## Setup:
To run these scripts, you will need ArcGIS Pro installed on the same computer on which you are running the scripts. Follow these instructions for first-time setup of an ArcPy environment: https://pro.arcgis.com/en/pro-app/3.3/arcpy/get-started/installing-arcpy.htm
When ArcGIS Pro uses licensing through the organization, the available product level and extensions are set by your account and available automatically from arcpy.
More information can be found in the ArcGIS Pro help documentation: https://pro.arcgis.com/en/pro-app/latest/arcpy/geoprocessing_and_python/using-tools-in-python.htm

## Script Catalog:
import_vector_to_gdb
Imports vector data into a geodatabase specified by the gdb_path variable. This script then reprojects the vector data into a specified coordinate system to ensure projection harmony.

create_network_dataset
Creates and builds a network dataset from a feature dataset. A network dataset forms the basis of the Network Analyst tool.

service_areas
Uses the Network Analyst, Service Areas tool to create a service area from a network dataset.

cost_matrix
Uses the Network Analyst, OD Cost Matrix tool to create a cost matrix showing costs between origins and destinations.
