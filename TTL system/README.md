# TTL In-Memory Cache System

A lightweight, high-performance in-memory key-value caching system implementing lazy Time-To-Live (TTL) data eviction mechanics. This utility mimics basic Redis-style session token management pipelines, demonstrating advanced object-oriented programming (OOP), epoch timestamp manipulation, and temporary memory state retention workflows.

## 🛠️ Features

*   **Time-Bounded Expiry Calculation**: Leverages the native `time` module to securely project precise UNIX epoch expiration thresholds for individual records.
*   **Lazy Eviction Logic**: Validates data fresh-state boundaries at the point of access, instantly suppressing expired references without consuming continuous compute cycles.
*   **Flexible Data Mapping**: Houses keys alongside tuple configuration pairs `(value, expiry_time)` inside optimized native dictionaries for fast operational lookups.

## 🚀 Usage

Execute the script using your custom shortcut or your text interface editor:

```bash
python TTL.py
```

### Expected Console Output
The execution block runs an evaluation loop displaying immediate retrieval followed by post-delay eviction:
```text
Ahmed
None
```

## 📊 Operational Mechanics Blueprint

1. **Storage Matrix Input Phase**:
   Calling `cache.set("username", "Ahmed", 2)` computes a systemic threshold: `Current Epoch Time + 2 Seconds`.
2. **Immediate Query Validation**:
   `cache.get("username")` compares current time against the boundary. Since `time.time() < expiry_time`, the data payload (`"Ahmed"`) is delivered.
3. **Threshold Eviction Invalidation**:
   After triggering `time.sleep(3)`, a secondary query detects that `time.time() > expiry_time`. Access is revoked, and `None` is safely returned.
