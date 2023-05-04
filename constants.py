UPCOMING = "https://upcomingnft.art/upcoming-nft-drops/"
SOLSEA = "https://solsea.io/collection-calendar"
TOKEN = ""
SOL_ID = 887597619570950144
ETH_ID = 887101618166841345
ADA_ID = 890775406649692200
OTHER_ID = 890122245551317043
with open("token.txt", 'r') as f:
    file = f.readlines()
TOKEN = file[0].split("=")[1]
