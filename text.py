def encode(data):
    data = data.encode('ascii')
    binary = [format(i,'#09b')[2:] for i in data]
    return binary

def decode(data):
    string = "".join([chr(int(i,2)) for i in data])
    return string
