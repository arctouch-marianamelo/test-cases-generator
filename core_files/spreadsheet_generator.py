import os
from data.data_handler import Data_Handler
from data.wb_handler import WB_Handler

def validate_input(choices, valid_choices):
    for choice in choices:
        if choice.strip() not in valid_choices:
            return False
    return True

def run():
    cli_tool_model_options = Data_Handler.get_cli_tool_model_options()
    cli_feature_replacement_options = Data_Handler.get_cli_replacement_feature_options()
    feature_replacement_path = Data_Handler.get_replacement_config_folder_path()

    # Replacement File choices (JSON files on /replacement_config folder)
    while True:
        replacement_choice = input('\nInform the replacements file name or press enter to see the list of available files:')
        if replacement_choice == '':
            for i, replacement_option in enumerate(sorted(cli_feature_replacement_options), start=1):
                print(f'{i}.{replacement_option}')
            replacement_choice = input("> Enter the replacement file option: ").split(',')
            if not validate_input(replacement_choice, map(str, range(1, len(cli_feature_replacement_options) + 1))):
                print('\n!!! Invalid tool choice. Please choose a number from the given options. !!!')
                continue
            replacement_file_path = feature_replacement_path / [cli_feature_replacement_options[int(replacement_choice[0]) - 1]][0]
        else:
            replacement_file_path = feature_replacement_path / replacement_choice[0]
            if not os.path.exists(feature_replacement_path / replacement_file_path):
                print('\n!!! The replacement file name does not exist. Please inform another name. !!!')
                continue
        break

    # Spreadsheet Tool choices (from spreadsheets on /spreadsheet_models folder)
    while True:
        print('\nChoose the spreadsheet tool between the following options:')
        for i, tool_option in enumerate(sorted(cli_tool_model_options), start=1):
            print(f'{i}.{tool_option}')
        tool_choices = input("> Enter the tool options separated by comma (e.g. 1,2): ").split(',')

        if not validate_input(tool_choices, map(str, range(1, len(cli_tool_model_options) + 1))):
            print('\n!!! Invalid tool choice. Please choose a number from the given options. !!!')
            continue

        selected_tools = [list(cli_tool_model_options.keys())[int(choice) - 1] for choice in tool_choices]
        valid_models_for_selected_tool = set.union(*[cli_tool_model_options[tool] for tool in selected_tools])
        break

    # Model choices (from spreadsheets on /spreadsheet_models folder)
    while True:
        print('\nChoose the spreadsheet model between the following options:')
        for i, model_option in enumerate(sorted(valid_models_for_selected_tool), start=1):
            print(f'{i}.{model_option}')
        model_choices = input("> Enter the model options separated by comma (e.g. 1,2): ").split(',')

        if not validate_input(model_choices, map(str, range(1, len(valid_models_for_selected_tool) + 1))):
            print('\n!!! Invalid model choice. Please choose a number from the given options. !!!')
            continue

        selected_models = [list(sorted(valid_models_for_selected_tool))[int(choice) - 1] for choice in model_choices]
        break


    WB_Handler.generate_output_spreadsheets(selected_tools, selected_models, replacement_file_path)     
    print ('!!! ---------- Spreadsheets successfully generated. Please check the /output folder. ---------- !!!')


if __name__ == '__main__':
    try:
        run()
    except KeyboardInterrupt:
        pass
