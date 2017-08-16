import codecs
from wand.image import Image
import sys

import pyocr
import pyocr.builders
import io

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)

# The tools are returned in the recommended order of usage
tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))
# Ex: Will use tool 'libtesseract'

langs = tool.get_available_languages()
print("Available languages: %s" % ", ".join(langs))
lang = langs[0]
print("Will use lang '%s'" % (lang))

builder = pyocr.builders.TextBuilder()


filename="THE_NATIONAL_MARINE_HABITAT_CLASSIFICATI.pdf"
 
#with Image(filename=filename) as img:
#     print('pages = ', len(img.sequence))
####      
#     with img.convert('png') as converted:
#         converted.save(filename='page.png')

# open PDF image and convert to PNG format
with(Image(filename=filename,resolution=200)) as source:
    images=source.sequence
    pages=len(images)
    print("num pages = "+pages)
    for i in range(pages):
        #Image(images[i]).save(filename=str(i)+'.png')
        #ilename="test.png"
        txt = tool.image_to_string(
            images[i],
            lang=lang,
            builder=builder
        )
        print(txt)

        with codecs.open("output.txt", 'w', encoding='utf-8') as file_descriptor:
            builder.write_file(file_descriptor, txt)



