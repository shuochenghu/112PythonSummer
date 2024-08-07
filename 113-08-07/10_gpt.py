import requests
import tkinter as tk
from tkinter import ttk, messagebox

# 取得天氣資料
def fetch_weather_data():
    URL = 'https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-D0047-063'
    P = {}
    P['Authorization'] = 'CWB-80B8FFEA-FFCC-4931-B91C-C38CD577ACD7'
    r = requests.get(URL, params=P)
    t = r.json()
    return t

# 初始化 GUI 界面
def create_gui(weather_data):
    root = tk.Tk()
    root.title("台北市天氣查詢")
    root.geometry("400x300")

    # 獲取所有地區名稱
    locations = [loc['locationName'] for loc in weather_data['records']['locations'][0]['location']]
    
    # 獲取氣象元素名稱
    elements = [element['description'] for element in weather_data['records']['locations'][0]['location'][0]['weatherElement']]
    
    # 獲取時間段
    times = [time['startTime'] for time in weather_data['records']['locations'][0]['location'][0]['weatherElement'][0]['time']]

    # 地區選單
    tk.Label(root, text="選擇地區:").pack(pady=5)
    location_var = tk.StringVar()
    location_menu = ttk.Combobox(root, textvariable=location_var, values=locations)
    location_menu.pack()

    # 氣象元素選單
    tk.Label(root, text="選擇氣象元素:").pack(pady=5)
    element_var = tk.StringVar()
    element_menu = ttk.Combobox(root, textvariable=element_var, values=elements)
    element_menu.pack()

    # 時間段選單
    tk.Label(root, text="選擇時間段:").pack(pady=5)
    time_var = tk.StringVar()
    time_menu = ttk.Combobox(root, textvariable=time_var, values=times)
    time_menu.pack()

    # 查詢按鈕
    def show_weather():
        location = location_var.get()
        element = element_var.get()
        time = time_var.get()

        # 找到選中的地區資料
        for loc in weather_data['records']['locations'][0]['location']:
            if loc['locationName'] == location:
                # 找到選中的氣象元素資料
                for elem in loc['weatherElement']:
                    if elem['description'] == element:
                        # 找到選中的時間段資料
                        for t in elem['time']:
                            if t['startTime'] == time:
                                value = t['elementValue'][0]['value']
                                messagebox.showinfo("查詢結果", f"{location} - {element} ({time}): {value}")
                                return
        messagebox.showerror("查詢失敗", "未找到相應資料")

    tk.Button(root, text="查詢", command=show_weather).pack(pady=20)

    root.mainloop()

# 主程式
if __name__ == "__main__":
    weather_data = fetch_weather_data()
    create_gui(weather_data)
