import pandas as pd

def main():
    xlsx_1 = pd.read_excel("附件1：123家有信贷记录企业的相关数据.xlsx", sheet_name="企业信息")
    xlsx_1.to_csv("数据/附件一_企业信息", encoding='utf_8_sig')
    xlsx_1 = pd.read_excel("附件1：123家有信贷记录企业的相关数据.xlsx", sheet_name="进项发票信息")
    xlsx_1.to_csv("数据/附件一_进项发票信息", encoding='utf_8_sig')
    xlsx_1 = pd.read_excel("附件1：123家有信贷记录企业的相关数据.xlsx", sheet_name="销项发票信息")
    xlsx_1.to_csv("数据/附件一_销项发票信息", encoding='utf_8_sig')
    
    xlsx_2 = pd.read_excel("附件2：302家无信贷记录企业的相关数据.xlsx", sheet_name="企业信息")
    xlsx_2.to_csv("数据/附件二_企业信息", encoding='utf_8_sig')
    xlsx_2 = pd.read_excel("附件2：302家无信贷记录企业的相关数据.xlsx", sheet_name="进项发票信息")
    xlsx_2.to_csv("数据/附件二_进项发票信息", encoding='utf_8_sig')
    xlsx_2 = pd.read_excel("附件2：302家无信贷记录企业的相关数据.xlsx", sheet_name="销项发票信息")
    xlsx_2.to_csv("数据/附件二_销项发票信息", encoding='utf_8_sig')


if __name__ == '__main__':
    print("wdnmd")
    main()
