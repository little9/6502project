# 6502 Schema 

This is a RelaxNG XML schema specification for 6502 assembly language documents. The goal of this project is to create a schema that can take advantge of XML tools and also be useful for digital preservation purposes.

The schema is based on the [MOS Technology 6500 Series Programming Manual](http://bytecollector.com/archive/misc/6500-50A_MCS6500pgmManJan76.pdf).



## Document modeling files

*6502schema.rng* - This is the schema itself

*sample6502.xml* - An encoded document 

## Document processing files

*6502xslt.xsl* - Beginning work on an XSLT to output asm from encoded documents

*6502asmtoxml.py* - Beginning work on a Python script to encode asm files 

