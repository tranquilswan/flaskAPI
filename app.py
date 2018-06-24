from flask import Flask
from flask import jsonify
from flask import request
#from flask import abort

app = Flask(__name__)

#defining the dictionary to hold object

stockDB=[
    {
        'ticker':'INTC',
        'company':'Intel',
        'comment':'Leader in semi-conductor space'
    },
    {
        'ticker':'NFLX',
        'company':'Netflix',
        'comment':'Stream movies and tv....n\'chill'
    }
]


#GET request on all stocks in DB
@app.route('/stocks/',methods=['GET'])
def getAllStocks():
    return jsonify({'STOCKS':stockDB})

'''
    stock = [stock for stock in stockDB
        if(stock['ticker']==ticker)]
    
    The above can be explained as:
    
    stock = [expression for item in dictionary
        if(condition)

'''

#GET request with ticker name
@app.route('/stocks/<ticker>',methods=['GET'])
def getStock(ticker):
    stock = [stock for stock in stockDB
        if(stock['ticker']==ticker)]
    return jsonify({'STOCK':stock})

#PUT Request (what if the user provides a lowercase ticker?)
@app.route('/stocks/<ticker>',methods=['PUT'])
def updateStock(ticker):
    stock = [stock for stock in stockDB
             if(stock['ticker']==ticker)]
    if 'comment' in request.json:
        stock[0]['comment'] = request.json['comment']
    return jsonify({'STOCK':stock[0]})

@app.route('/stocks/',methods=['POST'])
def addStock():
    data = {
        'ticker':request.json['ticker'],
        'company':request.json['company'],
        'comment':request.json['comment']
    }
    stockDB.append(data)
    return jsonify(data)

@app.route('/stocks/<ticker>',methods=['DELETE'])
def removeStock(ticker):
    stockToDelete = [stock for stock in stockDB
                     if(stock['ticker']==ticker)]
    if len(stockToDelete) == 0:
        return jsonify({'response': 'Le Failure!'})
        #abort(404) # displays a different message
    stockDB.remove(stockToDelete[0])
    #return jsonify({'STOCKS':stockDB}) # return the dict now
    return jsonify({'response': 'Le Success!'})


#when the user goes to URL/easterEgg => execute easterEgg()
@app.route("/easterEgg")
def easterEgg():
    return "It\'s like being on the bridge in GTA:SA"

if __name__ == '__main__':
    app.run(debug=True) #run with debug on