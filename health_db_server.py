from flask import Flask, request, jsonify


app = Flask(__name__)

db = list()


def add_patient_to_db(name, id, age):
    new_patient = {'name': name, 'id': id, 'age': age,
                   'tests': list()}
    db.append(new_patient)
    return True


def validate_new_patient_info(in_dict):
    expected_key = ("name", "id", "age")
    expected_type = (str, int, int)
    for key, ty in zip(expected_key, expected_type):
        if key not in in_dict.keys():
            return '{} key not found'.format(key)
        if type(in_dict[key]) != ty:
            return '{} key is the wrong value type'.format(key)

    return True


@app.route('/new_patient', methods=['POST'])
def post_new_patient():
    in_dict = request.get_json()
    # validate input
    check_input = validate_new_patient_info(in_dict)
    if check_input is not True:
        return check_input, 400
    answer = add_patient_to_db(in_dict['name'], in_dict['id'], in_dict['age'])
    if answer:
        return "Success adding patient", 200
    else:
        return "There was an error adding patient", 400








def init_server():
    add_patient_to_db('anna ables', 101, 30)
    add_patient_to_db('bob boyles', 102, 34)


if __name__ == '__main__':
    init_server()
    app.run()