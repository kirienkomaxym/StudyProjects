def text_to_bits(text, encoding='utf-8', errors='surrogatepass'): # Функция перевода в двойку
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


res = text_to_bits(input())
STEP = 4
print(res)

#print(len(res))

bits_by4 = [res[index:index+STEP] for index in range(0, len(res), STEP)]
print(bits_by4)


def s_1(list):
    for i in range(0,len(list),4):
        if list[i] == '0000': #0
            list[i] = '0111'
        elif list[i] == '0001': #1
            list[i] = '0011'
        elif list[i] == '0010': #2
            list[i] = '1100'
        elif list[i] == '0011': #3
            list[i] = '1010'
        elif list[i] == '0100': #4
            list[i] = '0010'
        elif list[i] == '0101': #5
            list[i] = '0000'
        elif list[i] == '0110': #6
            list[i] = '0001'
        elif list[i] == '0111': #7
            list[i] = '1001'
        elif list[i] == '1000': #8
            list[i] = '0101'
        elif list[i] == '1001': #9
            list[i] = '1110'
        elif list[i] == '1010': #10
            list[i] = '0110'
        elif list[i] == '1011': #11
            list[i] = '1101'
        elif list[i] == '1100': #12
            list[i] = '1111'
        elif list[i] == '1101': #13
            list[i] = '0100'
        elif list[i] == '1110': #14
            list[i] = '1011'
        else:
            list[i] = '1000'
    return(list)

bits_by4_s1 = s_1(bits_by4)
print(bits_by4_s1)

def s_2(list):
    for i in range(1,len(list),4):
        if list[i] == '0000': #0
            list[i] = '0011'
        elif list[i] == '0001': #1
            list[i] = '1110'
        elif list[i] == '0010': #2
            list[i] = '0110'
        elif list[i] == '0011': #3
            list[i] = '1111'
        elif list[i] == '0100': #4
            list[i] = '1001'
        elif list[i] == '0101': #5
            list[i] = '0100'
        elif list[i] == '0110': #6
            list[i] = '0010'
        elif list[i] == '0111': #7
            list[i] = '1010'
        elif list[i] == '1000': #8
            list[i] = '1100'
        elif list[i] == '1001': #9
            list[i] = '0001'
        elif list[i] == '1010': #10
            list[i] = '1101'
        elif list[i] == '1011': #11
            list[i] = '0000'
        elif list[i] == '1100': #12
            list[i] = '1000'
        elif list[i] == '1101': #13
            list[i] = '1011'
        elif list[i] == '1110': #14
            list[i] = '0111'
        else:
            list[i] = '0101'
    return(list)

bits_by4_s2 = s_2(bits_by4_s1)
print(bits_by4_s2)

def s_3(list):
    for i in range(2,len(list),4):
        if list[i] == '0000': #0
            list[i] = '1110'
        elif list[i] == '0001': #1
            list[i] = '0111'
        elif list[i] == '0010': #2
            list[i] = '0101'
        elif list[i] == '0011': #3
            list[i] = '1010'
        elif list[i] == '0100': #4
            list[i] = '1011'
        elif list[i] == '0101': #5
            list[i] = '0100'
        elif list[i] == '0110': #6
            list[i] = '0000'
        elif list[i] == '0111': #7
            list[i] = '0011'
        elif list[i] == '1000': #8
            list[i] = '1101'
        elif list[i] == '1001': #9
            list[i] = '0110'
        elif list[i] == '1010': #10
            list[i] = '0001'
        elif list[i] == '1011': #11
            list[i] = '1111'
        elif list[i] == '1100': #12
            list[i] = '1100'
        elif list[i] == '1101': #13
            list[i] = '0100'
        elif list[i] == '1110': #14
            list[i] = '0010'
        else:
            list[i] = '1001'
    return(list)


bits_by4_s3 = s_3(bits_by4_s2)
print(bits_by4_s3)

def s_4(list):
    for i in range(3,len(list),4):
        if list[i] == '0000': #0
            list[i] = '0110'
        elif list[i] == '0001': #1
            list[i] = '1001'
        elif list[i] == '0010': #2
            list[i] = '0111'
        elif list[i] == '0011': #3
            list[i] = '1100'
        elif list[i] == '0100': #4
            list[i] = '1111'
        elif list[i] == '0101': #5
            list[i] = '1010'
        elif list[i] == '0110': #6
            list[i] = '0001'
        elif list[i] == '0111': #7
            list[i] = '0011'
        elif list[i] == '1000': #8
            list[i] = '1000'
        elif list[i] == '1001': #9
            list[i] = '0000'
        elif list[i] == '1010': #10
            list[i] = '1011'
        elif list[i] == '1011': #11
            list[i] = '0010'
        elif list[i] == '1100': #12
            list[i] = '1110'
        elif list[i] == '1101': #13
            list[i] = '0101'
        elif list[i] == '1110': #14
            list[i] = '1101'
        else:
            list[i] = '0100'
    return(list)

