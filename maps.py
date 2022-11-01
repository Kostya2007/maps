from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkintermapview
def center(win):
    win.update_idletasks()

    width = win.winfo_width()

    height = win.winfo_height()

    x = (win.winfo_screenwidth() // 2) - (width // 2)

    y = (win.winfo_screenheight() // 2) - (height // 2)

    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

window = Tk()
window.title("room")
window.geometry("1000x800")
window.resizable(False, False)
window["bg"] = "white"
center(window)
map_widget=tkintermapview.TkinterMapView(window,width=1000,height=800)
map_widget.place(x=0,y=0)
map_widget.set_zoom(10)
map_widget.set_position(50,70)
marker0=map_widget.set_address("Бибирево",marker=True)

markers=[]
def addmark(cords):
    marker3=map_widget.set_marker(cords[0],cords[1])
    markers.append(marker3)
    print(cords)

def delet():
    for temp in markers:
        temp.delete()
def mark(cords):
    print(cords)
    # city=tkintermapview.convert_coordinates_to_city(cords[0],cords[1])
    # print(city)
    # info=tkintermapview.convert_coordinates_to_country(cords[0],cords[1])
    # print(info)
    adr=tkintermapview.convert_coordinates_to_address(cords[0],cords[1])
    print(adr.street,adr.housenumber,adr.state)
map_widget.add_left_click_map_command(mark)
def inf():
    pass

a = Button(window, text="Del", bg="black", fg="white", padx="20", pady="8", highlightcolor="black", bd=4, command=delet)
a.place(x=900,y=10)
map_widget.add_right_click_menu_command(label="add mark",command=addmark,pass_coords=True)

#map_widget.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png")  # OpenStreetMap (default)
#map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)  # google normal
#map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)  # google satellite

#map_widget.set_tile_server("http://c.tile.stamen.com/watercolor/{z}/{x}/{y}.png")  # painting style

#map_widget.set_tile_server("http://a.tile.stamen.com/toner/{z}/{x}/{y}.png")  # black and white


#example overlay tile server

#map_widget.set_overlay_tile_server("http://a.tiles.openrailwaymap.org/standard/{z}/{x}/{y}.png")  # railway infrastructure





window.mainloop()
