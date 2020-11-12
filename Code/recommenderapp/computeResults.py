import glob, csv

results = glob.glob("experiment_results/*.csv")
accuracy, total = 0, 0
like, dislike, notSeen = 0, 0, 0
errorResponse = 0
for result in results:
    if result[-7] == "T":
        with open(result) as f:
            fcsv = csv.reader(f, delimiter=",")
            for row in fcsv:
                total += 1
                decision = row[-1].strip()
                if decision == "Like":
                    like += 1
                elif decision == "Dislike":
                    dislike += 1
                elif decision == "Yet to watch":
                    notSeen += 1
                else:
                    errorResponse += 1
if total > 0:
    print("Total ratings: " + str(total))
    print("Likes: " + str(like))
    print("Like percentage: " + str(round(like * 100 / total, 2)))
    print("Dislikes: " + str(dislike))
    print("Dislike percentage: " + str(round(dislike * 100 / total, 2)))
    print("Not seen: " + str(notSeen))
    print("Not seen percentage: " + str(round(notSeen * 100 / total, 2)))
    print("Incorrect reponses: " + str(errorResponse))
else:
    print("Not enough responses")
