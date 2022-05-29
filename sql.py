# büyük harf küçük harf önemsiz
# loop halinde input bekleyecek, exit derse çıkacak.

# Insert -> yeni satırı dict'e atıp tekrar sort edecek
# Select -> dictionaryi dolaşıp koşullara göre get yapıcak
# Delete -> koşula göre sil

# exit demeden önce de json'a yazacak
# inputlar düzgün değilse hata verecek.

# Stringi id'yi cast ederken try catch

# print(sorted_dict)
import json

my_dict = {}


def read_csv():
    f = open("students.csv", "r")
    next(f)
    for x in f:
        x = x.split(";")
        my_dict[int(x[0])] = [x[1], x[2], x[3], int(x[4][:-1])]

    return dict(sorted(my_dict.items()))


def insert(values_splitted, sorted_dict):
    # id ve grade eklerken int mi dyie kontrol et
    # gerisi de string mi diye kontrol et
    # not 0 ile 100 arası olacak
    # HATA KONTROLU
    try:
        if int(values_splitted[0]) in sorted_dict:
            print("Id", int(values_splitted[0]), "already exists in the dictionary")
        else:
            sorted_dict[int(values_splitted[0])] = [
                values_splitted[1],
                values_splitted[2],
                values_splitted[3],
                int(values_splitted[4]),
            ]
            print("Eklendi")
        return sorted_dict

    except ValueError:  # id'ye string girerse hata veriyor.
        print("ID must be a number!")


def write_to_dictionary(filtered_by_params_dict, column_name):
    dictionary_To_add = {}
    for key, value in filtered_by_params_dict.items():
        if (
            "NAME" in column_name
            and "LASTNAME" in column_name
            and "EMAIL" in column_name
            and "GRADE" in column_name
        ):
            dictionary_To_add[key] = [value[0], value[1], value[2], value[3]]

        elif (
            "NAME" in column_name
            and "LASTNAME" in column_name
            and "EMAIL" in column_name
        ):
            dictionary_To_add[key] = [value[0], value[1], value[2]]

        elif (
            "NAME" in column_name
            and "LASTNAME" in column_name
            and "GRADE" in column_name
        ):
            dictionary_To_add[key] = [value[0], value[1], value[3]]

        elif (
            "NAME" in column_name and "EMAIL" in column_name and "GRADE" in column_name
        ):
            dictionary_To_add[key] = [value[0], value[2], value[3]]

        elif (
            "LASTNAME" in column_name
            and "EMAIL" in column_name
            and "GRADE" in column_name
        ):
            dictionary_To_add[key] = [value[1], value[2], value[3]]

        elif "NAME" in column_name and "LASTNAME" in column_name:
            dictionary_To_add[key] = [value[0], value[1]]

        elif "NAME" in column_name and "EMAIL" in column_name:
            dictionary_To_add[key] = [value[0], value[2]]

        elif "NAME" in column_name and "GRADE" in column_name:
            dictionary_To_add[key] = [value[0], value[3]]

        elif "LASTNAME" in column_name and "EMAIL" in column_name:
            dictionary_To_add[key] = [value[1], value[2]]

        elif "LASTNAME" in column_name and "GRADE" in column_name:
            dictionary_To_add[key] = [value[1], value[3]]

        elif "EMAIL" in column_name and "GRADE" in column_name:
            dictionary_To_add[key] = [value[2], value[3]]

        elif "NAME" in column_name:
            dictionary_To_add[key] = [value[0]]

        elif "LASTNAME" in column_name:
            dictionary_To_add[key] = [value[1]]

        elif "EMAIL" in column_name:
            dictionary_To_add[key] = [value[2]]

        elif "GRADE" in column_name:
            dictionary_To_add[key] = [value[3]]
    return dictionary_To_add


