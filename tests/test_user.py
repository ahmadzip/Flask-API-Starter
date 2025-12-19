def test_create_user(client):
    response = client.post('/users', json={
        'name': 'Test User',
        'email': 'test@example.com',
        'password': 'password123'
    })
    assert response.status_code == 200
    assert response.json['data']['name'] == 'Test User'
    assert response.json['data']['email'] == 'test@example.com'

def test_get_users(client):
    # Create a user first
    client.post('/users', json={
        'name': 'Test User',
        'email': 'test@example.com',
        'password': 'password123'
    })
    
    response = client.get('/users')
    assert response.status_code == 200
    assert len(response.json['data']) == 1
    assert response.json['data'][0]['name'] == 'Test User'

def test_get_user_detail(client):
    # Create a user first
    create_res = client.post('/users', json={
        'name': 'Test User',
        'email': 'test@example.com',
        'password': 'password123'
    })
    user_id = create_res.json['data']['id']

    response = client.get(f'/users/{user_id}')
    assert response.status_code == 200
    assert response.json['data']['name'] == 'Test User'

def test_update_user(client):
    # Create a user first
    create_res = client.post('/users', json={
        'name': 'Test User',
        'email': 'test@example.com',
        'password': 'password123'
    })
    user_id = create_res.json['data']['id']

    response = client.put(f'/users/{user_id}', json={
        'name': 'Updated User'
    })
    assert response.status_code == 200
    assert response.json['data']['name'] == 'Updated User'

def test_delete_user(client):
    # Create a user first
    create_res = client.post('/users', json={
        'name': 'Test User',
        'email': 'test@example.com',
        'password': 'password123'
    })
    user_id = create_res.json['data']['id']

    response = client.delete(f'/users/{user_id}')
    assert response.status_code == 200
    
    # Verify deletion
    get_res = client.get(f'/users/{user_id}')
    assert get_res.status_code == 400
