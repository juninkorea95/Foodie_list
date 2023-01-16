from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

# import requests
# from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.8y9lufi.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/home1')
def home1():
    return render_template('index1.html')

@app.route('/home2')
def home2():
    return render_template('index2.html')
@app.route('/home3')
def home3():
    return render_template('index3.html')
@app.route('/home4')
def home4():
    return render_template('index4.html')
@app.route('/home5')
def home5():
    return render_template('index5.html')

@app.route("/food", methods=["POST"])
def food_post():
    name_receive = request.form['name_give']
    url_receive = request.form['url_give']
    star_receive = request.form['star_give']
    comment_receive = request.form['comment_give']

    food_list = list(db.foodie.find({}, {'_id': False}))
    count = len(food_list) + 1

    doc = {
        'num': count,
        'name': name_receive,
        'url': url_receive,
        'star': star_receive,
        'comment': comment_receive
    }
    db.foodie.insert_one(doc)

    return jsonify({'msg':'저장 완료!'})

# @app.route("/movie/delete", methods=["POST"])
# def movie_delete():
#     num_receive = request.form['num_give']
#     db.movies.delete_one({'num': int(num_receive)})
#     return jsonify({'msg': '삭제 완료!'})

@app.route("/food", methods=["GET"])
def food_get():
    food_list = list(db.foodie.find({}, {'_id': False}))
    food_list.reverse()
    return jsonify({'foods': food_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)