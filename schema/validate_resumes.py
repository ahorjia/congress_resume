import json
import jsonschema
import os
from enum import Enum


class Session(Enum):
    SESSION_1 = 1
    SESSION_2 = 2


# Get the input directory and JSON schema
def validate_json_files(session: Session):
    input_directory = os.path.join(os.getcwd(), 'resumes')

    if session == Session.SESSION_1:
        schema_file_path = "session_1.schema.json"
        session_designation = "_1.json"
    else:
        schema_file_path = "session_2.schema.json"
        session_designation = "_2.json"

    json_files = [f for f in os.listdir(input_directory) \
                  if f.endswith(session_designation)]

    with open(os.path.join(os.getcwd(), "schema", schema_file_path), 'r') as schema_file:
        schema = json.load(schema_file)

    # Validate each JSON file against the JSON schema
    for json_file in json_files:
        with open(os.path.join(input_directory, json_file), "r") as f:
            json_data = json.load(f)

        try:
            jsonschema.validate(json_data, schema)
            print(f"Validation successful for {json_file}")
        except jsonschema.ValidationError as e:
            print(f"Validation error for {json_file}")


validate_json_files(Session.SESSION_1)