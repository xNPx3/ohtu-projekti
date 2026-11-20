"""
BibTeX-dataan ja tiedostoihin liittyvät funktiot tänne?

Esimerkki dataa:
@article{einstein1935can,
  author  = {Einstein, A. and Podolsky, B. and Rosen, N.},
  title   = {Can Quantum-Mechanical Description of Physical Reality Be Considered Complete?},
  journal = {Physical Review},
  year    = {1935},
  doi     = {10.1103/PhysRev.47.777}
}
"""
# Alun artikkeli vielä vaiheessa, voi miettiä parempaa toteutusta myöhemmin
# Muokataan loppuun valmiiksi, kun tiedetään miten ja mitä dataa saadaan


from modules.io_handler import IOHandler


class BibTeXHandler:
    """
    Luokka BibTeX-datan hallintaan
    """

    def __init__(self, io):
        self.io = io

    def create_bibtex_data(self, entries: list[tuple[int, str, str, str | None, int | None, str | None]]):
        """
        Create BibTeX data from database entries (rows)
        """

        # self.validate(data) # TODO: DOESNT WORK

        output = ""

        # DB keys
        keys = ["id", "author", "title", "journal", "year", "doi"]

        for entry in entries:
            type = "book"
            id = entry[0]

            content = ""
            for i in range(1, len(entry)):
                key = keys[i]
                value = entry[i]
                content += f"    {key} = {{{value}}},\n"

            output += f"""@{type}{{{id}\n{content}}}\n"""

        return output

    def validate(self, data: dict):
        """
        TODO TODO TODO
        Validoidaan data,
        esim. key:ssa ei saa olla välilyöntejä tms.
        """
        if " " in data["key"]:
            # TODO
            raise ValueError("Key sisältää välilyöntejä")

    def save_to_file(self, filepath: str, bibtex_data: str):
        """
        Saves the data to a file.
        """
        self.io.write_file(bibtex_data, filepath)


# Testi kehitysympäristössä
if __name__ == "__main__":
    data = {
        "type": "book",
        "key": "kirja123",
        "author": "Einstein, A.",
        "title": "Kirja",
        "journal": "tiedelehti",
        "year": 2027,
    }
    """
    init_database()

    db = OhtuDatabase()
    io = IOHandler()
    handler = BibTeXHandler(io)

    viittaukset = db.get_references()
    # for viittaus in viittaukset:
    #     print(viittaus)

    bibtex = handler.create_bibtex_data(viittaukset)
    io.console_print(bibtex)
    """
