import pickle


class Countries:
    def __init__(self):
        self.countries = {
            "slovakia": "Bratislava",
            "czech republic": "Prague"
        }

    def add_country(self, country, capital):
        self.countries[country] = capital
        print(f"pridané: {country} -> {capital}")

    def delete_country(self, country):
        if country in self.countries:
            del self.countries[country]
            print(f" vymazane {country} ")
        else:
            print(f"{country} neexistuje")

    def find_country(self, country):
        if country in self.countries:
            print(f"hlavne mesto {country} je {self.countries[country]}")
        else:
            print(f"{country} neexistuje")

    def edit_country(self, country, new_capital):
        if country in self.countries:
            self.countries[country] = new_capital
            print(f"{country} upravené na {new_capital}")
        else:
            print(f"{country} neexistuje")

    def print_countries(self):
        print("\nzoznam krajín:")
        for country, capital in self.countries.items():
            print(country, "->", capital)

    def save_data(self, filename="country.pkl"):
        with open(filename, "wb") as f:
            pickle.dump(self.countries, f)
        print("dáta uložené")

    def load_data(self, filename="country.pkl"):
        with open(filename, "rb") as f:
            self.countries = pickle.load(f)
        print("dáta načítané")


if __name__ == "__main__":
    c = Countries()

    c.add_country("hungary", "Budapest")
    c.add_country("poland", "Warsaw")

    c.find_country("slovakia")
    c.find_country("germany")

    c.edit_country("slovakia", "Bratislava")
    c.edit_country("germany", "Berlin")

    c.delete_country("czech republic")
    c.delete_country("france")

    c.print_countries()

    c.save_data()
    c.load_data()

    c.print_countries()