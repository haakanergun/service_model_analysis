from service_model_analysis.app import app

def test_index_route():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Service Model Analysis Demo" in response.data


def test_analyze_route():
    client = app.test_client()
    response = client.get('/analyze')
    assert response.status_code == 200
    data = response.get_json()
    assert data["root_cause"] == "Sample Root Cause"
