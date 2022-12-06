
# some test data to test my code
test1 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb" # result 19
test2 = "bvwbjplbgvbhsrlpgdmjqwftvncz" # result 23
test3 = "nppdvjthqldpwncqszvftbrmjlhg" # result 23


test_same = "aaaaaaaaaaaaaa" # result no signal
test_different = "abcdefghijklmn" # result 14
test_mix = "abababcdefghijklmn" # result 18

# the data set I need to analyse
signal = "tnmmpfmfzmmnsmsjmjjbvvhnhzzfmmgpmgpgbgnnwffjhffzqqmzzbnbssrqqrnnhsnngsszsqzszhzfhzfzwzfzrrmhmghgwhhjjqwqttwhttjllrtrtzzcfzfgzznfznfzfnnbddvmvzmmfsmfsmfffhlfldlqqrnrznnhmmgqqzhhmjhmhppqbpbbngnlldvvdqvvrtrdrtrnttnppfllrbbrprpnpdplpmllhwwddqpdprddzzfccqpcqpcpcbbdhdjdjwjcwcctdcttzgzmmscmsmdmttwhwzhhnjhnhlhvhlvlglpgpmmjmgmrgrddmwddjfftfwflfslffqtfqttpftppflfmmhvhvcvbvhbhggpbgbppvdpvpvfppbwwsnnhphllbdbnbvbmvvzffvsffdldmlmtmccnlnbnjbnjnhhbfhhgzzlwlfflzffdccggdcgcjjhffjfgfgcczjccvwcvvqgvvqvllqzqmqllhjjqnqggttsdddjgdjgjzzrgrfrbrssrgrgdgrgbbssmdsdfddsndnsdnsdnnmqqsspqqmrqqpmmsjmmszzqvqrvrzznnjdndtntfnttgtctqtwwnwswrrthrttsdttlhlvvdzzgqgttnppjpljplpgpvgvqqvppzmmqggtjgtgstslltjltjjgcjcmjmsshvvtppgmmlslqqshqshsllbggfpgffdsdgssncchctcwwtllgqlqblqlqvvmsvmmwnnzppqllsttgmttftvfvjjrzzswzzjvzjzljjchcshcscbbrdbrbcrrnvvtctntvtvbvjvqjqggsrspsprrbgghdghhmwwldldzdttrvrnrfftqtftrrdsszlzvvbtbffftzzrzqrrhjhghhwbhhsjsfsttdjdjnjhjmjpmplplrrdjdcdjdbjblllbqlqdlqlpqptppdhhqmqfqhqhchwwqjqfjqfqhqshsmswsbbvssdspdpsdssstntltrrgnnmttgmmsjjrlrnlrnrnwrwfwlfltlzllcjcmjcjpjhphcpcwppmvmjjzbzvbbfnfcflfddntddbmmmhnnsrnrrvdvnvcvwvcwvwrrqwqccqmmswmmjrjmmwjmjfjhwrtbjzdvlgrjmvzfmhcqsncvlhzzncjlbvcwrdwjmqjcnptqslvfzpsvltgzsvjdsjrppdrmqrbqwhddfhnftfblspsrhtdtjwdnhbcbtlwlvccsfscvczzrrqmwbwbdmwgzqntvflppqvppwrhnvtlsbzqglhsfdgssqzdtjdpwrrhbnbtwhhnmnlwfwlqffjjrndbpwwsvdrhddbjnnqzmtpvvtwbcpndjzlhcfrrdvmljswjzvmfqcdsgqwclqshwrmblszdvsnrpdgnllmlchzdjlrrpndmmgddjqgjqrhwfbwddqdfbvptrmzhtsqfsfswpnvmtswqprjhbzvntgrlzthhnqbtpplqpvcfnpgdtbhqbhflltbbtmmhcwztslmpznttmssclhmnbsbrwlblrbsdfmnpqbwwmsncvzmpqwhzjgcgdrzvglgdtswmstdhrprdjfmqtjlmplbjtzcgnrwpdvpfjjfwjfnnpmdtwtqsgfndngsbmcwjtglqwtfrclbczfcmjtgcwszhzrbcphrhwmhcwghjznzthnwpljjltdlvqtffsrbmwcsvrdmqqggbznnlzbbqtgspqvnjpbdhtzmgttrcwwszwpgdrcnfqtgrgqdrctlzwtdwqppbhnwgldnqltznnfpbfqtgmmwpcqnndbgmrrtgtvnmlfcwsldchjnnqfrhpzwtclrzftsqllgvpqbgmfjdhqjttwcvbpvfqsvhbhhtwnqnbgndbtzhcvgglbhghbzrbrmdllmgfgttqmhtdnwrpwllhnghrjctrbzrcpnjnctvmrlpjhftnfbczrjrnnbqplplcrbngbhvmmvcffmgvbhjzbhcmtwmwgmjmwjvvlqfldswpntjnsjvmdlbzqqlgbwspwvmnwtwjbczmwplrhmjgsppnmtwmvsfwnsgddgwqcvpftcpzrhpldnwmcjgtjmljjbcmjcqdbwczndnjnjgrmtjrqnnjndzqdqpcgdqptdbrqftnwrgqmrzrvsfmmmbpltlncvtgrjfjmvtgwqphczwjhdrdwtfvgztbhrndvpcbgfjfvmrrljwrvcrtdmtjndfnwgcnfrzgsnjpztbwwsbvqfnpjctgrhsflhnzbbsfqbnmtnvrmjzsbjfndvttpvpfjhqntflgbfnzcclcwmhbsgqfjdcgsvrhtstspfzgvgglgddqmclsmzgzgtncdsfmwdvtcsgwvbzjvclwppqdjgfcrcbzcwbdhrnssjbmnmfmwthdrnmlfhqlddwqrdhsdvdcsmcgjsgcmpnhlbnqftpdjswtmpbznlcrhtswgnmwjcdfmljdngzfsmlzjjnzmfzshmztdbdmcqwmlvcrzgpmbjqcghclwvdbrhgvwqchnndftnrtptmctdlhmfjvpzrpccddfpcdwmzqfhnsqzrvwblzfhcjdcjfctczwqrcbjnrpdcbbnsgnlvqqmnsfgsqschjlbzhhsrbvdbfrhvsgrlzwncgwpdbvmblgzbwbcbgqfwmdmgcrbbjfcvmqgztqpptdhwmvmsdqwplpgcjzgqzdrftzhqbltvhrmlrfffcgfpqzwrrbbtlsjgmtbjvtnmhwdpjptjwfwgjgvbfqwmflrrqzlzdcmtlnptdrpcpdnswcfscnndnrfbgwvvncdjgsdpbwptdtvrqlmrhmvvcwblhhzbjdpsbszhrftfbcgwhwrgglnjzqdhcqnvlhgqjhnddvrslhntssptsbhmqwwqqnbvfmcbgpvgjbrttnvlljdbtfplgmbwtcbcdtqdpqqdvhbmpmtszwpzblcfrtznhhtcljtdlhjdbnlhvwgjsmgvrslrfwnmzwlstpgltvrgnpdqztvfnvdhdtwwqdfsmtpbpdclsbnwcgjzchjcsjmvhbjshmjjlpgdzcgbmmchwmcsddsvhsnpqtcpnhqnbvwgwqhtjbqncgwwftnrzsbsjtvqmjzqvvncmncwflcfpcjqgdtbsmjzzsdjfvhnqbgjhmfgjghwscthbfmbndltbqzwpqtmrswvprpmgwqnqpfnmffrpdlpfqmhrthppzvzwbrtjvwvjndsqdlqtbpqwfcttggnjmcqqnmjwfhfjgcvlnmtlgbdvmctzlwbfgnflwtsflgnfbnfbhhdgjctzvvmrhdsmvmmtnqwtszmqcpsbrqrgjfrzctcbzmtdlhwjtfdqbtthdnqcrpwrhcrvjstbhpltvgmvpmvfjstgzjsgzprzcqzqztvvdcnrrqwrhddcrhhncdrlwzwqlnbbzcfmqtnwgfdscmrbwnbldlfrqchzdnlnmwncgrzdclnvcvplgwjsbzmbnnsdrsfhrlssvncnwmcrjdjbjpdtrrvlnbjvspfqbwdpcnnpjzfnmbhcdhlmdgbpvbzmfltzstnznfctcdzhbfsvnfbsjqzmwfllhtrsfghlrpjgrgzgchlwrdmqzbrncsvnwhfqmwjbnvjctzphcsftqsbmwntgvjqhhvwndvmfmjhhhmfdvrlhpvzmmhrbhbddqbdmgqqsvddsswmzqcjmvhztfqpchzpwhdshzjlmbmnsgzqhbnmrshwvtmgmgndtddpfwsjrrjdhncdhtlczdvlbvqplttnzrblthlcffdtfsdtpwzdgbldvnsttvpzmbgnqddrszftcpwrgmfzhjjvghpntmzcttcsnrjnfpqzqqqljhzlrpgwngllqjwnwfcsphqplgbzmfqfgbfsqpsrntszqbcqnhctsnbfshmlbwfflrwwsjwqwfqlgnftdwmctmclwjhjhbsspqldlshbmpbgrftpnbpsqldhrrbdqwfwvfhclrlfdjfmzgmptdjdcsplcspznfjrfhtsjndwpslrdgnllllwqjgznrhswfssdlvdpmwwgmstqbhfmdhtzvzzvhwzbrrvvsl"

