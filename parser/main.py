from pathlib import Path
import fnmatch
import os

from parser import TrademarkParser, DesignParser

def main():
    print("Parsing trademark files files..")
    
    # Parse trademark files
    for path in get_xml_paths('data/trademarks'):
        trademark_parser = TrademarkParser(file_path=path)
        trademark = trademark_parser.parse()
        trademark.commit()
        trademark.commit_classes()
    print("Done parsing trademark files")

    print("Parsing design files...")
    # Parse design files
    for path in get_xml_paths('data/designs'):
        design_parser = DesignParser(file_path=path)
        design = design_parser.parse()
        design.commit()
    print("Done parsing design files")

def get_xml_paths(start_folder):
    matches = []
    for root, dirnames, filenames in os.walk(start_folder):
        for filename in fnmatch.filter(filenames, '*.xml'):
            matches.append(os.path.join(root, filename))
    return matches
  
main()