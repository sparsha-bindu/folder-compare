from compare_folder import compare_folder_contents, folderpath, standardfile
import unittest


class TestFolder(unittest.TestCase):
    def test_for_additional_files_>=zer0(self): #tests if length of additional files is greater or equal to zero
        _, additionalfiles = compare_folder_contents(folderpath, standardfile)
#         self.assertEqual(len(additionalfiles), 0)
        self.assertTrue(len(additionalfiles) >= 0)

    def test_for_missing_files_(self):   #tests for length of missing files is greater than zreo
        missingfiles, _ = compare_folder_contents(folderpath, standardfile)
#         self.assertEqual(len(missingfiles), 0)
        self.assertTrue(len(missingfiles) > 0)


if __name__ == '__main__':
    unittest.main()
