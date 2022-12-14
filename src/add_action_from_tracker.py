def add_action_from_tracker(action, cursor):

    # @todo : ajouter une couche de POO ? Produit, action, etc

    print(cursor)

    # Insert product in table products
    product_id = action.loc["_TrackerAction__product_id"]
    product_ref = action.loc["_TrackerAction__product_ref"]
    product_template = action.loc["_TrackerAction__product_template"]
    product_language = action.loc["_TrackerAction__product_language"]
    add_product(product_id, product_ref, product_template, product_language, cursor)

    # # Insert action in tracker_action
    # tmp_io = action.loc["_TrackerAction__io"]
    # tmp_action = action.loc["_TrackerAction__action"]
    # tmp_created_at = action.loc["_TrackerAction__created_at"]
    # tmp_local_created_at = action.loc["_TrackerAction__local_created_at"]
    # print(tmp_io)
    # #
    # # add_tracker_action = ("INSERT INTO tracker_action"
    # #                       ())

def add_product(product_id, product_ref, product_template, product_language, cursor):

    # Insert product in table products

    if product_id != '-':

        add_product_query = ("INSERT INTO products"
                             "(product_id, product_ref, template, language)"
                             "VALUES (%s, %s, %s, %s)"
                             )
        data_product = (product_id, product_ref, product_template, product_language)
        cursor.execute(add_product_query, data_product)
        last_product = cursor.lastrowid
        print(last_product)

def delete_product(product_id, cursor):

    del_product_query = "DELETE FROM products WHERE product_id = %s"
    del_data = [product_id]
    cursor.execute(del_product_query, del_data)
    last_product = cursor.lastrowid
    print(last_product)