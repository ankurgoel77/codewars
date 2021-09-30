# https://www.codewars.com/kata/59f3956825d575e3330000a3/python

import re

letters = {
    "A":"A",
    "C":"C",
    "G":"G",
    "T":"T",
    "R":"[GA]",
    "Y":"[CT]",
    "M":"[AC]",
    "K":"[GT]",
    "S":"[GC]",
    "W":"[AT]",
    "B":"[^A]",
    "D":"[^C]",
    "H":"[^G]",
    "V":"[^T]",
    "N":"[ACGT]"
}

def get_pos(base, strng, query):
    lines = base.splitlines()
    for line in lines[10:]:
        columns = line.split(" ")
        if columns[0] == query:
            for col in columns[1:]:
                if not col =="" and not col[0]=="(":
                    substr = col
            regex="".join([letters[c] for c in substr])
            matches = re.finditer(regex,strng,re.IGNORECASE)
            result = [str(match.start()+1) for match in matches]
            if len(result) == 0:
                return query + " is not in given string"
            else:
                return " ".join(result)
    return "This query name does not exist in given Base"

Base = """Version xxxx                                             
  
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= 
Partial Database   
http://... 
Copyright (c) All rights reserved. 
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= 
  
<>

AaaI (XmaIII)                     CGGCCG 
AacI (BamHI)                      GGATCC 
AaeI (BamHI)                      GGATCC 
AagI (ClaI)                       ATCGAT 
AaqI (ApaLI)                      GTGCAC 
AarI                              NNNNNNNNGCAGGTG 
AatI (StuI)                       AGGCCT 
AatII                             GACGTC 
AauI (Bsp1407I)                   TGTACA 
AbaI (BclI)                       TGATCA 
AbeI (BbvCI)                      CCTCAGC 
AbrI (XhoI)                       CTCGAG 
AcaI (AsuII)                      TTCGAA 
AcaII (BamHI)                     GGATCC 
AcaIII (MstI)                     TGCGCA 
AcaIV (HaeIII)                    GGCC 
AccI                              GTMKAC 
AccII (FnuDII)                    CGCG 
AccIII (BspMII)                   TCCGGA 
Acc16I (MstI)                     TGCGCA 
Acc36I (BspMI)                    ACCTGCNNNN 
Acc38I (EcoRII)                   CCWGG 
Acc65I (KpnI)                     GGTACC 
Acc113I (ScaI)                    AGTACT 
AccB1I (HgiCI)                    GGYRCC 
AccB2I (HaeII)                    RGCGCY 
AccB7I (PflMI)                    CCANNNNNTGG 
AccBSI (BsrBI)                    CCGCTC 
AccEBI (BamHI)                    GGATCC 
AceI (TseI)                       GCWGC 
AceII (NheI)                      GCTAGC 
AceIII                            CAGCTCNNNNNNN 
AciI                              CCGC 
AclI                              AACGTT 
AclNI (SpeI)                      ACTAGT 
AclWI (BinI)                      GGATCNNNN"""

Base1 = """Version yyyy                                             
  
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= 
Partial Database   
http://... 
Copyright (c) All rights reserved. 
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= 
  
<>

BasI (PflMI)                      CCANNNNNTGG
BauI (BsiI)                       CACGAG
BavI (PvuII)                      CAGCTG
BavAI (PvuII)                     CAGCTG
BavAII (AsuI)                     GGNCC
BavBI (PvuII)                     CAGCTG
BavBII (AsuI)                     GGNCC
BavCI (ClaI)                      ATCGAT
BazI (ClaI)                       ATCGAT
Bba179I (BetI)                    WCCGGW
BbeI (NarI)                       GGCGCC
BbeAI (NarI)                      GGCGCC
BbfI (XhoI)                       CTCGAG
Bbf7411I (BspMII)                 TCCGGA
BbiI (PstI)                       CTGCAG
BbiII (AcyI)                      GRCGYC
BbiIII (XhoI)                     CTCGAG
Bbi24I (MluI)                     ACGCGT
BbiDI (PvuRts1I)                  CNNNNNNNNNN
BbrI (HindIII)                    AAGCTT
Bbr7I (BbvII)                     GAAGACNNNNNNN
BbrAI (HindIII)                   AAGCTT
BbrPI (PmaCI)                     CACGTG
BbrUII (SalI)                     GTCGAC
BbrUIII (PstI)                    CTGCAG
BbsI (BbvII)                      GAAGACNN
BbtI (HhaI)                       GCGC
BbuI (SphI)                       GCATGC
BbvI                              GCAGCNNNNNNNN
BbvII                             GAAGACNN
Bbv12I (HgiAI)                    GWGCWC
Bbv16II (BbvII)                   GAAGACNN
BbvAI (XmnI)                      GAANNNNTTC
BbvAII (ClaI)                     ATCGAT"""

