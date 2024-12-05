# import csv

# # Raw scraped data
# data : [
#     {"productName": "Samsung Galaxy Watch Ultra 47mm", "price": "$424.71", "gps": False, "connectivity": "N/A", "heartRateMonitor": "N/A", "operatingSystem": "N/A", "touchScreen": "Yes", "batteryLife": "N/A", "builtInStorage": "4GB", "imageUrl": "https://owp.klarna.com/product/252x252/3121449898/Samsung-Galaxy-Watch-Ultra-47mm.jpg?ph:true"},
#     {"productName": "Samsung Galaxy Watch7 44mm BT", "price": "$247.48", "gps": False, "connectivity": "N/A", "heartRateMonitor": "N/A", "operatingSystem": "N/A", "touchScreen": "Yes", "batteryLife": "N/A", "builtInStorage": "4GB", "imageUrl": "https://owp.klarna.com/product/252x252/3121548304/Samsung-Galaxy-Watch7-44mm-BT.jpg?ph:true"},
#     {"productName": "Samsung Galaxy Watch7 40mm BT", "price": "$202.60", "gps": False, "connectivity": "Wi-Fi 1 (802.11b), Wi-Fi 4 (802.11n), Wi-Fi 3 (802.11g), Wi-Fi 2 (802.11a)", "heartRateMonitor": "N/A", "operatingSystem": "N/A", "touchScreen": "Yes", "batteryLife": "N/A", "builtInStorage": "4GB", "imageUrl": "https://owp.klarna.com/product/252x252/3121558837/Samsung-Galaxy-Watch7-40mm-BT.jpg?ph:true"},
#     {"productName": "Samsung Galaxy Watch6 40mm BT", "price": "$149.99", "gps": False, "connectivity": "Wi-Fi 4 (802.11n)", "heartRateMonitor": "N/A", "operatingSystem": "N/A", "touchScreen": "Yes", "batteryLife": "N/A", "builtInStorage": "4GB", "imageUrl": "https://owp.klarna.com/product/252x252/3012361948/Samsung-Galaxy-Watch6-40mm-BT.jpg?ph:true"},
#     {"productName": "Samsung Galaxy Watch6 Classic 47mm BT", "price": "$199.95", "gps": False, "connectivity": "Wi-Fi 1 (802.11b), Wi-Fi 4 (802.11n), Wi-Fi 3 (802.11g), Wi-Fi 2 (802.11a)", "heartRateMonitor": "N/A", "operatingSystem": "N/A", "touchScreen": "Yes", "batteryLife": "N/A", "builtInStorage": "4GB", "imageUrl": "https://owp.klarna.com/product/252x252/3012361134/Samsung-Galaxy-Watch6-Classic-47mm-BT.jpg?ph:true"},
#     {"productName":"Samsung Galaxy Watch6 44mm BT", "price":"$159.99", "gps":False, "connectivity":"Wi-Fi 1 (802.11b), Wi-Fi 4 (802.11n), Wi-Fi 3 (802.11g), Wi-Fi 2 (802.11a)", "heartRateMonitor":"N/A", "operatingSystem":"N/A", "touchScreen":"Yes", "batteryLife":"N/A", "builtInStorage":"4GB", "imageUrl":"https://owp.klarna.com/product/252x252/3012344487/Samsung-Galaxy-Watch6-44mm-BT.jpg?ph:true"},
#     {"productName":"Samsung Galaxy Watch7 44mm LTE", "price":"$255.71", "gps":False, "connectivity":"N/A", "heartRateMonitor":"N/A", "operatingSystem":"N/A", "touchScreen":"Yes", "batteryLife":"N/A", "builtInStorage":"4GB", "imageUrl":"https://owp.klarna.com/product/252x252/3121450005/Samsung-Galaxy-Watch7-44mm-LTE.jpg?ph:true"},
#     {"productName":"Samsung Galaxy Watch 5 40mm", "price":"$142.98", "gps":False, "connectivity":"Wi-Fi 4 (802.11n)", "heartRateMonitor":"N/A", "operatingSystem":"N/A", "touchScreen":"Yes", "batteryLife":"N/A", "builtInStorage":"4GB", "imageUrl":"https://owp.klarna.com/product/252x252/3005891618/Samsung-Galaxy-Watch-5-40mm.jpg?ph:true"},
#     {"productName":"Samsung Galaxy Watch FE 40mm BT", "price":"$124.62", "gps":False, "connectivity":"Wi-Fi 4 (802.11n)", "heartRateMonitor":"N/A", "operatingSystem":"N/A", "touchScreen":"Yes", "batteryLife":"N/A", "builtInStorage":"4GB", "imageUrl":"https://owp.klarna.com/product/252x252/3117749441/Samsung-Galaxy-Watch-FE-40mm-BT.jpg?ph:true"},
#     {"productName":"Samsung Galaxy Watch 4 40mm Bluetooth", "price":"$119.99", "gps":False, "connectivity":"Wi-Fi, Bluetooth", "heartRateMonitor":"N/A", "operatingSystem":"N/A", "touchScreen":"Yes", "batteryLife":"N/A", "builtInStorage":"4GB", "imageUrl":"https://owp.klarna.com/product/252x252/3002519148/Samsung-Galaxy-Watch-4-40mm-Bluetooth.jpg?ph:true"},
#     {"productName":"Samsung Galaxy Watch7 40mm LTE", "price":"$257.76", "gps":False, "connectivity":"Wi-Fi 1 (802.11b), Wi-Fi 4 (802.11n), Wi-Fi 3 (802.11g), Wi-Fi 2 (802.11a)", "heartRateMonitor":"N/A", "operatingSystem":"N/A", "touchScreen":"Yes", "batteryLife":"N/A", "builtInStorage":"4GB", "imageUrl":"https://owp.klarna.com/product/252x252/3121564006/Samsung-Galaxy-Watch7-40mm-LTE.jpg?ph:true"},
#     {"productName":"Samsung Galaxy Watch 5 Pro 45mm", "price":"$219.49", "gps":False, "connectivity":"Wi-Fi, 3G, 4G, Bluetooth", "heartRateMonitor":"N/A", "operatingSystem":"N/A", "touchScreen":"Yes", "batteryLife":"N/A", "builtInStorage":"4GB", "imageUrl":"https://owp.klarna.com/product/252x252/3005891631/Samsung-Galaxy-Watch-5-Pro-45mm.jpg?ph:true"},
#     {"productName":"Samsung Galaxy Watch6 Classic 47mm 4G", "price":"$269.99", "gps":False, "connectivity":"Wi-Fi 1 (802.11b), Wi-Fi 4 (802.11n), Wi-Fi 3 (802.11g), Wi-Fi 2 (802.11a)", "heartRateMonitor":"N/A", "operatingSystem":"N/A", "touchScreen":"Yes", "batteryLife":"N/A", "builtInStorage":"4GB", "imageUrl":"https://owp.klarna.com/product/252x252/3012344275/Samsung-Galaxy-Watch6-Classic-47mm-4G.jpg?ph:true"},
#     {"productName":"Samsung Galaxy Watch 4 Classic 46mm Bluetooth", "price":"$118.88", "gps":False, "connectivity":"Wi-Fi 4 (802.11n)", "heartRateMonitor":"N/A", "operatingSystem":"N/A", "touchScreen":"Yes", "batteryLife":"N/A", "builtInStorage":"4GB", "imageUrl":"https://owp.klarna.com/product/252x252/3002519108/Samsung-Galaxy-Watch-4-Classic-46mm-Bluetooth.jpg?ph:true"},
#     {"productName":"Samsung Galaxy Watch6 Classic 43mm BT", "price":"$164.99", "gps":False, "connectivity":"Wi-Fi 1 (802.11b), Wi-Fi 4 (802.11n), Wi-Fi 3 (802.11g), Wi-Fi 2 (802.11a)", "heartRateMonitor":"N/A", "operatingSystem":"N/A", "touchScreen":"Yes", "batteryLife":"N/A", "builtInStorage":"4GB", "imageUrl":"https://owp.klarna.com/product/252x252/3012360636/Samsung-Galaxy-Watch6-Classic-43mm-BT.jpg?ph:true"},
#     {"productName":"Samsung Galaxy Watch6 44mm 4G", "price":"$219.99", "gps":False, "connectivity":"Wi-Fi 1 (802.11b), Wi-Fi 4 (802.11n), Wi-Fi 3 (802.11g), Wi-Fi 2 (802.11a)", "heartRateMonitor":"N/A", "operatingSystem":"N/A", "touchScreen":"Yes", "batteryLife":"N/A", "builtInStorage":"4GB", "imageUrl":"https://owp.klarna.com/product/252x252/3012354546/Samsung-Galaxy-Watch6-44mm-4G.jpg?ph:true"},
#     {"productName":"Samsung Galaxy Watch 5 44mm", "price":"$232.52", "gps":False, "connectivity":"Wi-Fi 4 (802.11n)", "heartRateMonitor":"N/A", "operatingSystem":"N/A", "touchScreen":"Yes", "batteryLife":"N/A", "builtInStorage":"4GB", "imageUrl":"https://owp.klarna.com/product/252x252/3005891599/Samsung-Galaxy-Watch-5-44mm.jpg?ph:true"},
#     {"productName":"Samsung Galaxy Watch 42mm Bluetooth", "price":"$127.85", "gps":False, "connectivity":"Wi-Fi 1 (802.11b), Wi-Fi 4 (802.11n), Wi-Fi 3 (802.11g)", "heartRateMonitor":"N/A", "operatingSystem":"N/A", "touchScreen":"Yes", "batteryLife":"N/A", "builtInStorage":"4GB", "imageUrl":"https://owp.klarna.com/product/252x252/1864776659/Samsung-Galaxy-Watch-42mm-Bluetooth.jpg?ph:true"},
#     {"productName":"Samsung Galaxy Watch 5 Pro 45mm LTE", "price":"$256.51", "gps":False, "connectivity":"Wi-Fi 1 (802.11b), Wi-Fi 4 (802.11n), Wi-Fi 3 (802.11g)", "heartRateMonitor":"N/A", "operatingSystem":"N/A", "touchScreen":"Yes", "batteryLife":"N/A", "builtInStorage":"4GB", "imageUrl":"https://owp.klarna.com/product/252x252/3005891631/Samsung-Galaxy-Watch-5-Pro-45mm-LTE.jpg?ph:true"},
#     {"productName":"Samsung Galaxy Watch6 Classic 43mm 4G", "price":"$289.99", "gps":False, "connectivity":"Wi-Fi 1 (802.11b), Wi-Fi 4 (802.11n), Wi-Fi 3 (802.11g), Wi-Fi 2 (802.11a)", "heartRateMonitor":"N/A", "operatingSystem":"N/A", "touchScreen":"Yes", "batteryLife":"N/A", "builtInStorage":"4GB", "imageUrl":"https://owp.klarna.com/product/252x252/3012344504/Samsung-Galaxy-Watch6-Classic-43mm-4G.jpg?ph:true"},
#     {"productName":"Samsung Galaxy Watch6 40mm 4G", "price":"$199.99", "gps":False, "connectivity":"Wi-Fi 1 (802.11b), Wi-Fi 4 (802.11n), Wi-Fi 3 (802.11g), Wi-Fi 2 (802.11a)", "heartRateMonitor":"N/A", "operatingSystem":"N/A", "touchScreen":"Yes", "batteryLife":"N/A", "builtInStorage":"4GB", "imageUrl":"https://owp.klarna.com/product/252x252/3012344436/Samsung-Galaxy-Watch6-40mm-4G.jpg?ph:true"},
#     {"productName":"Samsung Galaxy Watch Active 2 40mm LTE Stainless Steel", "price":"$97.99", "gps":False, "connectivity":"Wi-Fi 4 (802.11n)", "heartRateMonitor":"N/A", "operatingSystem":"N/A", "touchScreen":"Yes", "batteryLife":"N/A", "builtInStorage":"4GB", "imageUrl":"https://owp.klarna.com/product/252x252/1906939826/Samsung-Galaxy-Watch-Active-2-40mm-LTE-Stainless-Steel.jpg?ph:true"},
#     {"productName":"Samsung Galaxy Watch 4 44mm Bluetooth", "price":"$129.99", "gps":False, "connectivity":"Wi-Fi", "heartRateMonitor":"N/A", "operatingSystem":"N/A", "touchScreen":"Yes", "batteryLife":"N/A", "builtInStorage":"4GB", "imageUrl":"https://owp.klarna.com/product/252x252/3002519421/Samsung-Galaxy-Watch-4-44mm-Bluetooth.jpg?ph:true"},
#     {"productName":"Samsung Galaxy Watch 4 Classic 42mm Bluetooth", "price":"$159.99", "gps":False, "connectivity":"Wi-Fi", "heartRateMonitor":"N/A", "operatingSystem":"N/A", "touchScreen":"Yes", "batteryLife":"N/A", "builtInStorage":"4GB", "imageUrl":"https://owp.klarna.com/product/252x252/3002523058/Samsung-Galaxy-Watch-4-Classic-42mm-Bluetooth.jpg?ph:true"},
#     {"productName":"Samsung Galaxy Watch 5 40mm LTE", "price":"$250.49", "gps":False, "connectivity":"N/A", "heartRateMonitor":"N/A", "operatingSystem":"N/A", "touchScreen":"Yes", "batteryLife":"N/A", "builtInStorage":"4GB", "imageUrl":"https://owp.klarna.com/product/252x252/3005891618/Samsung-Galaxy-Watch-5-40mm-LTE.jpg?ph:true"},
#     {"productName":"Samsung Galaxy Watch 4 40mm LTE", "price":"$149.00", "gps":False, "connectivity":"N/A", "heartRateMonitor":"N/A", "operatingSystem":"N/A", "touchScreen":"Yes", "batteryLife":"N/A", "builtInStorage":"4GB", "imageUrl":"https://owp.klarna.com/product/252x252/3002518975/Samsung-Galaxy-Watch-4-40mm-LTE.jpg?ph:true"},
#     {"productName":"Samsung Galaxy Watch 4 44mm LTE", "price":"$149.99", "gps":False, "connectivity":"N/A", "heartRateMonitor":"N/A", "operatingSystem":"N/A", "touchScreen":"Yes", "batteryLife":"N/A", "builtInStorage":"4GB", "imageUrl":"https://owp.klarna.com/product/252x252/3002519263/Samsung-Galaxy-Watch-4-44mm-LTE.jpg?ph:true"}
# ]

