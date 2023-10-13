import base64


# converts input into string
def encoding64(transform):
    database64 = base64.b64encode(transform)
    str_output = database64.decode("utf-8")
    return str_output


# converts input into bytes
def decoding64(transform):
    # return base64.decodebytes(transform.encode("ascii"))
    if isinstance(transform, str):
        return base64.decodebytes(transform.encode("ascii"))

    # convert to 32-bytes (= 256-bit) in Little-Endian mode
    elif isinstance(transform, int):
        return transform.to_bytes(3000, byteorder='little')