data="agatggcggcgctgaggggtcttgggggctctaggccggccacctactgg\
tttgcagcggagacgacgcatggggcctgcgcaataggagtacgctgcct\
gggaggcgtgactagaagcggaagtagttgtgggcgcctttgcaaccgcc\
tgggacgccgccgagtggtctgtgcaggttcgcgggtcgctggcgggggt\
cgtgagggagtgcgccgggagcggagatatggagggagatggttcagacc\
cagagcctccagatgccggggaggacagcaagtccgagaatggggagaat\
gcgcccatctactgcatctgccgcaaaccggacatcaactgcttcatgat\
cgggtgtgacaactgcaatgagtggttccatggggactgcatccggatca\
ctgagaagatggccaaggccatccgggagtggtactgtcgggagtgcaga\
gagaaagaccccaagctagagattcgctatcggcacaagaagtcacggga\
gcgggatggcaatgagcgggacagcagtgagccccgggatgagggtggag\
ggcgcaagaggcctgtccctgatccagacctgcagcgccgggcagggtca\
gggacaggggttggggccatgcttgctcggggctctgcttcgccccacaa\
atcctctccgcagcccttggtggccacacccagccagcatcaccagcagc\
agcagcagcagatcaaacggtcagcccgcatgtgtggtgagtgtgaggca\
tgtcggcgcactgaggactgtggtcactgtgatttctgtcgggacatgaa\
gaagttcgggggccccaacaagatccggcagaagtgccggctgcgccagt\
gccagctgcgggcccgggaatcgtacaagtacttcccttcctcgctctca\
ccagtgacgccctcagagtccctgccaaggccccgccggccactgcccac\
ccaacagcagccacagccatcacagaagttagggcgcatccgtgaagatg\
agggggcagtggcgtcatcaacagtcaaggagcctcctgaggctacagcc\
acacctgagccactctcagatgaggaccta"

data1="agatggcggcgctgaggggtcttgggggctctaggccggccacctactggtttgcagcgg\
agacgacgcatggggcctgcgcaataggagtacgctgcctgggaggcgtgactagaagcg\
gaagtagttgtgggcgcctttgcaaccgcctgggacgccgccgagtggtctgtgcaggtt\
cgcgggtcgctggcgggggtcgtgagggagtgcgccgggagcggagatatggagggagat\
ggttcagacccagagcctccagatgccggggaggacagcaagtccgagaatggggagaat\
gcgcccatctactgcatctgccgcaaaccggacatcaactgcttcatgatcgggtgtgac\
aactgcaatgagtggttccatggggactgcatccggatcactgagaagatggccaaggcc\
atccgggagtggtactgtcgggagtgcagagagaaagaccccaagctagagattcgctat\
cggcacaagaagtcacgggagcgggatggcaatgagcgggacagcagtgagccccgggat\
gagggtggagggcgcaagaggcctgtccctgatccagacctgcagcgccgggcagggtca\
gggacaggggttggggccatgcttgctcggggctctgcttcgccccacaaatcctctccg\
cagcccttggtggccacacccagccagcatcaccagcagcagcagcagcagatcaaacgg\
tcagcccgcatgtgtggtgagtgtgaggcatgtcggcgcactgaggactgtggtcactgt\
gatttctgtcgggacatgaagaagttcgggggccccaacaagatccggcagaagtgccgg\
ctgcgccagtgccagctgcgggcccgggaatcgtacaagtacttcccttcctcgctctca\
ccagtgacgccctcagagtccctgccaaggccccgccggccactgcccacccaacagcag\
ccacagccatcacagaagttagggcgcatccgtgaagatgagggggcagtggcgtcatca\
acagtcaaggagcctcctgaggctacagccacacctgagccactctcagatgaggaccta\
cctctggatcctgacctgtatcaggacttctgtgcaggggcctttgatgaccatggcctg\
ccctggatgagcgacacagaagagtccccattcctggaccccgcgctgcggaagagggca\
gtgaaagtgaagcatgtgaagcgtcgggagaagaagtctgagaagaagaaggaggagcga\
tacaagcggcatcggcagaagcagaagcacaaggataaatggaaacacccagagagggct\
gatgccaaggaccctgcgtcactgccccagtgcctggggcccggctgtgtgcgccccgcc\
cagcccagctccaagtattgctcagatgactgtggcatgaagctggcagccaaccgcatc\
tacgagatcctcccccagcgcatccagcagtggcagcagagcccttgcattgctgaagag\
cacggcaagaagctgctcgaacgcattcgccgagagcagcagagtgcccgcactcgcctt\
caggaaatggaacgccgattccatgagcttgaggccatcattctacgtgccaagcagcag\
gctgtgcgcgaggatgaggagagcaacgagggtgacagtgatgacacagacctgcagatc\
ttctgtgtttcctgtgggcaccccatcaacccacgtgttgccttgcgccacatggagcgc\
tgctacgccaagtatgagagccagacgtcctttgggtccatgtaccccacacgcattgaa\
ggggccacacgactcttctgtgatgtgtataatcctcagagcaaaacatactgtaagcgg\
ctccaggtgctgtgccccgagcactcacgggaccccaaagtgccagctgacgaggtatgc\
gggtgcccccttgtacgtgatgtctttgagctcacgggtgacttctgccgcctgcccaag\
cgccagtgcaatcgccattactgctgggagaagctgcggcgtgcggaagtggacttggag\
cgcgtgcgtgtgtggtacaagctggacgagctgtttgagcaggagcgcaatgtgcgcaca\
gccatgacaaaccgcgcgggattgctggccctgatgctgcaccagacgatccagcacgat\
cccctcactaccgacctgcgctccagtgccgaccgctgagcctcctggcccggacccctt\
acaccctgcattccagatgggggagccgcccggtgcccgtgtgtccgttcctccactcat\
ctgtttctccggttctccctgtgcccatccaccggttgaccgcccatctgcctttatcag\
agggactgtccccgtcgacatgttcagtgcctggtggggctgcggagtccactcatcctt\
gcctcctctccctgggttttgttaataaaattttgaagaaaccaaaaaaaaaaaaaaaaa\
aaaaaaaaaaaaaaaaaaaaaaaaaaa"


s = "GCAGCaGCAGCgatggcggcgctgaggggtcttgggggctctaggccggccacctactgg"
q = "AcaIV"
print( get_pos(Base,data,q))