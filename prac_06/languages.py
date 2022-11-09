"""
Start time: 4:10
Finish time:4:20
"""
from prac_06.programming_language import ProgrammingLanguages
languages = []

python = ProgrammingLanguages("Python", "Dynamic", True, 1991)
languages.append(python)
ruby = ProgrammingLanguages("Ruby", "Dynamic", True, 1995)
languages.append(ruby)
visual_basic = ProgrammingLanguages("Visual Basic", "Static", False, 1991)
languages.append(visual_basic)
print(python)
for language in languages:
    if language.is_dynamic():
        print(language.name)
