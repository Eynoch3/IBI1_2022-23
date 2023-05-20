#load an MLA document and create a minidom object using the xml.dom module
from xml.dom.minidom import parse
import xml.dom.minidom 
import re 
from openpyxl import Workbook,load_workbook

#using a XML file as an input
#to get all the element from the file go_obo.xml
#the go_obo.xml file is too large to upload to the giuHub, so I didn't upload this file
DOMTree=xml.dom.minidom.parse('go_obo.xml')
collection=DOMTree.documentElement
terms=collection.getElementsByTagName('term')

#create an Excel document to save the information
wb=Workbook()
ws=wb.active
ws.append(['id','name','definition','childnodes'])

#custom function to compute the childnodes
#store the result in 'count'
def childnodes(id):
    count = 0
    ids = [id]
    while ids:
        current_id = ids.pop()
        for term in terms:
            is_a = term.getElementsByTagName('is_a')
            for term_is_a in is_a:
                if term_is_a.firstChild.data == current_id:
                    ids.append(term.getElementsByTagName('id')[0].firstChild.data)
                    count +=1
    return count

#to print details of the terms
for term in terms:
  defstr=term.getElementsByTagName('defstr')[0]
  defstr.child=defstr.childNodes[0].data
  if re.search('autophagosome',str(defstr.child)):
   id=term.getElementsByTagName('id')[0]
   name=term.getElementsByTagName('name')[0]
   id.child=id.childNodes[0].data
   name.child=name.childNodes[0].data
   is_a=term.getElementsByTagName('is_a')[0]
   is_a.child=is_a.childNodes[0].data
   print ('id:',id.childNodes[0].data)
   a=childnodes(id.child)
   ws.append({1:str(id.child),2:str(name.child),3:str(defstr.child),4:str(a)})
wb.save('autophagosome.xlsx')
