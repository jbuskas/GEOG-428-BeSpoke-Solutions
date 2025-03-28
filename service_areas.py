import arcpy
from arcpy import na

# Set environment - change path to location of geodatabase where network analysis will be performed
arcpy.env.workspace = r"C:\folder\example.gdb"
arcpy.env.overwriteOutput = True

def create_service_area(network_dataset, facilities, service_area_output):
    """
    Simple function to create a service area from a network dataset.
    
    Parameters:
    network_dataset: Path to your network dataset
    facilities: Path to facilities points from which the service area will be calculated
    service_area_output: Path to service area output layer (where you wish to store it)
    """
    # Create a new Service Area layer
    service_area_layer = arcpy.na.MakeServiceAreaLayer(
        in_network_dataset=network_dataset,
        out_network_analysis_layer="ServiceArea",
        impedance_attribute="Length",  # Change to "Length" for distance-based analysis
        travel_from_to="TRAVEL_FROM",
        default_break_values="15.0 45.0 75.0",  # Define service area breaks in minutes or distance units
        polygon_type="DETAILED_POLYS",
    )

    # Get the layer object from the result object
    layer_object = service_area_layer.getOutput(0)

    # Get the sublayer names
    sublayers = arcpy.na.GetNAClassNames(layer_object)
    facilities_layer_name = sublayers["Facilities"]

    # Add selected facilities to the service area layer
    # AddLocations(in_network_analysis_layer, sub_layer, in_table, {field_mappings}, {search_tolerance})
    arcpy.na.AddLocations(layer_object, facilities_layer_name, facilities, "", "")

    # Solve the service area analysis
    arcpy.na.Solve(layer_object)

    # Save the solved service area layer as a layer file on disk
    layer_object.saveACopy(service_area_output)

    print("Service area analysis completed and saved to:", service_area_output)

if __name__ == "__main__":
    create_service_area(r"Campus_Paths_FeatureD\Network_Dataset_3", r"Showers", "Service_Area")
