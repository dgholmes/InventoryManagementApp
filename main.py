# requirement: kivymd 0.104.2
from kivy.app import App
from kivy.core.image import Texture
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.properties import ListProperty, NumericProperty, StringProperty, ObjectProperty, BooleanProperty, \
    ReferenceListProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.textinput import TextInput
from kivy.utils import rgba
from kivymd.app import MDApp
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivymd.toast import toast
from kivymd.uix.behaviors import FakeRectangularElevationBehavior, RectangularRippleBehavior, \
    FakeCircularElevationBehavior, CircularRippleBehavior, FocusBehavior
from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.clock import Clock
import cv2
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.list import TwoLineIconListItem, IconLeftWidget, ILeftBodyTouch, TwoLineAvatarIconListItem, \
    IRightBodyTouch
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.selectioncontrol import MDCheckbox
from pylibdmtx.pylibdmtx import decode
import time
import winsound
import datetime
from datetime import datetime, date
import database

Window.size = (310, 580)


# Window.size = (375, 812)


# Window.size = (390, 844)


class CamBox(FakeRectangularElevationBehavior, MDFloatLayout):
    pass


class NavBar(FakeRectangularElevationBehavior, MDFloatLayout):
    pass


class SearchBar(FakeRectangularElevationBehavior, MDFloatLayout):
    pass


class ImageButton(FakeRectangularElevationBehavior, RectangularRippleBehavior, ButtonBehavior, MDBoxLayout):
    pass


class IconButton(FakeRectangularElevationBehavior, RectangularRippleBehavior, ButtonBehavior, MDFloatLayout):
    pass


# class for the 'others' Icon Buttons on the home page
class HomeIcon(ButtonBehavior, RectangularRippleBehavior, MDRelativeLayout):
    source = StringProperty('xpBattery.png')
    text = StringProperty('Home')
    no = StringProperty('10')


# class for Icon Buttons on the create page
class CreateButton(FakeRectangularElevationBehavior, RectangularRippleBehavior, ButtonBehavior, MDBoxLayout):
    source = StringProperty('xpBattery.png')
    text = StringProperty('Home')


# class for Icons in the summary widget in the homepage
class SummaryIcon(MDRelativeLayout):
    source = StringProperty('xpBattery.png')
    text = StringProperty('Home')
    no = StringProperty('100')


class SummaryIcon1(FakeRectangularElevationBehavior, RectangularRippleBehavior, ButtonBehavior, MDBoxLayout):
    source = StringProperty('xpBattery.png')
    text = StringProperty('Home')
    no = StringProperty('100')


# class for Navigation Icon Buttons
class NavIconButton(ButtonBehavior, RectangularRippleBehavior, FakeRectangularElevationBehavior, MDFloatLayout):
    icon = StringProperty('home')
    text = StringProperty('Home')
    text_color = ObjectProperty()


class InfoList(FakeRectangularElevationBehavior, MDFloatLayout):
    title = StringProperty('Device Name')
    content = StringProperty('XP Battery')


class ItemCard(FakeRectangularElevationBehavior, MDFloatLayout):
    source = StringProperty('ok2.png')
    device_name = StringProperty('P30 Fast Charger')
    serial_no = StringProperty('761304500011')


class ItemCard2(FakeRectangularElevationBehavior, MDFloatLayout):
    device_name = StringProperty()
    serial_no = StringProperty()
    no_of_device = NumericProperty()


class ItemCard3(FakeRectangularElevationBehavior, MDFloatLayout):
    device_name = StringProperty()
    serial_no = StringProperty()
    no_of_device = NumericProperty()


class AccountListItem(ButtonBehavior, RectangularRippleBehavior, MDBoxLayout):
    source = StringProperty('circled_user.png')
    text = StringProperty('Password')
    icon = StringProperty('chevron-right')


class RentalsListItem(ButtonBehavior, RectangularRippleBehavior, MDBoxLayout):
    source = StringProperty('circled_user.png')
    name = StringProperty('RoboAir Systems')
    rent_date = StringProperty('2020.04.16')
    status = StringProperty('Rented')


class CustomerCard1(ButtonBehavior, RectangularRippleBehavior, MDBoxLayout):
    source = StringProperty('circled_user.png')
    name = StringProperty('Dogara')
    phone_no = StringProperty('01012345678')
    org = StringProperty('ToppField')


class ProductCard(ButtonBehavior, RectangularRippleBehavior, MDBoxLayout):
    source = StringProperty('xpgen.ico')
    serial = StringProperty('761304500011')
    name_version = StringProperty('XP20, CN')
    status = StringProperty('inUse')

    def pass_serial(self, instance):
        serial = instance.serial
        do = ProductDetailScreen()
        do.get_details(serial)
        self.manager.current = "product_details"

    # def see_details(self):
    #     do = ProductDetailScreen()
    #     do.get_details(self.serial)
    #     print(self.serial)
    #     # self.manager.current = "product_details"


class BorrowCard(FakeRectangularElevationBehavior, MDBoxLayout):
    pass


class NoteCard(FakeRectangularElevationBehavior, MDBoxLayout):
    pass


class ListItemWithCheckbox(TwoLineAvatarIconListItem):
    '''Custom list item'''

    def __init__(self, serial=None, **kwargs):
        super().__init__(**kwargs)
        # state a pk which we shall use link the list items with the database primary keys
        self.serial = serial

    def on_release(self):
        print("Clicked")
        print(self.serial)
        print(self.secondary_text)

    def mark(self, check, list_item):
        '''mark the task as complete or incomplete'''
        if check.active == True:
            # list_item.text = '[s]' + list_item.text + '[/s]'
            print(list_item.serial)  # here
        else:
            print("list_item.serial")  # Here

    def delete_item(self, list_item):
        '''Delete the task'''
        print('deleted')
        # self.parent.remove_widget(list_item)
        # database.delete_task(list_item.serial)  # Here


class LeftCheckbox(ILeftBodyTouch, MDCheckbox):
    '''Custom left container'''


class RightLabel(IRightBodyTouch, MDBoxLayout):
    '''Custom right container.'''


