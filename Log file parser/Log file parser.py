import re

def load_log():
    """
    Reads the raw text data stream from a localized log file.
    Loads file lines sequentially into memory.
    Returns: list - A collection of unparsed string log entries.
    """
    lines = []
    with open('app.log', 'r') as file:
        for line in file:
            lines.append(line)
    return lines

# Primary ingestion step to initialize the text data payload
log_content = load_log()

def match_log():
    """
    Applies regular expressions to structure unparsed text logs.
    Extracts date, time, severity levels, and descriptive messages.
    Returns: list - A collection of standardized dictionaries representing data schemas.
    """
    result = []
    for line in log_content:
        # Structured token extraction via exact positional pattern matching
        match = re.match(r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) "
                         r"(ERROR|WARNING|INFO) (.+)", line)
        if match is not None:
            # Map raw groups into a normalized, structured dictionary payload
            collection ={
            'date' : match.group(1),
            'time' : match.group(2),
            'level' : match.group(3),
            'message' : match.group(4)
            }
            result.append(collection)
    return result

# Execute schema generation over the ingested payload
matched_log = match_log()

# print(match_log())

def level_count():
    """
    Aggregates log events by calculating frequencies for each severity type.
    Returns: dict - Counts mapping for each unique status (ERROR, WARNING, INFO).
    """
    counts = {}
    for entry in matched_log:
        level = entry['level']
        # Efficient frequency accumulation utilizing fallback dictionary mapping
        counts[level] = counts.get(level, 0) + 1
    return counts

print(level_count())

def message_count():
    """
    Analyzes error descriptions to identify specific failure trends.
    Isolates the absolute most frequent message string within the entries.
    Returns: tuple - Containing the top message text and its total occurrence tally.
    """
    counts = {}
    for entry in matched_log:
        message = entry['message']
        counts[message] = counts.get(message, 0) + 1
    # Locate the dictionary key holding the highest value metric
    top_message =  max(counts, key= counts.get)
    return top_message, counts.get(top_message)

# Evaluate and print data engineering trends to console
frequent_message = message_count()
print(frequent_message)
