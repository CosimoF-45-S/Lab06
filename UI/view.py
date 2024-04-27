import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.dd_anno = None
        self.dd_brand = None
        self.dd_retailer = None
        self.btn_TopV = None
        self.btn_AnalizzaV = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("Analizza Vendite", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW 1
        self.dd_anno = ft.Dropdown(width= 300, options = [ft.dropdown.Option(key = "Nessun filtro", text="Nessun filtro")], label = "anno")
        self._controller.fill_dd_anno()
        self.dd_brand = ft.Dropdown(width= 300, options = [ft.dropdown.Option(text="Nessun filtro")], label = "brand")
        self._controller.fill_dd_brand()
        self.dd_retailer = ft.Dropdown(width= 400, options = [ft.dropdown.Option(text="Nessun filtro")], label = "retailer")
        self._controller.fill_dd_retailer()
        row1 = ft.Row(controls=[self.dd_anno, self.dd_brand, self.dd_retailer], alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row1)


        #ROW 2
        self.btn_TopV = ft.ElevatedButton(text= "Top Vendite", on_click=self._controller.handle_top_vendite)
        self.btn_AnalizzaV = ft.ElevatedButton(text= "Analizza Vendite", on_click=self._controller.handle_analizza_vendite)
        row2 = ft.Row(controls=[self.btn_TopV, self.btn_AnalizzaV], alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row2)



        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