bits_by4_s4 = s_4(bits_by4_s3)
print(bits_by4_s4)


for i in range(0, len(bits_by4_s4), 2):
    bits_by4_s4[i] += bits_by4_s4[i+1]


del bits_by4_s4[1:len(bits_by4_s4):2]


for i in range(0, len(bits_by4_s4)-1, 2):
    bits_by4_s4[i] += bits_by4_s4[i+1]

if len(bits_by4_s4)%2 != 0:
    bits_by4_s4[-1] = bits_by4_s4[-1]+'00000000'

del bits_by4_s4[1:len(bits_by4_s4):2]
print(bits_by4_s4)

used_for_p_1 = ([list(i) for i in bits_by4_s4])

print(used_for_p_1)

for listed in used_for_p_1:
    listed[0], listed[1], listed[2], listed[3], listed[4], listed[5], listed[6], listed[7], listed[8], listed[9], listed[10], listed[11], listed[
        12], listed[13], listed[14], listed[15] = listed[5], listed[15], listed[7], listed[2], listed[13], listed[1], listed[4], listed[10], \
                                                  listed[11], listed[6], listed[0], listed[14], listed[9], listed[12], listed[8], listed[3]

print(used_for_p_1)

counter_1=''
for row in used_for_p_1:
    f = (''.join([str(elem) for elem in row]))
    counter_1 += f

bits_string_round_1 = counter_1

print(bits_string_round_1)

bits_by4_1 = [bits_string_round_1[index:index+STEP] for index in range(0, len(bits_string_round_1), STEP)] #По следующему кругу пошли
print(bits_by4_1)

def s_5(list):
    for i in range(0,len(list),4):
        if list[i] == '0000': #0
            list[i] = '1101'
        elif list[i] == '0001': #1
            list[i] = '0000'
        elif list[i] == '0010': #2
            list[i] = '1001'
        elif list[i] == '0011': #3
            list[i] = '1110'
        elif list[i] == '0100': #4
            list[i] = '1010'
        elif list[i] == '0101': #5
            list[i] = '1011'
        elif list[i] == '0110': #6
            list[i] = '0101'
        elif list[i] == '0111': #7
            list[i] = '1000'
        elif list[i] == '1000': #8
            list[i] = '0100'
        elif list[i] == '1001': #9
            list[i] = '0110'
        elif list[i] == '1010': #10
            list[i] = '1100'
        elif list[i] == '1011': #11
            list[i] = '1111'
        elif list[i] == '1100': #12
            list[i] = '0001'
        elif list[i] == '1101': #13
            list[i] = '0111'
        elif list[i] == '1110': #14
            list[i] = '0010'
        else:
            list[i] = '0011'
    return(list)

bits_by4_1_s5 = s_5(bits_by4_1)
print(bits_by4_1_s5)

def s_6(list):
    for i in range(1,len(list),4):
        if list[i] == '0000': #0
            list[i] = '0111'
        elif list[i] == '0001': #1
            list[i] = '0101'
        elif list[i] == '0010': #2
            list[i] = '0001'
        elif list[i] == '0011': #3
            list[i] = '1011'
        elif list[i] == '0100': #4
            list[i] = '0110'
        elif list[i] == '0101': #5
            list[i] = '1001'
        elif list[i] == '0110': #6
            list[i] = '1000'
        elif list[i] == '0111': #7
            list[i] = '0000'
        elif list[i] == '1000': #8
            list[i] = '1101'
        elif list[i] == '1001': #9
            list[i] = '1110'
        elif list[i] == '1010': #10
            list[i] = '0011'
        elif list[i] == '1011': #11
            list[i] = '1010'
        elif list[i] == '1100': #12
            list[i] = '0010'
        elif list[i] == '1101': #13
            list[i] = '1100'
        elif list[i] == '1110': #14
            list[i] = '1111'
        else:
            list[i] = '0100'
    return(list)


bits_by4_1_s6 = s_6(bits_by4_1_s5)
print(bits_by4_1_s6)


def s_7(list):
    for i in range(2,len(list),4):
        if list[i] == '0000':  #0
            list[i] = '0010'
        elif list[i] == '0001': #1
            list[i] = '1010'
        elif list[i] == '0010': #2
            list[i] = '1111'
        elif list[i] == '0011': #3
            list[i] = '1001'
        elif list[i] == '0100': #4
            list[i] = '0011'
        elif list[i] == '0101': #5
            list[i] = '1110'
        elif list[i] == '0110': #6
            list[i] = '0110'
        elif list[i] == '0111': #7
            list[i] = '1011'
        elif list[i] == '1000': #8
            list[i] = '0111'
        elif list[i] == '1001': #9
            list[i] = '0001'
        elif list[i] == '1010': #10
            list[i] = '0101'
        elif list[i] == '1011': #11
            list[i] = '1101'
        elif list[i] == '1100': #12
            list[i] = '1000'
        elif list[i] == '1101': #13
            list[i] = '1100'
        elif list[i] == '1110': #14
            list[i] = '0000'
        else:
            list[i] = '0100'
    return list


