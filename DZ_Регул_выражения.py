from pprint import pprint
import re
import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

print(contacts_list)

cont_list = []
for list in contacts_list:
  new_list =[]
  for el in list:
    res = re.sub(r"(\+7|8)\s?\(?(\d{3})\)?[\s-]?(\d{3})[\s-]?(\d{2})[\s-]?(\d{2})(\s*\(?(доб.)?\)?\s?(\d{4})\)?)?",
                 r"+7(\2)\3-\4-\5 \7\8", el)
    new_list.append(res)
  cont_list.append(new_list)

print(cont_list)

cont_list_2 = []

for list in cont_list:
  count = 0
  new_list = []
  for a in list:
    if len(new_list) < 3:
      count += 1
      if '' == a:
        new_list.append(a)
      else:
        new_list.extend(a.split())
    elif len(new_list) == 3 and count < 3:
      count += 1
      continue
    else:
      new_list.append(a)
  cont_list_2.append(new_list)

print(cont_list_2)

new_contacts_list = [cont_list_2[0]]

for id, list in enumerate(cont_list_2):
  if id != 0:
    count = 1
    for id_2, ncl in enumerate(new_contacts_list):
      if list[0] == ncl[0]:
        for id_3, elm in enumerate(list):
          if elm > ncl[id_3]:
            new_contacts_list[id_2][id_3] = elm
          else:
            continue
      elif count != len(new_contacts_list):
        count += 1
        continue
      else:
        new_contacts_list.append(list)
        break
  else:
    continue


# for id, list in enumerate(cont_list_2):
#   if id != 0:
#     for id_2, ncl in enumerate(new_contacts_list):
#       count = 0
#       if list[0] == ncl[0] and list[1] == ncl[1]:
#         count += 1
#         for id_3, a in enumerate(list):
#           if a > ncl[id_3]:
#             new_contacts_list[id_2][id_3] = a
#           else:
#             continue
#       elif count == len(new_contacts_list) - 1:
#         new_contacts_list.append(cont_list_2[id])
#         break
#       else:
#         count += 1
#     else:
#       continue

print(new_contacts_list)



with open("phonebook.csv", "w", encoding='UTF-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(new_contacts_list)