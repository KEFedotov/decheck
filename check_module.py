import yaml, re, logging

logger = logging.getLogger(__name__)

def dev_connect(testbed):
    for dev in testbed.devices:
        testbed.devices[dev].connect(mit=True)

def scheme_parse(file_path):
    with open(file_path, 'r') as in_file:
        scheme = yaml.safe_load(in_file)
    
    return scheme

def check_out(values, output):
    result = False
    for value in values:
        output = re.sub(r'\s+', ' ', output)
        value = re.sub(r'\s+', ' ', value)
        if re.findall(value, output):
            result = True
        else:
            result = False
    return result
