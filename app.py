from flask import Flask,render_template,request
from poly import polynomial
from meta1 import meta1
from dynamic1 import dyn1
from dynamic2 import dyn2
from meta2 import meta2
app=Flask(__name__)

@app.route('/')
#@app.route('/fafa')
def index():
    return render_template("home.html")  
@app.route('/result',methods=['POST','GET'])
def result():

    if request.method=='GET':
        return render_template("moore.html")
    elif request.method=='POST':
        f1=request.files['f']
        data=f1.stream.readlines()
        if len(data)==3:
            firstLine=int(data[0])
            secondLine=str(data[1].decode("utf-8")).split("\t")
            thirdLine=str(data[2].decode("utf-8")).split("\t")
            firstLine=[k for k in range(1,firstLine+1)]
            secondLine=[int(j) for j in secondLine]
            thirdLine=[int(j) for j in thirdLine]
            if request.form['toDO']=='Polynomial':
                res=polynomial(firstLine,secondLine,thirdLine)
                return render_template("moore.html",dD=res)
            elif request.form['toDO']=='Dynamic':
                res=dyn1(firstLine,secondLine,thirdLine)
                return render_template("dynamic.html",dD=res)
            else:
                res=meta1(firstLine,secondLine,thirdLine)
                return render_template("meta.html",dD=res)
        if len(data)==5:
            firstLine=int(data[0])
            secondLine=str(data[1].decode("utf-8")).split("\t")
            thirdLine=str(data[2].decode("utf-8")).split("\t")
            FourthLine=str(data[3].decode("utf-8")).split("\t")
            FifthLine=str(data[4].decode("utf-8")).split("\t")
            firstLine=[k for k in range(1,firstLine+1)]
            secondLine=[int(j) for j in secondLine]
            thirdLine=[int(j) for j in thirdLine]
            FourthLine=[int(j) for j in FourthLine]
            FifthLine=[int(j) for j in FifthLine]
            if request.form['toDO']=='Dynamic':
                res=dyn2(firstLine,secondLine,thirdLine,FourthLine,FifthLine)
                return render_template("dynamic.html",dD=res)
            else :
                res=meta2(firstLine,secondLine,thirdLine,FourthLine,FifthLine)
                return render_template("meta.html",dD=res)
                   
if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0")