class MainScreen(Screen):
    dialog = None

    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.prompt_get_all_products()

    def enter_name_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Enter Name:",
                type="custom",
                content_cls=Content(),
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        # theme_text_color="Custom",
                        # text_color=self.theme_cls.primary_color,
                        on_release=self.close_dialog
                    ),
                    MDFlatButton(
                        text="ENTER",
                        # theme_text_color="Custom",
                        # text_color=self.theme_cls.primary_color,
                        on_release=self.change_screen
                    ),
                ],
            )
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def change_screen(self, *args):
        self.manager.current = "scan"
        self.dialog.dismiss()

    def add_to_screen(self, products):
        if len(self.ids.inventory_list.children) > 0:
            for index in range(len(self.ids.inventory_list.children)):
                self.ids.inventory_list.remove_widget(self.ids.inventory_list.children[0])
        for product in products:
            add_products = ProductCard(name_version=f"{product[1]}, {product[3]}", serial=product[0],
                                       status=product[8], on_release=self.pass_serial)
            self.ids.screen_manager.get_screen('inventory').inventory_list.add_widget(add_products)

    def pass_serial(self, instance):
        serial = instance.serial
        do = ProductDetailScreen()
        do.get_details(serial)
        self.manager.current = "product_details"

    def prompt_get_all_products(self):
        try:
            # global products
            products = database.get_all_products(connection)
            print(products)
            if products:
                self.add_to_screen(products)
        except Exception as e:
            print(e)

    def search_by_serial(self, search_text):
        try:
            product = database.search_by_serial(connection, search_text)
            if product:
                self.add_to_screen(product)
            else:
                self.prompt_get_all_products()
        except Exception as e:
            print(e)

    def qr_search(self, serial):
        self.search_by_serial(serial)
        print(serial)

    # def search(self, search_text, search=False):
    #     for product in products:
    #         for item in product:
    #             if search:
    #                 if search_text in item:
    #                     results = []
    #                     results.append(product)
    #
    #                     for result in results:
    #                         if len(self.ids.inventory_list.children) > 0:
    #                             for index in range(len(self.ids.inventory_list.children)):
    #                                 self.ids.inventory_list.remove_widget(self.ids.inventory_list.children[0])
    #                         add_products = ProductCard1(name_version=f"{result[1]}, {result[3]}", serial=result[0],
    #                                                     status=result[8], on_release=self.pass_serial)
    #                         self.ids.screen_manager.get_screen('inventory').inventory_list.add_widget(add_products)

    # def prompt_get_all_products(self, search_text="", search=False):
    #
    #     def add_product_item(product_item):
    #         row = ProductCard()
    #         self.ids.rv.data.append(
    #             {
    #                 "viewclass": "ProductCard",
    #                 "name_version": f"{product_item[1]}, {product_item[3]}",
    #                 "serial": product_item[0],
    #                 "status": product_item[8],
    #                 "callback": row.pass_serial,
    #             }
    #         )
    #
    #     self.ids.rv.data = []
    #     global products
    #     products = database.get_all_products(connection)
    #
    #     for product in products:
    #         if search:
    #             for item in product:
    #
    #                 if search_text in item:
    #                     add_product_item(product)
    #         else:
    #             add_product_item(product)

    # RecycleView:
    # id: rv
    # key_viewclass: 'viewclass'
    # key_size: 'height'
    #
    # RecycleBoxLayout:
    # padding: dp(10)
    # default_size: None, dp(72)
    # default_size_hint: 1, None
    # size_hint_y: None
    # height: self.minimum_height
    # orientation: 'vertical'

    # def add_to_screen(self, added_product):
    #     #print(added_product)
    #     #print(added_product[1])
    #     add_product = ProductCard1(name_version=f"{added_product[1]}, {added_product[3]}", serial=added_product[0],
    #                      status=added_product[8], on_release=self.pass_serial)
    #     self.ids.screen_manager.get_screen('inventory').inventory_list.add_widget(add_product)

    def get_home_summary(self):
        try:
            self.ids.spray.no = str(database.get_no_of_products_home(connection, 'Spray Drone')[
                                        0])  # [0] returns the first value of the tuple [(12,)]
            self.ids.xmission.no = str(database.get_no_of_products_home(connection, 'Survey Drone')[0])
            self.ids.battery.no = str(database.get_no_of_products_home(connection, 'Battery')[0])
            self.ids.rover.no = str(database.get_no_of_products_home(connection, 'Rover')[0])
            self.ids.charger.no = str(database.get_no_of_products_home(connection, 'Charger')[0])
            self.ids.controller.no = str(database.get_no_of_products_home(connection, 'Controller')[0])
        except Exception as e:
            print(e)

    def get_product_summary(self):
        try:
            # global products
            summaries = database.get_no_of_products(connection)
            if summaries:
                if len(self.ids.summary_grid.children) > 0:
                    for index in range(len(self.ids.summary_grid.children)):
                        self.ids.summary_grid.remove_widget(self.ids.summary_grid.children[0])
                for summary in summaries:
                    add_summary = SummaryIcon1(text=summary[0], no=summary[1], source='P20.ico')
                    self.ids.screen_manager.get_screen('inventory').summary_grid.add_widget(add_summary)
        except Exception as e:
            print(e)

    def change_color(self, instance):
        if instance in self.root.ids.values():  # check that id tree is correct
            current_id = list(self.root.ids.keys())[list(self.root.ids.values()).index(instance)]
            for i in range(5):
                if f"nav_icon{i + 1}" == current_id:
                    self.root.ids[f"nav_icon{i + 1}"].text_color = rgba(71, 92, 119, 255)
                else:
                    self.root.ids[f"nav_icon{i + 1}"].text_color = rgba(222, 222, 222, 255)


class SingleScanScreen(Screen):

    def scan(self):
        self.image = Image()
        self.ids.camera.add_widget(self.image)

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 80)  # width
        self.capture.set(4, 54)
        Clock.schedule_interval(self.load_video, 1.0 / 30.0)

    def load_video(self, *args):
        ret, frame = self.capture.read()
        self.image_frame = frame

        display_scale = 4
        height, width = frame.shape[0:2]
        height_display, width_display = display_scale * height, display_scale * width
        # you can choose different interpolation methods
        frame_display = cv2.resize(frame, (width_display, height_display),
                                   interpolation=cv2.INTER_CUBIC)
        # Frame Initialize
        buffer = cv2.flip(frame_display, 0).tobytes()
        texture = Texture.create(size=(frame_display.shape[1], frame_display.shape[0]), colorfmt='bgr')
        texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
        self.image.texture = texture

        # Data Matrix Decoding Part
        dm_code = decode(self.image_frame)
        # print(dm_code)

        for code in dm_code:
            if code:
                # print(code.data.decode('utf-8'))
                serial = str(code.data.decode('utf-8'))
                self.pass_serial(serial)

    def pass_serial(self, serial):
        do = MainScreen()
        do.qr_search(serial)
        self.release_cam()

    def release_cam(self):
        # self.capture.release()
        self.ids.camera.remove_widget(self.image)
        self.manager.current = "main"


