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
    if n == -1:
        return 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    fi1 = (1 + m.sqrt(5))/2
    fi2 = 1 - fi1
    val = round(( fi1 ** n + (fi2) ** n ) / m.sqrt(5))
    if n < 0:
        val = -val
    return val

def c_n(n):
    return fib(n+1) + fib(n-1)

def p_rel_fib(path_lst):
    return np.prod(np.array([fib(i) for i in path_lst]))

def match_pf(path_lst):
    return np.prod(np.array([fib(i + 1) for i in path_lst]))

def match_p(n):
    return match_pf([n])

def match_t3(a, b, c):
    return fib(a+b+c+2) - fib(a)*fib(b)*fib(c)

def match_t4(x, a, b, c, d):
    return fib(d+1)*match_t3(a, b, x+c+1) + fib(d)*fib(c+1)*match_t3(a, b, x)


def match_t3_old(path_lst):
    f = match_pf([path_lst[0] + path_lst[1] + 1, path_lst[2]])
    s = match_pf([path_lst[0], path_lst[1], path_lst[2] - 1])

    return f + s

def match_t4_old(cp, path_lst):
    if cp == 1:
        f = match_t3_old(path_lst[0:3]) * match_p(path_lst[3])
        s = match_pf(path_lst[0:3] + [path_lst[3] - 1])

    elif cp == 2:
        f = match_pf([sum(path_lst[0:2]) + 1, sum(path_lst[2:4]) + 1])
        s = match_pf(path_lst)

    elif cp == 3:
        f = match_p(sum(path_lst[0:2]) + 1) * match_t3_old(path_lst[2:4] + [1])
        s = match_pf(path_lst[0:2] + [sum(path_lst[2:4]) + 1])

    elif cp >= 4:
        f = match_p(sum(path_lst[0:2]) + 1) * match_t3_old(path_lst[2:4] + [cp - 2])
        s = match_pf(path_lst[0:2]) * match_t3_old(path_lst[2:4] + [cp - 3])

    return f + s

def tetta3(k, p, q):
    num_match = (fib(p+1) + fib(p-1))*(fib(k+q+1) + fib(q-1)*fib(k+1)) + \
                         fib(p)*(fib(k+q) + fib(q-1)*fib(k))
    return num_match

def tetta3_2(k, l, m):
    num_match = fib(k+l+m+1) + 3*fib(k+1)*fib(l-1)*fib(m-1) +\
                     fib(k+2)*(fib(l+m-2) + fib(l-1)*fib(m-1))
    return num_match

def tetta1(r, s, t):
     num_match = fib(r + s + t + 4) + fib(r-1)*fib(s-1)*fib(t-1)
     return num_match

def tetta2(p, q):
     num_match = fib(p+q) + fib(p+q-2) + fib(p-1)*fib(q-1)
     return num_match
