scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]

def breakingRecords(scores):
    min_score = scores[0]
    max_score = scores[0]
    min_score_counter = 0
    max_score_counter = 0
    for i in range(1, len(scores)):
        if scores[i] < min_score:
            min_score_counter += 1
            min_score = scores[i]
        elif scores[i] > max_score:
            max_score_counter += 1
            max_score = scores[i]
        else:
            continue
    return [max_score_counter, min_score_counter]

print(breakingRecords(scores))
# [2, 4]