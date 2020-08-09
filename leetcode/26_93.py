#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
93. 复原IP地址
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

有效的 IP 地址正好由四个整数（每个整数位于 0 到 255 之间组成），整数之间用 '.' 分隔。

示例:

输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]

"""

def check_item(x):
    x_int = map(int, x)
    return (x_int[0] >= 0 and x_int[0] <= 255 and str(x_int[0]) == x[0]) and \
            (x_int[1] >= 0 and x_int[1] <= 255 and str(x_int[1]) == x[1]) and \
            (x_int[2] >= 0 and x_int[2] <= 255 and str(x_int[2]) == x[2]) and \
            (x_int[3] >= 0 and x_int[3] <= 255 and str(x_int[3]) == x[3])


def restore_ip_addresses(s):
    d_length = {
         4: ['1.1.1.1'],
         5: ['2.1.1.1', '1.2.1.1', '1.1.2.1', '1.1.1.2'],
         6: ['3.1.1.1', '2.2.1.1', '2.1.2.1', '2.1.1.2', '1.3.1.1', '1.2.2.1', '1.2.1.2', '1.1.3.1', '1.1.2.2', '1.1.1.3'],
         7: ['3.2.1.1', '3.1.2.1', '3.1.1.2', '2.3.1.1', '2.2.2.1', '2.2.1.2', '2.1.3.1', '2.1.2.2', '2.1.1.3', '1.3.2.1', '1.3.1.2', '1.2.3.1', '1.2.2.2', '1.2.1.3', '1.1.3.2', '1.1.2.3'],
         8: ['3.3.1.1', '3.2.2.1', '3.2.1.2', '3.1.3.1', '3.1.2.2', '3.1.1.3', '2.3.2.1', '2.3.1.2', '2.2.3.1', '2.2.2.2', '2.2.1.3', '2.1.3.2', '2.1.2.3', '1.3.3.1', '1.3.2.2', '1.3.1.3', '1.2.3.2', '1.2.2.3', '1.1.3.3'],
         9: ['3.3.2.1', '3.3.1.2', '3.2.3.1', '3.2.2.2', '3.2.1.3', '3.1.3.2', '3.1.2.3', '2.3.3.1', '2.3.2.2', '2.3.1.3', '2.2.3.2', '2.2.2.3', '2.1.3.3', '1.3.3.2', '1.3.2.3', '1.2.3.3'],
        10: ['3.3.3.1', '3.3.2.2', '3.3.1.3', '3.2.3.2', '3.2.2.3', '3.1.3.3', '2.3.3.2' ,'2.3.2.3', '2.2.3.3', '1.3.3.3'],
        11: ['3.3.3.2', '3.3.2.3', '3.2.3.3', '2.3.3.3'],
        12: ['3.3.3.3']
    }
    length = len(s)
    result_list = []
    for d in d_length[length]:
        d_list = map(int, d.split('.'))
        i = 0
        temp = []
        for v in d_list:
            t = s[i:i+v]
            temp.append(t)
            i += v
        result_list.append(temp)
    result_list = filter(check_item, result_list)
    result = []
    for r in result_list:
        result.append('.'.join(r))
    return result

# print(restore_ip_addresses("25525511135"))
# print(restore_ip_addresses("010010"))

"""
[], '25525511135'
    4 - 12
    ['2'], '5525511135'  return None
    ['25'], '525511135'  return None
    ['255'], '25511135'  return [['255', '255', '11', '135'], ['255', '255', '111', '35']]
    return [['255', '255', '11', '135'], ['255', '255', '111', '35']]

['2'], '5525511135'
    3 - 9
    return None

['25'], '525511135'
    ['25', '5'], '25511135'  return None
    ['25', '52'], '5511135'  return None
    return None

['255'], '25511135'
    ['255', '2'], '5511135'  return None
    ['255', '25'], '511135'  return None
    ['255', '255'], '11135'  return [['255', '255', '11', '135'], ['255', '255', '111', '35']]
    return [['255', '255', '11', '135'], ['255', '255', '111', '35']]

['25', '5'], '25511135'
    2 - 6
    return None

['25', '52'], '5511135'
    2 - 6
    return None

['255', '2'], '5511135'
    2 - 6
    return None

['255', '25'], '511135'
    ['255', '25', '5'], '11135'  return None
    ['255', '25', '51'], '1135'  return None
    return None

['255', '255'], '11135'
    ['255', '255', '1'], '1135'  return None
    ['255', '255', '11'], '135'  return ['255', '255', '11', '135']
    ['255', '255', '111'], '35'  return ['255', '255', '111', '35']
    return [['255', '255', '11', '135'], ['255', '255', '111', '35']]

['255', '25', '5'], '11135'
    1 - 3
    return None

['255', '25', '51'], '1135'
    1 - 3
    return None

['255', '255', '1'], '1135'
    1 - 3
    return None

['255', '255', '11'], '135'
    return [['255', '255', '11', '135']]

['255', '255', '111'], '35'
    return [['255', '255', '111', '35']]

"""

def restore_ip(ip_list, s):
    result = []
    length = len(s)
    length_list = len(ip_list)  # 0, 1, 2, 3

    if length_list == 3:
        if length > 0 and int(s) >= 0 and int(s) <= 255 and str(int(s)) == s:
            ip_list.append(s)
            return [ip_list]
        else:
            return None

    """
    1 3
    0 -> 4 - 12 (4-0)*1 (4-0)*3
    1 -> 3 - 9 (4-1)*1 (4-1)*3
    2 -> 2 - 6 (4-2)*1 (4-2)*3
    """
    if length < ((4 - length_list) * 1) or length > ((4 - length_list) * 3):
        return None
    one = s[0:1]
    one_list = None
    if int(one) >= 0 and int(one) <= 255 and str(int(one)) == one:
        temp = ip_list[:]
        temp.append(one)
        one_list = restore_ip(temp, s[1:])

    two = s[0:2]
    two_list = None
    if int(two) >= 0 and int(two) <= 255 and str(int(two)) == two:
        temp = ip_list[:]
        temp.append(two)
        two_list = restore_ip(temp, s[2:])

    three = s[0:3]
    three_list = None
    if int(three) >= 0 and int(three) <= 255 and str(int(three)) == three:
        temp = ip_list[:]
        temp.append(three)
        three_list = restore_ip(temp, s[3:])

    if one_list is not None:
        result.extend(one_list)

    if two_list is not None:
        result.extend(two_list)

    if three_list is not None:
        result.extend(three_list)

    return result



def restore_ip_addresses_other(s):
    length = len(s)
    if length < 4 or length > 12:
        return None
    return restore_ip([], s)

print(restore_ip_addresses_other("25525511135"))
print(restore_ip_addresses_other("010010"))