def name(a_dict, name_index, where_parameters):
    name_dict = {}
    if where_parameters[name_index + 1] == "=":
        for key, value in a_dict.items():
            if value[0].upper() == where_parameters[name_index + 2]:
                name_dict[key] = [value[0], value[1], value[2], value[3]]
                # name_dict = write_to_dictionary(key, value, column_name, name_dict)
        return name_dict

    elif where_parameters[name_index + 1] == "!=":
        for key, value in a_dict.items():
            if value[0].upper() != where_parameters[name_index + 2]:
                name_dict[key] = [value[0], value[1], value[2], value[3]]
                # name_dict = write_to_dictionary(key, value, column_name, name_dict)
        return name_dict


def grade(grade_index, where_parameters, sorted_dict):
    a_dict = {}
    if where_parameters[grade_index + 1] == "=":
        for key, value in sorted_dict.items():
            if value[3] == int(where_parameters[grade_index + 2]):
                a_dict[key] = [value[0], value[1], value[2], value[3]]
                # a_dict = write_to_dictionary(key, value, column_name, select_dict)
        return a_dict

    elif where_parameters[grade_index + 1] == ">":
        for key, value in sorted_dict.items():
            if value[3] > int(where_parameters[grade_index + 2]):
                a_dict[key] = [value[0], value[1], value[2], value[3]]
                # a_dict = write_to_dictionary(key, value, column_name, select_dict)
        return a_dict

    elif where_parameters[grade_index + 1] == ">=":
        for key, value in sorted_dict.items():
            if value[3] >= int(where_parameters[grade_index + 2]):
                a_dict[key] = [value[0], value[1], value[2], value[3]]
                # a_dict = write_to_dictionary(key, value, column_name, select_dict)
        return a_dict

    elif where_parameters[grade_index + 1] == ">!":
        for key, value in sorted_dict.items():
            if value[3] <= int(where_parameters[grade_index + 2]):
                a_dict[key] = [value[0], value[1], value[2], value[3]]
                # a_dict = write_to_dictionary(key, value, column_name, select_dict)
        return a_dict

    elif where_parameters[grade_index + 1] == "<":
        for key, value in sorted_dict.items():
            if value[3] < int(where_parameters[grade_index + 2]):
                a_dict[key] = [value[0], value[1], value[2], value[3]]
                # a_dict = write_to_dictionary(key, value, column_name, select_dict)
        return a_dict

    elif where_parameters[grade_index + 1] == "<=":
        for key, value in sorted_dict.items():
            if value[3] <= int(where_parameters[grade_index + 2]):
                a_dict[key] = [value[0], value[1], value[2], value[3]]
                # a_dict = write_to_dictionary(key, value, column_name, select_dict)
        return a_dict

    elif where_parameters[grade_index + 1] == "!<":
        for key, value in sorted_dict.items():
            if value[3] >= int(where_parameters[grade_index + 2]):
                a_dict[key] = [value[0], value[1], value[2], value[3]]
                # a_dict = write_to_dictionary(key, value, column_name, select_dict)
        return a_dict

    else:
        print("Wrong input for ->", where_parameters[1])


def lastname(a_dict, lastname_index, where_parameters):
    lastname_dict = {}
    if where_parameters[lastname_index + 1] == "=":
        for key, value in a_dict.items():
            if value[1].upper() == where_parameters[lastname_index + 2]:
                lastname_dict[key] = [value[0], value[1], value[2], value[3]]
                # name_dict = write_to_dictionary(key, value, column_name, name_dict)
        return lastname_dict

    elif where_parameters[lastname_index + 1] == "!=":
        for key, value in a_dict.items():
            if value[1].upper() != where_parameters[lastname_index + 2]:
                lastname_dict[key] = [value[0], value[1], value[2], value[3]]
                # name_dict = write_to_dictionary(key, value, column_name, name_dict)
        return lastname_dict


