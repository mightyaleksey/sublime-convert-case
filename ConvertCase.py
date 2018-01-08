import re
import sublime
import sublime_plugin

class ConvertCaseUtils:
  @staticmethod
  def convert_to_camel_case(parts):
    if len(parts) == 0:
      return ''
    if len(parts) == 1:
      return parts[0]
    if len(parts) > 1:
      return parts[0] + ''.join(map(lambda p: p.capitalize(), parts[1:]))

  @staticmethod
  def convert_to_kebab_case(parts):
    return '-'.join(parts);

  @staticmethod
  def convert_to_snake_case(parts):
    return '_'.join(parts)

  @staticmethod
  def extract_parts(string):
    parts = re.findall('[A-Z]?[a-z0-9$]+', string)
    return [p.lower() for p in parts]

  def region_to_camel_case(self, region):
    string = self.view.substr(region)
    parts = self.extract_parts(string)
    return (self.convert_to_camel_case(parts), region)

  def region_to_kebab_case(self, region):
    string = self.view.substr(region)
    parts = self.extract_parts(string)
    return (self.convert_to_kebab_case(parts), region)

  def region_to_snake_case(self, region):
    string = self.view.substr(region)
    parts = self.extract_parts(string)
    return (self.convert_to_snake_case(parts), region)

  def regions(self):
    regions = [region for region in self.view.sel() if not region.empty()]

    if len(regions) > 0:
      return regions

    # create a region from the contents of file in case all regions are empty
    return [sublime.Region(0, self.view.size())]


class ConvertCaseCamelCaseCommand(ConvertCaseUtils, sublime_plugin.TextCommand):
  def run(self, edit):
    strings = tuple(map(self.region_to_camel_case, self.regions()))

    for string, region in reversed(strings):
      self.view.replace(edit, region, string)


class ConvertCaseKebabCaseCommand(ConvertCaseUtils, sublime_plugin.TextCommand):
  def run(self, edit):
    strings = tuple(map(self.region_to_kebab_case, self.regions()))

    for string, region in reversed(strings):
      self.view.replace(edit, region, string)


class ConvertCaseSnakeCaseCommand(ConvertCaseUtils, sublime_plugin.TextCommand):
  def run(self, edit):
    strings = tuple(map(self.region_to_snake_case, self.regions()))

    for string, region in reversed(strings):
      self.view.replace(edit, region, string)
