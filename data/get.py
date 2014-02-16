from data import connect

def CustomerByNumer(number):
    # query = "SELECT * FROM customers WHERE customer_no = %i AND active = TRUE;" % number
    conn = connect.getConnection()
    pass

def ArticleByNumber(number):
    # query = "SELECT * FROM articles WHERE article_no = %i AND active = TRUE;" % number
    conn = connect.getConnection()
    pass