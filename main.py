from Cryptodome.Cipher import AES


def decrypt_file(filekey, filetoD, nonceFile):
    """
    Description : use file in params in order to decrypt the encrypted file
    :param filekey:
    :param filetoD:
    :param nonceFile:
    :return:
    """
    print("hello world")
    fn = open(nonceFile, "rb")
    fk = open(filekey, "rb")
    ff = open(filetoD, "rb")
    key = fk.read()
    dataf = ff.read()

    cipher = AES.new(key, AES.MODE_EAX, nonce=fn.read())

    data = cipher.decrypt(dataf)
    print(data.decode('utf-8'))


if __name__ == '__main__':
    ff = input("Please enter the file to decrypt path : ")
    fk = input("Please enter the key file path : ")
    fn = input("PLease enter the nonce file path : ")
    decrypt_file(fk, ff, fn)