bits_by4_1_s7 = s_7(bits_by4_1_s6)
print(bits_by4_1_s7)


def s_8(list):
    for i in range(3,len(list),4):
        if list[i] == '0000':  #0
            list[i] = '1011'
        elif list[i] == '0001': #1
            list[i] = '1001'
        elif list[i] == '0010': #2
            list[i] = '0110'
        elif list[i] == '0011': #3
            list[i] = '1100'
        elif list[i] == '0100': #4
            list[i] = '0010'
        elif list[i] == '0101': #5
            list[i] = '0111'
        elif list[i] == '0110': #6
            list[i] = '0001'
        elif list[i] == '0111': #7
            list[i] = '1010'
        elif list[i] == '1000': #8
            list[i] = '1101'
        elif list[i] == '1001': #9
            list[i] = '1110'
        elif list[i] == '1010': #10
            list[i] = '0000'
        elif list[i] == '1011': #11
            list[i] = '1000'
        elif list[i] == '1100': #12
            list[i] = '0011'
        elif list[i] == '1101': #13
            list[i] = '0101'
        elif list[i] == '1110': #14
            list[i] = '1111'
        else:
            list[i] = '0010'
    return list


bits_by4_1_s8 = s_8(bits_by4_1_s7)
print(bits_by4_1_s8)

for i in range(0, len(bits_by4_1_s8), 2):
    bits_by4_1_s8[i] += bits_by4_1_s8[i+1]


del bits_by4_1_s8[1:len(bits_by4_1_s8):2]


for i in range(0, len(bits_by4_1_s8)-1, 2):
    bits_by4_1_s8[i] += bits_by4_1_s8[i+1]

del bits_by4_1_s8[1:len(bits_by4_1_s8):2]
print(bits_by4_1_s8)

used_for_p_2 = ([list(i) for i in bits_by4_1_s8])
print(used_for_p_2)

for listed_1 in used_for_p_2:
    listed_1[0], listed_1[1], listed_1[2], listed_1[3], listed_1[4], listed_1[5], listed_1[6], listed_1[7], listed_1[8], listed_1[9], listed_1[10], listed_1[11], listed_1[
        12], listed_1[13], listed_1[14], listed_1[15] = listed_1[8], listed_1[3], listed_1[9], listed_1[13], listed_1[1], listed_1[14], listed_1[4], listed_1[10], \
                                                        listed_1[2], listed_1[7], listed_1[12], listed_1[5], listed_1[11], listed_1[15], listed_1[0], listed_1[6]


print(used_for_p_2)

counter_2=''
for row in used_for_p_2:
    f_2 = (''.join([str(elem) for elem in row]))
    counter_2 += f_2

bits_string_round_2 = counter_2
print(bits_string_round_2)

bits_by4_2 = [bits_string_round_2[index:index+STEP] for index in range(0, len(bits_string_round_2), STEP)]
print(bits_by4_2)

def s_9(list):
    for i in range(0,len(list),4):
        if list[i] == '0000':  #0
            list[i] = '0011'
        elif list[i] == '0001': #1
            list[i] = '0000'
        elif list[i] == '0010': #2
            list[i] = '1010'
        elif list[i] == '0011': #3
            list[i] = '0110'
        elif list[i] == '0100': #4
            list[i] = '1011'
        elif list[i] == '0101': #5
            list[i] = '0100'
        elif list[i] == '0110': #6
            list[i] = '1001'
        elif list[i] == '0111': #7
            list[i] = '1100'
        elif list[i] == '1000': #8
            list[i] = '0101'
        elif list[i] == '1001': #9
            list[i] = '1111'
        elif list[i] == '1010': #10
            list[i] = '0001'
        elif list[i] == '1011': #11
            list[i] = '1110'
        elif list[i] == '1100': #12
            list[i] = '1101'
        elif list[i] == '1101': #13
            list[i] = '0111'
        elif list[i] == '1110': #14
            list[i] = '0010'
        else:
            list[i] = '1000'
    return list


bits_by4_2_s9 = s_9(bits_by4_2)
print(bits_by4_2_s9)

