import arcpy

# Set variables
gdb_path = r"C:\folder\example.gdb"  # Path to your geodatabase
# Set environment - change path to location of geodatabase where network analysis will be performed
arcpy.env.workspace = gdb_path
arcpy.env.overwriteOutput = True

def cost_matrix(network_dataset, origins, destinations, output_path):
    """
    Function to create a cost matrix between origins and destinations.
    
    Parameters:
    network_dataset: Path to your network dataset
    origins: Path to origin points
    destinations: Path to destination points
    output_path: Where to save the results; the name of the cost matrix layer and path, if saving not in the geodatabase specified above
    """
    # Create OD Cost Matrix Layer
    result = arcpy.na.MakeODCostMatrixLayer(network_dataset, "OD_Matrix", "Minutes", default_number_destinations_to_find=3)
        
    layer = result.getOutput(0)
        
    # Add origins and destinations
    arcpy.na.AddLocations(layer, "Origins", origins)
    arcpy.na.AddLocations(layer, "Destinations", destinations)
        
    # Solve the matrix
    arcpy.na.Solve(layer)
        
    # Save the results
    lines_layer = layer.listLayers()[1]
    arcpy.CopyFeatures_management(lines_layer, output_path)
        
    print(f"Cost matrix created successfully at: {output_path}")

# Example usage
if __name__ == "__main__":
    cost_matrix(
        # Use the format Feature_Dataset_Name\File_Name. Do not include file extension.
        network_dataset = r"Transportation\Streets_ND",
        origins = r"Analysis\Patients",
        destinations = r"Analysis\Hospitals",
        output_path = r"Cost_Matrix"
    )
