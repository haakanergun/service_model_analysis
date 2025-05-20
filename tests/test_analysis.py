from service_model_analysis.analysis import ServiceRecord, average_duration

def test_average_duration():
    records = [ServiceRecord(service_id=1, duration_minutes=20), ServiceRecord(service_id=2, duration_minutes=40)]
    assert average_duration(records) == 30


def test_average_duration_empty():
    assert average_duration([]) == 0.0