global_count = 0
data_match = True

# function to full a set of 14 characters from a string based on the globabl start character
def data_group(input, global_count):
  # grab 14 characters including the one at count position - 1
  # return those 14 characters
  count = 0
  data = ""
  while count <  14:
    data = data + input[global_count + count]
    count += 1
  return data

# function to compare all the characters in a set of four with each other
def compare_four(data):
  if data[0] != data[1] and data[0] != data[2] and data[0] != data[3]:
    if data[1] != data[2] and data[1] != data[3]:
      if data[2] != data[3]:
        return True
  else:
    return False

# function to compare all the characters in the set of fourteen with each other
def compare(data):
  if data[0] != data[1] and data[0] != data[2] and data[0] != data[3] and data[0] != data[4] and data[0] != data[5] and data[0] != data[6] and data[0] != data[7] and data[0] != data[8] and data[0] != data[9] and data[0] != data[10]  and data[0] != data[11] and data[0] != data[12]  and data[0] != data[13]:
    if data[1] != data[2] and data[1] != data[3] and data[1] != data[4] and data[1] != data[5] and data[1] != data[6] and data[1] != data[7] and data[1] != data[8] and data[1] != data[9] and data[1] != data[10]  and data[1] != data[11] and data[1] != data[12]  and data[1] != data[13]:
      if data[2] != data[3] and data[2] != data[4] and data[2] != data[5] and data[2] != data[6] and data[2] != data[7] and data[2] != data[8] and data[2] != data[9] and data[2] != data[10]  and data[2] != data[11] and data[2] != data[12]  and data[2] != data[13]:
        if data[3] != data[4] and data[3] != data[5] and data[3] != data[6] and data[3] != data[7] and data[3] != data[8] and data[3] != data[9] and data[3] != data[10]  and data[3] != data[11] and data[3] != data[12]  and data[3] != data[13]:
          if data[4] != data[5] and data[4] != data[6] and data[4] != data[7] and data[4] != data[8] and data[4] != data[9] and data[4] != data[10]  and data[4] != data[11] and data[4] != data[12]  and data[4] != data[13]:
            if data[5] != data[6] and data[5] != data[7] and data[5] != data[8] and data[5] != data[9] and data[5] != data[10]  and data[5] != data[11] and data[5] != data[12]  and data[5] != data[13]:
              if data[6] != data[7] and data[6] != data[8] and data[6] != data[9] and data[6] != data[10]  and data[6] != data[11] and data[6] != data[12]  and data[6] != data[13]:
                if data[7] != data[8] and data[7] != data[9] and data[7] != data[10]  and data[7] != data[11] and data[7] != data[12]  and data[7] != data[13]:
                  if data[8] != data[9] and data[8] != data[10]  and data[8] != data[11] and data[8] != data[12]  and data[8] != data[13]:
                    if data[9] != data[10]  and data[9] != data[11] and data[9] != data[12]  and data[9] != data[13]:
                      if data[10] != data[11] and data[10] != data[12]  and data[10] != data[13]:
                        if data[11] != data[12] and data[11] != data[13]:
                          if data[12] != data[13]:
                            return True
  else:
    return False


# bring in the data set, itterate throgh it comparing each block of 14 characters, returning the chacter number at the end of the firs unique set of 14 characters
while data_match:
  if compare(data_group(signal, global_count)):
    data_match = False
    print(global_count + 14)
  else:
    global_count += 1


# print(data_group(test1, global_count))