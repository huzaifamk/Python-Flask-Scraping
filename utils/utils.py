from db.database import mongo


def check_lines(lines):
    lines_with_more_than_two_words = []
    for line in lines:
        line = line.strip()

        words = line.replace('\xa0', '').split()
        if len(words) > 4:
            lines_with_more_than_two_words.append(line)

    data = []
    dat1 = []

    for line in list(set(lines_with_more_than_two_words)):
        data.append(line)

    record = {
        'User_id': 'MllUlAtG9UWDUnzudOXL8HOjyCU2',
        'Data': ''.join(data)
    }
    dat1.append(record)

    print(dat1)
    try:
        mongo(dat1)  # call MongoDB function
    except Exception as f:
        print(f)
