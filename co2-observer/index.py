import subprocess
import insert_co2
import re
import json

def get_co2():
    out = subprocess.check_output(['sudo', 'python3', '-m', 'mh_z19'])
    result_json = out.decode("utf-8")
    co2_dict = json.loads(result_json)
    if co2_dict is None:
        print('mh_z19 returned None')
        return False
 
    result = insert_co2.insert_co2(co2_dict['co2'])
    return True
