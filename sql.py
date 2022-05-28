# büyük harf küçük harf önemsiz
# loop halinde input bekleyecek, exit derse çıkacak.

# Insert -> yeni satırı dict'e atıp tekrar sort edecek
# Select -> dictionaryi dolaşıp koşullara göre get yapıcak
# Delete -> koşula göre sil

# exit demeden önce de json'a yazacak
# inputlar düzgün değilse hata verecek.

# Stringi id'yi cast ederken try catch

# print(sorted_dict)


my_dict = {}
operands = {
    "lt": "<",
    "lte": "<=",
    "nlt": "!<",
    "gt": ">",
    "gte": ">=",
    "ngt": ">!",
    "eq": "==",
}


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

    except ValueError:  # id'ye string girerse hata veriyor.
        print("ID must be a number!")


def select(column_name, where_parameters, sorted_dict):
    # input satırında AND veya OR var mı diye bakmak lazım
    # varsa ona göre bir şeyler de yapcaz
    # id zaten var name , surname, email,grade olabilir
    #
    # column_name -> id zaten var name , surname, email,grade
    # where_parameters ->
    # grade varsa grade'i , operandı ve sayıyı alacaz
    # operanda göre sorted_dict ve grade'göre sorted_dict'te arama yapacaz
    # sonra column_name'i ve arama sonuçlarını yeni bir dict'e at {}

    print(column_name, where_parameters)
    # value[3] -> grade'e denk geliyor.
    if where_parameters[1] == "==":
        for key, value in sorted_dict.items():
            if value[3] == int(where_parameters[2]):
                print(key, value[3])

    elif where_parameters[1] == ">":
        for key, value in sorted_dict.items():
            if value[3] > int(where_parameters[2]):
                print(key, value[3])

    elif where_parameters[1] == ">=":
        for key, value in sorted_dict.items():
            if value[3] >= int(where_parameters[2]):
                print(key, value[3])

    elif where_parameters[1] == ">!":
        for key, value in sorted_dict.items():
            if value[3] <= int(where_parameters[2]):
                print(key, value[3])

    elif where_parameters[1] == "<":
        for key, value in sorted_dict.items():
            if value[3] < int(where_parameters[2]):
                print(key, value[3])

    elif where_parameters[1] == "<=":
        for key, value in sorted_dict.items():
            if value[3] <= int(where_parameters[2]):
                print(key, value[3])

    elif where_parameters[1] == "!<":
        for key, value in sorted_dict.items():
            if value[3] >= int(where_parameters[2]):
                print(key, value[3])

    else:
        print("Wrong input for ->", where_parameters[1])


def main():
    sorted_dict = read_csv()
    string = ""
    while True:
        string = input("Enter input: ")
        if string == "exit":
            break

        string = string.split(" ")
        for i in range(len(string)):
            string[i] = string[i].upper()

        if string[0] == "INSERT":
            values = string[3]
            values_subStr = values[7:-1]
            values_splitted = values_subStr.split(",")
            insert(values_splitted, sorted_dict)

        if string[0] == "SELECT":
            # COLUMN_NAME'ler ile bir şey yapmıyor şu anda
            # SELECT ALL da yapılmadı

            if string[2] != "FROM" or string[3] != "STUDENTS" or string[4] != "WHERE":
                print("Input must be like: 'SELECT < > FROM STUDENTS WHERE' ")
            else:
                column_name = string[1].split(",")
                # where'den sonra parametre vermemişse
                # SELECT name FROM STUDENTS WHERE grade > 40
                if len(string[5:-3]) == 0:
                    where_parameters = string[5:]
                    print(where_parameters)
                    select(column_name, where_parameters, sorted_dict)
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
                            select(column_name, where_parameters, sorted_dict)
                        elif string[-1] == "ASC":  # zaten artan şekilde
                            sorted_dict = dict(sorted(my_dict.items()))
                            where_parameters = string[5:-3]
                            print(where_parameters)
                            select(column_name, where_parameters, sorted_dict)
                        else:
                            print("Input Error -> ", string[2])

                    # where'den sonra parametre vermiş ama order by yok
                    # SELECT name FROM STUDENTS WHERE grade > 40 AND name='John'
                    else:
                        where_parameters = string[5:-2]
                        print(where_parameters)
                        select(column_name, where_parameters, sorted_dict)


main()