def email(a_dict, email_index, where_parameters):
    email_dict = {}
    if where_parameters[email_index + 1] == "=":
        for key, value in a_dict.items():
            if value[2].upper() == where_parameters[email_index + 2]:
                email_dict[key] = [value[0], value[1], value[2], value[3]]
                # email_dict = write_to_dictionary(key, value, column_name, email_dict)
        return email_dict

    elif where_parameters[email_index + 1] == "!=":
        for key, value in a_dict.items():
            if value[2].upper() != where_parameters[email_index + 2]:
                email_dict[key] = [value[0], value[1], value[2], value[3]]
                # email_dict = write_to_dictionary(key, value, column_name, email_dict)
        return email_dict


def select(column_name, where_parameters, sorted_dict):
    # SELECT ALL KALDI

    select_dict = {}

    print(column_name, where_parameters)
    # value[3] -> grade'e denk geliyor.
    if "AND" in where_parameters:
        if "GRADE" in where_parameters and "NAME" in where_parameters:
            # nota göre filtrelenmiş dictionary
            grade_index = where_parameters.index("GRADE")
            a_dict = grade(grade_index, where_parameters, sorted_dict)
            name_index = where_parameters.index("NAME")

            filtered_by_name = name(a_dict, name_index, where_parameters)
            final_dict = write_to_dictionary(filtered_by_name, column_name)
            # print(final_dict)
            # bu dicti isime göre filtreleyecez.

        elif "GRADE" in where_parameters and "EMAIL" in where_parameters:
            # nota göre filtrelenmiş dictionary
            grade_index = where_parameters.index("GRADE")
            a_dict = grade(grade_index, where_parameters, sorted_dict)
            email_index = where_parameters.index("EMAIL")

            filtered_by_email = email(a_dict, email_index, where_parameters)
            final_dict = write_to_dictionary(filtered_by_email, column_name)
            # print(final_dict)

        elif "GRADE" in where_parameters and "LASTNAME" in where_parameters:
            # nota göre filtrelenmiş dictionary
            grade_index = where_parameters.index("GRADE")
            a_dict = grade(grade_index, where_parameters, sorted_dict)
            lastname_index = where_parameters.index("LASTNAME")

            filtered_by_lastname = lastname(a_dict, lastname_index, where_parameters)
            final_dict = write_to_dictionary(filtered_by_lastname, column_name)
            # print(final_dict)

        elif "EMAIL" in where_parameters and "LASTNAME" in where_parameters:
            # nota göre filtrelenmiş dictionary
            email_index = where_parameters.index("EMAIL")
            a_dict = email(sorted_dict, email_index, where_parameters)
            lastname_index = where_parameters.index("LASTNAME")

            filtered_by_lastname = lastname(a_dict, lastname_index, where_parameters)
            final_dict = write_to_dictionary(filtered_by_lastname, column_name)
            # print(final_dict)

        elif "EMAIL" in where_parameters and "NAME" in where_parameters:
            # nota göre filtrelenmiş dictionary
            email_index = where_parameters.index("EMAIL")
            a_dict = email(sorted_dict, email_index, where_parameters)
            name_index = where_parameters.index("NAME")

            filtered_by_name = name(a_dict, name_index, where_parameters)
            final_dict = write_to_dictionary(filtered_by_name, column_name)
            # print(final_dict)

        elif "LASTNAME" in where_parameters and "NAME" in where_parameters:
            # nota göre filtrelenmiş dictionary
            lastname_index = where_parameters.index("LASTNAME")
            a_dict = lastname(sorted_dict, lastname_index, where_parameters)
            name_index = where_parameters.index("NAME")

            filtered_by_name = name(a_dict, name_index, where_parameters)
            final_dict = write_to_dictionary(filtered_by_name, column_name)
            # print(final_dict)

    # elif "OR" in where_parameters:
    elif "OR" in where_parameters:
        if "GRADE" in where_parameters or "NAME" in where_parameters:
            # nota göre filtrelenmiş dictionary
            grade_index = where_parameters.index("GRADE")
            a_dict = grade(grade_index, where_parameters, sorted_dict)
            name_index = where_parameters.index("NAME")

            filtered_by_name = name(a_dict, name_index, where_parameters)
            combined_dict = {**filtered_by_name, **a_dict}
            final_dict = write_to_dictionary(combined_dict, column_name)
            # print(final_dict)
            # bu dicti isime göre filtreleyecez.

        elif "GRADE" in where_parameters or "EMAIL" in where_parameters:
            # nota göre filtrelenmiş dictionary
            grade_index = where_parameters.index("GRADE")
            a_dict = grade(grade_index, where_parameters, sorted_dict)
            email_index = where_parameters.index("EMAIL")

            filtered_by_email = email(a_dict, email_index, where_parameters)
            combined_dict = {**filtered_by_email, **a_dict}
            final_dict = write_to_dictionary(combined_dict, column_name)
            # print(final_dict)

        elif "GRADE" in where_parameters or "LASTNAME" in where_parameters:
            # nota göre filtrelenmiş dictionary
            grade_index = where_parameters.index("GRADE")
            a_dict = grade(grade_index, where_parameters, sorted_dict)
            lastname_index = where_parameters.index("LASTNAME")

            filtered_by_lastname = lastname(a_dict, lastname_index, where_parameters)
            combined_dict = {**filtered_by_lastname, **a_dict}
            final_dict = write_to_dictionary(combined_dict, column_name)
            # print(final_dict)

        elif "EMAIL" in where_parameters or "LASTNAME" in where_parameters:
            # nota göre filtrelenmiş dictionary
            email_index = where_parameters.index("EMAIL")
            a_dict = email(sorted_dict, email_index, where_parameters)
            lastname_index = where_parameters.index("LASTNAME")

            filtered_by_lastname = lastname(a_dict, lastname_index, where_parameters)
            combined_dict = {**filtered_by_lastname, **a_dict}
            final_dict = write_to_dictionary(combined_dict, column_name)
            # print(final_dict)

        elif "EMAIL" in where_parameters or "NAME" in where_parameters:
            # nota göre filtrelenmiş dictionary
            email_index = where_parameters.index("EMAIL")
            a_dict = email(sorted_dict, email_index, where_parameters)
            name_index = where_parameters.index("NAME")

            filtered_by_name = name(a_dict, name_index, where_parameters)
            combined_dict = {**filtered_by_name, **a_dict}

            final_dict = write_to_dictionary(combined_dict, column_name)
            # print(final_dict)

        elif "LASTNAME" in where_parameters or "NAME" in where_parameters:
            # nota göre filtrelenmiş dictionary
            lastname_index = where_parameters.index("LASTNAME")
            a_dict = lastname(sorted_dict, lastname_index, where_parameters)
            name_index = where_parameters.index("NAME")

            filtered_by_name = name(a_dict, name_index, where_parameters)
            combined_dict = {**filtered_by_name, **a_dict}

            final_dict = write_to_dictionary(combined_dict, column_name)
            # print(final_dict)

    else:
        if "GRADE" in where_parameters:
            grade_index = where_parameters.index("GRADE")
            a_dict = grade(grade_index, where_parameters, sorted_dict)
            final_dict = write_to_dictionary(a_dict, column_name)
            # print(final_dict)
        elif "NAME" in where_parameters:
            name_index = where_parameters.index("NAME")
            a_dict = name(sorted_dict, name_index, where_parameters)
            final_dict = write_to_dictionary(a_dict, column_name)
            # print(final_dict)

        elif "EMAIL" in where_parameters:
            email_index = where_parameters.index("EMAIL")
            a_dict = email(sorted_dict, email_index, where_parameters)
            final_dict = write_to_dictionary(a_dict, column_name)
            # print(final_dict)

        elif "LASTNAME" in where_parameters:
            lastname_index = where_parameters.index("LASTNAME")
            a_dict = lastname(sorted_dict, lastname_index, where_parameters)
            final_dict = write_to_dictionary(a_dict, column_name)
            # print(final_dict)

    return final_dict


