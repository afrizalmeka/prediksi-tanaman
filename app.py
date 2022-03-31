from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model_file = open('model.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')
def index():
    return render_template('index.html', hasil_prediksi_tanaman="")

@app.route('/predict', methods=['POST'])
def predict():
    '''
    Predict the insurance cost based on user inputs
    and render the result to the html page
    '''
    nitrogen, fosfor, kalium, suhu, kelembaban, phtanah, curahhujan  = [x for x in request.form.values()]

    data = []

    data.append(float(nitrogen))
    data.append(float(fosfor))
    data.append(float(kalium))
    data.append(float(suhu))
    data.append(float(kelembaban))
    data.append(float(phtanah))
    data.append(float(curahhujan))
    # if sex == 'Laki-laki':
    #     data.extend([0, 1])
    # else:
    #     data.extend([1, 0])

    # if smoker == 'Ya':
    #     data.extend([0, 1])
    # else:
    #     data.extend([1, 0])
    
    nama = {0 : 'Tanaman Padi', 1 : 'Tanaman Jagung', 2 : 'Tanaman Kacang Chickpea', 3 : 'Tanaman Kacang Merah', 4 : 'Tanaman Kacang Polong',
        5 : 'Tanaman Ngengat', 6 : 'Tanaman Kacang Hijau', 7 : 'Tanaman Black Gram', 8 : 'Tanaman Lentil', 9 : 'Tanaman Buah Delima',
        10 : 'Tanaman Buah Pisang', 11 : 'Tanaman Buah Mangga', 12 : 'Tanaman Buah Anggur', 13 : 'Tanaman Buah Semangka', 14 : 'Tanaman Buan Melon', 15 : 'Tanaman Buah Apel',
        16 : 'Tanaman Buah Jeruk', 17 : 'Tanaman Buah Pepaya', 18 : 'Tanaman Kelapa', 19 : 'Tanaman Kapas', 20 : 'Tanaman Jute', 21 : 'Tanaman Kopi'}

    prediction = model.predict([data])
    output = nama[prediction[0]]

    # prediction2 = model.predict([data])
    # output2 = nama[prediction2[0]]

    return render_template('index.html', hasil_prediksi_tanaman=output, nitrogen=nitrogen, fosfor=fosfor, kalium=kalium, suhu=suhu, kelembaban=kelembaban, phtanah=phtanah, curahhujan=curahhujan)


if __name__ == '__main__':
    app.run(debug=True)