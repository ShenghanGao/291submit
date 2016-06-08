# coding: utf8
import operator
import string
'''
preprocess the poems in tang_poem.txt
initially in the form as:

   卷1_24 【初晴落景】李世民 

晚霞聊自怡，初晴弥可喜。日晃百花色，风动千林翠。
池鱼跃不同，园鸟声还异。寄言博通者，知予物外志。

convert a poem into a line, and get rid of the title
as:
晚霞聊自怡，初晴弥可喜。日晃百花色，风动千林翠。池鱼跃不同，园鸟声还异。寄言博通者，知予物外志。

collect and classify poems according to their format, and put into 
"jueju5.txt", "jueju7.txt", "lvshi5.txt", "lvshi7.txt"

'''
input_file = ['tang_poem.txt']
output_file = ["jueju5.txt", "jueju7.txt", "lvshi5.txt", "lvshi7.txt"]

def getUTF8Length(s):
  unicode_string = s.decode("utf-8")
  return len(unicode_string)

def main():
  counts = dict()
  cur_poem = ""
  poems = [[],[],[],[]]

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
        elif line and line.find('卷') != 0:
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
