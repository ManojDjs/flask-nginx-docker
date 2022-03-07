from flask import Flask,jsonify,request
app = Flask(__name__)
from app.large_number_addition import findSum
def checkPostedData(postedData, functionName):
        if "list" not in postedData:
            return 301 #Missing parameter
        if postedData["list"]==[]:
            return 302 # empty list
        else:
            return 200
        
    
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found!"})

@app.route('/')
def hello_world():
    return 'Hello, World - From a container!'

@app.route("/total",methods=["POST"])
def total_sum():
        #If I am here, then the resouce  was requested using the method POST

        #Step 1: Get posted data:
        postedData = request.get_json()
        print(postedData)

        #Steb 1b: Verify validity of posted data
        status_code = checkPostedData(postedData, "division")


        if (status_code!=200):
            retJson = {
                "Message": "An error happened,you must send list of numbers , example: list:[300,500,600] or list empty",
                "Status Code":status_code
            }
            return jsonify(retJson)
        


        #If i am here, then status_code == 200
    
        sum_list=postedData['list']
        # here we stored list sent to out api but we need to make sure thie works fine with all numbers
        # we wrote util funtiion called large_number_addition for adding large numbers 
        total=0
        if sum_list[0]>100000:
            total=sum_list[0]
            for num in range(1,len(sum_list)-1):
                print()
                total=int(findSum(str(total),str(sum_list[num])))
        else:
            total=sum(sum_list)
        #Step : Multiply the posted data
        
        retMap = {
            'total': total,
            'Status Code': 200
        }
        return jsonify(retMap)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')