class ScanScreen(Screen):
    add_list = ListProperty
    serial = NumericProperty
    add_list = []
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 150  # Set Duration To 1000 ms == 1 second
    prod = {"112": "P20 Smart Battery", "122": "P20 Smart Battery", "123": "P20 Smart Battery",
            "127": "P30 Smart Battery", "128": "XP Smart Battery", "174": "ARC1)", "175": "ACS2",
            "176": "ACS2 RTk Module", "214": "P20", "216": "P20(2018)", "231": "P20 Charger", "232": "P20 QB Charger",
            "233": "P20 Charger", "235": "XM Charger", "239": "XP Cooling Box", "251": "A2", "252": "A2", "253": "A2",
            "273": "Rover", "275": "Rover", "281": "ALR5/6", "284": "Pesticide Module", "351": "RTK Butt",
            "401": "C2000/XMission", "421": "XM Battery", "431": "C2000 Battery", "552": "P30(2019)",
            "661": "P30 Fast Charger/P20 QB Charger", "751": "XStation", "762": "P30 Seed Module",
            "761": "XP Seed Module", "771": "XP(2020)", }

    def scan(self):
        self.image = Image()
        self.ids.cam_box.add_widget(self.image)

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 160)  # width
        self.capture.set(4, 108)
        Clock.schedule_interval(self.load_video, 1.0 / 30.0)

    def load_video(self, *args):
        global items
        ret, frame = self.capture.read()
        self.image_frame = frame

        # Data Matrix Decoding Part
        dm_code = decode(self.image_frame)
        # print(dm_code)

        for code in dm_code:
            self.serial = str(code.data.decode('utf-8'))
            # self.add_list.append(self.serial)
            # print(serial)

            if self.serial not in self.add_list:
                self.add_list.append(self.serial)
                winsound.Beep(self.frequency, self.duration)
                for key in self.prod.keys():
                    if self.serial[0:3] == key:
                        item_name = self.prod[key]
                        print("This is a", self.prod[key])
                    elif self.serial[0:3] not in self.prod.keys():
                        toast("Not in Database!")
                        item_name = 'Item'
                icon = IconLeftWidget(icon='xp20.ico')
                items = TwoLineIconListItem(text=item_name, secondary_text=self.serial)
                items.add_widget(icon)
                self.ids.add_scan_list.add_widget(items)
            elif self.serial in self.add_list:
                print(self.serial + "is in list")
            print(self.add_list)

        # Scale
        display_scale = 4
        height, width = frame.shape[0:2]
        height_display, width_display = display_scale * height, display_scale * width
        # you can choose different interpolation methods
        frame_display = cv2.resize(frame, (width_display, height_display),
                                   interpolation=cv2.INTER_CUBIC)

        # Frame Initialize
        buffer = cv2.flip(frame_display, 0).tobytes()
        texture = Texture.create(size=(frame_display.shape[1], frame_display.shape[0]), colorfmt='bgr')
        texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
        self.image.texture = texture

    # def read_code(self, *args):

    def release_cam(self):
        # self.capture.release()
        self.ids.cam_box.remove_widget(self.image)
        self.add_list = []

    def scan_code(self):
        pass


class LendScreen(Screen):
    date = StringProperty
    borrowDB = {}
    borrowDB2 = {}

    def date_today(self, *args):
        today = date.today()
        self.ids.date_label.text = str(today)

    def on_save(self, instance, value, date_range):
        '''
        Events called when the "OK" dialog box button is clicked.

        :type instance: <kivymd.uix.picker.MDDatePicker object>;

        :param value: selected date;
        :type value: <class 'datetime.date'>;

        :param date_range: list of 'datetime.date' objects in the selected range;
        :type date_range: <class 'list'>;
        '''
        self.ids.date_label.text = str(value)

        # print(instance, value, date_range)

    def on_cancel(self, instance, value):
        '''Events called when the "CANCEL" dialog box button is clicked.'''

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

    # borrowDB = {}
    new_borrowed = {"Name": [], "Date Borrowed": [], "Phone Number": [], "Email": [], "Items": {}, "Notes": [],
                    "Date Returned": [], "Unique_ID": []};

    def add_new(self, name, date_label, ph_number, email):
        new_case = {"Name": name,
                    "Date Borrowed": date_label,
                    "Phone Number": ph_number,
                    "Email": email,
                    "Items": {},
                    "Notes": '',
                    "Date Returned": '',
                    "Unique ID": ''
                    }
        self.borrowDB[self.ids.name.text] = new_case
        # print(sm.get_screen("main").manager.get_screen("burrow"))

        # print(new_case)
        for k, v in self.borrowDB.items():
            print(k, v)
        # print(self.borrowDB)
        # new_case.clear()

    def clr_txt(self):
        self.ids.name.text = ""
        self.ids.date_label.text = ""
        self.ids.email.text = ""
        self.ids.ph_number.text = ""


class RentDetailsScreen(Screen):
    dialog = None

    def enter_note(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Enter Note:",
                type="custom",
                content_cls=Content(),
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        # theme_text_color="Custom",
                        # text_color=self.theme_cls.primary_color,
                        on_release=self.close_dialog
                    ),
                    MDFlatButton(
                        text="ENTER",
                        # theme_text_color="Custom",
                        # text_color=self.theme_cls.primary_color,
                        on_release=self.change_screen
                    ),
                ],
            )
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def change_screen(self, *args):
        # self.manager.current = "scan"
        self.dialog.dismiss()


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

    def show_entry_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

    def on_save1(self, instance, value, date_range):
        '''
        Events called when the "OK" dialog box button is clicked.

        :type instance: <kivymd.uix.picker.MDDatePicker object>;

        :param value: selected date;
        :type value: <class 'datetime.date'>;

        :param date_range: list of 'datetime.date' objects in the selected range;
        :type date_range: <class 'list'>;
        '''
        self.ids.open_date.text = str(value)

        # print(instance, value, date_range)

    def on_cancel1(self, instance, value):
        '''Events called when the "CANCEL" dialog box button is clicked.'''

    def show_open_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save1, on_cancel=self.on_cancel1)
        date_dialog.open()

    def add_new_product(self, serial, name, year, version, category, entry_date, owner, user, status):
        new_product = database.add_product(connection, serial, name, year, version, category, entry_date, owner, user,
                                           status)
        serial = new_product[0]
        do = ProductDetailScreen()
        do.get_details(serial)
        self.manager.current = "product_details"

    def clr_txt(self):
        self.ids.name.text = ""
        self.ids.serial.text = ""
        self.ids.version.text = ""
        self.ids.category.text = ""
        self.ids.year.text = ""
        self.ids.status.text = ""
        self.ids.entry_date.text = ""
        self.ids.open_date.text = ""
        self.ids.owner.text = ""
        self.ids.user.text = ""


