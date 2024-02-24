company_user = {}
while True:
    line = input()
    if line == "End":
        break
    company_name, id_number = line.split(" -> ")
    if company_name not in company_user.keys():
        company_user[company_name] = []
    is_with_same_id = False
    for key, value in company_user.items():
        for current in value:
            if current == id_number and key == company_name:
                is_with_same_id = True
    if not is_with_same_id:
        company_user[company_name].append(id_number)

for company, ids in company_user.items():
    print(company)
    for current_id in ids:
        print(f'-- {current_id}')