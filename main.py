def main():
    STRING = "aababbabbaaba"
    compressed = compress(STRING)
    print(compressed)
    decompressed = decompress(compressed)
    print(decompressed)


def compress(string):
    encode = {}  # string -> code
    known = ""
    count = 0
    result = []
    for letter in string:
        if known + letter in encode:
            known += letter
        else:
            count += 1
            encode[known + letter] = count
            result.append([encode[known] if known else 0, letter])
            known = ""
    if known:
        result.append([encode[known], ""])
    return result


def decompress(compressed):
    string = ""
    decode = {}  # code -> string
    known = ""
    count = 0
    for code, new in compressed:
        if not code:
            count += 1
            decode[count] = new
            string += new
        elif not new:
            string += decode[code]
        else:
            count += 1
            known = decode[code]
            decode[count] = known + new
            string += known + new
    return string


if __name__ == "__main__":
    main()
