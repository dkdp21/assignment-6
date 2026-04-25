"""
Project: Contact Management System
Name: Divyanshu Deep
Roll Number: 2401010215
Course: B.Tech CSE Core
Section: D
Date: 12-04-2026
"""

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage (no database)
contacts = []

# HOME - View all contacts
@app.route('/')
def index():
    return render_template('index.html', contacts=contacts)

# ADD CONTACT
@app.route('/add', methods=['GET', 'POST'])
def add_contact():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']

        # Validation
        if name and phone and email:
            contacts.append({
                'name': name,
                'phone': phone,
                'email': email
            })

        return redirect(url_for('index'))

    return render_template('add_contact.html')

# EDIT CONTACT
@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit_contact(index):
    contact = contacts[index]

    if request.method == 'POST':
        contact['name'] = request.form['name']
        contact['phone'] = request.form['phone']
        contact['email'] = request.form['email']

        return redirect(url_for('index'))

    return render_template('edit_contact.html', contact=contact, index=index)

# DELETE CONTACT
@app.route('/delete/<int:index>')
def delete_contact(index):
    contacts.pop(index)
    return redirect(url_for('index'))

# SEARCH (BONUS)
@app.route('/search', methods=['POST'])
def search():
    query = request.form['query'].lower()
    filtered = [c for c in contacts if query in c['name'].lower() or query in c['phone']]
    return render_template('index.html', contacts=filtered)

if __name__ == '__main__':
    app.run(debug=True)