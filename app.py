from flask import Flask, render_template, request
import mysql.connector 

app = Flask(__name__)


def fetch_data(product_id="", warranty_id="", product_det="", product_id_del=""):
    
    cnx = mysql.connector.connect(user='root', password='password',
                              host='localhost', database='apple_products')
    cursor = cnx.cursor()
    
    if len(product_id)>=1:

        product, product_id = product_id.split(",")
        print(product, product_id)
        if product == "computers":
            query = """

            select * from apple_products.computers
            where computers.comp_Id = {Id};
            
            """
        elif product == "mobiles":
            query = """

            select * from apple_products.mobiles
            where mobiles.mobile_Id = {Id};
            
            """
        elif product == "accessories":
            query = """

            select * from apple_products.accessories
            where accessories.accessory_Id = {Id};
            
            """

        main_query = query.format(Id=product_id)
        cursor.execute(main_query)
        rows = cursor.fetchall()
        sequence = cursor.column_names
        main_data = []
        for result in rows:
            main_data.append(result)
        return(sequence, tuple(main_data))
        
    if len(warranty_id)>=1:

        product, product_id = warranty_id.split(",")
        print(product, product_id)
        if product == "computers":
            query = """

            select * from apple_products.computers
            join apple_products.warranty
            on computers.comp_id = warranty.product_id
            where warranty.warranty_Id = {Id};
            
            """
        elif product == "mobiles":
            query = """

            select * from apple_products.mobiles
            join apple_products.warranty
            on mobiles.mobile_id = warranty.product_id
            where warranty.warranty_Id = {Id};
            
            """
        elif product == "accessories":
            query ="""

            select * from apple_products.accessories
            join apple_products.warranty
            on accessories.accessory_id = warranty.product_id
            where warranty.warranty_Id = {Id};
            
            """

        main_query = query.format(Id=product_id)
        cursor.execute(main_query)
        rows = cursor.fetchall()
        sequence = cursor.column_names
        main_data = []
        for result in rows:
            main_data.append(result)
        return(sequence, tuple(main_data))

    if len(product_det)>1:

        product, Id, A1, B1, C1, D1 = product_det.split(",")
        if product == "computers":
            query = """
            INSERT INTO apple_products.computers (comp_id, model_name, ram, ssd, processor)
            VALUES ({Id},"{A1}",{B1},{C1},{D1});
            """
            main_query = query.format(Id=Id, A1 = A1, B1 = B1, C1 = C1, D1 = D1)
            cursor.execute(main_query)
            cnx.commit()

            query = """
            
            select * from apple_products.computers

            """

        elif product == "mobiles":
            query = """
            INSERT INTO apple_products.mobiles (mobile_id, model_name, ram, storage, processor)
            VALUES ({Id},"{A1}",{B1},{C1},{D1});
            """
            main_query = query.format(Id=Id, A1 = A1, B1 = B1, C1 = C1, D1 = D1)
            cursor.execute(main_query)
            cnx.commit()

            query = """
            
            select * from apple_products.mobiles

            """
        elif product == "accessories":

            query = """
            INSERT INTO apple_products.accessories (accessory_id, name, type, compatibility, mode)
            VALUES ({Id},"{A1}","{B1}","{C1}","{D1}");
            """
            main_query = query.format(Id=Id, A1 = A1, B1 = B1, C1 = C1, D1 = D1)
            cursor.execute(main_query)
            cnx.commit()

            query = """
            
            select * from apple_products.accessories

            """

        main_query = query.format()
        cursor.execute(main_query)
        rows = cursor.fetchall()
        sequence = cursor.column_names
        main_data = []
        for result in rows:
            main_data.append(result)
        return(sequence, tuple(main_data))

    
    if len(product_id_del)>=1:
        product, product_id = product_id_del.split(",")
        
        if product == "computers":
            query = """

            Delete from apple_products.computers
            where computers.comp_id = {Id};
            
            """
            main_query = query.format(Id=product_id)
            cursor.execute(main_query)
            cnx.commit()

            query = """
            select * from apple_products.computers;
            """
        elif product == "mobiles":
            query = """

            Delete from apple_products.mobiles
            where mobiles.mobile_id = {Id};
            
            """
            main_query = query.format(Id=product_id)
            cursor.execute(main_query)
            cnx.commit()

            query = """
            select * from apple_products.mobiles;
            """
        elif product == "accessories":
            query = """

            Delete from apple_products.accessories
            where accessories.accessory_id = {Id};
            
            """
            main_query = query.format(Id=product_id)
            cursor.execute(main_query)
            cnx.commit()

            query = """
            select * from apple_products.accessories;
            """
        cursor.execute(query)
        rows = cursor.fetchall()
        print(rows)
        sequence = cursor.column_names
        main_data = []
        print(main_data)
        for result in rows:
            main_data.append(result)
        print(main_data)
        return(sequence, tuple(main_data))

   
@app.route("/", methods =["GET", "POST"])
def index():
    if request.method == "POST":
        product_id = request.form['product_id']
        warranty_id = request.form['warranty_id']
        product_det = request.form['product_det']
        product_id_del = request.form['product_id_del']
        headings, data = fetch_data(product_id, warranty_id, product_det, product_id_del)
        return render_template("Main_page.html", headings=headings, data=data)
    return render_template("Main_page.html")


if __name__=="__main__":
    app.run(debug=True)