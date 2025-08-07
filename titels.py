
import jobs_scrap
def titels():
    df = jobs_scrap.scrap()
    titels = df['titels'].tolist()
    return titels
if __name__ == '__main__':
    print(titels())