class AddProductScreenOld(Screen):
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
        new_product = database.add_product(connection, serial, name, year, version, category, entry_date, owner, user,
                                           status)
        serial = new_product[0]
        do = ProductDetailScreen()
        do.get_details(serial)
        self.manager.current = "product_details"
        # add = MainScreen()
        # add.prompt_get_all_products

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


class ProductSummaryScreen(Screen):

    def get_product_summary(self):
        try:
            # global products
            summaries = database.get_no_of_products(connection)
            if summaries:
                # print(summaries)
                if len(self.ids.summary_grid.children) > 0:
                    for index in range(len(self.ids.summary_grid.children)):
                        self.ids.summary_grid.remove_widget(self.ids.summary_grid.children[0])
                for summary in summaries:
                    # print(summary)
                    add_summary = SummaryIcon1(text=summary[0], no=str(summary[1]), source='P20.ico')
                    self.ids.summary_grid.add_widget(add_summary)
        except Exception as e:
            print(e)


class ProductDetailScreen(Screen):

    def get_details(self, serial):
        global details
        details = database.get_product_by_serial(connection, serial)

    def show_details(self):
        print(details)
        self.ids.show_serial.text = str(details[0])
        self.ids.show_name_version.text = f"{details[1]}, {details[3]}"
        self.ids.show_release_year.content = details[2]
        self.ids.show_category.content = details[4]
        self.ids.show_entry_date.content = details[5]
        self.ids.show_owner.content = details[6]
        self.ids.show_user.content = details[7]
        self.ids.show_status.text = details[8]

    def clr_txt(self):
        self.ids.show_serial.text = ''
        self.ids.show_name_version.text = ''
        self.ids.show_release_year.content = ''
        self.ids.show_category.content = ''
        self.ids.show_entry_date.content = ''
        self.ids.show_owner.content = ''
        self.ids.show_user.content = ''
        self.ids.show_status.text = ''


class RentalsScreen(Screen):
    date = StringProperty
    borrowDB = {}

    def current_slide(self, index):
        pass

    def date_today(self, *args):
        today = date.today()
        # self.ids.entry_date.text = str(today)
        self.ids.date.text = str(today)

    def on_save(self, instance, value, date_range):
        '''
        Events called when the "OK" dialog box button is clicked.

        :type instance: <kivymd.uix.picker.MDDatePicker object>;

        :param value: selected date;
        :type value: <class 'datetime.date'>;

        :param date_range: list of 'datetime.date' objects in the selected range;
        :type date_range: <class 'list'>;
        '''
        # self.ids.entry_date.text = str(value)
        self.ids.date.text = str(value)

        # print(instance, value, date_range)

    def on_cancel(self, instance, value):
        '''Events called when the "CANCEL" dialog box button is clicked.'''

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

    def add_new(self, name, date_label, ph_number, email):
        new_case = {"Name": name,
                    "Date Borrowed": date_label,
                    "Phone Number": ph_number,
                    "Email": email,
                    "Items": {},
                    "Notes": '',
                    "Date Returned": '',
                    "Unique ID": ''
                    }
        self.borrowDB[self.ids.name.text] = new_case
        # print(sm.get_screen("main").manager.get_screen("burrow"))

        # print(new_case)
        for k, v in self.borrowDB.items():
            print(k, v)
        # print(self.borrowDB)
        # new_case.clear()

    def clr_txt(self):
        self.ids.name.text = ""
        self.ids.date_label.text = ""
        self.ids.email.text = ""
        self.ids.ph_number.text = ""

    add_list = ListProperty
    serial = NumericProperty
    add_list = []
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 150  # Set Duration To 1000 ms == 1 second
    prod = {"112": "P20 Smart Battery", "122": "P20 Smart Battery", "123": "P20 Smart Battery",
            "127": "P30 Smart Battery", "128": "XP Smart Battery", "174": "ARC1)", "175": "ACS2",
            "176": "ACS2 RTk Module", "214": "P20", "216": "P20(2018)", "231": "P20 Charger", "232": "P20 QB Charger",
            "233": "P20 Charger", "235": "XM Charger", "239": "XP Cooling Box", "251": "A2", "252": "A2", "253": "A2",
            "273": "Rover", "275": "Rover", "281": "ALR5/6", "284": "Pesticide Module", "351": "RTK Butt",
            "401": "C2000/XMission", "421": "XM Battery", "431": "C2000 Battery", "552": "P30(2019)",
            "661": "P30 Fast Charger/P20 QB Charger", "751": "XStation", "762": "P30 Seed Module",
            "761": "XP Seed Module", "771": "XP(2020)", }

    def scan(self):
        self.image = Image()
        self.ids.cam_box.add_widget(self.image)

        self.capture = cv2.VideoCapture(1)
        self.capture.set(3, 160)  # width
        self.capture.set(4, 120)
        Clock.schedule_interval(self.load_video, 1.0 / 30.0)

    def load_video(self, *args):
        global items
        ret, frame = self.capture.read()
        self.image_frame = frame

        # Data Matrix Decoding Part
        dm_code = decode(self.image_frame)
        # print(dm_code)

        for code in dm_code:
            self.serial = str(code.data.decode('utf-8'))
            # self.add_list.append(self.serial)
            # print(serial)

            if self.serial not in self.add_list:
                self.add_list.append(self.serial)
                winsound.Beep(self.frequency, self.duration)
                for key in self.prod.keys():
                    if self.serial[0:3] == key:
                        item_name = self.prod[key]
                        print("This is a", self.prod[key])
                    elif self.serial[0:3] not in self.prod.keys():
                        toast("Not in Database!")
                        item_name = 'Item'
                # icon = IconLeftWidget(icon='xp20.ico')
                # items = TwoLineIconListItem(text=item_name, secondary_text=self.serial)
                # items.add_widget(icon)
                # self.ids.add_scan_list.add_widget(items)

                items = ScanListItem(text=self.serial, source='xpgen.ico', icon='close-circle-outline')
                self.ids.add_scan_list.add_widget(items)
            elif self.serial in self.add_list:
                print(self.serial + "is in list")
            print(self.add_list)

        # Scale
        display_scale = 4
        height, width = frame.shape[0:2]
        height_display, width_display = display_scale * height, display_scale * width
        # you can choose different interpolation methods
        frame_display = cv2.resize(frame, (width_display, height_display),
                                   interpolation=cv2.INTER_CUBIC)

        # Frame Initialize
        buffer = cv2.flip(frame_display, 0).tobytes()
        texture = Texture.create(size=(frame_display.shape[1], frame_display.shape[0]), colorfmt='bgr')
        texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
        self.image.texture = texture

    # def read_code(self, *args):
    def add_manually(self, serial):
        print(serial)
        if serial not in self.add_list:
            self.add_list.append(serial)
            # winsound.Beep(self.frequency, self.duration)
            for key in self.prod.keys():
                if serial[0:3] == key:
                    item_name = self.prod[key]
                    print("This is a", self.prod[key])
                elif serial[0:3] not in self.prod.keys():
                    toast("Not in Database!")
                    item_name = 'Item'

            items = ScanListItem(text=serial, source='xmission.ico', icon='close-circle-outline')
            self.ids.add_scan_list.add_widget(items)
        elif serial in self.add_list:
            print(serial + "is in list")
        print(self.add_list)

    def release_cam(self):
        # self.capture.release()
        self.ids.cam_box.remove_widget(self.image)
        self.add_list = []

    def scan_code(self):
        pass


