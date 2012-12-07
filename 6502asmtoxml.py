import sys
import elementtree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, Comment, tostring



comment_list = []
line_list = []

def convert_asm(asm_file):
    asm_file = open(asm_file, "r")

    for line in asm_file:
        if line[0] == ";":
            comment_list.append(line)
           
        if line[0] == ' ':
            line_list.append(line[1:5])
            
            

def make_xml():
    root = ET.Element('sixfivezerotwo')

    if comment_list:
        multiLineComment = ET.SubElement(root, 'multiLineComment')
        multiLineComment.text = ''.join(comment_list)

    if line_list:
        for line in line_list:
            lineNode = ET.SubElement(root, 'line')
            mnemonicNode = ET.SubElement(lineNode, 'mnemonic')
            mnemonicNode.text = line        

    tree = ET.ElementTree(root)
    
   

    tree.write("gen6502example.xml", encoding="utf-8")


convert_asm("sample6502.asm")
make_xml()

    
        
