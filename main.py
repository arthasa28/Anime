
from time import sleep

def loadbar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='#'):
  percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration/float(total)))
  filledLength = int(length * iteration // total)
  bar = fill * filledLength + '.' * (length - filledLength)
  print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
  if iteration == total:
    print()

items = list(range(0, 30))
l = len(items)

loadbar(0, l, prefix='Progress:', suffix='Done', length=l)
for i, item in enumerate(items):
  sleep(0.5)
  loadbar(i + 1, l, prefix='Progress System:', suffix='Done', length=l)

loadbar(0, l, prefix='Progress:', suffix='Done', length=l)
for i, item in enumerate(items):
  sleep(0.4)
  loadbar(i + 1, l, prefix='Progress Data Base:', suffix='Done', length=l)

loadbar(0, l, prefix='Progress:', suffix='Done', length=l)
for i, item in enumerate(items):
  sleep(0.2)
  loadbar(i + 1, l, prefix='Progress Scanning:', suffix='Done', length=l)

loadbar(0, l, prefix='Progress:', suffix='Done', length=l)
for i, item in enumerate(items):
  sleep(0.2)
  loadbar(i + 1, l, prefix='Progress Scanning:', suffix='Done', length=l)

loadbar(0, l, prefix='Progress:', suffix='Done', length=l)
for i, item in enumerate(items):
  sleep(0.2)
  loadbar(i + 1, l, prefix='Progress Scanning:', suffix='Done', length=l)

loadbar(0, l, prefix='Progress:', suffix='Done', length=l)
for i, item in enumerate(items):
  sleep(0.1)
  loadbar(i + 1, l, prefix='Progress Create Server:', suffix='Done', length=l)

loadbar(0, l, prefix='Progress:', suffix='Done', length=l)
for i, item in enumerate(items):
  sleep(0.1)
  loadbar(i + 1, l, prefix='Progress Create Server:', suffix='Done', length=l)

loadbar(0, l, prefix='Progress:', suffix='Done', length=l)
for i, item in enumerate(items):
  sleep(0.1)
  loadbar(i + 1, l, prefix='Progress Create Server:', suffix='Done', length=l)

loadbar(0, l, prefix='Progress:', suffix='Done', length=l)
for i, item in enumerate(items):
  sleep(0.1)
  loadbar(i + 1, l, prefix='Progress Create Server:', suffix='Done', length=l)

loadbar(0, l, prefix='Progress:', suffix='Done', length=l)
for i, item in enumerate(items):
  sleep(0.1)
  loadbar(i + 1, l, prefix='Progress Create Server:', suffix='Done', length=l)

loadbar(0, l, prefix='Progress:', suffix='Done', length=l)
for i, item in enumerate(items):
  sleep(0.1)
  loadbar(i + 1, l, prefix='Progress Create Server:', suffix='Done', length=l)

loadbar(0, l, prefix='Progress:', suffix='Done', length=l)
for i, item in enumerate(items):
  sleep(0.1)
  loadbar(i + 1, l, prefix='Progress Create Server:', suffix='Done', length=l)

loadbar(0, l, prefix='Progress:', suffix='Done', length=l)
for i, item in enumerate(items):
  sleep(0.1)
  loadbar(i + 1, l, prefix='Progress Create Server:', suffix='Done', length=l)

loadbar(0, l, prefix='Progress:', suffix='Done', length=l)
for i, item in enumerate(items):
  sleep(0.1)
  loadbar(i + 1, l, prefix='Progress Create Cloud:', suffix='Done', length=l)



print("")
print("Done!")
print("")
print("DVR cctv Telah Selasai Di Buat")
print("")
print("")

























