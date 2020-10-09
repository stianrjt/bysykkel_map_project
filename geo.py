import requests
from matplotlib import pyplot as plt
import pandas as pd
import mplleaflet


def draw_map():
    stations = get_stations()
    stations = pd.json_normalize(stations)
    longitude = stations["lon"]
    latitude = stations["lat"]

    status = get_status()
    status = pd.json_normalize(status)
    available_bikes = status["num_bikes_available"]

    fig = plt.figure()
    plt.scatter(longitude, latitude, s = stations["capacity"]*3, c=available_bikes, cmap="RdYlGn", vmin=0, vmax=10)

    for lon,lat, no_available in zip(longitude,latitude, available_bikes):
        label = str(no_available)
        plt.annotate(label, (lon,lat))
    mplleaflet.save_html(fileobj="static/map/map.html")


def get_stations():
    raw_stations = requests.get("https://gbfs.urbansharing.com/oslobysykkel.no/station_information.json", headers={"Client-Identifier":"test for hobbyprosjekt"})
    stations_response = raw_stations.json()
    stations = stations_response["data"]
    stations = stations["stations"]

    return stations


def get_status():
    raw_status = requests.get("https://gbfs.urbansharing.com/oslobysykkel.no/station_status.json", headers={"Client-Identifier":"test for hobbyprosjekt"})
    status_response = raw_status.json()
    status_response = status_response["data"]
    status = status_response["stations"]

    return status


def get_id_by_name(name):
    stations = get_stations()
    stations = pd.json_normalize(stations)
    station = stations.loc[stations['name'].str.lower() == name.lower()]
    id = station["station_id"]

    return int(id), station


def get_status_by_id(id):
    status = get_status()
    status = pd.json_normalize(status)
    status = status.loc[status["station_id"].str.lower() == str(id)]
    print(status)

    return status


def print_station_names():
    stations_response = get_stations()
    for station in stations_response:
        print(station["name"])


def vis_ledige_for_stasjon(stasjon="all"):
    status = get_status()
    stations = get_stations()

    if stasjon.lower() == "all":
        for stasjon_id, stasjon_name in zip(status, stations):
            print("Name:", stasjon_name["name"], "ID:", stasjon_id["station_id"])
            print("Capacity:", stasjon_name["capacity"], "Free:",stasjon_id["num_bikes_available"], "\n")

    else:
        for station_id, station_name in zip(status, stations):
            if station_name["name"].lower() == stasjon.lower():
                print("Name:", station_name["name"], "ID:", station_id["station_id"])
                print("Capacity:", station_name["capacity"], "Free:",station_id["num_bikes_available"], "\n")


if __name__ == '__main__':
    # vis_ledige_for_stasjon("botanisk hage sør")
    # vis_ledige_for_stasjon("birkelunden")
    # vis_ledige_for_stasjon("tøyen skole")
    # vis_ledige_for_stasjon()
    # print_station_names()
    draw_map()
    # id, station = get_id_by_name("botanisk hage sør")
    # get_status_by_id(460)
