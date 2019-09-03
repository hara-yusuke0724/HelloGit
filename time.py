import time
start=time.time()
hoge() #速度を調べたい処理
end=time.time()
print(f'処理にかかった時間は{end-start}秒です。')