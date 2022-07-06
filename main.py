import csv
from tabnanny import check


def check_dates(persons):
    all_data = read_csv_file()
    all_names = setup_name(all_data)
    all_dates = setup_date(all_data)
    all_true_flase = setup_true_false(all_data)
    
    check_name_exist = [0] * len(all_names)
    for i in range(len(all_names)):
      for j in range(len(persons)):
        if persons[j] == all_names[i]:
          check_name_exist[i] = 1
    
    print("======================================================\n")

    for name in range(len(all_names)):
      if check_name_exist[name] == 1:
        print(all_names[name])

    persons_count = 0
    for name in range(len(check_name_exist)):
      if check_name_exist[name] == 1:
        persons_count += 1
    print(f"の{persons_count}人の予定を確認します。\n可能な日は、\n")

    possible_all_dates = list()
    for date in range(len(all_dates)):
      possible_count = 0
      for name in range(len(all_names)):
        if check_name_exist[name] == 1:
          if all_true_flase[date][name] == '○':
            possible_count += 1
      if possible_count == persons_count:
        possible_all_dates.append(all_dates[date])

    for date in range(len(possible_all_dates)):
      print(f"{possible_all_dates[date]}")
    print("\nです。\n")
    print("======================================================\n")
          

def setup_name(all_data):
    all_names = list()
    for i in range(1, len(all_data[2])):
        all_names.append(all_data[2][i])
    return all_names


def setup_date(all_data):
    all_dates = list()
    for i in range(3, len(all_data)-1):
        all_dates.append(all_data[i][0])
    return all_dates


def setup_true_false(all_data):
    all_true_false = list()
    for i in range(3, len(all_data)-1):
      tmp_all_true_false = list()
      for j in range(1, len(all_data[i])):
          tmp_all_true_false.append(all_data[i][j])
      all_true_false.append(tmp_all_true_false)
    return all_true_false


def read_csv_file():
    all_data = []
    csv_path = 'data/chouseisan_konshinkai.csv'

    with open(csv_path, encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            all_data.append(row)
    return all_data

def input_names():
  flag = True
  persons = list()
  while(flag):
    input_str = input("確認したい人の名前を漢字名字で書いて。記入をやめるときは「やめる」と書いて。")
    if input_str == "やめる":
      print("\n")
      flag = False
    else:
      persons.append(input_str)
  return persons

if __name__ == "__main__":
    possible_dates = check_dates(input_names())
    
