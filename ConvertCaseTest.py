import sys
import unittest

import sublime_lib_mock
import sublime_plugin_lib_mock
sys.modules['sublime'] = sublime_lib_mock
sys.modules['sublime_plugin'] = sublime_plugin_lib_mock

from ConvertCase import ConvertCaseUtils

class UtilsTests(unittest.TestCase):
  def test_camel_case(self):
    string = ConvertCaseUtils.convert_to_camel_case(['convert', 'case', 'utils'])
    self.assertEqual(string, 'convertCaseUtils')

  def test_kebab_case(self):
    string = ConvertCaseUtils.convert_to_kebab_case(['convert', 'case', 'utils'])
    self.assertEqual(string, 'convert-case-utils')

  def test_snake_case(self):
    string = ConvertCaseUtils.convert_to_snake_case(['convert', 'case', 'utils'])
    self.assertEqual(string, 'convert_case_utils')

  def test_extract_parts(self):
    parts = ConvertCaseUtils.extract_parts('ConvertCaseUtils')
    self.assertEqual(parts, ['convert', 'case', 'utils'])


if __name__ == '__main__':
  unittest.main()
