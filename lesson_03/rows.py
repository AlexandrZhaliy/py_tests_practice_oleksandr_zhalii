first_string = 'string_example'
second_string = "string example #2"
brackets_and_slashN = ("Украї́нська Вікіпе́дія — українськомовний розділ Вікіпедії, багатомовного інтернет-проєкту \n"
                   "зі створення інтернет-енциклопедії на базі вікісайту, \n"
                   "яку може редагувати кожний охочий користувач Інтернету. \n")


triple_brackets = """Украї́нська Вікіпе́дія — українськомовний розділ Вікіпедії, багатомовного інтернет-проєкту
\t зі створення інтернет-енциклопедії на базі вікісайту,
\\яку може редагувати кожний охочий користувач Інтернету."""

#brackets_screening = \*something in brackets\*
#tab_screening = \t
#slash_screening = \\
#any_special_symbol_screening = \any_special_symbol

brackets_screening = "  "


print(first_string)
print(second_string)
print(brackets_and_slashN)
print(triple_brackets)