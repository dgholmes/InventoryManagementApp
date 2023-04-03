class AddProductScreen(Screen):
    date = StringProperty
    borrowDB = {}
    borrowDB2 = {}

    def date_today(self, *args):
        today = date.today()
        self.ids.entry_date.text = str(today)

    def on_save(self, instance, value, date_range):
        '''
        Events called when the "OK" dialog box button is clicked.

        :type instance: <kivymd.uix.picker.MDDatePicker object>;

        :param value: selected date;
        :type value: <class 'datetime.date'>;

        :param date_range: list of 'datetime.date' objects in the selected range;
        :type date_range: <class 'list'>;
        '''
        self.ids.entry_date.text = str(value)

        # print(instance, value, date_range)

    def on_cancel(self, instance, value):
        '''Events called when the "CANCEL" dialog box button is clicked.'''

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

    def add_new_product(self, serial, name, year, version, category, entry_date, owner, user, status):
        new_case = {"Serial": serial,
                    "Product Name": name,
                    "Year": year,
                    "Version": version,
                    "Category": category,
                    "Entry Date": entry_date,
                    "Owner": owner,
                    "User": user,
                    "Status": status
                    }
        self.borrowDB[self.ids.serial.text] = new_case
        for k, v in self.borrowDB.items():
            print(k, v)

        database.add_product(connection, serial, name, year, version, category, entry_date, owner, user, status)

    def clr_txt(self):
        self.ids.name.text = ""
        self.ids.serial.text = ""
        self.ids.version.text = ""
        self.ids.category.text = ""
        self.ids.year.text = ""
        self.ids.status.text = ""
        self.ids.entry_date.text = ""
        self.ids.owner.text = ""
        self.ids.user.text = ""