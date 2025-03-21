# coinGeckoBITCOIN
Download Data from coinGecko

Thank you for using this tool to download historical crypto based on coingecko API. 
Official Documentation on the coingecko API can be found on https://docs.coingecko.com/reference/introduction.

IMPORTANT: This tool is based on the Free API Account, assumptions on FREE account were made on the script. If you plan to upgrade your license, you could improve the process/script.

USAGE:

1.Generate your API key from you coinGecko account: https://www.coingecko.com/en/developers/dashboard

2.Go to main.py and define the following variables: 

*ticker: The crypto name
*start_date: the starting historical download date, use the example syntaxis Ex: (start_dt = date(2024, 10, 1))
*end_date: the end or last date that you will be able to retreive. 
*currency: currency symbol of the exchange you want to use. Ex (usd,mxn)
*api_key: Use the api key that you generated on step 1
*usr: You can enter the text of the user that is uploading data (
The ideal for this variable is that it is parameterized)

3.Run the script :)


SCALABILITY: 
This main code is set up to work with one or multiple crypto_currencies, you can set up the cryptos that you can to download by defining the ticker variable in the main code. 
Ex: One crypto ticker=['Bitcoin']
Ex: Two ticker=['Bitcoin','Dogecoin']

