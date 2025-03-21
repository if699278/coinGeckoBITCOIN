from utils import all_crypto, historical_data, date_delta
import pandas as pd
import time
from datetime import datetime, date

#Variables
ticker=['Bitcoin']
currency='usd'
api_key='CG-SiWix6uuyKHPV8sdWZnpHNGZ'
usr='TEST'
start_dt = date(2024, 10, 1)
end_dt = date(2024, 12, 31)

df=all_crypto(api_key)
df = df[df['name'].isin(ticker)]
df=df[df['name']==ticker]
id_cryp=df['id'].tolist()

for j in range(0,len(id_cryp)):
    df=pd.DataFrame(columns=['cryptoName','date','price','updt_dt','updt_usr'])
    dates=date_delta(start_dt,end_dt)
    for i in range(0,len(dates)-1):   #Doing a loop way to aggregate sleep funtion, so API won´t be saturated with free account type

        #print(id_cryp+":"+dates[i])
        df.at[i,'cryptoName']=id_cryp[j]
        df.at[i,'date']=str(dates[i])
        df.at[i,'price']=historical_data(id_cryp[j],api_key,dates[i],currency)
        time.sleep(2)
    df['updt_dt']=datetime.today().strftime('%d-%m-%Y')
    df['updt_usr']=usr
        
#Lets Validate if Historical data already exist, to ensure not duplicating data
    try:
        df_existente = pd.read_parquet(f"price_{ticker[j]}.parquet", engine="pyarrow")
    except:
        print("An exception occurred")
    
    df=df[~df['date'].isin(df_existente['date'])]
    df=pd.concat([df_existente, df], ignore_index=True)
    df.to_parquet(f"price_{ticker[j]}.parquet", engine="pyarrow", index=False)