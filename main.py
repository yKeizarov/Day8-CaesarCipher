# Caesar cipher
import re
import alphabet as alt

ALPHABET = alt.use_alphabet
MAX_INDEX = len(ALPHABET) - 1


def encode(text):
    encoding = re.split(" ", text.lower())
    encode_value = int(input("ENTER ENCRYPTION VALUE IN RANGE AT 1 TO 10: "))
    new_text = []
    for single_word in encoding:
        new_word = []
        for single_letter in single_word:
            if single_letter != "." and single_letter != ",":
                sl_index = ALPHABET.index(single_letter)
                new_index = sl_index + encode_value
                if new_index >= MAX_INDEX:
                    encode_index = new_index - (MAX_INDEX + 1)
                    new_sl = ALPHABET[encode_index]
                    new_word.append(new_sl)
                else:
                    new_sl = ALPHABET[new_index]
                    new_word.append(new_sl)
            else:
                new_sl = single_letter
                new_word.append(new_sl)
        new_text.append(new_word)
    result = []
    for letter_list in new_text:
        word_result = "".join(letter_list)
        result.append(word_result)
    final_result = " ".join(result)
    return final_result


def decode(text):
    decoding = re.split(" ", text.lower())
    decode_value = int(input("ENTER DECRYPTION VALUE IN RANGE AT 1 TO 10: "))
    new_text = []
    for single_word in decoding:
        new_word = []
        for single_letter in single_word:
            if single_letter != "." and single_letter != ",":
                sl_index = ALPHABET.index(single_letter)
                new_index = sl_index - decode_value
                if -1 >= new_index >= -9:
                    decode_index = (MAX_INDEX + 1) + new_index
                    new_sl = ALPHABET[decode_index]
                    new_word.append(new_sl)
                else:
                    new_sl = ALPHABET[new_index]
                    new_word.append(new_sl)
            else:
                new_sl = single_letter
                new_word.append(new_sl)
        new_text.append(new_word)
    result = []
    for letter_list in new_text:
        word_result = "".join(letter_list)
        result.append(word_result)
    final_result = " ".join(result)
    return final_result


def protocol_caesar():
    protocol_trigger = True
    while protocol_trigger:
        function = input("TWO FUNCTIONS ARE AVAILABLE TO YOU: \n"
                         "TEXT ENCRYPTION-(PRESS 1) and TEXT DECRYPTION-(PRESS 2). \n"
                         "PLEASE ENTER FUNCTION: ")
        if function == "1":
            encoding_text = input("ENTER TEXT FOR ENCRYPTION: ")
            encod_trigger = True
            while encod_trigger:
                if encoding_text != "":
                    result = encode(encoding_text)
                    return print(result)
                else:
                    print("WARNING! MISSING TEXT!")
                    encoding_text = input("ENTER TEXT FOR DECRYPTION: ")
                    continue

        elif function == "2":
            decoding_text = input("ENTER TEXT FOR DECODING: ")
            decode_trigger = True
            while decode_trigger:
                if decoding_text != "":
                    result = decode(decoding_text)
                    return print(result)
                else:
                    print("WARNING! MISSING TEXT!")
                    decoding_text = input("ENTER TEXT FOR DECODING: ")
                    continue
        else:
            print("WARNING! INCORRECT FUNCTION! \n")

            continue


if __name__ == '__main__':
    print("WELCOME TO *** PROTOCOL CAESAR *** ")
    re_use_protocol = True
    while re_use_protocol:
        protocol_caesar()
        answer = input("DO YOU WISH TO CONTINUE? 1-YES, 2-NO: ")
        if answer == "2":
            print("SEE YOU LATE...")
            re_use_protocol = False
        elif answer == "1":
            continue
        else:
            print("INCORRECT ANSWER. PLEASE ASK: ")
            answer = input("DO YOU WISH TO CONTINUE? 1-YES, 2-NO: ")
            continue