def delete(where_parameters, sorted_dict, select_dict):
    # select edilen dictionaryi delete' e parametre gönder
    # eğer o dict boş ise önce select çalışmamış demek o zaman sadece students'tan sil
    # dict dolu ise hem o select'ten hem de students'ten sil

    # if len(select_dict) == 0:
    dict_to_delete = select(
        ["NAME", "LASTNAME", "EMAIL", "GRADE"], where_parameters, sorted_dict
    )
    for key, value in dict_to_delete.items():
        del sorted_dict[key]
    print(sorted_dict)
    return sorted_dict


def write_to_json(data):

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


# else:
#     dict_to_delete = select(
#         ["NAME", "LASTNAME", "EMAIL", "GRADE"], where_parameters, select_dict
#     )
#     for key, value in dict_to_delete.items():
#         del sorted_dict[key]
#         del select_dict[key]
#     print(select_dict)
#     return select_dict


def main():
    selected_dict = {}
    sorted_dict = read_csv()
    string = ""
    while True:
        string = input("Enter input: ")
        if string == "exit":
            write_to_json(sorted_dict)
            break

        string = string.split(" ")
        for i in range(len(string)):
            string[i] = string[i].upper()

        if string[0] == "INSERT":
            values = string[3]
            values_subStr = values[7:-1]
            values_splitted = values_subStr.split(",")
            sorted_dict = insert(values_splitted, sorted_dict)

        if string[0] == "SELECT":
            # COLUMN_NAME'ler ile bir şey yapmıyor şu anda
            # SELECT ALL da yapılmadı

            if string[2] != "FROM" or string[3] != "STUDENTS" or string[4] != "WHERE":
                print("Input must be like: 'SELECT < > FROM STUDENTS WHERE' ")
            else:
                column_name = string[1].split(",")
                # where'den sonra parametre vermemişse
                # SELECT name FROM STUDENTS WHERE grade > 40
                # Order vermediği için direkt artan
                if len(string[5:-3]) == 0:
                    where_parameters = string[5:]
                    print(where_parameters)
                    sorted_dict = select(column_name, where_parameters, sorted_dict)
                else:
                    # where'den sonra parametre vermişse ve ORDER BY <> demişse
                    # SELECT name FROM STUDENTS WHERE grade > 40 AND name='John' ORDER BY ASC
                    # 5 ten başlayıp son 3 ü almayacaz
                    if string[10:] == ["ORDER", "BY", "ASC"] or string[10:] == [
                        "ORDER",
                        "BY",
                        "DSC",
                    ]:
                        if string[-1] == "DSC":  # azalan şekilde olacak
                            sorted_dict = dict(sorted(my_dict.items(), reverse=True))
                            where_parameters = string[5:-3]
                            print(where_parameters)
                            sorted_dict = select(
                                column_name, where_parameters, sorted_dict
                            )
                        elif string[-1] == "ASC":  # zaten artan şekilde
                            sorted_dict = dict(sorted(my_dict.items()))
                            where_parameters = string[5:-3]
                            print(where_parameters)
                            sorted_dict = select(
                                column_name, where_parameters, sorted_dict
                            )
                        else:
                            print("Input Error -> ", string[2])

                    # where'den sonra parametre vermiş ama order by yok
                    # SELECT name FROM STUDENTS WHERE grade > 40 AND name='John'
                    else:
                        where_parameters = string[5:]
                        print(where_parameters)
                        sorted_dict = select(column_name, where_parameters, sorted_dict)

        if string[0] == "DELETE":
            # DELETE FROM STUDENT WHERE name = ‘John’ and grade <= 20
            where_parameters = string[4:]
            sorted_dict = delete(where_parameters, sorted_dict, selected_dict)


main()
