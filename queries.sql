.open db.sqlite

-- Time spent open by days
SELECT ticket_id, julianday('now') - shipment_date AS time_open 
FROM long_activities
WHERE status="open"
GROUP by ticket_id;

-- Time spent waiting for response (pending status) by days
SELECT ticket_id, julianday('now') - shipment_date AS time_pending 
FROM long_activities
WHERE status="pending"
GROUP by ticket_id;

-- Time spent waiting for customer by days
SELECT ticket_id, julianday('now') - shipment_date AS time_waiting 
FROM long_activities
WHERE status="Waiting for Customer"
GROUP by ticket_id;

-- Time till resolved by days
SELECT t.ticket_id, shipment_date - performed_at AS time_till_resolved 
FROM tickets as t INNER JOIN long_activities as l
WHERE status="resolved"
GROUP by t.ticket_id;

-- All products where customer was contacted
SELECT product, COUNT(*) FROM
tickets INNER JOIN long_activities
WHERE contacted_customer=1 
GROUP BY product;