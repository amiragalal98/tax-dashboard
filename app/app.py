from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
app=Flask(__name__)
def get_db_connection():
    return mysql.connector.connect(
        host='db' ,
        user='root',
        password='rootpass',
        database='taxdb'
    )
    
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        taxpayer = request.form['taxpayer']
        tax_paid = request.form['tax_paid']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO taxes (taxpayer, tax_paid) VALUES (%s, %s)', (taxpayer, tax_paid ))
        conn.commit()
        conn.close()
        return redirect('/')
        
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM taxes')
    taxes = cursor.fetchall()
    conn.close()
    return render_template('index.html', taxes=taxes)
if __name__=="__main__":
        app.run (host="0.0.0.0", port=5000)