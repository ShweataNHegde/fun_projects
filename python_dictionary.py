# understanding python dictionary
name_list = ['shweata', 'shamanta', 'savita', 'nagapati']
import pandas as pd
def main_dict_creation_to_df(list_of_names):
    main_dictionary = {}
    name_dict = name_dict_creation(list_of_names)
    main_dictionary['family_name'] = name_dict
    df = pd.DataFrame(main_dictionary).T
    print(df)

def name_dict_creation(list_of_names):
    name_dict = {}
    name_dict['all_names'] = list_of_names
    return name_dict

main_dict_creation_to_df(name_list)