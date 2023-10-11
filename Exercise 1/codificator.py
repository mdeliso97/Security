import base64


# converts input into string
def encoding64(transform):
    database64 = base64.b64encode(transform)
    str_output = database64.decode("utf-8")
    return str_output


# converts input into bytes
def decoding64(transform):

    if isinstance(transform, str):
        return base64.decodebytes(transform.encode("ascii"))

    elif isinstance(transform, int):
        return transform.to_bytes((transform.bit_length() + 7) // 8, 'big')
