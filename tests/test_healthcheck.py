"""
tests/test_healthcheck.py
"""


def test_healthcheck(test_app):
    """test the healthcheck endpoint"""
    # Given
    # test app

    # When
    response = test_app.get("/healthcheck")

    # Then
    assert response.status_code == 200
    assert response.json() == {
        "environment": "dev",
        "message": "ok",
        "testing": True,
    }
