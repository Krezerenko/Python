ex1 = '''
||<sect>
    opt tima_834:=#( `quza . `enen . `raed . `biri_572 );
</sect>,
<sect>
    opt usdige :=#(`soisso . `regeen . `edreed_145 );
</sect>,||
'''

ex2 = '''
|| <sect>
    opt eddi_333:=#( `orsoqu_70 . `raria . `geed );
</sect>,
<sect>
    opt teleat_951 := #( `georat . `ananen_726 . `edat . `abe_329);
</sect>,
<sect>
    opt qumale := #( `isbean . `sodiri );
</sect>, ||
'''


def main(text):
    sections = (text.strip().replace("opt", "").
                removesuffix("||").
                split("<sect>"))

    sections = [section.strip().replace("</sect>,", "")
                for section in sections[1:]]

    pairs = [tuple(section.strip().split(":=")) for section in sections]

    pairs = [(a.strip(),
              [elem.strip().replace("`", "") for elem in
               b.replace("#(", "").
               replace(");", "").
               split(".")]) for a, b in pairs]
    return pairs