def s_10(list):
    for i in range(1,len(list),4):
        if list[i] == '0000':  #0
            list[i] = '1100'
        elif list[i] == '0001': #1
            list[i] = '1000'
        elif list[i] == '0010': #2
            list[i] = '0110'
        elif list[i] == '0011': #3
            list[i] = '1111'
        elif list[i] == '0100': #4
            list[i] = '1110'
        elif list[i] == '0101': #5
            list[i] = '0000'
        elif list[i] == '0110': #6
            list[i] = '0011'
        elif list[i] == '0111': #7
            list[i] = '1101'
        elif list[i] == '1000': #8
            list[i] = '0111'
        elif list[i] == '1001': #9
            list[i] = '0010'
        elif list[i] == '1010': #10
            list[i] = '1011'
        elif list[i] == '1011': #11
            list[i] = '0001'
        elif list[i] == '1100': #12
            list[i] = '1010'
        elif list[i] == '1101': #13
            list[i] = '0101'
        elif list[i] == '1110': #14
            list[i] = '1001'
        else:
            list[i] = '0100'
    return list


bits_by4_2_s10 = s_10(bits_by4_2_s9)
print(bits_by4_2_s10)

def s_11(list):
    for i in range(2,len(list),4):
        if list[i] == '0000':  #0
            list[i] = '1101'
        elif list[i] == '0001': #1
            list[i] = '1001'
        elif list[i] == '0010': #2
            list[i] = '0101'
        elif list[i] == '0011': #3
            list[i] = '0100'
        elif list[i] == '0100': #4
            list[i] = '1000'
        elif list[i] == '0101': #5
            list[i] = '0001'
        elif list[i] == '0110': #6
            list[i] = '1111'
        elif list[i] == '0111': #7
            list[i] = '0110'
        elif list[i] == '1000': #8
            list[i] = '0011'
        elif list[i] == '1001': #9
            list[i] = '0010'
        elif list[i] == '1010': #10
            list[i] = '1100'
        elif list[i] == '1011': #11
            list[i] = '0111'
        elif list[i] == '1100': #12
            list[i] = '1011'
        elif list[i] == '1101': #13
            list[i] = '1110'
        elif list[i] == '1110': #14
            list[i] = '1010'
        else:
            list[i] = '0000'
    return list


bits_by4_2_s11 = s_11(bits_by4_2_s10)
print(bits_by4_2_s11)

def s_12(list):
    for i in range(3,len(list),4):
        if list[i] == '0000':  #0
            list[i] = '1000'
        elif list[i] == '0001': #1
            list[i] = '1110'
        elif list[i] == '0010': #2
            list[i] = '1001'
        elif list[i] == '0011': #3
            list[i] = '0011'
        elif list[i] == '0100': #4
            list[i] = '1111'
        elif list[i] == '0101': #5
            list[i] = '0100'
        elif list[i] == '0110': #6
            list[i] = '0000'
        elif list[i] == '0111': #7
            list[i] = '1101'
        elif list[i] == '1000': #8
            list[i] = '1011'
        elif list[i] == '1001': #9
            list[i] = '0110'
        elif list[i] == '1010': #10
            list[i] = '1100'
        elif list[i] == '1011': #11
            list[i] = '0101'
        elif list[i] == '1100': #12
            list[i] = '0111'
        elif list[i] == '1101': #13
            list[i] = '0001'
        elif list[i] == '1110': #14
            list[i] = '1010'
        else:
            list[i] = '0010'
    return list


bits_by4_2_s12 = s_12(bits_by4_2_s11)
print(bits_by4_2_s12)

for i in range(0, len(bits_by4_2_s12), 2):
    bits_by4_2_s12[i] += bits_by4_2_s12[i+1]


del bits_by4_2_s12[1:len(bits_by4_2_s12):2]


for i in range(0, len(bits_by4_2_s12)-1, 2):
    bits_by4_2_s12[i] += bits_by4_2_s12[i+1]

del bits_by4_2_s12[1:len(bits_by4_2_s12):2]
print(bits_by4_2_s12)

used_for_p_3 = ([list(i) for i in bits_by4_2_s12])
print(used_for_p_3)

for listed_2 in used_for_p_3:
    listed_2[0], listed_2[1], listed_2[2], listed_2[3], listed_2[4], listed_2[5], listed_2[6], listed_2[7], listed_2[8], listed_2[9], listed_2[10], listed_2[11], listed_2[
        12], listed_2[13], listed_2[14], listed_2[15] = listed_2[1], listed_2[9], listed_2[0], listed_2[6], listed_2[7], listed_2[10], listed_2[4], listed_2[5], \
                                                        listed_2[14], listed_2[2], listed_2[13], listed_2[15], listed_2[12], listed_2[8], listed_2[3], listed_2[11]

print(used_for_p_3)

counter_3=''
for row in used_for_p_3:
    f_3 = (''.join([str(elem) for elem in row]))
    counter_3 += f_3

bits_string_round_3 = counter_3
print('Крайняя остановочка    '  +bits_string_round_3 + '   Крайняя остановочка')

# Начало обратных преобразований

STEP_1 = 16

#print(len(bits_string_round_3))

bits_by16_back = [bits_string_round_3[index:index+STEP_1] for index in range(0, len(bits_string_round_3), STEP_1)]
print(bits_by16_back)