class NewRentalScreen(Screen):
    def drop_down(self, instance):
        customers = database.get_all_customers(connection)
        staff_name = customers[1]
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "height": 56,
                "text": customer[1],
                "on_release": lambda x=customer[1]: self.set_item(x),
            } for customer in customers]
        self.menu = MDDropdownMenu(
            items=menu_items,
            width_mult=5,
            hor_growth="left",
        )
        self.menu.caller = instance
        self.menu.open()

    def field_drop_down(self, instance, staff_name):
        # customers = database.search_customer_by_name(connection, staff_name)
        customers = database.get_all_customers(connection)
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "height": 56,
                "text": customer[1],
                "on_release": lambda x=customer[1]: self.set_item(x),
            } for customer in customers]
        self.menu = MDDropdownMenu(
            items=menu_items,
            position="bottom",
            width_mult=5,
        )
        self.menu.caller = instance
        self.menu.open()

    # def search_customer(self, instance, staff_name, search=False):
    #     customers = database.get_all_customers(connection)
    #     customer_list = []
    #     if self.ids.customer.text != "":
    #         for customer in customers:
    #             customer_list.append(customer[1])
    #         # print(customer_list)
    #
    #         menu_items = [
    #             {
    #                 "viewclass": "OneLineListItem",
    #                 "height": 56,
    #                 "text": item,
    #                 "on_release": lambda x=item: self.set_item(x),
    #             } for item in customer_list if search if staff_name in item]
    #         self.menu = MDDropdownMenu(
    #             items=menu_items,
    #             position="bottom",
    #             width_mult=4,
    #         )
    #         self.menu.caller = instance
    #         self.menu.open()

    # data = []
    # for item in customer_list:
    #     if search:
    #         if staff_name in item:
    #             if item not in data:
    #                 data.append(item)
    #                 print(data)
    #

    def search_customer(self, instance, staff_name="", search=False):
        customers = database.get_all_customers(connection)
        customer_list = []
        if self.ids.customer.text != "":
            for customer in customers:
                customer_list.append(customer[1])
            # print(customer_list)

        def add_menu_item(item):
            self.menu_items.append(
                {
                    "viewclass": "OneLineListItem",
                    "height": 42,
                    "text": item,
                    "on_release": lambda x=item: self.set_item(x),
                }
            )

        self.menu_items = []
        for item in customer_list:
            if search:
                if staff_name in item:
                    add_menu_item(item)
            else:
                add_menu_item(item)

        self.menu = MDDropdownMenu(
            items=self.menu_items,
            position="bottom",
            width_mult=4,
        )
        self.menu.caller = instance
        self.menu.open()

    def set_item(self, text__item):
        self.ids.customer.text = text__item
        self.menu.dismiss()

    dialog = None

    def date_today(self, *args):
        today = date.today()
        self.ids.rent_date.text = str(today)

    def on_save(self, instance, value, date_range):
        '''
        Events called when the "OK" dialog box button is clicked.

        :type instance: <kivymd.uix.picker.MDDatePicker object>;

        :param value: selected date;
        :type value: <class 'datetime.date'>;

        :param date_range: list of 'datetime.date' objects in the selected range;
        :type date_range: <class 'list'>;
        '''
        # self.ids.entry_date.text = str(value)
        self.ids.rent_date.text = str(value)

        # print(instance, value, date_range)

    def on_cancel(self, instance, value):
        '''Events called when the "CANCEL" dialog box button is clicked.'''

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

    def pass_details(self, customer, date):
        if self.ids.customer.text != "":
            staff_name = database.get_customer_by_name(connection, customer)
            if staff_name is not None:
                if customer in staff_name:
                    #print(staff_name[1], date)
                    do = ScanScreenNew()
                    do.set_details(staff_name[1], date)
                    self.manager.current = "multi_scan"
            else:
                toast(f"{customer}, not in Database.")
        else:
            toast("Please select Customer")
        # self.ids.customer.text = staff_name[1]
        # self.ids.customer.text = 'Dogara'
        # print(self.ids.customer.text)

        # serial = instance.serial
        # do = ProductDetailScreen()
        # do.get_details(serial)
        # self.manager.current = "product_details"

    def clr_txt(self):
        self.ids.customer.text = ""

    def add_customer1(self):
        self.customer_bs = MDCustomBottomSheet(screen=Factory.AddCustomerBS())
        self.customer_bs.open()

    def show_add_customer_dialog(self, obj=None):
        def add_customer(obj):
            org_name = self.dialog.content_cls.ids.org_name.text
            name = self.dialog.content_cls.ids.staff_name.text
            phone_number = self.dialog.content_cls.ids.phone_no.text
            email = self.dialog.content_cls.ids.email.text

            try:
                if name != '':
                    new_customer = database.add_customer(connection, org_name, name, phone_number, email)
                    print(new_customer)
                    close_dialog()
                    clr_txt()
                    self.ids.customer.text = new_customer[1]
                else:
                    toast('Please Enter Name!')
            except Exception as e:
                print(e)

        def close_dialog(obj=None):
            self.dialog.dismiss()

        def clr_txt(obj=None):
            self.dialog.content_cls.ids.org_name.text = ""
            self.dialog.content_cls.ids.staff_name.text = ""
            self.dialog.content_cls.ids.phone_no.text = ""
            self.dialog.content_cls.ids.email.text = ""

        if not self.dialog:
            self.dialog = MDDialog(
                type="custom",
                size_hint=(.9, 1),
                content_cls=AddCustomerDialog(),
                buttons=[
                    MDFlatButton(
                        text="취소",
                        font_name="BNanum",
                        theme_text_color="Custom",
                        text_color=rgba(0, 0, 0, 178.5),
                        on_release=close_dialog
                    ),
                    MDFlatButton(
                        text="등록",
                        font_name="BNanum",
                        theme_text_color="Custom",
                        text_color=rgba(0, 0, 0, 178.5),
                        on_release=add_customer
                    ),
                ],
            )
        self.dialog.open()

        # def use_input(obj):
        #     org_name = self.dialog.content_cls.ids.org_name.text
        #     name = self.dialog.content_cls.ids.staff_name.text
        #     phone_number = self.dialog.content_cls.ids.phone_no.text
        #     email = self.dialog.content_cls.ids.email.text
        #
        #     print(org_name, name, phone_number, email)

    # def add_customer(self, obj, org_name, name, phone_number, email):
    #     new_customer = database.add_customer(connection, org_name, name, phone_number, email)
    #     print('do something')
    #     print(new_customer)
    #     # check if name inputted is in database
    #     # self.ids.customer.text = self.dialog.content_cls.ids.staff_name.text
    #
    # def add_new_customer(self):
    #     self.manager.current = "add_customer"


