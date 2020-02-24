#!/usr/bin/env python3
#-*-coding:utf8-*-
import base64,base36,base58,base91,base92,base62,base128
import binascii
import re
def base_decode(n):
    m=''
    flag=False

    try:
        if re.search('[a-e]',n):
            m=base64.b16decode(n,True)
        else:
            m=base64.b16decode(n)
    except binascii.Error:
        pass
    else:
        flag=True
        print("base16deocde:",m)
        return flag
    #'''''''''''''''''''''''''''''''''
    try:
        m=base64.b32decode(n)
    except binascii.Error:
        pass
    else:
        flag=True
        print("base32deocde:",m)
        return flag
    #'''''''''''''''''''''''''''''''''
    try:
        m = base58.b58decode(n)
    except ValueError:
        pass
    else:
        m=str(m)[2:-1]
        if '\\x' in m:
            pass
        else:
            flag=True
            print("base58deocde:",m)
            mm=str(base91.decode(n))
            if '\\x' not in mm:
                print("maybe base91decode:",mm)
            return flag
    #'''''''''''''''''''''''''''''''''
    try:
        m=base62.decodebytes(n)
    except    ValueError:
        pass
    else:
        m=str(m)
        if '\\x' in m:
            pass
        else:
            flag=True
            print("base62deocde:",m)
            return flag
    #'''''''''''''''''''''''''''''''''
    try:
        m=base64.b64decode(n)
    except binascii.Error:
        pass
    else:
        m=str(m)
        if '\\x' in m:
            pass
        else:
            flag=True
            print("base64deocde:",m)
            return flag
    #'''''''''''''''''''''''''''''''''
    try:
        m=base64.b85decode(n)
    except ValueError:
        pass
    else:
        m=str(m)
        if '\\x' in m:
            pass
        else:
            print("base_b85deocde:",m)
            flag=True
            return flag
    #'''''''''''''''''''''''''''''''''
    try:
        m=base64.a85decode(n)
    except ValueError:
        pass
    else:
        m=str(m)
        if '\\x' in m:
            pass
        else:
            print("base_a85deocde:",m)
            flag=True
            return flag
    #'''''''''''''''''''''''''''''''''
    try:
        m=base91.decode(n)
    except ValueError:
        pass
    else:
        m=str(m)
        if '\\x' in m:
            pass
        else:
            print("base91deocde:",m)
            flag=True
            return flag
    #'''''''''''''''''''''''''''''''''
    try:
        m = base92.decode(n)
    except ValueError:
        pass
    else:
        flag=True
        print("base92deocde:",m)
        return flag
    #'''''''''''''''''''''''''''''''''
    try:
        c = base36.loads(n)
        assert type(c) == int
        m = base36.dumps(c)
    except ValueError:
        pass
    else:
        flag=True
        print("base36deocde:",m)
        return flag
    # '''''''''''''''''''''''''''''''''
    try:
        b128 = base128.base128(chars=None, chunksize=7)
        n_str = bytes(n, encoding="utf8")
        c = list(b128.encode(n_str))
        m = b''.join(b128.decode(c))
    except ValueError:
        pass
    else:
        flag=True
        print("base128deocde:",m)
        return flag
    return flag
    #'''''''''''''''''''''''''''''''''


if __name__=='__main__':
    print("******There are has base64,base16,base32,base36,base58,base62,base85,base91,base92 and base128******")
    while(1):
        x=input("input the string(q to quit):")

        if x=='q':
            break
        a=base_decode(x)
        if a==True:
            print('\n')
        else:
            print("Fail")
