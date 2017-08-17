import codecs
from wand.image import Image
from PIL import Image as PI
import sys

import pyocr
import pyocr.builders
import io

def run_ocr(input_file,output_file):
    print("Running on ocr on " + input_file)

    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print("No OCR tool found")
        sys.exit(1)

    # The tools are returned in the recommended order of usage
    tool = tools[0]
    print("Will use tool '%s'" % (tool.get_name()))
    # Ex: Will use tool 'libtesseract'

    langs = tool.get_available_languages()
    #print("Available languages: %s" % ", ".join(langs))
    lang = langs[0]
    print("Will use lang '%s'" % (lang))

    builder = pyocr.builders.TextBuilder()
    req_image = []
    final_text = []

    # open PDF image and convert to PNG format
    image_pdf = Image(filename=input_file, resolution=300)
    image_jpeg = image_pdf.convert('jpeg')

    for img in image_jpeg.sequence:
        img_page = Image(image=img)
        req_image.append(img_page.make_blob('jpeg'))

    # loop through each page in required images
    for img in req_image: 
        txt = tool.image_to_string(
            PI.open(io.BytesIO(img)),
            lang=lang,
            builder=builder
        )
        final_text.append(txt)

    output_file= open(output_file, 'w')

    for item in final_text:
        output_file.write("%s\n" % item)
