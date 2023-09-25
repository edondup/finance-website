SELECT symbol, SUM(shares * price) AS 


-- SELECT
--     symbol,
--     SUM(shares * tradetype) AS totalshares,
--     SUM(price * tradetype) AS totalvalue
-- FROM
--     (t.* case WHEN type = 'BUY' then 1 else -1 end AS tradetype FROM trades) t
-- WHERE userid = '10'
-- GROUP BY symbol;