import pandas as pd
import re

# Sample text as provided
text = """
جدیدترین قیمت خودروهای پرفروش داخلی طبق استعلام از نمایشگاهداران، 14 آذر ماه 1403 

ساینا⬅️474
ساینا دوگانه برج۷⬅️528
ساینا اتو⬅️590
سهند⬅️542

کوییک اس⬅️459/سفشکی:461.5
کوییک(GX)⬅️458.5
کوییک(GXR)⬅️480
کوییک اتو⬅️616.5/سفشکی:636
اطلس سفشکی⬅️587.5

شاهین⬅️840/بی سانروف:740
شاهین اتو⬅️894/پلاس:1.158

سورن(XU7P)⬅️671/سیمی:677
سورن قالپاق⬅️770
سورن فول⬅️790
سورن دوگانه⬅️مخزن بزرگ:859

پارس سال⬅️777/سیمی:805
پارس فول⬅️826/سیمی:870

رانا ارتقا⬅️733
پ ۲۰۷ (tu3)⬅️707
پ ۲۰۷ هیدرول⬅️789
پ ۲۰۷ دنده پانا⬅️856
پ ۲۰۷ اتو فلز⬅️978
پ ۲۰۷ اتو پانا⬅️1.022
 
دنا بورسی⬅️789
دنا ۶دنده⬅️881
دنا اتو⬅️1.056

تارا (V1)⬅️869
تارا (V2)⬅️م۴۰۳برج۱: 985
تارا (V4)⬅️1.065

هایما(S5)⬅️1.504
هایما(S7)⬅️1.785
هایما(S8)⬅️مشکی:1.995
هایما(X7)⬅️مشکی:1.705

جک(S3)⬅️مشکی:1.248
جک(J7)⬅️مشکی:1.645
جک(X5)⬅️مشکی:1.758
جک(A5)⬅️1.554/مشکی:1.565
جک(T9)⬅️مشکی:2.298

فیدل۵سفید۵پر⬅️1.810/دهپر:1.830
فیدل۵مشکی۵پر⬅️1.825/دهپر:1.845
فیدل۷سفید۵پر⬅️1.860
فیدل۷مشکی۵پر⬅️1.895

فیدل۵سفیدنسکافه⬅️2.485/طوسی:2.420
فیدل۵مشکی‌‌‌نسکافه⬅️2.525
فیدل۷سفیدنسکافه⬅️2.545/طوسی:2.4‌70
فیدل۷مشکی‌‌نسکافه⬅️2.555

پرایم سفیدمشکی⬅️1.805
پرایم سفیدمارون⬅️1.825
پرایم مشکی‌مشکی⬅️1.835
پرایم مشکی‌مارون⬅️1.895

پرستیژ سفیدمشکی⬅️2.380
پرستیژ سفیدمارون⬅️2.425
پرستیژ مشکی‌مشکی⬅️2.445
پرستیژ مشکی‌مارون⬅️2.488

ایکس۲۲دنده⬅️مشکی:904
ایکس۳۳ اتو⬅️1.182مشکی:1.140
ایکس۵۵⬅️مشکی:1.495

آریزو۵⬅️1.410
آریزو۶ پرو⬅️1.600
آریزو۶ (gt)⬅️1.795/مشکی:1.760
آریزو۸مشکی۴۰۲⬅️2.720

تیگو۷⬅️مشکی2.010
تیگو۸(ie)⬅️مشکی:2.990
تیگ۸هیبرید⬅️مشکی:2.870
فونیکس اف‌ایکس⬅️مشکی:2.090
اکستریم (vx)⬅️مشکی:4.565

لاماری⬅️1.955/مشکی:1.900
رسپکت⬅️1.478/مشکی:1.510
تیگارد⬅️1.332

لوین هیبرید⬅️2.940/م۲۰۲۴: 3.055
لوین۱۲۰۰⬅️م۲۰۲۳: 2.630/م۲۰۲۴: 2.690

کرولا هیبرید⬅️م۲۰۲۴: 3.100
کرولا ۱۲۰۰⬅️2.610/م۲۰۲۴: 2.710
کرولا کراس⬅️4.150

سلتوس فول۲۰۲۴⬅️3.950
کیا (k5)م۲۰۲۳⬅️3.930
چانگان(CS55)م۲۰۲۴⬅️2.295
چانگان(CS35)م۲۰۲۴⬅️1.695
گک امپو۲۰۲۴⬅️2.730
وزل۲۰۲۴⬅️3.220
اوتلندر۲۰۲۳⬅️4.910
هونگچی⬅️3.200
آئودی برقی۲۰۲۴⬅️6.850
سیلفی مکس۲۰۲۳⬅️4.070
فولکس برقی⬅️4.430

پراید وانت پاششی⬅️333/لاینر:338
اریسان⬅️495
نیسان تک⬅️هیدرول:653/سیمی:760
نیسان دوگان سیمی رادیال⬅️715
کارون⬅️
"""

# Function to parse the text
def parse_text_to_dataframe(text):
    data = []
    lines = text.strip().split("\n")
    
    for line in lines:
        if '⬅️' in line:
            # Split by ⬅️ to separate car name and prices
            name_part, prices_part = line.split('⬅️', 1)
            name = name_part.strip()
            
            # Handle multiple prices (separated by / or :)
            price_variants = re.split(r'[/|:]', prices_part)
            for variant in price_variants:
                variant = variant.strip()
                
                # Extract variant name and price
                if ':' in variant:
                    variant_name, price = variant.split(':', 1)
                    variant_name = variant_name.strip()
                else:
                    variant_name = None
                    price = variant.strip()
                
                # Convert price to a float if possible
                try:
                    price = float(price.replace(',', ''))
                except ValueError:
                    price = None
                
                # Append to the data list
                data.append({
                    "Car Name": name,
                    "Variant": variant_name,
                    "Price": price
                })
    
    # Create DataFrame from data
    df = pd.DataFrame(data)
    return df

# Parse the text and create DataFrame
df = parse_text_to_dataframe(text)

# Save the DataFrame to CSV
output_csv = "car_prices.csv"
df.to_csv(output_csv, index=False, encoding="utf-8")
print(f"Data saved to {output_csv}")

# Display the DataFrame
print(df.head())
