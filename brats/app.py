import os
from flask import Flask, request, render_template
from brats.patient import show_patient_mri, show_segmentation

app = Flask(__name__)
saved_index = 0

@app.route('/')
def my_form():
    return render_template('patient_info.html')

@app.route('/info', methods=['POST'])
def patient_mri():
    global saved_index
    data_index = request.form["data_index"]
    saved_index = int(data_index)
    show_patient_mri(saved_index)
    return render_template('patient_info.html')

@app.route('/segmentation', methods=['POST'])
def tumor_segmentation():
    global saved_index
    show_segmentation(saved_index)
    return render_template('patient_info.html')



if __name__ == "__main__":
    app.run("127.0.0.1", 5000, debug=True)
    #show_patient_mri(104)