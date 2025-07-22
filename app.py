from flask import Flask,render_template,request
import requests
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)

class City(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String,nullable=False)


@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'POST':
        new_city=request.form.get('city')
        if new_city:
            new_city_obj=City(name=new_city)
            
        db.session.add(new_city_obj)
        db.session.commit()

    

    cities=City.query.all()
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=e621c45f4b26a86fb35e2213a310a139'

    weather_data = []

    for city in cities:
          r=requests.get(url.format(city.name)).json()
          weather = {
           'city' : city.name,
           'temperature' : r['main']['temp'],
           'description' : r['weather'][0]['description'],
           'icon' : r['weather'][0]['icon'],
        }
          
          weather_data.append(weather)
        
     
          


    
  

    return render_template('index.html', weather_data=weather_data)

if __name__ == "__main__":
    app.run(debug=True)

with app.app_context():
    db.create_all()