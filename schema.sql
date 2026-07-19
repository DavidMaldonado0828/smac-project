
-- ENUM TYPES
CREATE TYPE operation_type AS ENUM (
    'BALANCE_INQUIRY', 'TRANSFER', 'PAYMENT', 'WITHDRAWAL'
);

-- TABLES

CREATE TABLE  channels(
    channel_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

COMMENT ON COLUMN channels.channel_id IS 'Unique identifier for each channel';
COMMENT ON COLUMN channels.name IS 'Name of the channel, e.g., ATM, Mobile App, Web Portal';

CREATE TABLE codes(
    code_id VARCHAR(2) PRIMARY KEY,
    description VARCHAR(50) NOT NULL,
    is_correct BOOLEAN NOT NULL
);

COMMENT ON COLUMN codes.code_id IS 'Unique identifier for each code(ISO8583)';
COMMENT ON COLUMN codes.description IS 'Description of the code, e.g., Approved, Declined, Insufficient Funds';
COMMENT ON COLUMN codes.is_correct IS 'Indicates whether the code represents a successful transaction or an error';


CREATE TABLE transactions(
    transaction_id  SERIAL PRIMARY KEY,
    channel_id INT NOT NULL,
    code_id VARCHAR(2) NOT NULL,
    latency_ms INT NOT NULL,
    amount NUMERIC(15, 2) NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    operation_type operation_type NOT NULL
);

COMMENT ON COLUMN transactions.transaction_id IS 'Unique identifier for each transaction';
COMMENT ON COLUMN transactions.channel_id IS 'Foreign key referencing channels.channel_id';
COMMENT ON COLUMN transactions.code_id IS 'Foreign key referencing codes.code_id';
COMMENT ON COLUMN transactions.latency_ms IS 'Time taken to process the transaction in milliseconds';
COMMENT ON COLUMN transactions.amount IS 'Amount involved in the transaction';
COMMENT ON COLUMN transactions.timestamp IS 'Timestamp when the transaction occurred';
COMMENT ON COLUMN transactions.operation_type IS 'Type of operation performed in the transaction, e.g., BALANCE_INQUIRY, TRANSFER, PAYMENT, WITHDRAWAL';

-- CONSTRAINTS

ALTER TABLE transactions
    ADD CONSTRAINT fk_channel
    FOREIGN KEY (channel_id) REFERENCES channels(channel_id)
    ON DELETE RESTRICT;

ALTER TABLE transactions
    ADD CONSTRAINT fk_code
    FOREIGN KEY (code_id) REFERENCES codes(code_id)
    ON DELETE RESTRICT;


-- INDEXES

CREATE INDEX idx_transactions_channel_id ON transactions(channel_id);
CREATE INDEX idx_transactions_timestamp ON transactions(timestamp);
CREATE INDEX idx_transactions_code_id ON transactions(code_id);