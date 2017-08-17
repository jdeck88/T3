# T3: A Toolset for processing Text and building Taxonomies

This work was initiated at the ClearEarth hackathon in Boulder, CO in August, 2017.

A Toolset for processing Text and building Taxonomies (T3) is a proposed python package and virtual machine image whose purpose will 
be to aid in the processing of raw text (stored as PDFs, HTML, Text) quickly extract keywords, discover relationships, and build taxonomies (represented in the Web Ontology Language- OWL).  The word "taxonomy" used here broadly defines any classification of related words or phrases denoting a 
type of subsumption relationship or heirarchy of terms.   While there exists a myriad of tools for creating text from images, 
annotating text, cleaning up text, and building taxonomies or ontologies, the processing steps are often disjoint and difficult 
to use.  The intended goal here is to streamline this process in a single accessible package, thereby accelerating the pace of 
work and lowering barriers for participation.  

T3 currently has two intended outputs: 1) development of a python package and 2) development of a virtual machine (VM) image 
which containing a pre-built Linux based environment available through CyVerse Atmosphere. 


```
usage: process.py [-h]
                  [ocr,cleanup,keywords,discovery,build_owl] input_file
                  output_file

T3: A Toolset for processing Text and building Taxonomies

positional arguments:
  [ocr,cleanup,keywords,discovery,build_owl]
                        Choose one of the following options:
                        ocr,cleanup,keywords,discovery,build_owl
  input_file            Input PDF file location
  output_file           Output Text file location

optional arguments:
  -h, --help            show this help message and exit
```
   
The following sections describe what each of the steps do in the process.py script:

## ocr
    
Take harvested PDF files and convert them to readable text.  Sample ocr python script for PDF files.
    
``` 
python process.py ocr sample/input/sample.pdf sample/output/sample_ocr.txt
```

Package Options:
  * [pyocr](https://github.com/openpaperwork/pyocr) works well but is slow.
  * others?

## cleanup

No actual cleanup scripts here yet

Data cleanup tasks encountered during the ClearEarth hackathon include removing hard linebreaks in mid-sentence, 
page headers, section headings, figure captions, references, and bibliographies.  Doing these tasks by hands is time consuming.  
Brian Stucky has started on development of tools for this step and i'm sure others have useful scripts.
    
## keywords
   
No actual keyword generation scripts here yet 

From Brian Stucky's work, the keyword generation works best when guided by words harvested from an index.  Brian's work is available at his [github repository)[https://gitlab.com/stuckyb/gkphrases]

Packages Tested: Visited rake-nltk package but did not find to be useful

     
## discovery
    
Automated subsumption relationship discovery relying on previously acquired training set data. The following script should theoretically work, assuming the clearOnto website is up:

```
python process.py discovery sample/output/sample_ocr.txt sample/output/sample_discovery.csv 
```
Output of this command is a tab-separated value (TSV) listing of parent/child relationships between terms.

Packages Tested:
     *  clearOnto website-- in development.  The current package relies on screen-scraping output and generating text.  This is a super brittle approach, just for demostration.  What we're demonstrating here is some of the expected outputs.
    
## build_owl

 Automatically build OWL files and setup project for further work using a simple parent/child CSV file.  The goal for this step is to take a single CSV file with the correct information and we can setup an ontology build project.  In an ideal world, we pipe information from the discovery section into this script.  [Ontopilot](https://github.com/stuckyb/ontopilot) was used for testing automated ontology building by starting with a single CSV file defining parent/child relationships.   The following are steps take to run this (ontopilot software must be downloaded and installed first):

```
ontopilot init
cp {a CSV file with class relationships} src/entities/sample_classes_1.csv
ontopilot make ontology
```

A sample of this was run on files in this repository using the input file (sample_classes_1.csv) with the output file [sample_classes-raw.owl](https://raw.githubusercontent.com/jdeck88/T3/master/sample/ontopilot_sample_class/ontology/sample_classes-raw.owl) 

Another sample file using only instance with input file [sample_individuals_1.csv](https://github.com/jdeck88/T3/blob/master/sample/ontopilot_individual_class/src/entities/sample_individuals_1.csv) and output file  [sample_individuals-raw.owl](https://raw.githubusercontent.com/jdeck88/T3/master/sample/ontopilot_individual_class/ontology/ontopilot_individual-raw.owl

    
## Software and dependencies

Python dependencies in `requirements.txt`. These can be installed by running `pip install -r requirements.txt`.

Additional dependencies:

* Java 8
* [ontopilot](https://github.com/stuckyb/ontopilot) (Will be propted to download during cli exectuion if not found)

## Intended Usage
Build a main entry point to run software immediately after downloading the source tree: e.g. `process.py` being a convenience wrapper 
script for running the app from the source tree.

Running from the process.py script -- define arguments here
