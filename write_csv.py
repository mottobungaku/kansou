# -*- coding: utf-8 -*-
import csv
import datetime

def main():
# 内容
    time = str(datetime.date.today())#日付の取得
# Title
    print('Input the Title')
    title = input().split()#spaceで文字を区切っている
# 感想の有無：Y/Nを入力
    print('Input the Y/N[Impressions]')
    impre = input().split()#spaceで文字を区切っている
# 書き込む内容
    data = [['Date','Title','Impressions(Y/N)'],[time, title[0], impre[0]],[ 2, title[1], impre[1]],[ 3, title[2], impre[2]]]

    with open('data.csv', 'w', newline='') as f:    #newline=''を追加した
        writer = csv.writer(f)
        writer.writerows(data)
    f.close()
    print('-----End-----')
if __name__=='__main__':
    main()