class CustomerCard(ButtonBehavior, RectangularRippleBehavior, MDBoxLayout):
    name_org = StringProperty('임현준, 탑필드')
    name = StringProperty('임현준')
    phone_number = StringProperty('01012345678')
    email = StringProperty('lim@toppfield.com')


class CustomerScreen(Screen):
    def add_customers_to_screen(self, customers):
        if len(self.ids.customer_list.children) > 0:
            for index in range(len(self.ids.customer_list.children)):
                self.ids.customer_list.remove_widget(self.ids.customer_list.children[0])
        for customer in customers:
            add_customer = CustomerCard(name=customer[1], name_org=f"{customer[1]}, {customer[0]}",
                                        phone_number=customer[2],
                                        email=customer[3], on_release=self.pass_customer_name)
            self.ids.customer_list.add_widget(add_customer)

    def pass_customer_name(self, instance):
        name = instance.name
        print(name)
        # do = USIMDetailScreen()
        # do.get_details(name)
        # self.manager.current = "customer_details"

    def prompt_get_all_customers(self):
        try:
            customers = database.get_all_customers(connection)
            print(customers)
            if customers:
                self.add_customers_to_screen(customers)
        except Exception as e:
            print(e)

    def search_customer_by_name(self, search_text):
        try:
            customers = database.search_customer_by_name(connection, search_text)
            if customers:
                print(customers)
                self.add_customers_to_screen(customers)
            else:
                self.prompt_get_all_customers()
        except Exception as e:
            print(e)


class AddCustomerDialog(BoxLayout):
    org_name = StringProperty('탑필드')
    staff_name = StringProperty('홍길동')
    phone_no = StringProperty('01012345678')
    email = StringProperty('staff@company.com')
    # obj = ObjectProperty(None)
    # org_name = StringProperty("")
    # staff_name = StringProperty("")
    # phone_no = StringProperty("")
    # email = StringProperty("")
    #
    # def __init__(self, obj, **kwargs):
    #     super(BoxLayout, self).__init__(**kwargs)
    #     self.obj = obj
    #     self.org_name = obj.org_name.text
    #     self.staff_name = obj.staff_name.text
    #     self.phone_no = obj.phone_no.text
    #     self.email = obj.email.text


class AddCustomerScreen(Screen):
    def add_new_customer(self, org_name, name, phone_number, email):
        global new_customer
        try:
            new_customer = (org_name, name, phone_number, email)
            database.add_customer(connection, org_name, name, phone_number, email)
            # print(new_customer)
        except Exception as e:
            print(e)

        # customer = 'Dogara'
        # customer = new_customer[1]
        # do = NewRentalScreen()
        # do.get_details(customer)

        self.manager.current = 'customer'
        customer = new_customer[1]
        return customer

    def clr_txt(self):
        self.ids.org_name.text = ""
        self.ids.staff_name.text = ""
        self.ids.phone_no.text = ""
        self.ids.email.text = ""


