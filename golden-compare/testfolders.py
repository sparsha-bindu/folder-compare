from compare_folder import compare_folder_contents, folderpath1, folderpath2, standardfile
import unittest


class TestFolder(unittest.TestCase):
    def test_for_additional_files(self):
        _, additionalfiles = compare_folder_contents(folderpath1, standardfile)
        self.assertTrue(len(additionalfiles) > 0)
    
    def test_for_missing_files(self):
        missingfiles, _ = compare_folder_contents(folderpath2, standardfile)
        self.assertTrue(len(missingfiles) > 0)
 

if __name__ == '__main__':
    unittest.main()
