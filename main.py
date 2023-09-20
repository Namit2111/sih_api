from flask import Flask,request
from gradio_client import Client
import requests
from html_similarity import style_similarity, structural_similarity, similarity
from python_sim import calculate_structure_similarity 
import os



app = Flask(__name__)
HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
@app.route('/hello', methods=['GET'])
def hello():
    return 'Hello'




@app.route('/Sentence_similarity',methods=['GET','POST'])
def Sentence():
    sen1= request.args.get('sen1')
    # sen2 = request.args.get('sen2') 
    sen2 = "It is an online retailer and web service provider.\nIt is a shop for buuying groceries\n"
    response = requests.post("https://namit2111-sentence-similarity.hf.space/run/predict", headers=HEADERS,json={
	"data": [
		sen1,
        sen2
        
	]
}).json()
    if response["data"]:
        return response['data']
    return "Error"





@app.route('/html_struc_sim',methods=['GET','POSt'])
def html_struc_sim():
    data = request.get_json()

    if 'html1' in data and 'html2' in data:
        html1 = data['html1']
        html2 = data['html2']

        # Calculate structural similarity
        similarity_ratio = structural_similarity(html1, html2)
        return str(similarity_ratio)



@app.route("/python_sim",methods=['GET','POST'])
def py_sim():

    file1 = request.files['file1']
    file2 = request.files['file2']
    file1_path = os.path.join(os.curdir, 'file1.py')
    file2_path = os.path.join(os.curdir, 'file2.py')
    file1.save(file1_path)
    file2.save(file2_path)
    print(file1)
    value =calculate_structure_similarity(file1_path,file2_path)
    
    return str(value)



@app.route("/cal_score",methods=["GET","POST"])
def cal():
    v1 = request.args.get("des_score")
    v2 = request.args.get("proj_score")


    # Weightage for description and project (40% to description, 60% to project)
    weight_description = 0.4
    weight_project = 0.6

    # Calculate the combined similarity score (S)
    S = weight_description * v1 + weight_project * v2

    # Print the combined similarity score
    return str(S)



if __name__ == '__main__':
    app.run(debug=True)