bits_list_back_P3 = ([list(i) for i in bits_by16_back])
print(bits_list_back_P3)

for listed_4 in bits_list_back_P3:
    listed_4[1], listed_4[9], listed_4[0], listed_4[6], listed_4[7], listed_4[10], listed_4[4], listed_4[5], \
    listed_4[14], listed_4[2], listed_4[13], listed_4[15], listed_4[12], listed_4[8], listed_4[3], listed_4[11] = listed_4[0], listed_4[1], listed_4[2], listed_4[3], listed_4[4], listed_4[5], listed_4[6], listed_4[7], listed_4[8], listed_4[9], listed_4[10], listed_4[11], listed_4[12], listed_4[13], listed_4[14], listed_4[15]

print(bits_list_back_P3)

counter_4 = ''
for row in bits_list_back_P3:
    f_4 = (''.join([str(elem) for elem in row]))
    counter_4 += f_4

bits_list_back_try = counter_4
print(bits_list_back_try)

#print(len(res))

bits_by4_back_try_1 = [bits_list_back_try[index:index+STEP] for index in range(0, len(bits_list_back_try), STEP)]
print(bits_by4_back_try_1)


def s_9_back(list):
    for i in range(0,len(list),4):
        if list[i] == '0011':  #0
            list[i] = '0000'
        elif list[i] == '0000': #1
            list[i] = '0001'
        elif list[i] == '1010': #2
            list[i] = '0010'
        elif list[i] == '0110': #3
            list[i] = '0011'
        elif list[i] == '1011': #4
            list[i] = '0100'
        elif list[i] == '0100': #5
            list[i] = '0101'
        elif list[i] == '1001': #6
            list[i] = '0110'
        elif list[i] == '1100': #7
            list[i] = '0111'
        elif list[i] == '0101': #8
            list[i] = '1000'
        elif list[i] == '1111': #9
            list[i] = '1001'
        elif list[i] == '0001': #10
            list[i] = '1010'
        elif list[i] == '1110': #11
            list[i] = '1011'
        elif list[i] == '1101': #12
            list[i] = '1100'
        elif list[i] == '0111': #13
            list[i] = '1101'
        elif list[i] == '0010': #14
            list[i] = '1110'
        elif list[i] == '1000':  # 15
            list[i] = '1111'
    return list


bits_by4_back_s9 = s_9_back(bits_by4_back_try_1)
print(bits_by4_back_s9)


def s_10_back(list):
    for i in range(1,len(list),4):
        if list[i] == '1100':  #0
            list[i] = '0000'
        elif list[i] == '1000' : #1
            list[i] = '0001'
        elif list[i] == '0110': #2
            list[i] = '0010'
        elif list[i] == '1111': #3
            list[i] = '0011'
        elif list[i] == '1110': #4
            list[i] = '0100'
        elif list[i] == '0000': #5
            list[i] = '0101'
        elif list[i] == '0011': #6
            list[i] = '0110'
        elif list[i] == '1101': #7
            list[i] = '0111'
        elif list[i] == '0111': #8
            list[i] = '1000'
        elif list[i] == '0010': #9
            list[i] = '1001'
        elif list[i] == '1011': #10
            list[i] = '1010'
        elif list[i] == '0001': #11
            list[i] = '1011'
        elif list[i] == '1010': #12
            list[i] = '1100'
        elif list[i] == '0101': #13
            list[i] = '1101'
        elif list[i] == '1001': #14
            list[i] = '1110'
        else:
            list[i] = '1111'
    return list

bits_by4_back_s10 = s_10_back(bits_by4_back_s9)
print(bits_by4_back_s10)

def s_11_back(list):
    for i in range(2,len(list),4):
        if list[i] == '1101':  #0
            list[i] = '0000'
        elif list[i] == '1001': #1
            list[i] = '0001'
        elif list[i] == '0101': #2
            list[i] = '0010'
        elif list[i] == '0100': #3
            list[i] = '0011'
        elif list[i] == '1000': #4
            list[i] = '0100'
        elif list[i] == '0001': #5
            list[i] = '0101'
        elif list[i] == '1111': #6
            list[i] = '0110'
        elif list[i] == '0110': #7
            list[i] = '0111'
        elif list[i] == '0011': #8
            list[i] = '1000'
        elif list[i] == '0010': #9
            list[i] = '1001'
        elif list[i] == '1100': #10
            list[i] = '1010'
        elif list[i] == '0111': #11
            list[i] = '1011'
        elif list[i] == '1011': #12
            list[i] = '1100'
        elif list[i] == '1110': #13
            list[i] = '1101'
        elif list[i] == '1010': #14
            list[i] = '1110'
        else:
            list[i] = '1111'
    return list

bits_by4_back_s11 = s_11_back(bits_by4_back_s10)
print(bits_by4_back_s11)

