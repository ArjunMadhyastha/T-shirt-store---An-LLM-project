few_shots = [
    {
        'Question': "How many t-shirts do we have left for Nike in XS size and white color?",
        'SQLQuery': "select SUM(stock_quantity) from t_shirts where brand='Nike' and color='white' and size='XS'",
        'SQLResult': "Result of the SQL query",
        'Answer': 72
    },
    {
        'Question': "How much is the total size of the inventory for all S-size t-shirts?",
        'SQLQuery': "SELECT SUM(price*stock_quantity) from t_shirts where size='S'",
        'SQLResult': "Result of the query",
        'Answer': 21216
    },
    {
        'Question': "If we have to sell all the Levi's T-shirts today.How much revenue our store will generate?",
        'SQLQuery': "select sum(a.total_amount * ((100-COALESCE(discounts.pct_discount,0))/100)) as total_revenue from (select sum(price*stock_quantity) as total_amount, t_shirt_id from t_shirts where brand = 'Levi' group by t_shirt_id) a left join discounts on a.t_shirt_id = discounts.t_shirt_id",
        'SQLResult': "Result of the query",
        'Answer': 22251
    },
    {
        'Question': "How many white color Levi's shirt I have?",
        'SQLQuery': "select SUM(stock_quantity) from t_shirts where brand='Levi' and color='White'",
        'SQLResult': "Result of the query",
        'Answer': 198
    }

]
