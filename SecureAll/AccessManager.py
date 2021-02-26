import json
from .AccessManagementException import AccessManagementException
from .AccessRequest import AccessRequest

class AccessManager:
    def __init__(self):
        pass

    def ValidateDNI(self, DNI):
        dict = {0: 'T', 1: 'R', 2: 'W', 3: 'A', 4: 'G', 5: 'M', 6: 'Y', 7: 'F', 8: 'P', 9: 'D', 10: 'X', 11: 'B',
                12: 'N', 13: 'J', 14: 'Z', 15: 'S', 16: 'Q', 17: 'V', 18: 'H', 19: 'L', 20: 'C', 21: 'K', 22: 'E'}
        nums = int(DNI[:8])
        let = DNI[8]
        res = nums % 23
        print(nums, let, res)
        if let == dict[res]:
            return True
        else:
            return False

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