def s_12_back(list):
    for i in range(3,len(list),4):
        if list[i] == '1000':  #0
            list[i] = '0000'
        elif list[i] == '1110': #1
            list[i] = '0001'
        elif list[i] == '1001': #2
            list[i] = '0010'
        elif list[i] == '0011': #3
            list[i] = '0011'
        elif list[i] == '1111': #4
            list[i] = '0100'
        elif list[i] == '0100': #5
            list[i] = '0101'
        elif list[i] == '0000': #6
            list[i] = '0110'
        elif list[i] == '1101': #7
            list[i] = '0111'
        elif list[i] == '1011': #8
            list[i] = '1000'
        elif list[i] == '0110': #9
            list[i] = '1001'
        elif list[i] == '1100': #10
            list[i] = '1010'
        elif list[i] == '0101': #11
            list[i] = '1011'
        elif list[i] == '0111': #12
            list[i] = '1100'
        elif list[i] == '0001': #13
            list[i] = '1101'
        elif list[i] == '1010': #14
            list[i] = '1110'
        else:
            list[i] = '1111'
    return list

bits_by4_back_s12 = s_12_back(bits_by4_back_s11)
print(bits_by4_back_s12)

counter_5 = ''
for row in bits_by4_back_s12:
    f_5 = (''.join([str(elem) for elem in row]))
    counter_5 += f_5

bits_P2_back = counter_5



bits_by16_back_2 = [bits_P2_back[index:index+STEP_1] for index in range(0, len(bits_P2_back), STEP_1)]
print(bits_by16_back_2)

bits_list_back_P2 = ([list(i) for i in bits_by16_back_2])
print(bits_list_back_P2)

for listed_5 in bits_list_back_P2:
     listed_5[8], listed_5[3], listed_5[9], listed_5[13], listed_5[1], listed_5[14], listed_5[4], listed_5[10],listed_5[2], listed_5[7], listed_5[12], listed_5[5], listed_5[11], listed_5[15], listed_5[0], listed_5[6] = listed_5[0], listed_5[1], listed_5[2], listed_5[3], listed_5[4], listed_5[5], listed_5[6], listed_5[7], listed_5[8], listed_5[9], listed_5[10], listed_5[11], listed_5[12], listed_5[13], listed_5[14], listed_5[15]

print(bits_list_back_P2)

counter_6 = ''
for row in bits_list_back_P2:
    f_6 = (''.join([str(elem) for elem in row]))
    counter_6 += f_6

bits_s4_s8 = counter_6
print(bits_s4_s8)

bits_by4_back_s4_s8 = [bits_s4_s8[index:index+STEP] for index in range(0, len(bits_s4_s8), STEP)]
print(bits_by4_back_s4_s8)

def s_5_back(list):
    for i in range(0,len(list),4):
        if list[i] == '1101': #0
            list[i] = '0000'
        elif list[i] == '0000': #1
            list[i] = '0001'
        elif list[i] == '1001': #2
            list[i] = '0010'
        elif list[i] == '1110': #3
            list[i] = '0011'
        elif list[i] == '1010': #4
            list[i] = '0100'
        elif list[i] == '1011': #5
            list[i] = '0101'
        elif list[i] == '0101': #6
            list[i] = '0110'
        elif list[i] == '1000': #7
            list[i] = '0111'
        elif list[i] == '0100': #8
            list[i] = '1000'
        elif list[i] == '0110': #9
            list[i] = '1001'
        elif list[i] == '1100': #10
            list[i] = '1010'
        elif list[i] == '1111': #11
            list[i] = '1011'
        elif list[i] == '0001': #12
            list[i] = '1100'
        elif list[i] == '0111': #13
            list[i] = '1101'
        elif list[i] == '0010': #14
            list[i] = '1110'
        elif list[i] == '0011': #14
            list[i] = '1111'
    return(list)



bits_by4_back_s5 = s_5_back(bits_by4_back_s4_s8)
print(bits_by4_back_s5)


def s_6_back(list):
    for i in range(1, len(list), 4):
        if list[i] == '0111':  # 0
            list[i] = '0000'
        elif list[i] == '0101':  # 1
            list[i] = '0001'
        elif list[i] == '0001':  # 2
            list[i] = '0010'
        elif list[i] == '1011':  # 3
            list[i] = '0011'
        elif list[i] == '0110':  # 4
            list[i] = '0100'
        elif list[i] == '1001':  # 5
            list[i] = '0101'
        elif list[i] == '1000':  # 6
            list[i] = '0110'
        elif list[i] == '0000':  # 7
            list[i] = '0111'
        elif list[i] == '1101':  # 8
            list[i] = '1000'
        elif list[i] == '1110':  # 9
            list[i] = '1001'
        elif list[i] == '0011':  # 10
            list[i] = '1010'
        elif list[i] == '1010':  # 11
            list[i] = '1001'
        elif list[i] == '0010':  # 12
            list[i] = '1100'
        elif list[i] == '1100':  # 13
            list[i] = '1101'
        elif list[i] == '1111':  # 14
            list[i] = '1110'
        elif list[i] == '0100':  # 14
            list[i] = '1111'
    return list



