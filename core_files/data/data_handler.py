import json
from pathlib import Path
import os
import shutil

# Path to the /core_files folder
CORE_FILES_PATH = Path(__file__).parents[1]

def get_core_files_path():
    return CORE_FILES_PATH

# Get the model spreadsheet file path
def get_spreadsheet_model_path (tool, model):
    path = 'config/spreadsheet_models/'+f"{tool}_{model}.xlsx"
    return CORE_FILES_PATH / path

# Get the output spreadsheet file path
def get_workbook_destination_path (tool, model, ui_name, ui_type):
    folder_path = CORE_FILES_PATH / 'output'
    if not Path.exists(folder_path): #Create the output folder if it doesn't exist
        os.makedirs (CORE_FILES_PATH / 'output')
    
    destination_path = folder_path / f"{tool}_{model}_{ui_name}_{ui_type}.xlsx" 
    return destination_path

class Data_Handler:

    def get_replacement_config_folder_path():
        return CORE_FILES_PATH/'config'/'replacement_config'
    
    # Copy the model spreadhsheet to the output file path
    def copy_config_workbook(tool, model, ui_name, ui_type):
        source_file = get_spreadsheet_model_path (tool, model)
        destination_file = get_workbook_destination_path (tool, model, ui_name, ui_type)
        shutil.copy(source_file, destination_file)
        return destination_file
    
    # Map the Features from the JSON file to a dict      
    def map_features_json_to_features_dict(feature_file_path):
        with open(feature_file_path) as f:
            features_dict = json.load(f)
        return features_dict
    
    # Get the command line interface options to display for the user on the terminal
    def get_cli_tool_model_options():
        model_spreadsheets_path = CORE_FILES_PATH / 'config' / 'spreadsheet_models'
        spreadsheet_files = list(model_spreadsheets_path.glob('*'))
        tools = {}

        for spreadsheet_file in spreadsheet_files:
            tool_name, rest = spreadsheet_file.stem.split('_') # First part of the spreadsheet name
            model_name = rest.split('.')[0] # Second part of the spreadsheet name minus the file extension
            
            if tool_name not in tools:
                tools[tool_name] = set()

            tools[tool_name].add(model_name)
            
        return tools
    
    # Get the command line interface options to display for the user on the terminal
    def get_cli_replacement_feature_options():
        replacements_path = CORE_FILES_PATH / 'config' / 'replacement_config'
        replacement_files = list(replacements_path.glob('*'))
        replacements = []

        for replacement in replacement_files:
            if replacement.name not in replacements:
                replacements.append(replacement.name)
            
        return replacements