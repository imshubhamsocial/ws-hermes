import logging
import uuid
from datetime import datetime

logger = logging.getLogger(__name__).setLevel(logging.INFO)

def process_telemetry_record(record: dict) -> dict | None:
    """
    Processes a single telemetry record, handling missing fields gracefully.
    Returns the processed record or None if input is invalid.
    """
    # 3. Input validation: Ensure the record is a dictionary
    if not isinstance(record, dict):
        logger.error(f"Received non-dictionary record type: {type(record)}")
        return None

    # 1. Safely handle event_id
    event_id = record.get('event_id')
    if event_id is None:
        fallback_id = str(uuid.uuid4())
        logger.warning(f"Missing 'event_id' in record. Using fallback UUID: {fallback_id}")
        event_id = fallback_id

    # 2. Validate timestamp and add default if missing
    timestamp = record.get('ts') or record.get('timestamp', datetime.utcnow().isoformat())
    
    payload = record.get('payload', {})
    
    return {
        'processed_id': f"EVT_{event_id}",
        'timestamp': timestamp,
        'metrics': payload.get('metrics', {})
    }

# Example usage (for testing purposes)
if __name__ == '__main__':
    test_record = {'event_id': '12345', 'timestamp': '2023-10-01T10:00:00Z', 'data': {'metrics': [1, 2]}}
    print(process_telemetry_record(test_record))

    legacy_record = {'id': 'LEGACY_99', 'payload': {'metrics': [3, 4]}}
    print(process_telemetry-record(legacy_record))

    invalid_record = "not a dict"
    print(process_telemetry(invalid_record))