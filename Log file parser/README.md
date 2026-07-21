# Log File Parser & Analytics Utility

A foundational text processing and analysis tool built to ingest, structure, and aggregate server event stream data. The project leverages advanced string processing operations and regular expressions to parse unstructured log streams into a standardized data model, extracting key operational metrics for telemetry reporting.

## 🛠️ Features

*   **Log Tokenization**: Ingests raw text files sequentially using Python's file tracking capabilities.
*   **Regex Pattern Matching**: Evaluates and splits semi-structured text patterns dynamically using positional groups into formal key-value dictionary attributes.
*   **Metric Ingestion Aggregation**: Summarizes system activity by tracking log type distribution (`INFO`, `WARNING`, `ERROR`).
*   **Anomaly Trend Detection**: Evaluates message tracking to immediately isolate the most frequent error description string and its recurrence tally.

## 🚀 Usage

Place your `app.log` file in the project folder and execute the script directly using your custom shortcut or your text interface editor:

```bash
python "Log file parser.py"
```

### Expected Console Output
The analytics suite calculates operational distribution maps and returns statistical summaries to the screen:
```text
{'INFO': 142, 'WARNING': 23, 'ERROR': 5}
('Connection timed out on server instance cluster-3', 4)
```

## 📊 Pipeline Schemas

### Input Log format
```text
2026-07-21 15:24:02 ERROR Connection timed out on server instance cluster-3
```

### Parsed Memory Payload Schema
```json
{
    "date": "2026-07-21",
    "time": "15:24:02",
    "level": "ERROR",
    "message": "Connection timed out on server instance cluster-3"
}
```
