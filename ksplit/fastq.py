from collections import namedtuple

FastQSeq = namedtuple('FastQSeq', ['header', 'seq', 'qs'])

def fastq_iter1(ifile):
    '''
    for h, seq in fastq_iter1(open('example.fq', 'rb'))):
        print(h, seq)
    '''
    while True:
        h = ifile.readline()
        seq = ifile.readline()
        _ = ifile.readline()
        qs = ifile.readline()
        if not qs:
            break
        yield FastQSeq(h, seq.strip(), qs.strip())


def fastq_iter(base):
    '''
    Read in an interleaved FastQ as an iterator

    This is function supports optionally-interleaved format. It yields tuples
    of 1 or 2 sequences.

    Two adjacent reads are considered to form a pair if their headers are
    identical; otherwise they are considered single-end.

    Example
    -------

    for seqs in fastq_iter(open('interleaved.fq', 'rb')):
        if len(seqs) == 1:
            [s] = seqs
        else:
            [mate1, mate2] = seqs
    '''

    prev = None
    for seq in fastq_iter1(base):
        if prev is None:
            prev = seq
        elif prev.header != seq.header:
            yield (prev,)
            prev = seq
        else:
            yield (prev, seq)
            prev = None
    if prev is not None:
        yield (prev,)
