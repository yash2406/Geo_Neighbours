def geoHash(lt, ln):
    lat = lt
    lng = ln
    lis = []
    for lower_case_alphabets in range(0, 26):
        char = chr(lower_case_alphabets + 97)
        if char == 'a' or char == 'i' or char == 'l' or char == 'o':
            continue
        lis.append(char)

    low_lat = -90.0
    high_lat = 90.0
    low_lng = -180.0
    high_lng = 180.0
    lat_req = 17
    lng_req = 18
    lat_ans = ""
    lng_ans = ""
    bit_hash = ""
    for i in range(0, lat_req):
        mid = (low_lat + high_lat) / 2
        if low_lat <= lat <= mid:
            lat_ans = lat_ans + "0"
            high_lat = mid
        else:
            lat_ans = lat_ans + "1"
            low_lat = mid

    for i in range(0, lng_req):
        mid = (low_lng + high_lng) / 2
        if low_lng <= lng <= mid:
            lng_ans = lng_ans + "0"
            high_lng = mid
        else:
            lng_ans = lng_ans + "1"
            low_lng = mid

    cur_lat_bit = 0
    cur_lng_bit = 0
    for bit in range(0, 35):
        if bit % 2 == 1:
            bit_hash = bit_hash + lat_ans[cur_lat_bit]
            cur_lat_bit = cur_lat_bit + 1
        else:
            bit_hash = bit_hash + lng_ans[cur_lng_bit]
            cur_lng_bit = cur_lng_bit + 1

    hash_string = ""
    for char in range(0, 7):
        power_of_two = 1
        char_val = 0
        for bit in range(char * 5 + 4, char * 5 - 1, -1):
            char_val = char_val + (power_of_two * int(bit_hash[bit]))
            power_of_two = power_of_two * 2
        if char_val <= 9:
            hash_string = hash_string + str(char_val)
        else:
            char_val -= 10
            hash_string = hash_string + lis[char_val]

    return hash_string
