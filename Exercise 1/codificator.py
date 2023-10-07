import base64


# converts input into string
def encoding64(transform):
    database64 = base64.b64encode(transform)
    database64p = database64.decode("utf-8")
    return database64p


# converts input into bytes
def decoding64(transform):
    input_conv = base64.decodebytes(transform.encode("ascii"))
    return input_conv
