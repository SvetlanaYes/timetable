def Cartesian(ar_list):
    if not ar_list:
        yield ()
    else:
        for a in ar_list[0]:
            for prod in Cartesian(ar_list[1:]):
                yield (a,)+prod