import hashlib as hash
import time 

def sha256hash():
    # fist .txt file (less than 256 bytes)
    st1 = time.time()
    with open("small.txt","rb") as f1:
        contents1 = f1.read()
        sha256 = hash.sha256()
        sha256.update(contents1)
        print("\n{}: {}".format(sha256.name, sha256.hexdigest()))
    et1 = time.time()
    total1 = (et1 - st1) * 10000
    print("Total time: ", total1, "ns\n")

    # second .txt file (greater than 1KB)
    st2 = time.time()
    with open("big.txt","rb") as f2:
        contents2 = f2.read()
        sha = hash.sha256()
        sha.update(contents2)
        print("{}: {}".format(sha.name, sha.hexdigest()))
    et2 = time.time()
    total2 = (et2 - st2) * 10000
    print("Total time: ", total2, "ns\n")


def main():
    sha256hash()

if __name__ == "__main__":
    main()