# # # File name for the output CSV
# output_file = "products.csv"

# # Writing the data to CSV
# with open(output_file, mode="w", newline="", encoding="utf-8") as file:
#     writer = csv.DictWriter(file, fieldnames=data[0].keys())
#     writer.writeheader()  # Write the header
#     writer.writerows(data)  # Write the rows

# print(f"Data successfully written to {output_file}")  
# 
# 
import csv

# Raw scraped data
data = [
    {"productName": "Samsung Galaxy Watch Ultra 47mm", "price": "$424.71", "gps": False, "connectivity": "N/A", "heartRateMonitor": "N/A", "operatingSystem": "N/A", "touchScreen": "Yes", "batteryLife": "N/A", "builtInStorage": "4GB", "imageUrl": "https://owp.klarna.com/product/252x252/3121449898/Samsung-Galaxy-Watch-Ultra-47mm.jpg?ph:true"},
    {"productName": "Samsung Galaxy Watch7 44mm BT", "price": "$247.48", "gps": False, "connectivity": "N/A", "heartRateMonitor": "N/A", "operatingSystem": "N/A", "touchScreen": "Yes", "batteryLife": "N/A", "builtInStorage": "4GB", "imageUrl": "https://owp.klarna.com/product/252x252/3121548304/Samsung-Galaxy-Watch7-44mm-BT.jpg?ph:true"},
    {"productName": "Samsung Galaxy Watch7 40mm BT", "price": "$202.60", "gps": False, "connectivity": "Wi-Fi 1 (802.11b), Wi-Fi 4 (802.11n), Wi-Fi 3 (802.11g), Wi-Fi 2 (802.11a)", "heartRateMonitor": "N/A", "operatingSystem": "N/A", "touchScreen": "Yes", "batteryLife": "N/A", "builtInStorage": "4GB", "imageUrl": "https://owp.klarna.com/product/252x252/3121558837/Samsung-Galaxy-Watch7-40mm-BT.jpg?ph:true"},
    # Add more items from the data list here
    {"productName": "Samsung Galaxy Watch6 40mm BT", "price": "$149.99", "gps": False, "connectivity": "Wi-Fi 4 (802.11n)", "heartRateMonitor": "N/A", "operatingSystem": "N/A", "touchScreen": "Yes", "batteryLife": "N/A", "builtInStorage": "4GB", "imageUrl": "https://owp.klarna.com/product/252x252/3012361948/Samsung-Galaxy-Watch6-40mm-BT.jpg?ph:true"},
    {"productName": "Samsung Galaxy Watch6 Classic 47mm BT", "price": "$199.95", "gps": False, "connectivity": "Wi-Fi 1 (802.11b), Wi-Fi 4 (802.11n), Wi-Fi 3 (802.11g), Wi-Fi 2 (802.11a)", "heartRateMonitor": "N/A", "operatingSystem": "N/A", "touchScreen": "Yes", "batteryLife": "N/A", "builtInStorage": "4GB", "imageUrl": "https://owp.klarna.com/product/252x252/3012361134/Samsung-Galaxy-Watch6-Classic-47mm-BT.jpg?ph:true"},
    {"productName":"Samsung Galaxy Watch6 44mm BT", "price":"$159.99", "gps":False, "connectivity":"Wi-Fi 1 (802.11b), Wi-Fi 4 (802.11n), Wi-Fi 3 (802.11g), Wi-Fi 2 (802.11a)", "heartRateMonitor":"N/A", "operatingSystem":"N/A", "touchScreen":"Yes", "batteryLife":"N/A", "builtInStorage":"4GB", "imageUrl":"https://owp.klarna.com/product/252x252/3012344487/Samsung-Galaxy-Watch6-44mm-BT.jpg?ph:true"},
    {"productName":"Samsung Galaxy Watch7 44mm LTE", "price":"$255.71", "gps":False, "connectivity":"N/A", "heartRateMonitor":"N/A", "operatingSystem":"N/A", "touchScreen":"Yes", "batteryLife":"N/A", "builtInStorage":"4GB", "imageUrl":"https://owp.klarna.com/product/252x252/3121450005/Samsung-Galaxy-Watch7-44mm-LTE.jpg?ph:true"},
    {"productName":"Samsung Galaxy Watch 5 40mm", "price":"$142.98", "gps":False, "connectivity":"Wi-Fi 4 (802.11n)", "heartRateMonitor":"N/A", "operatingSystem":"N/A", "touchScreen":"Yes", "batteryLife":"N/A", "builtInStorage":"4GB", "imageUrl":"https://owp.klarna.com/product/252x252/3005891618/Samsung-Galaxy-Watch-5-40mm.jpg?ph:true"},
    {"productName":"Samsung Galaxy Watch FE 40mm BT", "price":"$124.62", "gps":False, "connectivity":"Wi-Fi 4 (802.11n)", "heartRateMonitor":"N/A", "operatingSystem":"N/A", "touchScreen":"Yes", "batteryLife":"N/A", "builtInStorage":"4GB", "imageUrl":"https://owp.klarna.com/product/252x252/3117749441/Samsung-Galaxy-Watch-FE-40mm-BT.jpg?ph:true"},
    {"productName":"Samsung Galaxy Watch 4 40mm Bluetooth", "price":"$119.99", "gps":False, "connectivity":"Wi-Fi, Bluetooth", "heartRateMonitor":"N/A", "operatingSystem":"N/A", "touchScreen":"Yes", "batteryLife":"N/A", "builtInStorage":"4GB", "imageUrl":"https://owp.klarna.com/product/252x252/3002519148/Samsung-Galaxy-Watch-4-40mm-Bluetooth.jpg?ph:true"},
    {"productName":"Samsung Galaxy Watch7 40mm LTE", "price":"$257.76", "gps":False, "connectivity":"Wi-Fi 1 (802.11b), Wi-Fi 4 (802.11n), Wi-Fi 3 (802.11g), Wi-Fi 2 (802.11a)", "heartRateMonitor":"N/A", "operatingSystem":"N/A", "touchScreen":"Yes", "batteryLife":"N/A", "builtInStorage":"4GB", "imageUrl":"https://owp.klarna.com/product/252x252/3121564006/Samsung-Galaxy-Watch7-40mm-LTE.jpg?ph:true"},
    {"productName":"Samsung Galaxy Watch 5 Pro 45mm", "price":"$219.49", "gps":False, "connectivity":"Wi-Fi, 3G, 4G, Bluetooth", "heartRateMonitor":"N/A", "operatingSystem":"N/A", "touchScreen":"Yes", "batteryLife":"N/A", "builtInStorage":"4GB", "imageUrl":"https://owp.klarna.com/product/252x252/3005891631/Samsung-Galaxy-Watch-5-Pro-45mm.jpg?ph:true"},
    {"productName":"Samsung Galaxy Watch6 Classic 47mm 4G", "price":"$269.99", "gps":False, "connectivity":"Wi-Fi 1 (802.11b), Wi-Fi 4 (802.11n), Wi-Fi 3 (802.11g), Wi-Fi 2 (802.11a)", "heartRateMonitor":"N/A", "operatingSystem":"N/A", "touchScreen":"Yes", "batteryLife":"N/A", "builtInStorage":"4GB", "imageUrl":"https://owp.klarna.com/product/252x252/3012344275/Samsung-Galaxy-Watch6-Classic-47mm-4G.jpg?ph:true"},
    {"productName":"Samsung Galaxy Watch 4 Classic 46mm Bluetooth", "price":"$118.88", "gps":False, "connectivity":"Wi-Fi 4 (802.11n)", "heartRateMonitor":"N/A", "operatingSystem":"N/A", "touchScreen":"Yes", "batteryLife":"N/A", "builtInStorage":"4GB", "imageUrl":"https://owp.klarna.com/product/252x252/3002519108/Samsung-Galaxy-Watch-4-Classic-46mm-Bluetooth.jpg?ph:true"},
    {"productName":"Samsung Galaxy Watch6 Classic 43mm BT", "price":"$164.99", "gps":False, "connectivity":"Wi-Fi 1 (802.11b), Wi-Fi 4 (802.11n), Wi-Fi 3 (802.11g), Wi-Fi 2 (802.11a)", "heartRateMonitor":"N/A", "operatingSystem":"N/A", "touchScreen":"Yes", "batteryLife":"N/A", "builtInStorage":"4GB", "imageUrl":"https://owp.klarna.com/product/252x252/3012360636/Samsung-Galaxy-Watch6-Classic-43mm-BT.jpg?ph:true"},
    {"productName":"Samsung Galaxy Watch6 44mm 4G", "price":"$219.99", "gps":False, "connectivity":"Wi-Fi 1 (802.11b), Wi-Fi 4 (802.11n), Wi-Fi 3 (802.11g), Wi-Fi 2 (802.11a)", "heartRateMonitor":"N/A", "operatingSystem":"N/A", "touchScreen":"Yes", "batteryLife":"N/A", "builtInStorage":"4GB", "imageUrl":"https://owp.klarna.com/product/252x252/3012354546/Samsung-Galaxy-Watch6-44mm-4G.jpg?ph:true"},
    {"productName":"Samsung Galaxy Watch 5 44mm", "price":"$232.52", "gps":False, "connectivity":"Wi-Fi 4 (802.11n)", "heartRateMonitor":"N/A", "operatingSystem":"N/A", "touchScreen":"Yes", "batteryLife":"N/A", "builtInStorage":"4GB", "imageUrl":"https://owp.klarna.com/product/252x252/3005891599/Samsung-Galaxy-Watch-5-44mm.jpg?ph:true"},
    {"productName":"Samsung Galaxy Watch 42mm Bluetooth", "price":"$127.85", "gps":False, "connectivity":"Wi-Fi 1 (802.11b), Wi-Fi 4 (802.11n), Wi-Fi 3 (802.11g)", "heartRateMonitor":"N/A", "operatingSystem":"N/A", "touchScreen":"Yes", "batteryLife":"N/A", "builtInStorage":"4GB", "imageUrl":"https://owp.klarna.com/product/252x252/1864776659/Samsung-Galaxy-Watch-42mm-Bluetooth.jpg?ph:true"},
    {"productName":"Samsung Galaxy Watch 5 Pro 45mm LTE", "price":"$256.51", "gps":False, "connectivity":"Wi-Fi 1 (802.11b), Wi-Fi 4 (802.11n), Wi-Fi 3 (802.11g)", "heartRateMonitor":"N/A", "operatingSystem":"N/A", "touchScreen":"Yes", "batteryLife":"N/A", "builtInStorage":"4GB", "imageUrl":"https://owp.klarna.com/product/252x252/3005891631/Samsung-Galaxy-Watch-5-Pro-45mm-LTE.jpg?ph:true"},
    {"productName":"Samsung Galaxy Watch6 Classic 43mm 4G", "price":"$289.99", "gps":False, "connectivity":"Wi-Fi 1 (802.11b), Wi-Fi 4 (802.11n), Wi-Fi 3 (802.11g), Wi-Fi 2 (802.11a)", "heartRateMonitor":"N/A", "operatingSystem":"N/A", "touchScreen":"Yes", "batteryLife":"N/A", "builtInStorage":"4GB", "imageUrl":"https://owp.klarna.com/product/252x252/3012344504/Samsung-Galaxy-Watch6-Classic-43mm-4G.jpg?ph:true"},
    {"productName":"Samsung Galaxy Watch6 40mm 4G", "price":"$199.99", "gps":False, "connectivity":"Wi-Fi 1 (802.11b), Wi-Fi 4 (802.11n), Wi-Fi 3 (802.11g), Wi-Fi 2 (802.11a)", "heartRateMonitor":"N/A", "operatingSystem":"N/A", "touchScreen":"Yes", "batteryLife":"N/A", "builtInStorage":"4GB", "imageUrl":"https://owp.klarna.com/product/252x252/3012344436/Samsung-Galaxy-Watch6-40mm-4G.jpg?ph:true"},
    {"productName":"Samsung Galaxy Watch Active 2 40mm LTE Stainless Steel", "price":"$97.99", "gps":False, "connectivity":"Wi-Fi 4 (802.11n)", "heartRateMonitor":"N/A", "operatingSystem":"N/A", "touchScreen":"Yes", "batteryLife":"N/A", "builtInStorage":"4GB", "imageUrl":"https://owp.klarna.com/product/252x252/1906939826/Samsung-Galaxy-Watch-Active-2-40mm-LTE-Stainless-Steel.jpg?ph:true"},
    {"productName":"Samsung Galaxy Watch 4 44mm Bluetooth", "price":"$129.99", "gps":False, "connectivity":"Wi-Fi", "heartRateMonitor":"N/A", "operatingSystem":"N/A", "touchScreen":"Yes", "batteryLife":"N/A", "builtInStorage":"4GB", "imageUrl":"https://owp.klarna.com/product/252x252/3002519421/Samsung-Galaxy-Watch-4-44mm-Bluetooth.jpg?ph:true"},
    {"productName":"Samsung Galaxy Watch 4 Classic 42mm Bluetooth", "price":"$159.99", "gps":False, "connectivity":"Wi-Fi", "heartRateMonitor":"N/A", "operatingSystem":"N/A", "touchScreen":"Yes", "batteryLife":"N/A", "builtInStorage":"4GB", "imageUrl":"https://owp.klarna.com/product/252x252/3002523058/Samsung-Galaxy-Watch-4-Classic-42mm-Bluetooth.jpg?ph:true"},
    {"productName":"Samsung Galaxy Watch 5 40mm LTE", "price":"$250.49", "gps":False, "connectivity":"N/A", "heartRateMonitor":"N/A", "operatingSystem":"N/A", "touchScreen":"Yes", "batteryLife":"N/A", "builtInStorage":"4GB", "imageUrl":"https://owp.klarna.com/product/252x252/3005891618/Samsung-Galaxy-Watch-5-40mm-LTE.jpg?ph:true"},
    {"productName":"Samsung Galaxy Watch 4 40mm LTE", "price":"$149.00", "gps":False, "connectivity":"N/A", "heartRateMonitor":"N/A", "operatingSystem":"N/A", "touchScreen":"Yes", "batteryLife":"N/A", "builtInStorage":"4GB", "imageUrl":"https://owp.klarna.com/product/252x252/3002518975/Samsung-Galaxy-Watch-4-40mm-LTE.jpg?ph:true"},
    {"productName":"Samsung Galaxy Watch 4 44mm LTE", "price":"$149.99", "gps":False, "connectivity":"N/A", "heartRateMonitor":"N/A", "operatingSystem":"N/A", "touchScreen":"Yes", "batteryLife":"N/A", "builtInStorage":"4GB", "imageUrl":"https://owp.klarna.com/product/252x252/3002519263/Samsung-Galaxy-Watch-4-44mm-LTE.jpg?ph:true"}
]

# Specify the CSV file name
csv_file = "scraped_data.csv"

# Writing data to the CSV file
try:
    with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()  # Write header row
        writer.writerows(data)  # Write data rows
    print(f"Data has been written to {csv_file} successfully.")
except Exception as e:
    print(f"An error occurred: {e}")
  