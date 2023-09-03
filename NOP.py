def lcs(str1, str2):
    matrix = [["" for x in range(len(str2))] for x in range(len(str1))]
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                if i == 0 or j == 0:
                    matrix[i][j] = str1[i]
                else:
                    matrix[i][j] = matrix[i-1][j-1] + str1[i]
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1], key=len)
    result = matrix[-1][-1]
    print("НОП: " , end = "")
    return result
def GetStr(message):
    str = input(f"{message}")
    return str
print(lcs(GetStr("Введите первую строку: "), GetStr("Введите вторую строку: "))) 