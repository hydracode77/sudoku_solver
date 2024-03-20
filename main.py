from more_itertools import flatten
rare_rows_list = [[5, 0, 4, 6, 7, 0, 9, 0, 2],
                  [6, 7, 2, 1, 0, 5, 3, 4, 0],
                  [1, 9, 8, 0, 4, 2, 5, 6, 7],
                  [8, 5, 9, 7, 6, 1, 4, 2, 0],
                  [4, 2, 6, 8, 0, 3, 0, 9, 0],
                  [0, 1, 3, 9, 2, 4, 0, 5, 6],
                  [0, 6, 1, 5, 3, 7, 2, 0, 4],
                  [0, 8, 7, 4, 0, 9, 0, 3, 5],
                  [3, 0, 0, 2, 8, 6, 1, 0, 9]]

old_missing_fields_num = 1000
missing_fields_num = 999
final_solved_list = rare_rows_list  # anfangs bloße vorlage

def count_empty_fields(sudoku_game_field):
    number_of_zeros = 0
    for e in sudoku_game_field:
        for i in e:
            if i == 0:
                number_of_zeros += 1
    return number_of_zeros


def turn_rows_in_columns(rows_list):
    loose_columns_list = [] # ohne unterlisten
    columns_list = [] # mit unterlisten
    e_index = -1  # bessere indexanzeige als jedes zu indexieren, da ja 2 0er vorkommen könnten
    for e in rows_list:
        i_index = -1 # -1, damits mit 0 anfängt, da platziert, dass bei jeder e runde i neu anfängt
        e_index += 1
        for i in e:
            i_index += 1
            loose_columns_list.append(rows_list[i_index][e_index]) # rows werden durchgegangen und dann immer 1., 2., 3., als liste genommen

    for i in range(0, 81, 9): # immer 9 zsm als unterliste
        columns_list.append(loose_columns_list[i:i+9])

    return columns_list

def turn_rows_in_boxes(rows_list):
    loose_boxes_list = [] # ohne unterlisten
    boxes_list = [] # mit unterlisten

    for e in range(0, 3):
        for i in range(0 + e * 3, 3 + e * 3):
            loose_boxes_list.append(rows_list[i][0:3])  # erste boxreihe
        for i in range(0 + e * 3, 3 + e * 3):
            loose_boxes_list.append(rows_list[i][3:6])  # zweite boxreihe
        for i in range(0 + e * 3, 3 + e * 3):
            loose_boxes_list.append(rows_list[i][6:9])  # dritte boxreihe

    loose_boxes_list = list(flatten(loose_boxes_list))  # Unterlisten auflösen

    for i in range(0, 81, 9): # neue Unterlisten machen
        boxes_list.append(loose_boxes_list[i:i+9])

    return boxes_list

def find_missing_one(uncomplete_list):
    for row_num in range(0, 9):
        if uncomplete_list[row_num].count(0) == 1:  # checken, ob wirklich nur eine zahl fehlt
            num_missing = None
            sorted_list = list(uncomplete_list[row_num])
            sorted_list.sort()

            for i in range(0, 9):
                if not sorted_list[i] == i: # wenn eins nicht in reihe passt, beachte das bei einer 0 am anfang 0 ist
                    num_missing = i
                    break # andere sind wegen num_missing out of order, deswegen fehler vermeiden und break

            if num_missing is None: # also obwohl eine Null drin ist, keine fehlende Zahl gefunden wurde
                num_missing = 9 # dann muss es neun sein

            if num_missing is not None: # dmait nicht iwi ne 0 mit none rzetzt wird
                index_of_missing_num = uncomplete_list[row_num].index(0)  # index von der 0 rauskriegen, geht da nur eine 0
                uncomplete_list[row_num][index_of_missing_num] = num_missing  # zahl mit der fehlenden zahl ersetzen

    return uncomplete_list

def compare_and_combine_everything(row_list, columns_list, boxes_list):
    # alle 3 listen sollten im gleichen format sein (row format)
    loosed_solved_list = [] # ohne unterlisten
    final_solved_list = [] # mit unterlisten
    e_index = -1
    for e in row_list:
        e_index += 1
        i_index = -1
        for i in e:
            i_index += 1
            if i != 0:
                loosed_solved_list.append(i)
            elif columns_list[e_index][i_index] != 0:
                loosed_solved_list.append(columns_list[e_index][i_index])
            elif boxes_list[e_index][i_index] != 0:
                loosed_solved_list.append(boxes_list[e_index][i_index])
            else:
                loosed_solved_list.append(0)

    for i in range(0, 81, 9): # neue Unterlisten machen
        final_solved_list.append(loosed_solved_list[i:i+9])


    return final_solved_list




print(count_empty_fields(final_solved_list)) # So viele Nuller in normaler geg Liste
print(final_solved_list)  # bisher normale gegebene Liste
while missing_fields_num != old_missing_fields_num: # sobald ein weiteres wiederholen nicht bringt, stoppt es
    rare_rows_list = final_solved_list # ergebnis von letzter runde ist das rare von dieser
    old_missing_fields_num = missing_fields_num # von letzter runde

    # columns und box list erstellen
    rare_columns_list = turn_rows_in_columns(rare_rows_list)
    rare_boxes_list = turn_rows_in_boxes(rare_rows_list)

    # alle seperat versuchen fehlende stellen zu finden
    solved_columns_list = find_missing_one(rare_columns_list)
    solved_boxes_list = find_missing_one(rare_boxes_list)
    solved_rows_list = find_missing_one(rare_rows_list)

    # alle in einheitliche rows format bringen
    columns_in_rows = turn_rows_in_columns(solved_columns_list) # kann man gleiche funktion nehmen
    boxes_in_rows = turn_rows_in_boxes(solved_boxes_list) # hier auch

    # vergleichen und kombinieren
    final_solved_list = compare_and_combine_everything(solved_rows_list, columns_in_rows, boxes_in_rows)

    missing_fields_num = count_empty_fields(final_solved_list)  # zählen wie viele 0er diese runde

    print(missing_fields_num)
    print(final_solved_list)
