from app.main import app

def test_transactions():
    with app.test_client() as client:
        res = client.get('/transactions')
        assert res.status_code == 200
        assert type(res.json) == list