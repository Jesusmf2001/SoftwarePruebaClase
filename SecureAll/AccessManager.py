import json
from .AccessManagementException import AccessManagementException
from .AccessRequest import AccessRequest

class AccessManager:
    def __init__(self):
        pass

    def ValidateDNI(self, DNI):
        # PLEASE INCLUDE HERE THE CODE FOR VALIDATING THE DNI
        # RETURN TRUE IF THE DNI IS RIGHT, OR FALSE IN OTHER CASE
        return True

    def ReadaccessrequestfromJSON(self, fi):

        try:
            with open(fi) as f:
                DATA = json.load(f)
        except FileNotFoundError as e:
            raise AccessManagementException("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise AccessManagementException("JSON Decode Error - Wrong JSON Format") from e


        try:
            idDoc = DATA["id"]
            name = DATA["name"]
            req = AccessRequest(idDoc, name)
        except KeyError as e:
            raise AccessManagementException("JSON Decode Error - Invalid JSON Key") from e
        if not self.ValidateDNI(idDoc):
            raise AccessManagementException("Invalid DNI")

        # Close the file
        return req