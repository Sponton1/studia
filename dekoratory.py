def klucz(k:None):
    def dekorator(funkcja):
        def funkcja_dekorowana(seq):
            if k is None:
                return funkcja(seq)
            else:
                seq_k = [k(elem) for elem in seq]
                return funkcja(seq_k)
        return funkcja_dekorowana
    return dekorator

@klucz(abs)
def maximum(seq):
    return max(seq)

seq = [-5, 3, -1, 9, -4, 6, 100]
print(maximum(seq))
