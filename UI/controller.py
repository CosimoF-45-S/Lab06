import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def fill_dd_anno(self):
        anni = self._model.fill_dd_anno()
        for anno in anni:
            self._view.dd_anno.options.append(ft.dropdown.Option(anno[0]))

    def fill_dd_brand(self):
        brands = self._model.fill_dd_brand()
        for brand in brands:
            self._view.dd_brand.options.append(ft.dropdown.Option(brand))

    def fill_dd_retailer(self):
        retailers = self._model.fill_dd_retailer()
        for ret in retailers:
            self._view.dd_retailer.options.append(ft.dropdown.Option(key= ret.retailer_code, text= ret.retailer_name, data= ret))

    def handle_top_vendite(self, e):
        self._view.txt_result.controls.clear()
        anno = self._view.dd_anno.value
        brand = self._view.dd_brand.value
        retailer = self._view.dd_retailer.value

        if retailer == "Nessun filtro":
            retailer = None
        if brand == "Nessun filtro":
            brand = None
        if anno == "Nessun filtro":
            anno = None
        topV = self._model.handle_top_vendite(anno, brand, retailer)
        for vendita in topV:
            self._view.txt_result.controls.append(ft.Text(f"Data: {vendita[0]}; Ricavo: {vendita[1]}; Retailer: {vendita[2]}; Product: {vendita[3]}"))
        self._view.update_page()


    def handle_analizza_vendite(self, e):
        self._view.txt_result.controls.clear()
        anno = self._view.dd_anno.value
        brand = self._view.dd_brand.value
        retailer = self._view.dd_retailer.value
        if retailer == "Nessun filtro":
            retailer = None
        if brand == "Nessun filtro":
            brand = None
        if anno == "Nessun filtro":
            anno = None
        analisi = self._model.handle_analizza_vendite(anno, brand, retailer)
        self._view.txt_result.controls.append(ft.Text("Statistiche vendite:"))
        self._view.txt_result.controls.append(ft.Text(f"Giro d'affari: {analisi[0]}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero vendite: {analisi[1]}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero retailers coinvolti: {analisi[2]}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero prodotti coinvolti: {analisi[3]}"))
        self._view.update_page()

