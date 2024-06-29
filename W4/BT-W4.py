import streamlit as st

def levenshtein_distance(token1, token2):
    len1 = len(token1)
    len2 = len(token2)

    # Tạo ma trận distances
    distances = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    # Khởi tạo giá trị ban đầu
    for i in range(len1 + 1):
        distances[i][0] = i
    for j in range(len2 + 1):
        distances[0][j] = j

    # Tính toán khoảng cách Levenshtein
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if token1[i - 1] == token2[j - 1]:
                substitution_cost = 0
            else:
                substitution_cost = 1

            distances[i][j] = min(distances[i - 1][j] + 1,  # Xóa
                                  distances[i][j - 1] + 1,  # Thêm
                                  distances[i - 1][j - 1] + substitution_cost)  # Thay thế

    # Trả về khoảng cách Levenshtein giữa token1 và token2
    return distances[len1][len2]

def load_vocab(file_path):
    with open(file_path, "r") as f:
        lines = f . readlines()
    words = sorted(set([line . strip() . lower() for line in lines]))
    return words


vocabs = load_vocab(file_path=r"C:\Users\HP\AIO-Exercises\vocab.txt")


st . title(" Word Correction using Levenshtein Distance ")
word = st . text_input("Word :")
if st . button(" Compute "):
    # compute levenshtein distance
    distances = dict()
    for vocab in vocabs:
        distance = levenshtein_distance(word, vocab)
        distances[vocab] = distance
        # sorted by distance
    sorted_distances = dict(
        sorted(distances.items(), key=lambda item: item[1]))
    correct_word = list(sorted_distances.keys())[0]
    st . write("Correct word : ", correct_word)
    col1, col2 = st.columns(2)
    col1.write("Vocabulary:")
    col1.write(vocabs)
    col2.write("Distances:")
    col2.write(sorted_distances)
