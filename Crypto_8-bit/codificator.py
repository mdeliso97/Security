import base64

'''
This class defines encoding and decoding, the encoding method gets as input a bite string and converts it into a string,
whereas the decoding method gets as input a string or an integer and converts them 
'''


# converts input into string
def encoding64(transform):
    database64 = base64.b64encode(transform)
    str_output = database64.decode("utf-8")
    return str_output


# converts input into bytes
def decoding64(transform):
    if isinstance(transform, str):
        return base64.decodebytes(transform.encode("ascii"))

    # convert to 32-bytes (= 256-bit) in Little-Endian mode
    elif isinstance(transform, int):
        return transform.to_bytes(32, byteorder='little')
