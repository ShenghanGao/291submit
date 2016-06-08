# coding: utf8
import operator
import string

'''
preprocess the poems in song_poem.txt
initially in the form as:

艾丑?登立鱼山
    杳杳灵岩洞府深，有人岩下振潮音。
    龙天耸听生欢喜，留得神鱼立到今。

convert a poem into a line, and get rid of the title
as:

杳杳灵岩洞府深，有人岩下振潮音。龙天耸听生欢喜，留得神鱼立到今。


collect and classify poems according to their format, and put into 
"jueju5s.txt", "jueju7s.txt", "lvshi5s.txt", "lvshi7s.txt"

'''


input_file = ['song_poem.txt']
output_file = ["jueju5s.txt", "jueju7s.txt", "lvshi5s.txt", "lvshi7s.txt"]

def getUTF8Length(s):
  unicode_string = s.decode("utf-8")
  return len(unicode_string)

def main():
  counts = dict()
  cur_poem = ""
  poems = [[],[],[],[]]
  poem_start = False
  for i in range(1):
    with open(input_file[i],'r') as in_f:
      for line in in_f:
        line = line.strip()
        if (not line) and cur_poem:
          poem_len = len(cur_poem.decode("utf-8"))
          # print cur_poem
          # print "length is: " + str(poem_len)
          if poem_len == 24 and cur_poem.find('，') == 15 and cur_poem.find('。') == 33:
            poems[0].append(cur_poem) # jueju5
          elif poem_len == 32 and cur_poem.find('，') == 21 and cur_poem.find('。') == 45:
            poems[1].append(cur_poem) # jueju7
          elif poem_len == 48 and cur_poem.find('，') == 15 and cur_poem.find('。') == 33:
            poems[2].append(cur_poem) # lvshi5
          elif poem_len == 64 and cur_poem.find('，') == 21 and cur_poem.find('。') == 45:
            poems[3].append(cur_poem) # lvshi7
          cur_poem = ""
          poem_start = False
        elif line and (not poem_start):
          poem_start = True
        elif line and poem_start:
          # remove () and --
          a = line.find('-')
          if a > 0:
            line = line[:a]
            line.strip()
          a = line.find('(')
          if a > 0:
            line = line[:a]
            line.strip()
          a = line.find('（')
          if a > 0:
            line = line[:a]
            line.strip()
          if line.find('）') > 0:
            line = ""
          cur_poem = cur_poem + line
          #print cur_poem
    in_f.close()

  for i in range(4):    
    print "There are totally " + str(len(poems[i])) + " in" + output_file[i]
    with open(output_file[i], 'w+') as out_f:
      for cur_poem in poems[i]:
        out_f.write(cur_poem + '\n')
        for c in cur_poem.decode('utf8'):
          counts[c] = counts.get(c, 0) + 1
    out_f.close()

  sorted_counts = sorted(counts.items(), key=operator.itemgetter(1))
  sorted_counts = reversed(sorted_counts)
  with open("chars.txt", 'w+') as out_f:
    for i in sorted_counts:
      out_f.write(i[0].encode('utf8') + ": " + str(i[1]) + "\n")
  out_f.close()                                 
  
if __name__ == '__main__':
  main()
