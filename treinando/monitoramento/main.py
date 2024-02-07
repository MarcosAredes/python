import psutil
import customtkinter as ct

# Initial tkinter settings
ct.set_appearance_mode("Dark")
ct.set_default_color_theme("dark-blue")

app = ct.CTk()
app.geometry("640x480")
app.title("System Monitoring")

# System title


label_titulo = ct.CTkLabel(
    app, text="Monitoramento Do Sistema", font=("arial", 30), text_color="#14747F"
)
label_titulo.place(x=100, y=25)


# Functions


# CPU
def view_cpu_info():
    cpu_usage = psutil.cpu_percent(interval=1)
    cpu_freq = psutil.cpu_freq()
    frequency_cpu = cpu_freq.current

    cpu_label.configure(text="{}% / {} MHz".format(cpu_usage, frequency_cpu))
    cpu_label.after(200, view_cpu_info)


# Converting bytes to gigabytes
def converting_bytes_to_gb(byte):
    one_gb = 1073741824
    gb = byte / one_gb
    gb = "{0:.1f}".format(gb)
    return gb


# RAM memory


def view_ram_info():
    ram_usage = psutil.virtual_memory()
    ram_usage = dict(ram_usage._asdict())
    for key in ram_usage:
        if key != "percent":
            ram_usage[key] = converting_bytes_to_gb(ram_usage[key])

    ram_label.configure(
        text="{} GB / {} GB ({}%)".format(
            ram_usage["used"], ram_usage["total"], ram_usage["percent"]
        )
    )
    ram_label.after(200, view_ram_info)


# HardDisk


def view_hd_info():
    partitions = psutil.disk_partitions()

    def view_hd_info():
        partitions = psutil.disk_partitions()

    for partitions in partitions:
        disk_usage = psutil.disk_usage(partitions.device)
        disk_usage = dict(disk_usage._asdict())
        for key in disk_usage:
            if key != "percent":
                disk_usage[key] = converting_bytes_to_gb(disk_usage[key])
        disk_text.insert(
            index="1.0",
            text="{} {} GB/ {} GB ({} GB livre) - Total: {} GB, Livre: {} GB\n ".format(
                partitions.device.replace("\\", ">"),
                disk_usage["used"],
                disk_usage["total"],
                disk_usage["free"],
                disk_usage["total"],
                disk_usage["free"],
            ),
        )


# CPU Usage Title


cpu_title_label = ct.CTkLabel(
    app, text="CPU Usage", font=("arial", 30), text_color="#FA5125"
)
cpu_title_label.place(x=35, y=125)


# CPU usage (percentage)


cpu_label = ct.CTkLabel(app, font=("arial", 30))
cpu_label.place(x=325, y=125)

# RAM Usage Title


ram_title_label = ct.CTkLabel(
    app, text="RAM Usage", font=("arial", 30), text_color="#34A96C"
)
ram_title_label.place(x=35, y=200)


# RAM usage (percentage)


ram_label = ct.CTkLabel(app, font=("arial", 30))
ram_label.place(x=325, y=200)


# Disk usage title


disk_title_label = ct.CTkLabel(
    app, text="Disk Usage", font=("arial", 30), text_color="#797E1E"
)
disk_title_label.place(x=200, y=275)


# Disk Information


disk_text = ct.CTkTextbox(
    app,
    bg_color="#071C1E",
    text_color="yellow",
    width=605,
    height=150,
    padx=10,
    font=("arial", 15),
)
disk_text.place(x=15, y=325)


if __name__ == "__main__":
    view_cpu_info()
    view_ram_info()
    view_hd_info()
    app.mainloop()

