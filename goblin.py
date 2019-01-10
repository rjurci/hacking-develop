
import codecs

def goblin():

    id = codecs.encode(b'admin','hex_codec')
    print(id)


if __name__ == "__main__":
    goblin()