class ScanScreenNew(Screen):
    add_list = ListProperty
    serial = NumericProperty
    add_list = []

    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 150  # Set Duration To 1000 ms == 1 second
    prod = {"112": "P20 Smart Battery", "122": "P20 Smart Battery", "123": "P20 Smart Battery",
            "127": "P30 Smart Battery", "128": "XP Smart Battery", "174": "ARC1)", "175": "ACS2",
            "176": "ACS2 RTk Module", "214": "P20", "216": "P20(2018)", "231": "P20 Charger", "232": "P20 QB Charger",
            "233": "P20 Charger", "235": "XM Charger", "239": "XP Cooling Box", "251": "A2", "252": "A2", "253": "A2",
            "273": "Rover", "275": "Rover", "281": "ALR5/6", "284": "Pesticide Module", "351": "RTK Butt",
            "401": "C2000/XMission", "421": "XM Battery", "431": "C2000 Battery", "552": "P30(2019)",
            "661": "P30 Fast Charger/P20 QB Charger", "751": "XStation", "762": "P30 Seed Module",
            "761": "XP Seed Module", "771": "XP(2020)", }

    def scan(self):
        self.image = Image()
        self.ids.cam_box.add_widget(self.image)

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 160)  # width
        self.capture.set(4, 120)
        Clock.schedule_interval(self.load_video, 1.0 / 30.0)

    def load_video(self, *args):
        global items
        ret, frame = self.capture.read()
        self.image_frame = frame

        # Data Matrix Decoding Part
        dm_code = decode(self.image_frame)
        # print(dm_code)

        for code in dm_code:
            self.serial = str(code.data.decode('utf-8'))
            # self.add_list.append(self.serial)
            # print(serial)

            if self.serial not in self.add_list:
                self.add_list.append(self.serial)
                winsound.Beep(self.frequency, self.duration)
                for key in self.prod.keys():
                    if self.serial[0:3] == key:
                        print("This is a", self.prod[key])
                    elif self.serial[0:3] not in self.prod.keys():
                        toast("Not in Database!")

                items = ScanListItem(text=self.serial, source='xpgen.ico', icon='close-circle-outline')
                self.ids.add_scan_list.add_widget(items)
            elif self.serial in self.add_list:
                print(self.serial + "is in list")
            print(self.add_list)

        # Scale
        display_scale = 4
        height, width = frame.shape[0:2]
        height_display, width_display = display_scale * height, display_scale * width
        # you can choose different interpolation methods
        frame_display = cv2.resize(frame, (width_display, height_display),
                                   interpolation=cv2.INTER_CUBIC)

        # Frame Initialize
        buffer = cv2.flip(frame_display, 0).tobytes()
        texture = Texture.create(size=(frame_display.shape[1], frame_display.shape[0]), colorfmt='bgr')
        texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
        self.image.texture = texture

    def set_title(self, name, date):
        self.ids.title.text = f"{name}, {date}"


    def set_details(self, name, date):
        self.ids.title.text = f"{name}, {date}"

        self.ids.title.text = name
        self.add_list.append(name)
        self.add_list.append(date)
        print(self.add_list)

    def search_product(self, instance, prod_name="", search=False):
        products = database.get_all_products(connection)
        product_list = []
        if self.ids.manual_serial.text != "":
            for product in products:
                product_list.append(product[0])
            #print(product_list)

        def add_menu_item(item):
            self.menu_items.append(
                {
                    "viewclass": "OneLineListItem",
                    "height": 56,
                    "text": item,
                    "on_release": lambda x=item: self.set_item(x),
                }
            )

        self.menu_items = []
        for item in product_list:
            if search:
                if prod_name in item:
                    add_menu_item(item)
            else:
                add_menu_item(item)

        self.menu = MDDropdownMenu(
            items=self.menu_items,
            position="bottom",
            width_mult=4,
            border_margin=24
        )
        self.menu.caller = instance
        self.menu.open()

    def set_item(self, text__item):
        self.ids.manual_serial.text = text__item
        self.menu.dismiss()

    # def read_code(self, *args):
    def add_manually(self, serial):
        print(serial)
        if serial not in self.add_list:
            self.add_list.append(serial)
            self.ids.title.text = serial
            # winsound.Beep(self.frequency, self.duration)
            for key in self.prod.keys():
                if serial[0:3] == key:
                    print("This is a", self.prod[key])
                elif serial[0:3] not in self.prod.keys():
                    toast("Not in Database!")

            items = ScanListItem(text=serial, source='xmission.ico', icon='close-circle-outline')
            self.ids.add_scan_list.add_widget(items)
        elif serial in self.add_list:
            print(serial + "is in list")
        self.ids.manual_serial.text = ""
        print(self.add_list)

    def remove_item(self, serial):
        self.add_list.remove(serial)
        print(self.add_list)

    def release_cam(self):
        self.capture.release()
        self.ids.cam_box.remove_widget(self.image)
        self.add_list = []


class ScanListItem(MDBoxLayout):
    source = StringProperty('xmission.ico')
    icon = StringProperty('close-circle-outline')
    text = StringProperty('1234567890')

    def delete_item(self, list_item):
        scan_list = ScanScreenNew()
        scan_list.remove_item(list_item.text)
        self.parent.remove_widget(list_item)


class ProductChip(FakeRectangularElevationBehavior, MDBoxLayout):
    icon = StringProperty('close-circle-outline')
    text = StringProperty('1234567890')


class MyTextField(FakeRectangularElevationBehavior, MDBoxLayout):
    title = StringProperty('Name')
    hint_text = StringProperty('Enter Name')


class DGALTextField(FakeRectangularElevationBehavior, MDBoxLayout):
    title = StringProperty('Name')
    hint_text = StringProperty('Enter Name')


class DGTextField(FakeRectangularElevationBehavior, FocusBehavior, MDBoxLayout):
    text = StringProperty()
    title = StringProperty('Name')
    hint_text = StringProperty('Enter Name')


class DGIconTextField(FakeRectangularElevationBehavior, MDBoxLayout):
    title = StringProperty('Name')
    icon = StringProperty('close-circle')
    hint_text = StringProperty('Enter Name')
    pos_hint = ObjectProperty({"center_x": .5, "center_y": .5})
    on_release = StringProperty("root.manager.current = 'main'")
    # size_hint = ReferenceListProperty()


class DGFAB(ButtonBehavior, FakeCircularElevationBehavior, CircularRippleBehavior, MDBoxLayout):
    icon = StringProperty('plus')


class Content(BoxLayout):
    pass


class USIMScreen(Screen):
    def add_usims_to_screen(self, usims):
        if len(self.ids.usim_list.children) > 0:
            for index in range(len(self.ids.usim_list.children)):
                self.ids.usim_list.remove_widget(self.ids.usim_list.children[0])
        for usim in usims:
            add_usim = UsimCard(device=usim[2], serial=usim[1], name_number=f"{usim[0]}, {usim[3]}",
                                status=usim[7], on_release=self.pass_usim_serial)
            self.ids.usim_list.add_widget(add_usim)

    def pass_usim_serial(self, instance):
        serial = instance.serial
        do = USIMDetailScreen()
        do.get_details(serial)
        self.manager.current = "usim_details"

    def prompt_get_all_usim(self):
        try:
            usims = database.get_all_usims(connection)
            # print(usims)
            if usims:
                self.add_usims_to_screen(usims)
        except Exception as e:
            print(e)

    def search_usim_by_serial(self, search_text):
        try:
            usims = database.search_usim_by_serial(connection, search_text)
            if usims:
                print(usims)
                self.add_usims_to_screen(usims)
            else:
                self.prompt_get_all_usim()
        except Exception as e:
            print(e)


class AddUSIMScreen(Screen):

    def current_slide(self, index):
        pass

    def date_today(self, *args):
        today = date.today()
        # self.ids.entry_date.text = str(today)
        self.ids.start_date.text = str(today)
        self.ids.end_date.text = str(today)

    def on_save(self, instance, value, date_range):
        '''
        Events called when the "OK" dialog box button is clicked.

        :type instance: <kivymd.uix.picker.MDDatePicker object>;

        :param value: selected date;
        :type value: <class 'datetime.date'>;

        :param date_range: list of 'datetime.date' objects in the selected range;
        :type date_range: <class 'list'>;
        '''
        # self.ids.entry_date.text = str(value)
        self.ids.start_date.text = str(value)

        # print(instance, value, date_range)

    def on_cancel(self, instance, value):
        '''Events called when the "CANCEL" dialog box button is clicked.'''

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

    def add_new_usim(self, owner, serial, device, phone_number, period, start_date, end_date, status):
        try:
            new_usim = database.add_usim(connection, owner, serial, device, phone_number, period, start_date, end_date,
                                         status)
            # print(new_usim)
            serial = new_usim[1]
            do = USIMDetailScreen()
            do.get_details(serial)
            self.manager.current = "usim_details"
        except Exception as e:
            print(e)

    def clr_txt(self):
        self.ids.usim_owner.text = ""
        self.ids.usim_serial.text = ""
        self.ids.device.text = ""
        self.ids.usim_no.text = ""
        self.ids.usim_period.text = ""
        self.ids.start_date.text = ""
        self.ids.end_date.text = ""
        # self.ids.status.text = ""