bits_by4_back_s6 = s_6_back(bits_by4_back_s5)
print(bits_by4_back_s6)


def s_7_back(list):
    for i in range(2, len(list), 4):
        if list[i] == '0010':  # 0
            list[i] = '0000'
        elif list[i] == '1010':  # 1
            list[i] = '0001'
        elif list[i] == '1111':  # 2
            list[i] = '0010'
        elif list[i] == '1001':  # 3
            list[i] = '0011'
        elif list[i] == '0011':  # 4
            list[i] = '0100'
        elif list[i] == '1110':  # 5
            list[i] = '0101'
        elif list[i] == '0110':  # 6
            list[i] = '0110'
        elif list[i] == '1011':  # 7
            list[i] = '0111'
        elif list[i] == '0111':  # 8
            list[i] = '1000'
        elif list[i] == '0001':  # 9
            list[i] = '1001'
        elif list[i] == '0101':  # 10
            list[i] = '1010'
        elif list[i] == '1101':  # 11
            list[i] = '1011'
        elif list[i] == '1000':  # 12
            list[i] = '1100'
        elif list[i] == '1100':  # 13
            list[i] = '1101'
        elif list[i] == '0000':  # 14
            list[i] = '1110'
        elif list[i] == '0100':  # 15
            list[i] = '1111'
    return list


bits_by4_back_s7 = s_7_back(bits_by4_back_s6)
print(bits_by4_back_s7)


def s_8_back(list):
    for i in range(3, len(list), 4):
        if list[i] == '1011':  # 0
            list[i] = '0000'
        elif list[i] == '1001':  # 1
            list[i] = '0001'
        elif list[i] == '0110':  # 2
            list[i] = '0010'
        elif list[i] == '1100':  # 3
            list[i] = '0011'
        elif list[i] == '0010':  # 4
            list[i] = '0100'
        elif list[i] == '0111':  # 5
            list[i] = '0101'
        elif list[i] == '0001':  # 6
            list[i] = '0110'
        elif list[i] == '1010':  # 7
            list[i] = '0111'
        elif list[i] == '1101':  # 8
            list[i] = '1000'
        elif list[i] == '1110':  # 9
            list[i] = '1001'
        elif list[i] == '0000':  # 10
            list[i] = '1010'
        elif list[i] == '1000':  # 11
            list[i] = '1011'
        elif list[i] == '0011':  # 12
            list[i] = '1100'
        elif list[i] == '0101':  # 13
            list[i] = '1101'
        elif list[i] == '1111':  # 14
            list[i] = '1110'
        elif list[i] == '0010':  # 14
            list[i] = '1111'
    return list

bits_by4_back_s8 = s_8_back(bits_by4_back_s7)
print(bits_by4_back_s8)

counter_7 = ''
for row in bits_by4_back_s8:
    f_7 = (''.join([str(elem) for elem in row]))
    counter_7 += f_7
bits_for_p1 = counter_7
print(bits_for_p1)

bits_by16_back_p1 = [bits_for_p1[index:index+STEP_1] for index in range(0, len(bits_for_p1), STEP_1)]
print(bits_by16_back_p1)


bits_for_p1_1 = ([list(i) for i in bits_by16_back_p1])
print(bits_for_p1_1)

for listed in bits_for_p1_1:
    listed[5], listed[15], listed[7], listed[2], listed[13], listed[1], listed[4], listed[10], \
    listed[11], listed[6], listed[0], listed[14], listed[9], listed[12], listed[8], listed[3] = listed[0], listed[1], listed[2], listed[3], listed[4], listed[5], listed[6], listed[7], listed[8], listed[9], listed[10], listed[11], listed[12], listed[13], listed[14], listed[15]

print(bits_for_p1_1)

counter_8 = ''
for row in bits_for_p1_1:
    f_8 = (''.join([str(elem) for elem in row]))
    counter_8 += f_8

good_luck = counter_8
print(good_luck)


if good_luck.endswith('00000000'):
    Finally = good_luck[:-8]
    abc = Finally
    print(abc)
else:
    abc = good_luck



bits_by4_back_s0_s3 = [abc[index:index+STEP] for index in range(0, len(abc), STEP)]
print(bits_by4_back_s0_s3)



