import requests
import tkinter as tk
from tkinter import ttk, messagebox

def fetch_weather_data():
    # API URL 和授權參數
    URL = 'https://opendata.cwa.gov.tw/api/v1/rest/datastore/O-A0003-001'
    params = {'Authorization': 'CWB-80B8FFEA-FFCC-4931-B91C-C38CD577ACD7'}
    try:
        response = requests.get(URL, params=params)
        response.raise_for_status()  # 確認請求成功
        return response.json()
    except requests.RequestException as e:
        messagebox.showerror("錯誤", f"無法獲取天氣資料: {e}")
        return None

def update_station_info(*args):
    station_name = station_var.get()
    if not station_name:
        return

    # 查找選中的站點資料
    for station in weather_data['records']['Station']:
        if station['StationName'] == station_name:
            # 提取並顯示觀測站資訊
            obs_time = station['ObsTime']['DateTime']
            weather_info = station['WeatherElement']
            air_temp = weather_info.get('AirTemperature', 'N/A')
            rel_humidity = weather_info.get('RelativeHumidity', 'N/A')
            weather = weather_info.get('Weather', 'N/A')

            # 更新顯示資訊
            station_info.set(
                f"觀測地點: {station_name}\n"
                f"觀測時間: {obs_time}\n"
                f"觀測溫度: {air_temp} °C\n"
                f"觀測濕度: {rel_humidity} %\n"
                f"觀測天氣: {weather}"
            )
            return

    station_info.set("無法找到該站點的資料。")

# 初始化主視窗
root = tk.Tk()
root.title("氣象觀測站查詢")

# 提取天氣資料
weather_data = fetch_weather_data()
if not weather_data:
    root.destroy()  # 如果無法獲取資料則退出

# 提取所有觀測站名稱
station_names = [station['StationName'] for station in weather_data['records']['Station']]

# 設置下拉式選單
station_var = tk.StringVar()
station_var.trace('w', update_station_info)

station_label = ttk.Label(root, text="選擇觀測站:")
station_label.pack(padx=10, pady=5)

station_dropdown = ttk.Combobox(root, textvariable=station_var, values=station_names, state="readonly")
station_dropdown.pack(padx=10, pady=5)

# 顯示觀測站資訊
station_info = tk.StringVar()
station_info_label = ttk.Label(root, textvariable=station_info, justify="left")
station_info_label.pack(padx=10, pady=10)

# 啟動GUI應用程式
root.mainloop()
