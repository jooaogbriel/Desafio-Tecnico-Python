from .serializers import DatasSerializer
from storage.serializers import StorageSerializer
from .models import Datas
from storage.models import Storage

def refresh_database(file):
    
    datas_list = get_datas_list_from_file(file)

    for datas in datas_list:
        
        serializer = DatasSerializer(data=datas)
        serializer.is_valid(raise_exception=True)

        serializer.save()


def get_datas_list_from_file(file):
    
    cnab_field_sizes = [1, 8, 10, 11, 12, 6, 14, 19]
    
    fields = [
        "type_transaction",
        "date",
        "value",
        "cpf",
        "card",
        "hour",
        "owner",
        "name",
    ]

    data_dict_list = parse_cnab_file(file, fields, cnab_field_sizes)
    
    convert_to_datas_model(data_dict_list)

    alter_datetime(data_dict_list)

    return data_dict_list


def alter_datetime(data_dict_list):
    for data in data_dict_list:
        date = data["date"]
        hour = data["hour"]
        data["date"] = date[:4] + '-' + date[4:6] + '-' + date[6:8]
        data["hour"] = hour[:2] + ':' + hour[2:4] + ':' + hour[4:6]

def parse_cnab_file(file, field_names_list, cnab_field_sizes_list):
    objects_list = []
    while True:
    
        index_field = 0
        object = {}

        cnab_line_str: str = file.readline().decode()
        
        if not cnab_line_str:
            break

        last_index = 0
        for field_size in cnab_field_sizes_list:
            
            field_value = cnab_line_str[last_index : last_index + field_size]
            
            current_field = field_names_list[index_field]

            object[current_field] = field_value

            index_field += 1
            last_index += field_size

        objects_list.append(object)
    
    return objects_list


def convert_to_datas_model(list):
    for obj in list:
        storage = {
            'name': obj['name'],
            'owner': obj['owner'],
        }
        obj.pop('name')
        obj.pop('owner')
        obj['store'] = storage
        obj['value'] = int(obj['value'])/100


def get_storage_from_database():

    storage = Storage.objects.all()

    serializer = StorageSerializer(storage, many=True)

    add_datas_to_storage_list(serializer.data)

    return serializer.data


def add_datas_to_storage_list(store_list):
    for storage in store_list:
        
        datas = Datas.objects.filter(store_id = storage['id'])
        serializer = DatasSerializer(datas, many = True)
        storage['datas'] = serializer.data
        
        storage['balance'] = calculate_total_value(serializer.data)


def calculate_total_value(datas_list):
    datas_types = [1 , -1, -1, 1, 1, 1, 1, 1, -1]
    
    result = 0

    for data in datas_list:
        
        current_value = data['value']

        current_type = int(data['type_data']) - 1

        result += datas_types[current_type] * current_value

    return result
