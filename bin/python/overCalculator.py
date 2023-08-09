from predictor import changeDir

def over(home, away, over):
    changeDir()

    with open("lib/NBA/" + home + ".txt") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            spread(row[0], row[1], row[2])
            print(over(row[0], row[1], row[3]))
            print("Processing game: " + row[0] + " vs " + row[1] + " with spread " + row[2] + " and over/under " + row[3])
            line_count += 1
        print(f'Processed {line_count} games.')
    