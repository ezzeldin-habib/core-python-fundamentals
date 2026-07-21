import re
def load_log():
    lines = []
    with open('app.log', 'r') as file:
        for line in file:
            lines.append(line)
    return lines

log_content = load_log()

def match_log():
    result = []
    for line in log_content:
        match = re.match(r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) "
                         r"(ERROR|WARNING|INFO) (.+)", line)
        if match is not None:
            collection ={
            'date' : match.group(1),
            'time' : match.group(2),
            'level' : match.group(3),
            'message' : match.group(4)
            }
            result.append(collection)
    return result

matched_log = match_log()

# print(match_log())

def level_count():
    counts = {}
    for entry in matched_log:
        level = entry['level']
        counts[level] = counts.get(level, 0) + 1
    return counts

print(level_count())

def message_count():
    counts = {}
    for entry in matched_log:
        message = entry['message']
        counts[message] = counts.get(message, 0) + 1
    top_message =  max(counts, key= counts.get)
    return top_message, counts.get(top_message)

frequent_message = message_count()
print(frequent_message)

