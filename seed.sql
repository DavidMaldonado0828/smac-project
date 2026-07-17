INSERT INTO channels(name) VALUES 
    ('MOBILE APP'),
    ('BRANCH'),
    ('ATM'),
    ('PSE'),
    ('BANKING CORRESPONDENT');


INSERT INTO codes(code_id, description, is_correct) VALUES 
    ('00', 'Approved', TRUE),
    ('51', 'Insufficient Funds', FALSE),
    ('91', 'Issuer Unavailable', FALSE),
    ('96', 'System Error', FALSE),
    ('68','Timeout', FALSE);