def s_4_back(list):
    for i in range(3, len(list), 4):
        if list[i] == '0110':  # 0
            list[i] = '0000'
        elif list[i] == '1001':  # 1
            list[i] = '0001'
        elif list[i] == '0111':  # 2
            list[i] = '0010'
        elif list[i] == '1100':  # 3
            list[i] = '0011'
        elif list[i] == '1111':  # 4
            list[i] = '0100'
        elif list[i] == '1010':  # 5
            list[i] = '0101'
        elif list[i] == '0001':  # 6
            list[i] = '0110'
        elif list[i] == '0011':  # 7
            list[i] = '0111'
        elif list[i] == '1000':  # 8
            list[i] = '1000'
        elif list[i] == '0000':  # 9
            list[i] = '1001'
        elif list[i] == '1011':  # 10
            list[i] = '1010'
        elif list[i] == '0010':  # 11
            list[i] = '1011'
        elif list[i] == '1110':  # 12
            list[i] = '1100'
        elif list[i] == '0101':  # 13
            list[i] = '1101'
        elif list[i] == '1101':  # 14
            list[i] = '1110'
        elif list[i] == '0100':  # 14
            list[i] = '1111'
    return list

bits_s4_back = s_4_back(bits_by4_back_s0_s3)
print(bits_s4_back)

def s_3_for_back(list):
    for i in range(2,len(list),4):
        if list[i] == '1110': #0
            list[i] = '0000'
        elif list[i] == '0111': #1
            list[i] = '0001'
        elif list[i] == '0101': #2
            list[i] = '0010'
        elif list[i] == '1010': #3
            list[i] = '0011'
        elif list[i] == '1011': #4
            list[i] = '0100'
        elif list[i] == '1000': #5
            list[i] = '0101'
        elif list[i] == '0000': #6
            list[i] = '0110'
        elif list[i] == '0011': #7
            list[i] = '0111'
        elif list[i] == '1101': #8
            list[i] = '1000'
        elif list[i] == '0110': #9
            list[i] = '1001'
        elif list[i] == '0001': #10
            list[i] = '1010'
        elif list[i] == '1111': #11
            list[i] = '1011'
        elif list[i] == '1100': #12
            list[i] = '1100'
        elif list[i] == '0100': #13
            list[i] = '1101'
        elif list[i] == '0010': #14
            list[i] = '1110'
        elif list[i] == '1001': #15
            list[i] = '1111'
    return(list)

bits_s3_back = s_3_for_back(bits_s4_back)
print(bits_s3_back)

def s_2_for_back(list):
    for i in range(1,len(list),4):
        if list[i] == '0011': #0
            list[i] = '0000'
        elif list[i] == '1110': #1
            list[i] = '0001'
        elif list[i] == '0110': #2
            list[i] = '0010'
        elif list[i] == '1111': #3
            list[i] = '0011'
        elif list[i] == '1001': #4
            list[i] = '0100'
        elif list[i] == '0100': #5
            list[i] = '0101'
        elif list[i] == '0010': #6
            list[i] = '0110'
        elif list[i] == '1010': #7
            list[i] = '0111'
        elif list[i] == '1100': #8
            list[i] = '1000'
        elif list[i] == '0001': #9
            list[i] = '1001'
        elif list[i] == '1101': #10
            list[i] = '1010'
        elif list[i] == '0000': #11
            list[i] = '1011'
        elif list[i] == '1000': #12
            list[i] = '1100'
        elif list[i] == '1011': #13
            list[i] = '1101'
        elif list[i] == '0111': #14
            list[i] = '1110'
        elif list[i] == '0101': #14
            list[i] = '1111'
    return(list)

bits_s2_back = s_2_for_back(bits_s3_back)
print(bits_s2_back)


def s_1_for_back(list):
    for i in range(0, len(list), 4):
        if list[i] == '0111':  # 0
            list[i] = '0000'
        elif list[i] == '0011':  # 1
            list[i] = '0001'
        elif list[i] == '1100':  # 2
            list[i] = '0010'
        elif list[i] == '1010':  # 3
            list[i] = '0011'
        elif list[i] == '0010':  # 4
            list[i] = '0100'
        elif list[i] == '0000':  # 5
            list[i] = '0101'
        elif list[i] == '0001':  # 6
            list[i] = '0110'
        elif list[i] == '1001':  # 7
            list[i] = '0111'
        elif list[i] == '0101':  # 8
            list[i] = '1000'
        elif list[i] == '1110':  # 9
            list[i] = '1001'
        elif list[i] == '0110':  # 10
            list[i] = '1010'
        elif list[i] == '1101':  # 11
            list[i] = '1011'
        elif list[i] == '1111':  # 12
            list[i] = '1100'
        elif list[i] == '0100':  # 13
            list[i] = '1101'
        elif list[i] == '1011':  # 14
            list[i] = '1110'
        elif list[i] == '1000':  # 14
            list[i] = '1111'
    return list

bits_s1_back = s_1_for_back(bits_s2_back)
print(bits_s1_back)

counter_final = ''
for row in bits_s1_back:
    f_final = (''.join([str(elem) for elem in row]))
    counter_final += f_final

FINAL_FORM = counter_final
print(FINAL_FORM)

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

print(text_from_bits(FINAL_FORM))