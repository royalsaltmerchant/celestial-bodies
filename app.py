import ephem
from flask import Flask, jsonify, send_from_directory

app = Flask(__name__)


@app.route("/")
def serve_static_page():
    return send_from_directory("static", "index.html")


@app.route("/api/planets")
def get_planet_info():
    # Set the current date and time
    date = ephem.now()

    # Create the planet objects
    mercury = ephem.Mercury()
    venus = ephem.Venus()
    mars = ephem.Mars()
    jupiter = ephem.Jupiter()
    saturn = ephem.Saturn()
    uranus = ephem.Uranus()
    neptune = ephem.Neptune()
    sun = ephem.Sun()
    moon = ephem.Moon()

    # Compute the positions of the planets
    mercury.compute(date)
    venus.compute(date)
    mars.compute(date)
    jupiter.compute(date)
    saturn.compute(date)
    uranus.compute(date)
    neptune.compute(date)
    sun.compute(date)
    moon.compute(date)

    planets = [sun, moon, mercury, venus, mars, jupiter, saturn, uranus, neptune]

    # Get the constellations for each planet
    planet_info = []
    for planet in planets:
        item = {
            "constellation": ephem.constellation(planet),
            "name": planet.name,
            "right_ascension": planet.ra,
            "declination": planet.dec,
        }
        planet_info.append(item)

    return jsonify(planet_info)


if __name__ == "__main__":
    app.run()
