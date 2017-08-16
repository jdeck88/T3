# T3: A Text-based Toolset for building Taxonomies

The Text-based Toolset for building Taxonomies (T3) is a proposed python package and virtual machine image whose purpose will be to aid in the processing of raw text (stored as PDFs, HTML, Text) for extracting keywords, assist with data cleanup of raw text files, and quickly build taxonomies (represented in the Web Ontology Language- OWL).  The word "taxonomy" used here broadly defines any classification of related words or phrases denoting a type of subsumption relationship or heirarchy of terms.   While there exists a myriad of tools for creating text from images, annotating text, cleaning up text, and building taxonomies from text, the processing steps are often disjoint and difficult to use.  The intended goal here is to streamline this process in a single accessible package, thereby accelerating the pace of work and lowering barriers for participation and development of the taxonomies themselves.  This work was initiated at the ClearEarth hackathon in Boulder, CO in August, 2017.

T3 has two intended outputs: 1) development of a python package and 2) development of a virtual machine (VM) image which containing a pre-built Linux based environment available through CyVerse Atmosphere. 

## The T3 pipeline
T3 follows a pipeline model for data processing with entry or exit at any point in the data processing chain.  The following contain the built-in functions:
   
1. OCR Source files
    Calls Python OCR software and converts to raw text.  Utilize https://github.com/openpaperwork/pyocr for OCR work.  NOTE: are their better python OCR packages?

2. Data Cleanup

    Some data cleanup difficulties encountered during the ClearEarth hackathon included easily scriptable functions, such as:
     * removing hard linebreaks in mid-sentence
     * automatically remove page headers, section headings, figure captions, references, and bibliographies
    
3. Keyword Extraction
   
    REF ClearEarth tools.  Need link to Ontoboot. Goal here is see if this is available for incorporation in pipeline here.
     
4. Build Taxonomy

    This step uses [ontopilot](https://github.com/stuckyb/ontopilot) project build ontologies from tabular data structures.  The appropriate tabular data structures are a product of the previous step.
    
5. Publication

    Step for quickly sharing or publishing results
    
## Software and dependencies

Python dependencies in `requirements.txt`. These can be installed by running `pip install -r requirements.txt`.

Additional dependencies:

* Java 8
* [ontopilot](https://github.com/stuckyb/ontopilot) (Will be propted to download during cli exectuion if not found)

## Intended Usage
Build a main entry point to run software immediately after downloading the source tree: e.g. `process.py` being a convenience wrapper script for running the app from the source tree.

Running from the process.py script -- define arguments here




   