class USIMDetailScreen(Screen):
    def get_details(self, serial):
        global details
        details = database.get_usim_by_serial(connection, serial)

    def show_details(self):
        print(details)
        self.ids.show_device.text = details[2]
        self.ids.show_serial.text = str(details[1])
        self.ids.show_status.text = details[7]
        self.ids.show_owner.content = details[0]
        self.ids.show_phone_no.content = details[3]
        self.ids.show_period.content = details[4]
        self.ids.show_contract_start.content = details[5]
        self.ids.show_contract_end.content = details[6]

    def clr_txt(self):
        self.ids.show_device.text = ''
        self.ids.show_serial.text = ''
        self.ids.show_status.text = ''
        self.ids.show_owner.content = ''
        self.ids.show_phone_no.content = ''
        self.ids.show_period.content = ''
        self.ids.show_contract_start.content = ''
        self.ids.show_contract_end.content = ''


class UsimCard(ButtonBehavior, RectangularRippleBehavior, MDBoxLayout):
    source = StringProperty('sim_card.png')
    serial = StringProperty('XXXX-XXXX-XXXX-XXXX-XXXF')
    name_number = StringProperty('Dogara, 01012345678')
    device = StringProperty('XP20, CN')
    status = StringProperty('Valid')


class Status(MDBoxLayout):
    status = StringProperty('Valid')
    bg_color = ListProperty([215, 223, 204, 255])  # 68,107,17,255
    text_color = ListProperty([68, 107, 17, 255])  # 215,223,204,255

    def set_status(self, status):
        if status == 'New':
            self.bg_color = [231, 238, 254, 255]  # lavender
            self.text_color = [52, 88, 128, 255]  # darkslateblue
        elif status == 'inUse':
            self.bg_color = [215, 223, 204, 255]  # green
            self.text_color = [68, 107, 17, 255]
        elif status == 'Burrowed':
            self.bg_color = [243, 245, 249, 255]  # grey
            self.text_color = [174, 175, 179, 255]
        elif status == 'Sold':
            self.bg_color = [250, 246, 202, 255]  # yellow
            self.text_color = [130, 109, 60, 255]
        elif status == 'Damaged':
            self.bg_color = [255, 231, 227, 255]  # red
            self.text_color = [118, 44, 42, 255]


class Camera(MDApp):
    title = "Topp Inventory"

    global connection
    connection = database.connect()
    database.create_tables(connection)

    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name="main"))

        sm.add_widget(ScanScreen(name="scan"))
        sm.add_widget(ScanScreenNew(name="multi_scan"))
        sm.add_widget(SingleScanScreen(name="single_scan"))

        sm.add_widget(AddProductScreen(name="add_product"))
        sm.add_widget(AddProductScreenOld(name="add_product_old"))
        sm.add_widget(ProductDetailScreen(name="product_details"))
        sm.add_widget(ProductSummaryScreen(name="product_summary"))

        sm.add_widget(LendScreen(name="lend"))
        sm.add_widget(RentalsScreen(name="rental"))
        sm.add_widget(NewRentalScreen(name="new_rental"))
        sm.add_widget(RentDetailsScreen(name="rent_details"))

        sm.add_widget(CustomerScreen(name="customer"))
        sm.add_widget(AddCustomerScreen(name="add_customer"))

        sm.add_widget(USIMScreen(name="usim"))
        sm.add_widget(AddUSIMScreen(name="add_usim"))
        sm.add_widget(USIMDetailScreen(name="usim_details"))

    def change_color(self, instance):
        if instance in self.root.ids.values():  # check that id tree is correct
            print(instance)
            current_id = list(self.root.ids.keys())[list(self.root.ids.values()).index(instance)]
            for i in range(5):
                if f"nav_icon{i + 1}" == current_id:
                    self.root.ids[f"nav_icon{i + 1}"].text_color = rgba(71, 92, 119, 255)
                else:
                    self.root.ids[f"nav_icon{i + 1}"].text_color = rgba(222, 222, 222, 255)


LabelBase.register(name='BPoppins', fn_regular="C:\\Users\dogig\\PycharmProjects\\Camera\\fonts\\Poppins\\Poppins-Bold.ttf")
LabelBase.register(name='MPoppins', fn_regular="C:\\Users\dogig\\PycharmProjects\\Camera\\fonts\\Poppins\\Poppins-Medium.ttf")
LabelBase.register(name='LPoppins', fn_regular="C:\\Users\dogig\\PycharmProjects\\Camera\\fonts\\Poppins\\Poppins-Light.ttf")
LabelBase.register(name='TPoppins', fn_regular="C:\\Users\dogig\\PycharmProjects\\Camera\\fonts\\Poppins\\Poppins-Thin.ttf")

LabelBase.register(name='TNoto', fn_regular="C:\\Users\dogig\\PycharmProjects\\Camera\\fonts\\NotoSansKR-Thin.otf")
LabelBase.register(name='Noto', fn_regular="C:\\Users\dogig\\PycharmProjects\\Camera\\fonts\\NotoSansKR-Black.otf")
LabelBase.register(name='BNoto', fn_regular="C:\\Users\dogig\\PycharmProjects\\Camera\\fonts\\NotoSansKR-Bold.otf")
LabelBase.register(name='LNoto', fn_regular="C:\\Users\dogig\\PycharmProjects\\Camera\\fonts\\NotoSansKR-Light.otf")
LabelBase.register(name='MNoto', fn_regular="C:\\Users\dogig\\PycharmProjects\\Camera\\fonts\\NotoSansKR-Medium.otf")
LabelBase.register(name='RNoto', fn_regular="C:\\Users\dogig\\PycharmProjects\\Camera\\fonts\\NotoSansKR-Regular.otf")

LabelBase.register(name='BNanum', fn_regular="C:\\Users\dogig\\PycharmProjects\\Camera\\fonts\\NanumGothic-Bold.ttf")
LabelBase.register(name='ENanum',
                   fn_regular="C:\\Users\dogig\\PycharmProjects\\Camera\\fonts\\NanumGothic-ExtraBold.ttf")
LabelBase.register(name='RNanum', fn_regular="C:\\Users\dogig\\PycharmProjects\\Camera\\fonts\\NanumGothic-Regular.ttf")

Camera().run()
