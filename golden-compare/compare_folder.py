import os
import json

standardfile = "standardfile.json"
folderpath1 = "."
folderpath2 = "envfiles"


def load_contents_of_standardfile(standardfilename):
    fileObject = open(standardfilename, "r")
    jsoncontent = fileObject.read()
    standardfilelist = json.loads(jsoncontent)
    fileObject.close()
    return standardfilelist


def missingfileslist(filelist, givenfiles):
    missing_files = []
    [missing_files.append(file) for file in filelist if file not in givenfiles]
    return missing_files


def compared_and_additionalfiles(path, standardfilelist):
    compared_files = []
    additional_files = []
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename in standardfilelist:
                compared_files.append(filename)
            else:
                additional_files.append(filename)
    return compared_files, additional_files


def compare_folder_contents(directory_path, standard_file):
    standardfilelist = load_contents_of_standardfile(standard_file)
    compared_files, additional_files = compared_and_additionalfiles(directory_path, standardfilelist)
    missing_files = missingfileslist(standardfilelist, compared_files)
    return missing_files, additional_files
