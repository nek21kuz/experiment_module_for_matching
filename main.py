import math as m
import numpy as np

def rec(n, k, ind=0, s=0, lst=1):
    if s == n:
        if len(tmp_vec[:ind]) == k:
            full_splt_lst.append(tmp_vec[:ind])
        return
    for i in range(lst, n - s + 1):
        tmp_vec[ind] = i
        rec(n, k, ind + 1, s + i, i)

def splt(n, k):
    global tmp_vec, full_splt_lst
    full_splt_lst = list()
    tmp_vec = [0]*n  
    rec(n, k)
    return full_splt_lst

def fib(n):
    if n == 0:
        return 0 
    if n == 1:
        return 1
    fi1 = (1 + m.sqrt(5))/2
    fi2 = 1 - fi1
    return round(( fi1 ** n + (fi2) ** n ) / m.sqrt(5))

def p_rel_fib(path_lst):
    return np.prod(np.array([fib(i) for i in path_lst]))

def match_pf(path_lst):
    return np.prod(np.array([fib(i + 1) for i in path_lst]))

def match_p(n):
    return match_pf([n])

def match_t3(path_lst):
    f = match_pf([path_lst[0] + path_lst[1] + 1, path_lst[2]])
    s = match_pf([path_lst[0], path_lst[1], path_lst[2] - 1])

    return f + s

def match_t4(cp, path_lst):
    if cp == 1:
        f = match_t3(path_lst[0:3]) * match_p(path_lst[3])
        s = match_pf(path_lst[0:3] + [path_lst[3] - 1])
        
    elif cp == 2:
        f = match_pf([sum(path_lst[0:2]) + 1, sum(path_lst[2:4]) + 1])
        s = match_pf(path_lst)

    elif cp == 3:
        f = match_p(sum(path_lst[0:2]) + 1) * match_t3(path_lst[2:4] + [1])
        s = match_pf(path_lst[0:2] + [sum(path_lst[2:4]) + 1])

    elif cp >= 4:
        f = match_p(sum(path_lst[0:2]) + 1) * match_t3(path_lst[2:4] + [cp - 2])
        s = match_pf(path_lst[0:2]) * match_t3(path_lst[2:4] + [cp - 3])

    return f + s
    
