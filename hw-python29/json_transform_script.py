import json

def load_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def convert_to_dict(json_data):
    return json_data

def generate_full_name(person_dict):
    full_name = person_dict['city']
    return full_name

def process_data(json_data):
    result = {}
    for person in json_data:
        full_name = generate_full_name(person)
        item_list = list(person.items())
        sorted_items = sorted(item_list, key=lambda x: type(x[1]).__name__)
        result[full_name] = sorted_items
    return result

def save_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)  # Зміна тут

def process_json_files(input_file, output_file):
    json_data = load_json(input_file)
    result_dict = process_data(json_data)
    save_json(output_file, result_dict)

process_json_files('hw.json', 'nw_result.json')
