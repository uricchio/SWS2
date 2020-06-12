# this is a script that takes tblastx outfmt 7 and the
# subject sequence and returns a new fasta file that 
# has the matching sequences
import sys
evalThresh = float(sys.argv[1])
scaffs = {}


#functions for reverse complement
def comp(l):
    if l == "A":
       return "T"
    if l == "C":
       return "G"
    if l == "G":
       return "C"
    if l == "T":
       return "A"
    return

def rev_comp(s):
    s = s[::-1]
    ret_s = ''
    for i in range(0,len(s)):
        ret_s += comp(s[i])
    return ret_s


# function to translate to protein
def translate(seq): 
       
    table = { 
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                  
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L', 
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_', 
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W', 
    } 
    protein ="" 
    if len(seq)%3 == 0: 
        for i in range(0, len(seq), 3): 
            codon = seq[i:i + 3] 
            protein+= table[codon] 
    return protein 

# first get scaffolds and coords of the sequences we want according to E-value thresh
fh = open(sys.argv[2], 'r')
for line in fh:
    if line[0] == "#":
        continue
    
    data = line.strip().split()
    if float(data[10]) > evalThresh:
        continue

    st = int(data[8])
    end = int(data[9])
    rt = 0

    if int(data[8]) > int(data[9]):
        st = int(data[9])
        end = int(data[8])
        rt = 1

    if data[1] in scaffs:
        scaffs[data[1]].append([float(data[10]), st-1, end, rt])
    else:
        scaffs[data[1]] = [[float(data[10]), st-1, end, rt]]

#for scaff in scaffs:
#    print scaff, scaffs[scaff]

fh.close()
# next get the sequences for the scaffolds using the corrdinates

fh = open(sys.argv[3],'r')
scaff_seqs = {}

pr = 0
scaff = ''
for line in fh:
    if line[0] == ">":
        if line.strip()[1:] in scaffs:
            scaff = line.strip()[1:]  
            pr = 1
            continue
    if pr ==1 and line[0] != ">":
        if scaff in scaff_seqs:
            scaff_seqs[scaff]+=line.strip()
        else:
            scaff_seqs[scaff]=line.strip()
    if line[0] == ">" and pr == 1:
       pr = 0
       scaff = ''

# subset the sequences
for scaff in scaffs:
    print (">"+scaff)
    myseq = ''
    for coords in scaffs[scaff]:
        if coords[3] == 0:
            myseq += scaff_seqs[scaff][coords[1]:coords[2]]
        else:
            myseq += rev_comp(scaff_seqs[scaff][coords[1]:coords[2]])
    print (translate(myseq))



